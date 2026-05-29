# `commons`

## Summary

- `src/commons` にある cmoc 共通ユーティリティ群の入口です。
- Codex CLI 呼び出し、サブコマンド実行制御、リポジトリ状態管理、共通エラー整形を扱うモジュールへの案内をまとめます。
- サブコマンドログ、タイミング計測、タイムスタンプ生成、`INDEX.md` 生成・維持の共通処理をたどるための目次です。

## Read this when

- cmoc の共通処理をまとめて把握したいとき
- `codex.py`、`command_runner.py`、`repo.py`、`errors.py` などの役割分担を確認したいとき
- サブコマンドログ、経過時間計測、タイムスタンプ生成、`INDEX.md` メンテナンスの入口を探したいとき

## Do not read this when

- 個別サブコマンドの業務ロジックや引数定義だけを確認したいとき
- `src/commons` 以外の機能、例えば `oracles` 配下の仕様やテストの詳細だけを確認したいとき
- `INDEX.md` の自動生成ロジックや更新判定そのものを確認したいとき

## hash

- 753e51bbbb5bab03b4c6737abbf2aafc80c079102896b96366bbaa4c891005a7

# `main.py`

## Summary

- `cmoc` CLI のエントリーポイントで、Typer アプリ本体と `session` / `apply` / `review` のサブアプリを組み立てています。
- `init`、`session fork/join/abandon`、`apply fork/join/abandon`、`review oracles` の各コマンドを定義し、実処理は `src/sub_commands/` 側へ委譲しています。
- Typer / Click の例外を共通エラーレポートへ変換し、`NoArgsIsHelpError` を含む起動時エラーを終了コード付きで処理します。

## Read this when

- `cmoc` のエントリーポイント、Typer アプリの構成、サブコマンド登録を修正・レビューしたいとき
- `init`、`session fork/join/abandon`、`apply fork/join/abandon`、`review oracles` とその引数定義を確認したいとき
- サブコマンドなし起動時の `NoArgsIsHelpError` の扱い、`--help` 相当の挙動、終了コードの伝播を確認したいとき
- Typer / Click の例外を `CmocError` と共通エラーレポートへ変換する起動経路を確認したいとき
- `python src/main.py` で直接起動する経路の振る舞いを確認したいとき

## Do not read this when

- 各サブコマンド本体の処理内容だけを確認したいとき
- 共通エラー型やエラーレポートの整形だけを確認したいとき
- CLI の設計ルールや配置方針だけを確認したいとき
- サブコマンドごとの仕様断片だけを確認したいとき

## hash

- 0c76935e2e4d5e562d321e1b65e17c49e36e89415a7d311c6f037b13785a396f

# `sub_commands`

## Summary

- このディレクトリは `cmoc` の各サブコマンド実装を集めた入口です。
- `__init__.py`、`init.py`、`eval_oracles.py`、`apply/`、`session/` の役割分担をまとめています。
- 個別コマンドの実装本文へ進む前のルーティング目次です。

## Read this when

- `src/sub_commands` 配下にどのコマンド実装があるか俯瞰したいとき。
- `init`、`review oracles`、`apply`、`session` の入口を切り分けたいとき。
- どのファイルを先に読むべきか整理したいとき。

## Do not read this when

- `cmoc apply` や `cmoc session` の単一コマンドの詳細仕様だけを確認したいとき。
- `src/main.py` のコマンド登録や共通処理だけを追いたいとき。
- `src/commons` の共通基盤や `oracles` 配下の仕様断片だけを確認したいとき。

## hash

- 4be7079c1f7ac3c627cb68bdf0b618b63f954d3c0035506d7eb8b79eda4d863d
