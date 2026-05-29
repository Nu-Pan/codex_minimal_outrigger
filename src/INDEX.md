# `commons`

## Summary

- cmoc 全体で共有する共通処理をまとめたディレクトリで、git / repository 周りの基盤、session / apply state、エラー処理、ログ、計測、タイムスタンプ、Codex CLI 呼び出し補助を収めています。
- 個別コマンドの実装そのものではなく、CLI 全体で再利用する基盤モジュール群への入口です。

## Read this when

- `src/commons` 配下の共通ユーティリティ全体を把握したいとき。
- repo root 探索、session/apply state、branch 判定、runtime pid などの共通状態管理を確認したいとき。
- 共通エラー整形、サブコマンドログ、経過時間計測、タイムスタンプ生成を確認したいとき。
- Codex CLI 呼び出しの共通処理、Structured Output の検証、quota 待機、capacity 再試行、`INDEX.md` 事前メンテナンスを確認したいとき。

## Do not read this when

- 個別サブコマンドの業務ロジック、CLI 引数、状態遷移だけを確認したいとき。
- `oracles` 配下の正本仕様や `app_specs` の操作手順だけを確認したいとき。
- テストコードや他ディレクトリの実装を探したいとき。

## hash

- 04dd5f44c7f801cc33c4ccb1b74836b90451863465dc3593b02314b7926e65b0

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

- `src/sub_commands` 配下のサブコマンド実装全体を案内する入口です。
- `__init__.py`、`init.py`、`eval_oracles.py`、`apply/`、`session/` への導線をまとめる目次として使います。
- 個別コマンドの詳細は各モジュールまたは下位ディレクトリの `INDEX.md` を参照します。

## Read this when

- `src/sub_commands` 配下にどのサブコマンド実装があるかを一覧で把握したいとき。
- `cmoc` の各サブコマンド入口がどのモジュールやディレクトリに分かれているかを整理したいとき。
- 実装やテストを始める前に、`src/sub_commands` のルーティング先を確認したいとき。

## Do not read this when

- `cmoc init`、`cmoc review oracles`、`cmoc apply`、`cmoc session` の個別仕様や引数だけを確認したいとき。
- `src/sub_commands/apply` や `src/sub_commands/session` の下位実装だけを深く追いたいとき。
- `src/sub_commands/__init__.py` や `init.py` など、単一モジュールの実装詳細を直接見たいとき。

## hash

- 2951c538a564c07d8a5652a32655d2d30b7752961cae421a9bb0424eaeaa3f09
