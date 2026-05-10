"""外部コマンド実行の薄いラッパー。"""

import subprocess
from pathlib import Path

from commons.errors import CmotError


def run_command(
    args: list[str],
    cwd: Path,
    *,
    capture_output: bool = True,
    check: bool = True,
) -> subprocess.CompletedProcess[str]:
    """外部コマンドを実行し、失敗時は cmot のエラーへ変換する。

    Args:
        args: 実行するコマンドと引数。
        cwd: コマンドの実行ディレクトリ。
        capture_output: 標準出力と標準エラーを捕捉するか。
        check: 非ゼロ終了をエラーにするか。

    Returns:
        コマンドの実行結果。
    """
    try:
        return subprocess.run(
            args,
            cwd=cwd,
            text=True,
            capture_output=capture_output,
            check=check,
        )
    except FileNotFoundError as exc:
        raise CmotError(f"command not found: {args[0]}") from exc
    except subprocess.CalledProcessError as exc:
        stderr = (exc.stderr or "").strip()
        stdout = (exc.stdout or "").strip()
        detail = stderr or stdout or f"exit status {exc.returncode}"
        raise CmotError(f"command failed: {' '.join(args)}\n{detail}") from exc
