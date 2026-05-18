"""`eval-oracles.py` 本体処理への互換 import。"""

import importlib.util
from pathlib import Path


# Python の通常 import では hyphen を含むモジュール名を扱えないため、明示ロードする。
_MODULE_PATH = Path(__file__).with_name("eval-oracles.py")
_SPEC = importlib.util.spec_from_file_location(
    "sub_commands.eval-oracles",
    _MODULE_PATH,
)
if _SPEC is None or _SPEC.loader is None:
    raise ImportError(f"Failed to load {_MODULE_PATH}")
_MODULE = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_MODULE)


# 既存テストや利用箇所の monkeypatch が効くよう、本体モジュールの依存を再公開する。
run_codex_exec = _MODULE.run_codex_exec
maintain_indexes = _MODULE.maintain_indexes


def cmoc_eval_oracles_impl(*args: object, **kwargs: object) -> None:
    """互換 import 経由で `eval-oracles.py` の本体処理を呼ぶ。"""
    # wrapper 側で monkeypatch された依存を本体モジュールへ反映してから実行する。
    _MODULE.run_codex_exec = run_codex_exec
    _MODULE.maintain_indexes = maintain_indexes
    _MODULE.cmoc_eval_oracles_impl(*args, **kwargs)


_evaluation_prompt = _MODULE._evaluation_prompt
_write_report = _MODULE._write_report
