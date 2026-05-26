# `commons`

## Summary

- `src/commons` 配下の共通モジュール群の入口です。リポジトリ探索、共通エラー、Codex CLI 呼び出し、サブコマンド実行制御、ログ、タイミング、タイムスタンプ生成をまとめています。
- `command_runner.py`、`codex.py`、`errors.py`、`repo.py`、`subcommand_log.py`、`timing.py`、`timestamps.py` など、`cmoc` の複数サブコマンドで再利用する処理が入っています。
- `INDEX.md` はこの共有基盤のどのファイルを読むべきかを案内するための目次です。

## Read this when

- 複数のサブコマンドにまたがる共通処理の置き場所や役割分担を確認したいとき。
- `cmoc` の実行制御、エラー整形、リポジトリ探索、ログ出力、経過時間表示、タイムスタンプ生成のどのモジュールを読むべきか判断したいとき。
- 共通処理を追加・修正するときに、既存の `commons` モジュールを横断して確認したいとき。

## Do not read this when

- 個別サブコマンドの業務ロジックだけを確認したいときは、`src/sub_commands` 側を読むべきです。
- ユーザー向けの使い方やコマンド一覧だけを知りたいときは、`src/main.py` や別の案内文書を参照すべきです。
- この配下の特定モジュールの実装だけを追いたいときは、`INDEX.md` ではなく該当する `*.py` を直接読むべきです。

## hash

- c31ef5af71410891f8e5679789bab0b0a512ab9fcda58c33c80458e9d84f8869

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

- `src/sub_commands` 全体の入口だけで足りるときは、個別モジュールを読む必要はありません。
- `cmoc apply`、`cmoc session fork/join/abandon`、`cmoc eval-oracles`、`cmoc init` の具体的な挙動だけを確認したいときは、対応する `.py` を直接読むべきです。
- `src/commons` の共通処理や `oracles` 側の正本仕様だけを確認したいときは、この目次ではなく該当ディレクトリの文書を読むべきです。
- パッケージ宣言の有無だけを確認したいときは、`__init__.py` のみで十分です。

## hash

- 3f8e0c5c3b6179230b9508d97dbac3d826a6d0e72d918457c247a56206b03859
