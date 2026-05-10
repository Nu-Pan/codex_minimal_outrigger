"""cmot eval-oracles サブコマンド。"""

from pathlib import Path

from commons.codex import run_codex_exec
from commons.errors import CmotError, exit_with_error
from commons.git import prepare_repo, require_cmot_branch
from commons.logs import new_log_path
from commons.oracles import list_oracle_files


def cmot_eval_oracles_impl() -> None:
    """oracles の個別評価と関係性評価を行い、レポートを保存する。"""
    try:
        repo_root = prepare_repo()
        require_cmot_branch(repo_root)

        # oracles ファイルごとに Codex CLI で評価する。
        oracle_files = list_oracle_files(repo_root)
        per_file_reports: list[tuple[Path, str]] = []
        for oracle_file in oracle_files:
            relative_path = oracle_file.relative_to(repo_root).as_posix()
            prompt = (
                f"{relative_path} を評価してください。"
                "この oracles ファイルに致命的な問題が無いかを確認し、"
                "必要なら関係するファイルも読みに行って、評価結果を日本語で報告してください。"
            )
            per_file_reports.append((oracle_file, run_codex_exec(repo_root, prompt)))

        # 全 oracles 間の関係性を Codex CLI で評価する。
        oracle_list = "\n".join(
            f"- {path.relative_to(repo_root).as_posix()}" for path in oracle_files
        )
        relation_prompt = (
            "以下の oracles ファイルを全て読んで、ファイル間の関係性に"
            "致命的な問題が無いかを評価し、日本語で報告してください。\n\n"
            f"{oracle_list}"
        )
        relation_report = run_codex_exec(repo_root, relation_prompt)

        # これまでの評価を 1 つのレポートにまとめる。
        report_parts = ["# cmot eval-oracles report\n"]
        report_parts.append("## Oracle files\n")
        if oracle_files:
            report_parts.extend(
                f"- `{path.relative_to(repo_root).as_posix()}`\n"
                for path in oracle_files
            )
        else:
            report_parts.append("- No oracle files found.\n")

        report_parts.append("\n## Per-file evaluation\n")
        for oracle_file, report in per_file_reports:
            relative_path = oracle_file.relative_to(repo_root).as_posix()
            report_parts.append(f"\n### `{relative_path}`\n\n{report.strip()}\n")

        report_parts.append("\n## Cross-file evaluation\n\n")
        report_parts.append(relation_report.strip())
        report_parts.append("\n")

        log_path = new_log_path(repo_root, "eval-oracles")
        log_path.write_text("".join(report_parts), encoding="utf-8")
        print(log_path)
    except CmotError as error:
        exit_with_error(error)
