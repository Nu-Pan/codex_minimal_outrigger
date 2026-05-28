# `commons`

## Summary

- cmoc 全体で使う共通ユーティリティをまとめたパッケージです。
- Codex CLI 呼び出し、サブコマンド実行制御、共通エラー整形、リポジトリ root / session state / apply state の扱いを含みます。
- サブコマンド単位のログ、経過時間計測、タイムスタンプ生成、`INDEX.md` のメンテナンス処理もここにあります。

## Read this when

- cmoc で共有される基盤処理の実装や修正をしたいとき。
- Codex CLI の実行ラッパー、Structured Output、リトライや quota 待ちの流れを確認したいとき。
- リポジトリルート探索、session/apply branch 判定、`session state` の読み書きや検証を追いたいとき。
- サブコマンドのログ記録、終了時レポート、タイムスタンプ、経過時間表示、`INDEX.md` 自動生成の入口を探したいとき。

## Do not read this when

- 個別サブコマンドの業務ロジックや CLI 引数だけを見たいときは、この配下ではなく `src/sub_commands` 側を読むべきです。
- `cmoc` の使い方や運用フロー全体を知りたいだけなら、共通基盤ではなく上位の正本仕様を参照すべきです。
- 特定の 1 ファイルだけの実装詳細を確認したいときは、`codex.py`、`repo.py`、`errors.py` など該当モジュールを直接読むべきです。
- テストコードや他パッケージの実装を探しているときは、このディレクトリではありません。

## hash

- 014e32c1d02449767ccbdd29d861e72734ca9f7f35bba3a1c090f466c4ef2614

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

- `src/sub_commands` は `cmoc` の個別サブコマンド実装の入口をまとめるディレクトリで、`apply`、`session`、`init.py`、`eval_oracles.py` へ案内します。
- このディレクトリを起点に、各サブコマンドの実装モジュールと、パッケージ入口としての `__init__.py` を整理できます。
- `cmoc review oracles` の本体実装もこの配下に含まれており、サブコマンド実装を横断して確認するための目次です。

## Read this when

- `src/sub_commands` 配下にどのサブコマンド実装があり、それぞれどの入口へ進むべきかを整理したいとき。
- `cmoc apply`、`cmoc session`、`cmoc init`、`cmoc review oracles` の実装入口をまとめて把握したいとき。
- サブコマンドごとの責務分担や、どのモジュールがどのコマンドを担当しているかを素早く確認したいとき。

## Do not read this when

- 個別のサブコマンド仕様だけを確認したいときは、この目次ではなく `apply`、`session`、`init.py`、`eval_oracles.py` それぞれの正本仕様や実装を直接読むべきです。
- `cmoc` 全体の共通規約、branch model、ログ、エラーハンドリングなど、`src/sub_commands` 以外の共通仕様だけを確認したいときは、このディレクトリを読む必要はありません。
- 実装コードやテストコードの修正だけで足りるときは、この目次を読む必要はありません。

## hash

- 1f52714a72fe72585fce56277cc29d296e120729fe967fa152699da448c3bf77
