# `commons`

## Summary

- `cmoc` 全体で使う共通ユーティリティをまとめたパッケージです。
- Codex CLI 実行、コマンド共通制御、エラー整形、git / session state 操作、サブコマンドログ、タイマー、タイムスタンプ、`INDEX.md` メンテナンスを含みます。
- 個別サブコマンドではなく、横断処理の土台を探す入口です。

## Read this when

- cmoc 全体で共有する共通基盤の実装や修正をしたいときに読むべきです。
- Codex CLI の実行ラッパー、Structured Output、リトライや quota 待ちの流れを確認したいときに読むべきです。
- repo root 探索、session / apply state、branch 判定、サブコマンドログ、経過時間、タイムスタンプ、`INDEX.md` 更新を追いたいときに読むべきです。
- サブコマンドの共通実行制御やエラー表示を実装・レビューしたいときに読むべきです。

## Do not read this when

- 個別サブコマンドの引数や業務ロジックを確認したいときは、この配下ではなく `src/sub_commands` を読むべきです。
- cmoc の使い方や運用フロー全体を知りたいだけなら、この配下ではなく上位の正本仕様を読むべきです。
- 1 つの機能だけを深掘りしたいときは、このディレクトリ全体ではなく該当モジュールだけを読むべきです。
- テストコードや別パッケージの実装を探しているときは、この配下ではありません。

## hash

- 4685f1abb42cd0edd196b0a8eca7f3d6a5d26174b7d42771c2cc34845f58e1c1

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

- `src/sub_commands` は cmoc の個別サブコマンド実装をまとめる入口ディレクトリです。
- `apply` と `session` の各パッケージ、`init.py`、`eval_oracles.py`、`__init__.py` を案内し、各コマンド本体へのルーティングを担います。
- `cmoc init` と `cmoc review oracles` もここから辿れるため、サブコマンド横断の起点として使います。

## Read this when

- `src/sub_commands` 配下にどの実装があるかを整理したいとき。
- `cmoc apply`、`cmoc session`、`cmoc init`、`cmoc review oracles` の実装入口をまとめて確認したいとき。
- `apply` / `session` のパッケージ構造と、`__init__.py` を含む配置関係を把握したいとき。
- 個別モジュールへ進む前に、サブコマンド横断の役割分担を俯瞰したいとき。

## Do not read this when

- `cmoc apply`、`cmoc session`、`cmoc init`、`cmoc review oracles` の個別処理や引数仕様を深く追いたいときは、ここではなく該当モジュールや正本仕様を読むべきです。
- `src/commons` の共通ユーティリティや基盤処理だけを確認したいときは、このディレクトリではありません。
- `oracles` の正本仕様や `INDEX.md` 更新ルールだけを確認したいときは、この目次ではなく `oracles` 側を読むべきです。
- CLI の起動経路やサブコマンド登録だけを見たいときは、この目次ではなく `src/main.py` を読むべきです。

## hash

- bec6f0120bfe7a20606209e7b41b1fcd348c238df3beb541ef00c4886999cce0
