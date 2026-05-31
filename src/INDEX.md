# `commons`

## Summary

- `src/commons` は `cmoc` 全体で共有する基盤モジュール群をまとめるディレクトリです。
- `codex.py`、`command_runner.py`、`errors.py`、`indexing.py`、`repo.py`、`report_files.py`、`subcommand_log.py`、`timestamps.py`、`timing.py` が主要な構成要素です。
- この目次は、実行制御、共通エラー、リポジトリ操作、目次維持、ログ、時間表示、レポート保存のどこへ進むかを素早く判断するための入口です。

## Read this when

- `cmoc` 全体で使う共通基盤の役割分担を把握したいとき。
- CLI 実行、エラー整形、ログ、時間計測、タイムスタンプ、レポート保存の共通処理を確認したいとき。
- repo root や `.cmoc` の管理、`INDEX.md` 生成・維持の流れを追いたいとき。
- `src/commons` 配下のどのモジュールを読むべきか切り分けたいとき。

## Do not read this when

- 個別サブコマンドの業務ロジックや引数解析だけを追いたいとき。
- `src/sub_commands/` 側の実装や CLI の振る舞いだけを確認したいとき。
- `oracles` 配下の正本仕様断片を直接たどりたいとき。
- テストケースの期待値だけを確認したいとき。

## hash

- ca47d61b847f9e0afe7c517c6caceab4b6a115f63b01c06a4089e8a71d926cc3

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

- 34ab9fdae7d4622e261437958669dd52ce211f233a2300c1c7c831efc256c365

# `sub_commands`

## Summary

- `src/sub_commands` は `cmoc` の個別サブコマンド実装の入口で、`apply`、`session`、`review`、`init.py` を束ねるディレクトリです。
- この配下には `__init__.py` と、`apply` 配下の `abandon.py`、`fork.py`、`join.py`、`session` 配下の `abandon.py`、`fork.py`、`join.py`、`review/oracles.py`、`init.py` があります。
- 個別実装に進む前に、各サブコマンドの責務分担と入口構造を俯瞰するための目次です。

## Read this when

- `cmoc` の個別サブコマンドの入口をまとめて確認したいとき。
- `apply`、`session`、`review`、`init` のどの仕様断片へ進むべきか整理したいとき。
- サブコマンドごとの目的、入力条件、実行手順、状態遷移、終了条件を俯瞰したいとき。

## Do not read this when

- 個別の `apply`、`session`、`review`、`init` の詳細仕様だけを確認したいときは、この目次ではなく該当する下位ディレクトリやモジュールの `INDEX.md` を直接読むべきです。
- 実装コードやテストコードの作業だけで足りるときは、この目次を読む必要はありません。
- `branch_model`、`codex_call`、ログ、エラーハンドリング、`oracles` 全体の扱いなど、別の共通仕様を確認したいときはこのディレクトリではなく他の入口文書を読むべきです。

## hash

- ca91bb97794564d72e92daa8157a55ead9e86a920431c1989fdf089356d73cdc
