# `commons`

## Summary

- cmoc 全体で共有する実行基盤をまとめたディレクトリです。
- Codex CLI 呼び出し、共通エラー整形、repo root / branch / session state 操作、サブコマンドログ、経過時間計測、タイムスタンプ生成、INDEX.md メンテナンスを扱います。
- 個別サブコマンドではなく、複数機能から再利用される共通部品の入口です。

## Read this when

- Codex CLI 呼び出し、Structured Output 検証、quota 待機や再試行の共通処理を確認したいとき。
- repo root 探索、branch 判定、session/apply state、git 操作補助を確認したいとき。
- 共通エラー表示、サブコマンドログ、経過時間計測、タイムスタンプ、INDEX.md 自動生成の仕組みを追いたいとき。

## Do not read this when

- 個別サブコマンドの業務ロジックや CLI 引数だけを確認したいとき。
- `src/commons` の特定モジュールだけを直接見たいときは、この目次ではなく該当ファイルを読むべきです。
- `src` 配下の別機能や `tests` の実装だけを追いたいとき。

## hash

- e3dc47e0b9023b8290ec846676040ffde9c76196984d9bfc9120e260536bc102

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

- `src/sub_commands` は `cmoc` の各サブコマンド実装をまとめるディレクトリです。
- 配下にはパッケージ宣言用の `__init__.py`、`cmoc apply` 系の `apply` ディレクトリ、`cmoc session` 系の `session` ディレクトリ、`cmoc init` の本体である `init.py`、`cmoc review oracles` の本体である `eval_oracles.py` があります。
- この目次は、個別処理の詳細へ進む前に、どのファイルがどのコマンドの入口かを整理するための案内です。

## Read this when

- `src/sub_commands` 配下にどのサブコマンド実装が置かれているかを俯瞰したいとき。
- `apply`、`session`、`init.py`、`eval_oracles.py` の入口をたどって、必要な実装モジュールへ素早く移動したいとき。
- `cmoc` のサブコマンド実装全体の構成と、パッケージ入口・個別コマンド本体の役割分担を確認したいとき。

## Do not read this when

- `cmoc apply` 系や `cmoc session` 系の個別サブコマンドの詳細仕様だけを確認したいときは、この目次ではなく各モジュールの `INDEX.md` や実装本体を読むべきです。
- `cmoc init` や `cmoc review oracles` の処理順、状態遷移、エラー処理だけを追いたいときは、このディレクトリ全体の目次ではなく該当する実装ファイルを直接読むべきです。
- `src.sub_commands` のパッケージ宣言だけを確認したいときは、ここではなく `__init__.py` だけを見れば足ります。

## hash

- ef3a5df20f37dd34383d161d097026457912ca1b3602c0ad90d5cfe5c0d346c4
