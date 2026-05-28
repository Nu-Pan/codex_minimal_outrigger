# `commons`

## Summary

- `cmoc` 全体で使う共通処理をまとめたパッケージ入口で、`codex`、`command_runner`、`errors`、`indexing`、`repo`、`subcommand_log`、`timestamps`、`timing` を束ねます。
- `codex exec` の共通ラッパー、サブコマンド共通ランナー、共通エラー整形、`INDEX.md` メンテナンス、リポジトリ探索、ログ記録、タイムスタンプ生成、経過時間計測を扱います。
- `__init__.py` はパッケージ宣言のみで、実装本体は各モジュールに分かれています。

## Read this when

- `cmoc` 全体で使う共通処理の役割分担を整理したいとき。
- `codex exec` 呼び出し、`<repo-root>` 探索、共通エラー処理、`INDEX.md` 保守、ログ記録、経過時間計測、タイムスタンプ生成のどのモジュールを読むべきか切り分けたいとき。
- サブコマンド実行制御や共通ユーティリティの実装・修正・レビューの前に、`src/commons` 内の着地点を把握したいとき。
- `src/commons` が Python パッケージとしてどう構成されているか確認したいとき。

## Do not read this when

- `src/commons` 配下のうち特定 1 ファイルだけの実装を確認したいときは、この目次ではなく該当モジュールを直接読むべきです。
- `cmoc` の個別サブコマンドの業務ロジックだけを確認したいときは、このディレクトリではなく `src/sub_commands` 側を読むべきです。
- `oracles` の正本仕様やユーザー向けコマンド説明だけを確認したいときは、この目次は不要です。
- テストコードや CLI の引数定義だけを追いたいときは、この共通モジュール群の入口を読む必要はありません。

## hash

- 192339bf88c2f1b295aa4256d53847a3289dbddbbd7c89c2bcd10db5f2683269

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

- `cmoc` のサブコマンド実装をまとめる入口で、`apply/`、`session/`、`eval_oracles.py`、`init.py`、`__init__.py` への案内を提供します。
- `apply` と `session` はそれぞれ下位の `INDEX.md` で個別サブコマンドへ辿れる構成です。
- このディレクトリの目次は、目的の実装モジュールを素早く見つけるための案内です。

## Read this when

- `src/sub_commands` 配下の実装全体の入口を確認したいとき。
- `apply` 系、`session` 系、`eval_oracles.py`、`init.py`、`__init__.py` の役割分担を整理したいとき。
- どのサブコマンド実装へ進むべきかを素早く判断したいとき。

## Do not read this when

- `apply` や `session` など個別サブコマンドの処理内容を直接確認したいときは、この目次ではなく各実装ファイルや下位の `INDEX.md` を読むべきです。
- `init.py` や `eval_oracles.py` の詳細な挙動だけを追いたいときは、このディレクトリの入口情報ではなく該当モジュールを直接参照すべきです。
- `cmoc` 全体の設計規則や `oracles` 側の正本仕様だけを確認したいときは、この実装ディレクトリの目次は不要です。

## hash

- 1c17625e9d10900484cb552b1b450f5605fd9a28949faeb09ce2e2cce0680035
