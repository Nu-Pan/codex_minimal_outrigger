"""cmot のエラー表現。"""

import sys


class CmotError(RuntimeError):
    """ユーザーへ短く提示すべき cmot の実行時エラー。"""


def exit_with_error(error: CmotError) -> None:
    """cmot のエラーを標準エラーへ出して終了する。

    Args:
        error: 表示対象のエラー。
    """
    print(f"cmot: error: {error}", file=sys.stderr)
    raise SystemExit(1)
