"""oracles ファイル列挙の共通処理。"""

from pathlib import Path

from commons.process import run_command


def list_oracle_files(repo_root: Path) -> list[Path]:
    """oracles 配下の評価対象ファイルを列挙する。

    Args:
        repo_root: 操作対象 repository root。

    Returns:
        ROUTING.md と git ignore 対象を除外したファイル一覧。
    """
    oracles_dir = repo_root / "oracles"
    if not oracles_dir.exists():
        return []

    oracle_files: list[Path] = []
    for path in sorted(oracles_dir.rglob("*")):
        relative_path = path.relative_to(repo_root)

        # ファイル以外、ROUTING.md、git ignore 対象は除外する。
        if not path.is_file() or path.name == "ROUTING.md":
            continue
        ignored = run_command(
            ["git", "check-ignore", "-q", relative_path.as_posix()],
            repo_root,
            check=False,
        )
        if ignored.returncode == 0:
            continue
        oracle_files.append(path)

    return oracle_files
