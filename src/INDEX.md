# `commons`

## Summary

- `src/commons` は cmoc 全体で共有する基盤処理の集約先で、`__init__.py` と各種共通モジュールをまとめています。
- `codex.py` は `codex exec` の共通起動基盤、`command_runner.py` はサブコマンド共通実行、`repo.py` は git と cmoc 状態管理、`errors.py` は共通エラー整形を担当します。
- `subcommand_log.py`、`timing.py`、`timestamps.py`、`report_files.py`、`indexing.py` はそれぞれログ記録、経過時間計測、タイムスタンプ生成、レポート保存、`INDEX.md` 目次維持を扱います。
- このディレクトリの目次は、共通処理の役割を素早く切り分けて、必要な実装へ最短でたどるための入口です。

## Read this when

- cmoc 全体で使う共通基盤モジュールの役割分担を把握したいとき。
- `codex.py`、`command_runner.py`、`repo.py`、`errors.py`、`subcommand_log.py`、`timing.py`、`timestamps.py`、`report_files.py`、`indexing.py` のどれに何があるかを俯瞰したいとき。
- 共通処理の入口を確認してから、実装やテストの対象モジュールへ進みたいとき。

## Do not read this when

- `src/sub_commands` 側の個別サブコマンドの業務ロジックや CLI 引数だけを確認したいとき。
- `oracles` の正本仕様や `INDEX.md` の生成ルールだけを確認したいとき。
- 特定の共通モジュール 1 つだけの詳細実装を追いたいとき。

## hash

- e96c77a0a4f9c1684cb598a016371c6e97a12f05165463aed067a752844a737e

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

- `src/sub_commands` は cmoc のサブコマンド実装の入口で、`__init__.py`、`init.py`、`eval_oracles.py`、`apply/`、`session/` に振り分けます。
- `__init__.py` はパッケージ宣言だけを担い、`init.py` は `cmoc init`、`eval_oracles.py` は `cmoc review oracles` の本体です。
- `apply/` は `cmoc apply` 系、`session/` は `cmoc session` 系の実装入口で、それぞれ配下に個別の `INDEX.md` があります。

## Read this when

- `src/sub_commands` 配下で、どのファイルがどのサブコマンドを担当しているかを素早く確認したいとき。
- `__init__.py`、`init.py`、`eval_oracles.py`、`apply/`、`session/` の入口を整理したいとき。
- サブコマンド実装・修正・レビュー・テストを始める前に、該当モジュールや配下ディレクトリへ進むためのルーティングを把握したいとき。

## Do not read this when

- 個別のサブコマンド実装の引数、状態遷移、例外条件だけを確認したいときは、この目次ではなく該当モジュールを直接読むべきです。
- `apply/` や `session/` の配下にあるさらに細かい仕様を見たいときは、この目次ではなく各配下の `INDEX.md` を読むべきです。
- `cmoc` 全体の共通仕様や `oracles` 側の仕様断片だけを確認したいときは、このディレクトリではなく別の入口文書を読むべきです。

## hash

- 464467478d842cd55a4eb18ca88877c3c21249afef2988cb9c2d5b72d2595ec7
<!-- cmoc-index-kind: directory -->
