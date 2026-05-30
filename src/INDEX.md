# `commons`

## Summary

- `src/commons` は cmoc 全体で使う共通基盤モジュール群の集約先です。`codex.py`、`command_runner.py`、`repo.py`、`errors.py`、`subcommand_log.py`、`timing.py`、`timestamps.py`、`report_files.py`、`indexing.py` が入ります。
- `codex.py` は Codex CLI の共通実行基盤、`command_runner.py` はサブコマンド実行制御、`repo.py` は git と cmoc 状態管理、`errors.py` は共通エラー整形を担います。
- `subcommand_log.py`、`timing.py`、`timestamps.py`、`report_files.py`、`indexing.py` はそれぞれログ記録、時間計測、タイムスタンプ生成、レポート保存、`INDEX.md` 自動整備を担当します。
- `__init__.py` はパッケージ宣言のみで、公開 API の本体は各モジュールに分かれています。

## Read this when

- cmoc 全体で使う共通処理の役割分担を確認したいとき。
- `codex exec` 呼び出し、サブコマンド共通実行、git と cmoc 状態管理、エラー整形、ログ、計時、レポート保存、`INDEX.md` メンテナンスの入口を把握したいとき。
- `src/commons` の各モジュールに何があるかを俯瞰したいとき。

## Do not read this when

- 個別サブコマンドの業務ロジックや `src/sub_commands` 側の挙動だけを確認したいとき。
- `oracles` の正本仕様や `INDEX.md` の生成ルールだけを確認したいとき。
- `codex.py`、`repo.py`、`errors.py` など特定モジュールの詳細実装だけを追いたいとき。

## hash

- a556701f2149259badb7055515ed862180071a6cbc5659198e01af0db53d3b3c
<!-- cmoc-index-kind: directory -->

# `main.py`

## Summary

- cmoc CLI のエントリーポイントで、Typer のルート `app` と `session` / `apply` / `review` の各サブアプリを組み立てるファイルです。
- `init`、`session`、`apply`、`review` の各コマンド登録に加えて、`eval-oracle` / `eval-oracles` の隠し別名や、`apply fork` の繰り返し回数・`scope`、`apply join` の `--force-resolve` などの既定値をまとめています。
- サブコマンド未指定時の `CmocError` 生成、補完プローブ時の分岐、Click/Typer 例外の共通整形、`python src/main.py` 直実行の起動経路を扱います。

## Read this when

- cmoc CLI の起動点と、`session` / `apply` / `review` のサブアプリ構成を確認したいとき。
- `init`、`session fork/join/abandon`、`apply fork/join/abandon`、`review oracles` の登録名、隠し別名、既定オプションを確認したいとき。
- サブコマンド未指定時の利用者向けエラー、補完プローブ時の分岐、Click/Typer 例外の共通整形を追いたいとき。
- `python src/main.py` で直接起動する経路と、そのときの例外処理を確認したいとき。

## Do not read this when

- `src/sub_commands/` 配下の各サブコマンド本体の実装だけを追いたいとき。
- `commons.errors` のエラー型や `format_error_report()` の整形ロジックだけを確認したいとき。
- `INDEX.md` の生成ルールや `oracles` 側のルーティング方針だけを確認したいとき。

## hash

- d03b4e0b3d0c12971884d8bc1e159f95c3f0efe50e8fca99dc96066066992456

# `sub_commands`

## Summary

- `src/sub_commands` は `cmoc` の個別サブコマンド実装を集めたパッケージです。
- `__init__.py` はパッケージ宣言だけを担い、`apply/` と `session/` は各系統の本体実装、`eval_oracles.py` と `init.py` は単独コマンドの本体実装を持ちます。
- `src/main.py` から呼ばれる CLI ルーティング先をたどるための入口です。

## Read this when

- `cmoc` のサブコマンド本体がどのファイルにあるか確認したいとき。
- `init` / `review oracles` / `apply` / `session` の実装入口をまとめて把握したいとき。
- `src/main.py` のコマンド登録と、各本体モジュールの対応関係を整理したいとき。
- `src/sub_commands` 配下を修正・レビュー・テストする前に入口を確認したいとき。

## Do not read this when

- 個別サブコマンドの引数、状態遷移、終了条件だけを確認したいときは、該当モジュールや `oracles/app_specs/sub_commands/` を直接読むべきです。
- `cmoc` 全体の起動処理や共通エラーハンドリングだけを確認したいときは、`src/main.py` や共通モジュールを読むべきです。
- `__init__.py` だけのパッケージ宣言確認で足りるときは、この目次を読む必要はありません。

## hash

- 034868617c3886835f5c2a396982ac7bbb7db5f68eceb1e74588640551118471
<!-- cmoc-index-kind: directory -->
