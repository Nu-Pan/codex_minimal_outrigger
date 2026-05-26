# `commons`

## Summary

- `cmoc` の複数サブコマンドから共通利用する基盤処理をまとめたディレクトリです。
- Codex CLI 呼び出し、サブコマンド実行ラッパー、共通エラー、リポジトリ操作、INDEX 生成、ログ、タイムスタンプ、経過時間計測などを収録します。
- 個別サブコマンドの本体ではなく、横断的に使う共通機能の入口として参照します。

## Read this when

- 複数サブコマンドで共有する処理の実装や修正を確認したいとき。
- `codex` 呼び出し、共通エラー処理、リポジトリ操作、ログ、タイムスタンプ、計測などの基盤機能を確認したいとき。
- 共有処理をどこに置くべきか、`src/commons` の責務を整理したいとき。
- `INDEX.md` を維持するための共通ロジックや、その周辺の仕様を確認したいとき。

## Do not read this when

- 個別サブコマンドの業務ロジックだけを確認したいとき。
- `src/main.py` や `src/sub_commands` の引数解析やコマンド分岐だけを確認したいとき。
- 特定の共通ユーティリティ 1 つの実装詳細だけを追いたいときは、このディレクトリではなく該当モジュールを直接読むべきです。
- `INDEX.md` の生成・更新ルールだけを確認したいときは、このディレクトリではなく `indexing.md` を読むべきです。

## hash

- 068b1f29203afabc1ce1c75e56dbb1d91ea9a45417f673a2b4d5223ad15f5f76

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
