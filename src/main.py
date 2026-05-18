"""cmoc CLI エントリーポイント。"""

import importlib.util
import sys
from collections.abc import Callable
from pathlib import Path

import click
import typer

from commons.errors import format_error_report
from commons.repo import enter_repo_root
from sub_commands.apply import cmoc_apply_impl
from sub_commands.branch import cmoc_branch_impl
from sub_commands.init import cmoc_init_impl
from sub_commands.merge import cmoc_merge_impl

app = typer.Typer(no_args_is_help=True)


@app.command("init")
def init_command() -> None:
    """Initialize a repository for cmoc work."""
    # 共通 runner へサブコマンド本体を渡す。
    _run_command(lambda repo_root: cmoc_init_impl(repo_root))


@app.command("branch")
def branch_command() -> None:
    """Create a cmoc work branch."""
    # 共通 runner へサブコマンド本体を渡す。
    _run_command(lambda repo_root: cmoc_branch_impl(repo_root))


@app.command("eval-oracles")
def eval_oracles_command(
    full: bool = typer.Option(False, "--full", "-f"),
) -> None:
    """Evaluate oracle files."""
    # `eval-oracles.py` に配置した本体へ CLI option を渡す。
    _run_command(
        lambda repo_root: cmoc_eval_oracles_impl(repo_root, full=full)
    )


@app.command("apply")
def apply_command() -> None:
    """Apply oracle requirements to implementation."""
    # 共通 runner へサブコマンド本体を渡す。
    _run_command(lambda repo_root: cmoc_apply_impl(repo_root))


@app.command("merge")
def merge_command(cmoc_branch: str | None = typer.Argument(None)) -> None:
    """Merge a cmoc branch into the current branch."""
    # optional な merge 元 branch 名を本体へ渡す。
    _run_command(lambda repo_root: cmoc_merge_impl(repo_root, cmoc_branch))


def _load_eval_oracles_impl() -> Callable[..., None]:
    """`eval-oracles.py` からサブコマンド本体を明示ロードする。"""
    # hyphen を含むファイル名は通常 import できないため、ファイルパスで loader を作る。
    module_path = (
        Path(__file__).resolve().parent
        / "sub_commands"
        / "eval-oracles.py"
    )
    spec = importlib.util.spec_from_file_location(
        "sub_commands.eval-oracles",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Failed to load {module_path}")

    # モジュールを実行し、公開されている本体関数だけを返す。
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.cmoc_eval_oracles_impl


cmoc_eval_oracles_impl = _load_eval_oracles_impl()


def _run_command(handler: Callable[[Path], int | None]) -> None:
    """例外を仕様通り stdout のエラーレポートへ変換する。"""
    # repo root へ移動してからサブコマンド本体を実行する。
    try:
        repo_root = enter_repo_root()
        result = handler(repo_root)
        if isinstance(result, int):
            raise typer.Exit(result)
    # Typer の正常終了はそのまま上位へ伝える。
    except typer.Exit:
        raise
    # それ以外の例外は cmoc の共通エラーレポートへ変換する。
    except Exception as error:
        print(format_error_report(error))
        code = getattr(error, "exit_code", 1)
        raise typer.Exit(code) from error


def main() -> None:
    """Typer の parse error も共通エラーレポートへ変換して起動する。"""
    # standalone_mode=False で Click/Typer の例外を cmoc 側で整形する。
    try:
        app(standalone_mode=False)
    except typer.Exit as exit_error:
        raise SystemExit(exit_error.exit_code) from exit_error
    except click.ClickException as error:
        # CLI parse error は Click の exit_code を維持する。
        print(format_error_report(error))
        raise SystemExit(error.exit_code) from error
    except Exception as error:
        # 想定外エラーも共通形式で表示し、可能なら例外側の exit_code を使う。
        print(format_error_report(error))
        code = getattr(error, "exit_code", 1)
        raise SystemExit(code) from error


if __name__ == "__main__":
    # `bin/cmoc` から直接実行される経路でも typer を起動する。
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    main()
