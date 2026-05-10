"""cmot fork サブコマンド。"""

from datetime import datetime

from commons.errors import CmotError, exit_with_error
from commons.git import (
    default_branch,
    fetch_origin,
    prepare_repo,
    require_clean_worktree,
    require_not_cmot_branch,
)
from commons.process import run_command


def cmot_fork_impl() -> None:
    """remote default branch から cmot feature branch を作る。"""
    try:
        repo_root = prepare_repo()

        # fork は人間がクリーンにした状態からだけ開始する。
        require_clean_worktree(repo_root)
        require_not_cmot_branch(repo_root)

        # remote 最新 commit を分岐元にする。
        fetch_origin(repo_root)
        base_branch = default_branch(repo_root)
        branch_name = f"cmot_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
        run_command(
            ["git", "checkout", "-b", branch_name, f"origin/{base_branch}"],
            repo_root,
            capture_output=False,
        )
    except CmotError as error:
        exit_with_error(error)
