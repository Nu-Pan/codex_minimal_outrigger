# `commons`

## Summary

- `cmoc` の共通処理をまとめた `src/commons` の入口です。
- リポジトリルート探索、共通エラー処理、サブコマンドログ、経過時間計測、タイムスタンプ生成、git 補助、Codex 呼び出し、`INDEX.md` 生成・維持を扱います。
- 個別サブコマンドから横断的に使う基盤機能の参照先を整理するための目次です。

## Read this when

- cmoc の共通処理の役割分担や、どのモジュールを参照すべきかを確認したいとき。
- `enter_repo_root`、`run_command`、`subcommand_log`、`StepTimer` などの横断的な実行基盤を扱いたいとき。
- Codex CLI 呼び出し、エラー整形、タイムスタンプ生成、git リポジトリ操作、セッション state の共通ロジックを追いたいとき。
- `INDEX.md` の維持や、共通ユーティリティ群の入口をまとめて把握したいとき。

## Do not read this when

- 個別サブコマンドの業務ロジックだけを確認したいときは、`src/sub_commands` 側を読むべきです。
- 特定の 1 モジュールの実装だけを追いたいときは、`src/commons` 全体ではなく該当ファイルを直接読むべきです。
- CLI 引数定義やユーザー向けの操作手順だけを確認したいときは、この共通層の案内は不要です。
- `INDEX.md` の生成ルールそのものだけを確認したいときは、`src/commons/indexing.py` を読むべきです。

## hash

- 4eb013e822bbbbcddea07fde9d88540ce737d4f4e8fa705c843c22c044c07835

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

- `src/sub_commands` 配下のサブコマンド実装をまとめる入口です。
- `apply` 系、`session` 系、`eval-oracles`、`init`、およびパッケージ宣言用の `__init__.py` への案内をまとめます。
- 個別サブコマンドの詳細仕様や実装本文へ進むための目次として使います。

## Read this when

- `src/sub_commands` 配下の各サブコマンド実装への入口をまとめて把握したいとき。
- `apply.py`、`apply_abandon.py`、`apply_join.py`、`eval-oracles.py`、`init.py`、`session_abandon.py`、`session_fork.py`、`session_join.py` のどれを読むべきか整理したいとき。
- `cmoc` のサブコマンド実装の配置方針や、各モジュールの役割分担を確認したいとき。
- `src/sub_commands` パッケージ全体のルーティング文書を作成・更新したいとき。

## Do not read this when

- このディレクトリの入口だけで足りるときは、個別モジュールを読む必要はありません。
- `cmoc apply`、`cmoc session fork/join/abandon`、`cmoc eval-oracles`、`cmoc init` の具体的な挙動だけを確認したいときは、対応する `.py` を直接読むべきです。
- `src/commons` の共通処理や `oracles` 側の正本仕様だけを確認したいときは、この目次ではなく該当ディレクトリの文書を読むべきです。
- パッケージ宣言の有無だけを確認したいときは、`__init__.py` のみで十分です。

## hash

- ea28ddc1a74a2ed2f0f380319aa205af80e16e975be05c3ed53d8ae4ef3cff6b
