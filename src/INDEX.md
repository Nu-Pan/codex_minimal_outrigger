# `commons`

## Summary

- `src/commons` 配下の共通処理をまとめるパッケージの目次です。
- `codex.py`、`command_runner.py`、`errors.py`、`indexing.py`、`repo.py`、`subcommand_log.py`、`timestamps.py`、`timing.py`、`__init__.py` への入口をまとめます。
- 個別サブコマンドではなく、CLI 実行・エラー処理・git / session state・ログ・時刻・`INDEX.md` 生成の共通基盤を案内します。

## Read this when

- cmoc 全体で共有する共通処理の所在を一覧で確認したいとき。
- Codex CLI 呼び出し、共通実行ラッパー、エラー整形、repo / session state、サブコマンドログ、タイムスタンプ、経過時間計測、INDEX.md 生成のどこを読むべきか整理したいとき。
- 実装やテストの前に、共通基盤の担当範囲を俯瞰したいとき。

## Do not read this when

- 個別サブコマンドの引数や業務ロジックだけを確認したいとき。
- `src/sub_commands` 配下の実装や利用手順だけを追いたいとき。
- 共通機能 1 つだけを深掘りしたいときは、この目次ではなく該当モジュールを直接読むべきです。

## hash

- 29697e9faea611decf72d6d9710cd92d63b86942c759e470f559851d8e31e420

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
- `cmoc` の各サブコマンド入口がどのモジュールに分かれているかを整理したいとき。
- 実装やテストを始める前に、`src/sub_commands` のルーティング先を確認したいとき。

## Do not read this when

- `cmoc init`、`cmoc review oracles`、`cmoc session`、`cmoc apply` の個別仕様や引数を深掘りしたいとき。
- `src/sub_commands/apply` や `src/sub_commands/session` のような下位ディレクトリの詳細だけを確認したいとき。
- `src/sub_commands/__init__.py` や `init.py` など、単一モジュールの実装詳細を直接追いたいとき。

## hash

- fdbffe7e51ba851768982b2119b7770127da46267940ede1ea27a115ba57f37a
