
# `cmoc` による `cmoc` の自己開発のやり方

## セットアップ

- Codex Minimal Outrigger CLI を `~/codex_minimal_outrigger_cli_stage0`, `~/codex_minimal_outrigger_cli_stage1` のニ箇所に Clone する
- stage0 の方で初期セットアップを行い `~/codex_minimal_outrigger_cli_stage0/bin/cmoc` が実行可能な状態にする
- 環境変数 `PATH` を `~/codex_minimal_outrigger_cli_stage0/bin` に通す

## 基本的なワークフロー

1. stage0 cmoc を使って stage1 上で cmoc 開発フローを１周回す
2. stage1 上で master branch を remote へ push
3. stage0 側で remote の master branch を pull
4. 先頭に戻る

## stage0 cmoc が動かなくなった場合

- stage0 上で Codex CLI を直接使って修正を行う
