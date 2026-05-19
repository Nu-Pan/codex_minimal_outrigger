"""`eval-oracles.py` 本体を通常 import 名から読み込む互換ローダー。"""

from pathlib import Path

# Python import できないハイフン名ファイルを、このモジュール名前空間へ展開する。
_body_path = Path(__file__).with_name("eval-oracles.py")
exec(
    compile(_body_path.read_text(encoding="utf-8"), str(_body_path), "exec"),
    globals(),
)
