# `commons`

## Summary

- `src/commons` は、`cmoc` 全体で共有する基盤モジュールをまとめたディレクトリで、エラー処理、サブコマンド実行制御、`codex exec` 連携、リポジトリ操作、ログ、タイムスタンプ、経過時間計測、`INDEX.md` 生成を含みます。
- `command_runner.py` や `errors.py` は CLI の横断的な実行制御とエラーレポート整形を担い、`repo.py` は git リポジトリ探索や `.cmoc` 関連 state を扱います。
- `codex.py` は `codex exec` の共通ラッパーと Structured Output 検証をまとめ、`indexing.py` は `INDEX.md` メンテナンス処理の本体です。
- `subcommand_log.py`、`timestamps.py`、`timing.py` は、それぞれ tee ログ、タイムスタンプ生成、ステップ別経過時間の表示を担当します。

## Read this when

- `cmoc` の共通エラー処理、ログ、タイムスタンプ、経過時間表示、リポジトリ探索などの横断機能を確認したいとき。
- `codex exec` の呼び出し、Structured Output の検証、`INDEX.md` 生成、再試行や quota 待機の流れを確認したいとき。
- サブコマンド共通の実行制御や、`<repo-root>` 解決、`typer.Exit` の扱い、終了時レポートの出力を見直したいとき。
- git リポジトリのルート探索、session / apply ブランチ判定、`.cmoc` 配下の state やログ保存先を確認したいとき。

## Do not read this when

- 個別サブコマンドの業務ロジックや CLI 引数定義だけを確認したいときは、`src/sub_commands` 側を読むべきです。
- `cmoc` のユーザー向け仕様や正本断片だけを確認したいときは、`oracles` 側を読むべきです。
- `INDEX.md` の生成・更新ルールそのものだけを確認したいときは、`src/commons/indexing.py` ではなく対応する正本仕様を読むべきです。
- 共通処理ではなく、特定の 1 機能だけを深掘りしたいときは、このディレクトリ全体を読む必要はありません。

## hash

- cbebfbeb5f2fe97f7e82b31ed5d25eea014f26d2c3b3d34e43e18455f68a451e

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

- `src/sub_commands` は cmoc のサブコマンド実装群の入口です。`__init__.py` はパッケージ宣言のみで、`apply` と `session` は専用サブディレクトリに分かれています。
- `eval_oracles.py` は `cmoc eval-oracles` の本体、`init.py` は `cmoc init` の本体です。
- この目次から `apply/INDEX.md` と `session/INDEX.md` へ進み、各サブコマンドの詳細実装へたどれます。

## Read this when

- `src/sub_commands` 配下の実装入口をまとめて確認したいとき。
- `apply`、`session`、`eval-oracles`、`init` の実装ファイルがどこにあるか整理したいとき。
- 個別モジュールへ入る前に、サブコマンド群の役割分担と配置方針を把握したいとき。
- `apply/INDEX.md` や `session/INDEX.md` へ進むべきか判断したいとき。

## Do not read this when

- `cmoc apply` や `cmoc session` の個別処理だけを確認したいときは、この目次ではなく各下位 `INDEX.md` を直接読むべきです。
- `cmoc eval-oracles` や `cmoc init` の本体処理だけを確認したいときは、この目次ではなく `eval_oracles.py` や `init.py` を直接読むべきです。
- `src/sub_commands` が Python パッケージとして存在するかだけを確認したいときは、`__init__.py` だけで足ります。
- サブコマンドの仕様断片や利用手順だけを確認したいときは、`oracles/app_specs/sub_commands/` 側を読むべきです。

## hash

- c38b9eefb1ca26896d06bc808b4c27f0dec659f5d4fff50c7c5d7e7b591cab81
