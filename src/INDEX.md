# `commons`

## Summary

- `cmoc` の各サブコマンドから共通利用される基盤処理をまとめたディレクトリです。
- 実行ラッパー、Codex 呼び出し、Git リポジトリ操作、共通エラー、サブコマンドログ、時間計測、タイムスタンプ生成、レポート保存、`INDEX.md` 目次維持が入っています。
- サブコマンド実装の土台と、目次文書の自動維持を支える共通モジュール群の入口です。

## Read this when

- `cmoc` 全体で共有する実行制御、エラー整形、Git 操作、ログ記録の役割分担を把握したいとき。
- `codex exec` 呼び出し、`INDEX.md` 生成・維持、レポート保存、タイムスタンプ生成の共通処理を確認したいとき。
- サブコマンド本体の土台になるユーティリティ群の入口をまとめて見たいとき。

## Do not read this when

- 個別サブコマンドの引数解析や業務ロジックだけを確認したいとき。
- `src/sub_commands` 側の実装や各コマンドの実行フローだけを追いたいとき。
- `oracles` 配下の正本仕様や運用手順だけを確認したいとき。

## hash

- 70ff3c924c8ffd5f7a868ca72c53bac80361aa4256253209aa91510602584892

# `main.py`

## Summary

- cmoc CLI のエントリーポイントで、Typer のルート app と `session` / `apply` / `review` のサブアプリを組み立てます。
- `init`、`session fork/join/abandon`、`apply fork/join/abandon`、`review oracles` の登録と、それぞれのオプション既定値やエイリアスをまとめます。
- サブコマンド未指定時の利用者向けエラー、Click/Typer 例外の共通整形、`python src/main.py` 直実行の起動経路を扱います。

## Read this when

- cmoc の起動点やサブコマンド登録を修正・レビューしたいとき。
- `init` / `session` / `apply` / `review` のコマンド名、エイリアス、オプション既定値を確認したいとき。
- サブコマンドなし起動時の利用者向けエラー、終了コード、`--help` への誘導を確認したいとき。
- `python src/main.py` で直接起動する経路と、その例外ハンドリングを確認したいとき。

## Do not read this when

- 各サブコマンドの本体ロジックや `src/sub_commands/` 配下の処理だけを確認したいとき。
- 共通エラー型や `format_error_report` の整形仕様だけを確認したいとき。
- `INDEX.md` の生成ルールや共通ユーティリティの設計だけを追いたいとき。

## hash

- 725244cd04649c14efdc472340862818b2eabfb76416af919258408edf3121cc

# `sub_commands`

## Summary

- `src/sub_commands` は `cmoc` のサブコマンド実装群の入口で、`apply`、`session`、`init.py`、`eval_oracles.py`、`__init__.py` をまとめる目次です。
- `apply` と `session` はそれぞれ開始・統合・破棄の系統を持つサブパッケージで、詳細は配下の `INDEX.md` からたどります。
- `init.py` は `cmoc init` の本体、`eval_oracles.py` は `cmoc review oracles` の本体を実装します。

## Read this when

- `cmoc` のサブコマンド実装が `src/sub_commands` のどこにあるかをまとめて把握したいとき。
- `apply` と `session` の各パッケージから、配下の個別 `INDEX.md` へ進む入口を探したいとき。
- `init.py` と `eval_oracles.py` の実装位置と役割を素早く確認したいとき。
- `src/sub_commands` 配下の実装・修正・テストを始める前に、読むべきファイルを切り分けたいとき。

## Do not read this when

- `src/sub_commands/apply` や `src/sub_commands/session` の個別手順・状態遷移・終了条件だけを確認したいとき。
- `cmoc init` や `cmoc review oracles` など、特定コマンド単体の詳細仕様だけを確認したいとき。
- `src/sub_commands/__init__.py` のような最小パッケージ宣言だけを確認したいとき。
- `oracles` 配下の正本仕様や、`INDEX.md` の生成ルールそのものだけを確認したいとき。

## hash

- 39456c34aff8b260da256f7b12ac7a2c8003195f58e95b06e5aa85261ae41ee1
