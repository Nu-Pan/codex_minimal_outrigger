"""`cmoc eval-oracles` の本体処理。"""

from pathlib import Path

from commons.codex import run_codex_exec
from commons.indexing import maintain_indexes
from commons.repo import (
    current_branch,
    ensure_cmoc_ignored,
    head_commit,
    is_cmoc_branch,
    list_oracle_files,
    read_branch_base_commit,
    changed_oracle_files,
)
from commons.timestamps import make_timestamp


def cmoc_eval_oracles_impl(repo_root: Path, *, full: bool) -> None:
    """oracle 断片を Codex CLI で評価し、レポートを作る。"""
    print("eval-oracles (1/5) ensure .cmoc is ignored")
    ensure_cmoc_ignored(repo_root)

    print("eval-oracles (2/5) maintain INDEX.md files")
    maintain_indexes(repo_root)

    print("eval-oracles (3/5) select oracle files")
    branch_name = current_branch(repo_root)
    partial = is_cmoc_branch(branch_name) and not full
    all_oracle_files = list_oracle_files(repo_root)
    if partial:
        changed_files = set(changed_oracle_files(repo_root, read_branch_base_commit(repo_root, branch_name)))
        oracle_files = [path for path in all_oracle_files if path in changed_files]
        mode = "partial"
    else:
        oracle_files = all_oracle_files
        mode = "full"

    print("eval-oracles (4/5) evaluate oracle files")
    evaluations = []
    for oracle_file in oracle_files:
        output = run_codex_exec(
            repo_root,
            _evaluation_prompt(repo_root, oracle_file),
            read_only=True,
            expect_json=False,
        )
        evaluations.append((oracle_file, output))

    print("eval-oracles (5/5) write report")
    report_path = _write_report(repo_root, mode, branch_name, head_commit(repo_root), evaluations)
    print(str(report_path))


def _evaluation_prompt(repo_root: Path, oracle_file: Path) -> str:
    """oracle 評価用 prompt を組み立てる。"""
    return "\n".join(
        [
            "あなたはソフトウェア仕様のレビュー担当です。",
            f"`{repo_root}` 内の oracle ファイル `{oracle_file}` を評価してください。",
            "完了条件は、致命的な仕様問題の有無と根拠を報告することです。",
            "致命的な問題とは、主要ワークフローを壊す、完了判定を妨げる、または中核目的を満たしたと判断できなくする問題です。",
            f"`{repo_root / 'memo'}` は読み書き禁止です。",
            "ファイル編集は禁止です。",
        ]
    )


def _write_report(
    repo_root: Path,
    mode: str,
    branch_name: str,
    commit_hash: str,
    evaluations: list[tuple[Path, str]],
) -> Path:
    """評価結果を `.cmoc/reports/eval-oracles` に保存する。"""
    report_dir = repo_root / ".cmoc" / "reports" / "eval-oracles"
    report_dir.mkdir(parents=True, exist_ok=True)
    report_path = report_dir / f"{make_timestamp()}.md"
    lines = [
        "---",
        f"mode: {mode}",
        f"branch: {branch_name}",
        f"commit: {commit_hash}",
        f"oracle_count: {len(evaluations)}",
        "---",
        "",
    ]
    for oracle_file, output in evaluations:
        lines.extend([f"## {oracle_file}", "", output.strip(), ""])
    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path
