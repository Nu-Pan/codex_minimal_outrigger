# `commons`

## Summary

- `src/commons` の共通ユーティリティ群の入口で、エラー処理、Codex CLI 呼び出し、リポジトリ探索、サブコマンド実行制御、ログ、計測、タイムスタンプ生成への案内をまとめます。
- `indexing.py` は `INDEX.md` の生成・更新ルールを扱い、各ディレクトリの目次メンテナンスを担います。
- `codex.py`、`repo.py`、`command_runner.py` は、外部コマンド実行、作業リポジトリの特定、共通実行制御の中心です。
- `errors.py`、`subcommand_log.py`、`timing.py`、`timestamps.py` は、エラーレポート、ログ保存、経過時間表示、時刻文字列生成をそれぞれ担当します。

## Read this when

- `cmoc` 全体で使う共通処理の入口を確認したいとき。
- 共通エラー処理、`codex exec` 呼び出し、リポジトリ探索、サブコマンド実行制御、ログ、経過時間計測、タイムスタンプ生成のどこへ進むべきか整理したいとき。
- `src/commons` 配下の各モジュールが何を担当しているかを横断的に見直したいとき。
- `INDEX.md` の対象になる共通ユーティリティ群の役割分担を把握したいとき。

## Do not read this when

- `src/commons` 配下の個別モジュールの実装詳細だけを確認したいときは、該当する `*.py` を直接読むべきです。
- `cmoc` のユーザー向けサブコマンド仕様だけを確認したいときは、この共通モジュール群ではなく `oracles/app_specs` 側を読むべきです。
- `INDEX.md` の生成・更新ルールそのものだけを確認したいときは、`src/commons/indexing.py` を読むべきです。
- `src/commons` 以外の CLI 本体やテストだけを追いたいときは、このディレクトリの案内は不要です。

## hash

- fde860c2c02bef9aecf7cbd4097403248ec2f620542901f5c7627ff5521cbfc8

# `main.py`

## Summary

- `cmoc` CLI のエントリーポイントで、Typer アプリ本体と `session` / `apply` のサブアプリを組み立てています。
- `init`、`session`、`apply`、`eval-oracles` の各コマンドを定義し、実処理は `src/sub_commands/` 側の実装へ委譲しています。
- Typer / Click の例外処理をまとめて受け、`NoArgsIsHelpError` を含むエラーを `format_error_report()` で整形して終了コード付きで終了します。

## Read this when

- `cmoc` のエントリーポイント、Typer アプリの構成、サブコマンド登録を修正・レビューしたいとき。
- `init`、`session fork/join/abandon`、`apply fork/join/abandon`、`eval-oracles` とその引数定義を確認したいとき。
- サブコマンドなし起動時の `NoArgsIsHelpError` の扱い、`--help` 相当の挙動、終了コードの伝播を確認したいとき。
- Typer / Click の例外を `CmocError` と共通エラーレポートへ変換する起動経路を確認したいとき。
- `python src/main.py` で直接起動する経路の振る舞いを確認したいとき。

## Do not read this when

- 各サブコマンド本体の処理内容だけを確認したいときは、このファイルではなく `src/sub_commands/` 配下の実装を見るべきです。
- 共通エラー型やエラーレポートの整形だけを確認したいときは、このファイルではなく `src/commons/errors.py` を見るべきです。
- CLI の設計ルールや配置方針だけを確認したいときは、このファイルではなく `oracles/dev_rules/design_rules.md` を見るべきです。
- サブコマンドごとの仕様断片だけを確認したいときは、このファイルではなく `oracles/app_specs/sub_commands/` 配下の文書を見るべきです。

## hash

- fd4b3fe58ddc1bb32e637e83cc5ddca509458ade3b15a69c1c5d5bc677ba138b

# `sub_commands`

## Summary

- `cmoc` の個別サブコマンド実装群の入口で、`__init__.py`、`apply`、`session`、`eval_oracles.py`、`init.py` への案内をまとめるディレクトリです。
- `apply` と `session` はそれぞれ専用パッケージに分かれ、`eval-oracles` と `init` は単独モジュールとして置かれています。
- ここでは実装の役割分担と進み先だけを整理し、具体的な処理は各モジュールに委ねます。

## Read this when

- `src/sub_commands` 配下のどの実装を読むべきか切り分けたいとき。
- `cmoc apply`、`cmoc session`、`cmoc eval-oracles`、`cmoc init` の本体実装へ直接進みたいとき。
- サブコマンドごとの責務分担や入口を俯瞰したいとき。
- 新しい処理を追加・修正するときに配置先を確認したいとき。

## Do not read this when

- `apply`、`session`、`eval-oracles`、`init` のうち特定の 1 つだけの処理詳細を確認したいときは、該当モジュールを直接読むべきです。
- ユーザー向けの利用手順や正本仕様だけを見たいときは、`oracles/app_specs/sub_commands/` 側を読むべきです。
- CLI のエントリーポイントや引数定義だけを確認したいときは、`src/main.py` を読むべきです。
- 共通ユーティリティやエラーハンドリングだけを見たいときは、`src/commons/` を読むべきです。

## hash

- c370780a251e9beb8c8e963cea58f4aab3fbbcc4e6454737c18f9f2ab782514c
