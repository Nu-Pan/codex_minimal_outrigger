# `commons`

## Summary

- `src/commons` は cmoc の共通処理をまとめた Python パッケージの入口です。
- Codex CLI 呼び出し、`INDEX.md` 生成、リポジトリ探索、共通エラー整形、サブコマンドログ、タイムスタンプ、計時の補助モジュールが入っています。
- サブコマンド本体ではなく、複数の機能から再利用する横断的な基盤ロジックを読むための目次です。

## Read this when

- `codex exec` 呼び出し、Structured Output、`INDEX.md` メンテナンスの共通処理を確認したいとき。
- リポジトリルート探索、`session` / `apply` 系ブランチ判定、session state 周辺の共通処理を確認したいとき。
- 共通エラー整形、サブコマンドログ、タイムスタンプ、経過時間表示の実装を見直したいとき。

## Do not read this when

- 個別サブコマンドの引数解析や業務ロジックだけを確認したいときは、`src/sub_commands` 側を読むべきです。
- `INDEX.md` の自動生成ルールや `oracles` 側の正本仕様だけを確認したいときは、この配下を読む必要はありません。
- テスト実装だけを追いたいときは、`tests` 側を確認すべきです。

## hash

- 4063ff50c5df71f21ad447f56991a248512bb0eeba1ba2bb127ce71e57241221

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

- `src/sub_commands` は cmoc のサブコマンド実装の入口です。
- `apply` と `session` はそれぞれ独立したパッケージで、配下の `INDEX.md` から個別実装へ進めます。
- `init.py` は `cmoc init`、`eval_oracles.py` は `cmoc review oracles` の本体で、`__init__.py` はパッケージ宣言だけを担います。

## Read this when

- cmoc のサブコマンド実装全体の入口を確認したいとき。
- `apply` や `session` のような複数ファイルの実装群と、`init.py` / `eval_oracles.py` の単体モジュールを見分けたいとき。
- どのサブコマンド実装へ進むべきか、この目次から判断したいとき。

## Do not read this when

- CLI の起動口やコマンド登録全体を確認したいときは、このディレクトリではなく `src/main.py` を読むべきです。
- 個別サブコマンドの利用手順や正本仕様だけを確認したいときは、`oracles/app_specs/sub_commands/` 側の文書を直接読むべきです。
- 共通処理やリポジトリ操作、エラー整形などの横断的な仕組みを確認したいときは、`src/commons/` 側を読むべきです。

## hash

- b85279da3ae168cf8cdcae3a0d1ff5f4f27367ee9ca0de1349198c27da5150ac
