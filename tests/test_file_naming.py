"""リポジトリ構成の命名規則テスト。"""

from pathlib import Path


def test_routing_file_uses_snake_case_name() -> None:
    """指定のないルーティングファイル名はスネークケースにする。"""
    repo_root = Path(__file__).resolve().parents[1]

    assert (repo_root / "routing.md").is_file()
    assert not (repo_root / "ROUTING.md").exists()
