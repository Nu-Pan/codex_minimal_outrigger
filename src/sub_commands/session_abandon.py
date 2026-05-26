"""`cmoc session abandon` の本体処理。"""

from pathlib import Path

from commons.command_runner import run_command
from commons.errors import CmocError
from commons.repo import (
    assert_no_uncommitted_changes,
    current_branch,
    ensure_cmoc_ignored,
    is_session_branch,
    read_session_state,
    run_git,
    session_id_from_branch,
    write_session_state,
)
from commons.timing import StepTimer, start_step


def cmoc_session_abandon_impl(repo_root: Path | None = None) -> None:
    """現在の session branch を merge せず破棄する。"""
    # 直接呼び出し時は共通 runner で repo root 解決とエラー整形を行う。
    if repo_root is None:
        run_command(cmoc_session_abandon_impl)
        return

    timer = StepTimer("session abandon")
    start_step(timer, 1, 4, "validate session state")
    session_branch = _current_session_branch(repo_root)
    session_id = session_id_from_branch(session_branch)
    state = read_session_state(repo_root, session_id)
    home_branch = _validate_abandonable_state(state, session_branch)
    _assert_local_branch_exists(repo_root, home_branch)
    assert_no_uncommitted_changes(repo_root)

    start_step(timer, 2, 4, "ensure .cmoc is ignored")
    ensure_cmoc_ignored(repo_root)

    start_step(timer, 3, 4, "switch to session home branch")
    run_git(repo_root, ["switch", home_branch])

    start_step(timer, 4, 4, "record abandoned session")
    try:
        _mark_session_abandoned(repo_root, session_id, state)
        run_git(repo_root, ["branch", "-D", session_branch])
    except Exception as error:
        _restore_abandon_state(repo_root, session_id, state, session_branch)
        raise CmocError(
            "session abandon のクリーンアップに失敗しました。",
            [
                "Detail を確認して問題を手動で解消してから "
                "`cmoc session abandon` を再実行してください。",
                "session branch と session state の状態を確認してください。",
            ],
            str(error),
        ) from error

    print(f"abandoned session branch: {session_branch}")
    print(f"session home branch: {home_branch}")
    timer.report()


def _current_session_branch(repo_root: Path) -> str:
    """現在 checkout している session branch 名を返す。"""
    branch_name = current_branch(repo_root)
    if not is_session_branch(branch_name):
        raise CmocError(
            "`cmoc session abandon` は session branch 上で実行してください。",
            [
                "`cmoc session fork` で作成した branch へ移動してから"
                "再実行してください。",
                "通常 branch を削除する場合は `git branch -D` を直接実行してください。",
            ],
            f"現在の branch: {branch_name or '(detached HEAD)'}",
        )
    return branch_name


def _validate_abandonable_state(
    state: dict[str, object],
    session_branch: str,
) -> str:
    """session abandon の state 前提条件を検証し、home branch 名を返す。"""
    session = state.get("session")
    apply = state.get("apply")
    if not isinstance(session, dict) or not isinstance(apply, dict):
        raise CmocError(
            "session state ファイルの形式が不正です。",
            ["state JSON の session/apply セクションを確認してください。"],
            f"現在の branch: {session_branch}",
        )
    if session.get("state") != "active":
        raise CmocError(
            "active な session ではありません。",
            [
                "対象 session の state を確認してください。",
                "既に join または abandon 済みの場合は、追加の abandon は実行できません。",
            ],
            f"session.state: {session.get('state')}",
        )
    if apply.get("state") != "ready":
        raise CmocError(
            "apply run が完了または整理されていません。",
            [
                "残っている apply run を `cmoc apply abandon` で破棄してから"
                "再実行してください。",
                "session state の apply.state を確認してください。",
            ],
            f"apply.state: {apply.get('state')}",
        )
    home_branch = session.get("session_home_branch")
    if not isinstance(home_branch, str) or not home_branch:
        raise CmocError(
            "session home branch を特定できませんでした。",
            [
                "session state の session.session_home_branch を確認してください。",
                "state が壊れている場合は、手動で戻り先 branch を確認してください。",
            ],
            f"現在の branch: {session_branch}",
        )
    return home_branch


def _assert_local_branch_exists(repo_root: Path, branch_name: str) -> None:
    """記録済み home branch が local branch として存在することを確認する。"""
    result = run_git(
        repo_root,
        ["show-ref", "--verify", f"refs/heads/{branch_name}"],
        check=False,
    )
    if result.returncode != 0:
        raise CmocError(
            "session home branch が見つかりませんでした。",
            [
                "session state に記録された branch 名を確認してください。",
                "削除済みの場合は、手動で復元または戻り先を判断してください。",
            ],
            f"session home branch: {branch_name}",
        )


def _mark_session_abandoned(
    repo_root: Path,
    session_id: str,
    state: dict[str, object],
) -> None:
    """session state を abandoned として保存する。"""
    session = state.get("session")
    if not isinstance(session, dict):
        raise CmocError(
            "session state ファイルの形式が不正です。",
            ["state JSON の session セクションを確認してください。"],
        )
    session["state"] = "abandoned"
    write_session_state(repo_root, session_id, state)


def _restore_abandon_state(
    repo_root: Path,
    session_id: str,
    state: dict[str, object],
    session_branch: str,
) -> None:
    """cleanup 失敗時に再実行しやすい状態へ戻す。"""
    session = state.get("session")
    if isinstance(session, dict):
        session["state"] = "active"
        write_session_state(repo_root, session_id, state)

    branch_exists = run_git(
        repo_root,
        ["show-ref", "--verify", f"refs/heads/{session_branch}"],
        check=False,
    )
    if branch_exists.returncode == 0:
        run_git(repo_root, ["switch", session_branch], check=False)
