"""git 操作に関する共通処理。"""

import os
from pathlib import Path

from commons.errors import CmotError
from commons.process import run_command


CMOT_BRANCH_PREFIX = "cmot_"


def prepare_repo() -> Path:
    """呼び出し元から repo root を探索し、cmot 用 ignore を整える。

    Returns:
        探索した git repository root。
    """
    repo_root = find_repo_root(Path.cwd())
    os.chdir(repo_root)
    ensure_cmot_ignored(repo_root)
    return repo_root


def find_repo_root(start: Path) -> Path:
    """直下に .git を持つ最初の親ディレクトリを返す。

    Args:
        start: 探索開始ディレクトリ。

    Returns:
        git repository root。
    """
    current = start.resolve()

    # カレントからルートへ向かって .git を持つ場所を探す。
    while True:
        if (current / ".git").exists():
            return current
        if current.parent == current:
            raise CmotError("git repository root was not found")
        current = current.parent


def ensure_cmot_ignored(repo_root: Path) -> None:
    """repo root の .gitignore に .cmot/ を含める。

    Args:
        repo_root: 操作対象 repository root。
    """
    gitignore_path = repo_root / ".gitignore"
    existing = gitignore_path.read_text(encoding="utf-8") if gitignore_path.exists() else ""

    # 既に .cmot が無視対象なら何もしない。
    ignored = run_command(
        ["git", "check-ignore", "-q", ".cmot/probe"],
        repo_root,
        check=False,
    )
    if ignored.returncode == 0:
        return

    # ログファイルが差分として現れないよう .gitignore に追記する。
    suffix = "" if existing.endswith("\n") or existing == "" else "\n"
    gitignore_path.write_text(f"{existing}{suffix}/.cmot/\n", encoding="utf-8")


def require_clean_worktree(repo_root: Path) -> None:
    """未コミット差分が無いことを要求する。

    Args:
        repo_root: 操作対象 repository root。
    """
    if status_entries(repo_root):
        raise CmotError("working tree has uncommitted changes")


def require_cmot_branch(repo_root: Path) -> str:
    """現在の branch が cmot feature branch であることを要求する。

    Args:
        repo_root: 操作対象 repository root。

    Returns:
        現在の branch 名。
    """
    branch = current_branch(repo_root)
    if not branch.startswith(CMOT_BRANCH_PREFIX):
        raise CmotError("current branch is not a cmot feature branch")
    return branch


def require_not_cmot_branch(repo_root: Path) -> None:
    """現在の branch が cmot feature branch でないことを要求する。

    Args:
        repo_root: 操作対象 repository root。
    """
    if current_branch(repo_root).startswith(CMOT_BRANCH_PREFIX):
        raise CmotError("already on a cmot feature branch")


def current_branch(repo_root: Path) -> str:
    """現在の branch 名を返す。

    Args:
        repo_root: 操作対象 repository root。

    Returns:
        現在の branch 名。
    """
    result = run_command(["git", "branch", "--show-current"], repo_root)
    branch = result.stdout.strip()
    if branch == "":
        raise CmotError("detached HEAD is not supported")
    return branch


def status_entries(repo_root: Path) -> list[str]:
    """porcelain status の各行を返す。

    Args:
        repo_root: 操作対象 repository root。

    Returns:
        git status --porcelain の非空行。
    """
    result = run_command(
        ["git", "status", "--porcelain", "--untracked-files=all"],
        repo_root,
    )
    return [line for line in result.stdout.splitlines() if line.strip()]


def dirty_paths(repo_root: Path) -> list[str]:
    """未コミット差分の path 部分を返す。

    Args:
        repo_root: 操作対象 repository root。

    Returns:
        未コミット差分の path 一覧。
    """
    paths: list[str] = []
    for entry in status_entries(repo_root):
        path = entry[3:]
        if " -> " in path:
            path = path.split(" -> ", maxsplit=1)[1]
        paths.append(path)
    return paths


def default_branch(repo_root: Path) -> str:
    """origin の default branch 名を返す。

    Args:
        repo_root: 操作対象 repository root。

    Returns:
        default branch 名。
    """
    symbolic_ref = run_command(
        ["git", "symbolic-ref", "refs/remotes/origin/HEAD", "--short"],
        repo_root,
        check=False,
    )
    if symbolic_ref.returncode == 0:
        return symbolic_ref.stdout.strip().removeprefix("origin/")

    remote_show = run_command(["git", "remote", "show", "origin"], repo_root)
    for line in remote_show.stdout.splitlines():
        stripped = line.strip()
        if stripped.startswith("HEAD branch:"):
            return stripped.split(":", maxsplit=1)[1].strip()

    raise CmotError("origin default branch was not found")


def fetch_origin(repo_root: Path) -> None:
    """origin の最新 ref を取得する。

    Args:
        repo_root: 操作対象 repository root。
    """
    run_command(["git", "fetch", "origin"], repo_root, capture_output=False)


def commit_all(repo_root: Path, message: str) -> None:
    """現在の差分をすべて commit する。

    Args:
        repo_root: 操作対象 repository root。
        message: commit message。
    """
    run_command(["git", "add", "-A"], repo_root)
    run_command(["git", "commit", "-m", message], repo_root, capture_output=False)


def merge_base_ref(repo_root: Path) -> str:
    """現在の default branch remote ref を返す。

    Args:
        repo_root: 操作対象 repository root。

    Returns:
        origin/<default branch> 形式の ref。
    """
    return f"origin/{default_branch(repo_root)}"
