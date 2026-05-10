"""cmot の CLI エントリーポイント。"""

import typer

from sub_commands.apply import cmot_apply_impl
from sub_commands.eval_oracles import cmot_eval_oracles_impl
from sub_commands.fork import cmot_fork_impl
from sub_commands.merge import cmot_merge_impl


app = typer.Typer(no_args_is_help=True)


@app.command("fork")
def fork() -> None:
    """cmot feature branch を作成する。"""
    cmot_fork_impl()


@app.command("eval-oracles")
def eval_oracles() -> None:
    """oracles の致命的な問題を評価する。"""
    cmot_eval_oracles_impl()


@app.command("apply")
def apply() -> None:
    """oracles に実装を追従させる。"""
    cmot_apply_impl()


@app.command("merge")
def merge() -> None:
    """cmot feature branch を default branch にマージする。"""
    cmot_merge_impl()


if __name__ == "__main__":
    app()
