"""リポジトリ構成の命名規則テスト。"""

from pathlib import Path


def test_routing_file_uses_snake_case_name() -> None:
    """指定のないルーティングファイル名はスネークケースにする。"""
    repo_root = Path(__file__).resolve().parents[1]

    assert (repo_root / "routing.md").is_file()
    assert not (repo_root / "ROUTING.md").exists()


def test_routing_file_points_to_current_oracle_indexes() -> None:
    """ルーティングファイルは現行の oracle 入口だけを案内する。"""
    repo_root = Path(__file__).resolve().parents[1]
    content = (repo_root / "routing.md").read_text(encoding="utf-8")

    current_paths = [
        "oracles/INDEX.md",
        "oracles/app_specs/INDEX.md",
        "oracles/app_specs/sub_commands/INDEX.md",
        "oracles/dev_rules/INDEX.md",
        "oracles/considered_alternatives/INDEX.md",
    ]
    for path in current_paths:
        assert f"<cmoc-root>/{path}" in content
        assert (repo_root / path).exists()

    stale_paths = [
        "oracles/docs",
        "oracles/docs/app_spec.md",
        "oracles/docs/code_design.md",
        "oracles/docs/coding_rule.md",
        "oracles/docs/development_environment.md",
    ]
    for path in stale_paths:
        assert f"<cmoc-root>/{path}" not in content
