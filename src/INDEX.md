# `commons`

## Summary

- `src/commons` は cmoc 全体で共有する基盤処理の入口です。
- `command_runner.py`、`codex.py`、`repo.py`、`errors.py`、`indexing.py`、`report_files.py`、`subcommand_log.py`、`timing.py`、`timestamps.py`、`__init__.py` への導線をまとめます。
- 共通実行制御、Codex CLI 呼び出し、Git リポジトリ検出、`INDEX.md` 生成・維持、レポート保存、サブコマンドログ、計時、タイムスタンプ生成の責務分担を把握するための目次です。

## Read this when

- 共通の実行制御、エラー整形、リポジトリ検出、計時、タイムスタンプ、ログ保存の入口をまとめて把握したいとき。
- `codex exec` の呼び出し方や Structured Output の扱いを確認したいとき。
- `INDEX.md` 生成・維持の共通処理や、どのモジュールを読むべきかを素早く振り分けたいとき。
- `src/commons` が Python パッケージとしてどう責務分割されているかを確認したいとき。

## Do not read this when

- 個別のサブコマンド実装や CLI 引数の詳細だけを追いたいとき。
- `src/sub_commands` 側の処理フローだけが目的で、共通基盤の実装詳細までは不要なとき。
- `INDEX.md` の生成ルールや維持アルゴリズムだけを知りたいときは、`indexing.py` を直接読むべきとき。
- `oracles` 側の仕様断片やテスト観点だけを確認したいとき。

## hash

- 0d5b92309befbdba6f1d601b46b54a60a66a65c5d3510d971d4502537191ad36
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
<!-- cmoc-index-kind: file -->

# `sub_commands`

## Summary

- `src/sub_commands` は `cmoc` のサブコマンド実装をまとめるディレクトリの入口です。
- 直下にはパッケージ宣言の `__init__.py`、初期化処理の `init.py`、`cmoc review oracles` 実装の `eval_oracles.py` があり、さらに `apply/` と `session/` の各パッケージに分かれます。
- この目次は、各サブコマンドの詳細仕様へ進む前に、どの実装ファイルを読むべきかを振り分けるための案内です。

## Read this when

- `src/sub_commands` 配下にどのサブコマンド実装があるかを素早く把握したいとき。
- `__init__.py`、`init.py`、`eval_oracles.py`、`apply/`、`session/` の役割分担を確認したいとき。
- `cmoc` のサブコマンド実装の入口を整理して、読むべきファイルを振り分けたいとき。
- `apply` 系と `session` 系のどちらに進むべきか、入口レベルで判断したいとき。

## Do not read this when

- `cmoc` 全体の起動エントリや共通基盤だけを確認したいときは、`src/main.py` や `src/commons` を見るべきです。
- `cmoc apply` や `cmoc session` の個別仕様だけを追いたいときは、この目次ではなく各配下の `INDEX.md` を直接見るべきです。
- `cmoc review oracles` の評価ロジックの詳細だけを確認したいときは、この目次ではなく `src/sub_commands/eval_oracles.py` を直接見るべきです。
- `cmoc init` の初期化処理だけを確認したいときは、この目次ではなく `src/sub_commands/init.py` を直接見るべきです。

## hash

- a7a7a8d8179d7cdf2a9e327003e899112af1bcc3fb883cc038d13adad2531639
<!-- cmoc-index-kind: directory -->
