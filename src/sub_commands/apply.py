"""cmot apply サブコマンド。"""

from pathlib import Path

from commons.codex import run_codex_exec
from commons.errors import CmotError, exit_with_error
from commons.git import (
    commit_all,
    dirty_paths,
    fetch_origin,
    merge_base_ref,
    prepare_repo,
    require_cmot_branch,
    status_entries,
)
from commons.logs import new_log_path
from commons.oracles import list_oracle_files
from commons.process import run_command


def cmot_apply_impl() -> None:
    """oracles に実装を追従させ、branch 全体の変更レポートを保存する。"""
    try:
        repo_root = prepare_repo()
        require_cmot_branch(repo_root)

        # 作業前の未コミット差分を仕様通り処理する。
        paths = dirty_paths(repo_root)
        if paths and all(path.startswith("oracles/") for path in paths):
            commit_all(repo_root, "Update oracles")
        elif paths:
            raise CmotError("working tree has changes outside oracles")

        # 最大 3 回、差異調査と実装追従を繰り返す。
        for _ in range(3):
            diff_report_path = _write_oracle_implementation_diff(repo_root)
            diff_report = diff_report_path.read_text(encoding="utf-8")
            if _report_has_no_clear_difference(diff_report):
                break

            prompt = (
                "<repo-root> の実装を <repo-root>/oracles に追従させてください。"
                "以下は oracles と実装の差異調査結果です。\n\n"
                f"{diff_report}"
            )
            run_codex_exec(repo_root, prompt)

            if status_entries(repo_root):
                commit_message = _generate_commit_message(repo_root)
                commit_all(repo_root, commit_message)
            else:
                break

        # default branch remote 最新 commit へ merge した時の変更内容を report にする。
        fetch_origin(repo_root)
        report_prompt = (
            "現状の cmot feature branch を default branch のリモート最新コミットに"
            "マージした時の変更内容の要約を日本語で書いてください。"
            "この cmot apply で行った作業内容ではなく、branch 全体の差分を要約してください。"
        )
        report_body = run_codex_exec(repo_root, report_prompt)
        log_path = new_log_path(repo_root, "apply")
        base_ref = merge_base_ref(repo_root)
        diff_stat = run_command(["git", "diff", "--stat", base_ref, "HEAD"], repo_root)
        log_path.write_text(
            "# cmot apply report\n\n"
            f"Base: `{base_ref}`\n\n"
            "## Summary\n\n"
            f"{report_body.strip()}\n\n"
            "## Diff stat\n\n"
            "```text\n"
            f"{diff_stat.stdout.strip()}\n"
            "```\n",
            encoding="utf-8",
        )
        print(log_path)
    except CmotError as error:
        exit_with_error(error)


def _write_oracle_implementation_diff(repo_root: Path) -> Path:
    """oracles ファイル単位の差異調査結果を 1 ファイルにまとめる。

    Args:
        repo_root: 操作対象 repository root。

    Returns:
        差異調査結果ファイル path。
    """
    oracle_files = list_oracle_files(repo_root)
    report_parts = ["# oracles と実装の差異\n"]

    # 各 oracles ファイルと実装との差異を Codex CLI に調査させる。
    for oracle_file in oracle_files:
        relative_path = oracle_file.relative_to(repo_root).as_posix()
        prompt = (
            f"{relative_path} と実装との明確な差異が無いかを確認して、"
            "差異とその説明を日本語で報告してください。"
        )
        report = run_codex_exec(repo_root, prompt)
        report_parts.append(f"\n## `{relative_path}`\n\n{report.strip()}\n")

    path = new_log_path(repo_root, "oracle-implementation-diff")
    path.write_text("".join(report_parts), encoding="utf-8")
    return path


def _report_has_no_clear_difference(report: str) -> bool:
    """差異無しと判断できる report かを保守的に判定する。

    Args:
        report: Codex CLI が出力した差異調査 report。

    Returns:
        明確に差異無しと読める場合だけ True。
    """
    lower_report = report.lower()
    difference_markers = [
        "差異があります",
        "差異がある",
        "明確な差異があります",
        "未実装",
        "不足",
        "不一致",
        "ズレ",
        "実装されていません",
        "missing",
        "not implemented",
        "difference exists",
    ]
    if any(marker in lower_report for marker in difference_markers):
        return False

    no_diff_markers = [
        "差異はありません",
        "差異なし",
        "明確な差異はありません",
        "明確な差異なし",
        "no clear difference",
        "no differences",
    ]
    return any(marker in lower_report for marker in no_diff_markers)


def _generate_commit_message(repo_root: Path) -> str:
    """現在の差分に対する commit message を Codex CLI に生成させる。

    Args:
        repo_root: 操作対象 repository root。

    Returns:
        1 行の commit message。
    """
    diff_stat = run_command(["git", "diff", "--stat"], repo_root).stdout
    prompt = (
        "以下の差分統計に対する簡潔な git commit message を英語で 1 行だけ生成してください。"
        "引用符や箇条書きは不要です。\n\n"
        f"{diff_stat}"
    )
    raw_message = run_codex_exec(repo_root, prompt).strip()
    message = raw_message.splitlines()[0].strip() if raw_message else ""
    return message or "Apply oracle changes"
