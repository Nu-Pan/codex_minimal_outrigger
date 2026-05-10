"""Codex CLI 呼び出しの共通処理。"""

from pathlib import Path

from commons.process import run_command


def run_codex_exec(repo_root: Path, prompt: str) -> str:
    """codex exec へ prompt を渡して実行する。

    Args:
        repo_root: 操作対象 repository root。
        prompt: Codex CLI に渡す指示。

    Returns:
        codex exec の標準出力。
    """
    result = run_command(["codex", "exec", prompt], repo_root)
    return result.stdout
