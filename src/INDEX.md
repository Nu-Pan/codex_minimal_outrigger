# `commons`

## Summary

- `cmoc` の各サブコマンドから共有される基盤処理をまとめたディレクトリです。
- `codex.py`、`command_runner.py`、`errors.py`、`indexing.py`、`repo.py`、`subcommand_log.py`、`timestamps.py`、`timing.py` など、実行制御・エラー・ログ・計測・リポジトリ操作・INDEX 管理を担う共通機能を収録します。
- 個別サブコマンドを薄く保ち、横断的な処理を集約するための共通層です。

## Read this when

- サブコマンド間で共通利用する処理の置き場所や役割分担を確認したいとき。
- `codex exec` のラッパー、共通エラー、repo ルート探索、ログ tee、タイミング計測、タイムスタンプ生成、INDEX 管理を扱いたいとき。
- CLI 実装やレビューで、処理を `src/commons` に寄せるべきか判断したいとき。

## Do not read this when

- 個別サブコマンドの業務ロジックだけを追いたいときは、`src/sub_commands` 側を読むべきです。
- `oracles` の正本仕様やユーザー向け手順だけを確認したいときは、このディレクトリではなく該当文書を読むべきです。
- `src/commons` のうち特定 1 モジュールだけを確認したいときは、`command_runner.py` などの個別ファイルを直接読むべきです。

## hash

- 1a24cc72da5b59d07fedc3a28e9c5abd78a16fa078bd1f214af8bdd31dac9949

# `main.py`

## Summary

- `cmoc` CLI の Typer エントリーポイントで、`init`、`session`、`apply`、`eval-oracles` のトップレベルルーティングを定義します。
- `session fork/join/abandon` と `apply fork/join/abandon` の CLI 入口を登録し、各サブコマンド実装への委譲をまとめています。
- `eval-oracles` は `src/sub_commands/eval-oracles.py` を動的読み込みし、互換の `eval-oracle` hidden alias も含めています。
- `main()` は Typer / Click の例外を `cmoc` 形式のエラーレポートへ変換し、`python src/main.py` の直接起動経路も担います。

## Read this when

- `cmoc` のトップレベルコマンド登録と、`init`、`session`、`apply`、`eval-oracles` のルーティング構成を確認したいとき。
- `session fork/join/abandon` や `apply fork/join/abandon` の CLI 入口がどこで登録されているかを確認したいとき。
- `eval-oracles` の動的読み込みや、互換用の hidden alias `eval-oracle` の扱いを確認したいとき。
- `NoArgsIsHelpError` を含む Typer / Click の例外を、`cmoc` 形式のエラーレポートへ変換する流れや、`python src/main.py` での直接起動経路を確認したいとき。

## Do not read this when

- 各サブコマンド本体の業務ロジックや状態遷移だけを確認したいときは、`src/sub_commands` 配下の該当モジュールを読むべきです。
- 共通エラー整形の内部実装や、`commons.errors` の詳細だけを追いたいときは、このファイルではなく共通モジュールを読むべきです。
- `cmoc` の利用手順や `oracles` 側の正本仕様だけを確認したいときは、この CLI  प्रवेश点ではなく該当文書を読むべきです。
- `apply` や `session` の個別処理そのものを見たいだけで、トップレベルのルーティングや起動処理が不要なときは読む必要がありません。

## hash

- 1d39a93edfb5c7866f8de10ccc4cb645f39cf6684d9ede63ee90507bed1e7431

# `sub_commands`

## Summary

- `cmoc` のサブコマンド実装の入口をまとめたディレクトリです。
- `apply` 系、`session` 系、`init`、`eval-oracles` の各コマンド本体と、その周辺の専用処理が入っています。
- 各コマンドの細かな仕様本文は `oracles/app_specs/sub_commands` 側にあり、このディレクトリはそれを実装する側の入口として使います。

## Read this when

- `cmoc apply`、`cmoc apply abandon`、`cmoc apply join` の実装・修正・テスト・レビューを行うとき。
- `cmoc session fork`、`cmoc session join`、`cmoc session abandon` の実装・修正・テスト・レビューを行うとき。
- `cmoc init` や `cmoc eval-oracles` のサブコマンド本体の振る舞いを確認したいとき。
- サブコマンド間の責務分担や、各コマンドがどの処理を担当するかを整理したいとき。

## Do not read this when

- 共通の Git/Repository ヘルパーや `commons` 側の実装だけを確認したいときは、このディレクトリではなく対応する共通モジュールを読むべきです。
- `oracles` の仕様本文や `INDEX.md` の生成ルールだけを確認したいときは、このディレクトリではなく `oracles` 配下の正本仕様を読むべきです。
- サブコマンドの外側にある CLI 起動・引数解釈・設定値だけを追いたいときは、このディレクトリを読む必要はありません。

## hash

- 419c2f8b95e25475525f2ab52a148360e56aef8b9e2f56fbbeb0577f548c4653
