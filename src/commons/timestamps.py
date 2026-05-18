"""cmoc 仕様のタイムスタンプ生成。"""

from datetime import datetime


def make_timestamp(now: datetime | None = None) -> str:
    """ローカル時刻から cmoc の `<time-stamp>` 文字列を作る。"""
    # 引数指定時はその時刻を使い、未指定時は現在のローカル時刻を使う。
    current = now or datetime.now().astimezone()

    # 仕様上 msec は 3 桁のゼロ埋めにする。
    return (
        f"{current.year:04d}-{current.month:02d}-{current.day:02d}_"
        f"{current.hour:02d}-{current.minute:02d}_{current.second:02d}_"
        f"{current.microsecond // 1000:03d}"
    )
