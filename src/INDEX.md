# `commons`

## Summary

- `src/commons` にある cmoc 共通基盤モジュール群の入口です。CLI 実行制御、git リポジトリ操作、共通エラー整形、ログ、タイムスタンプ、経過時間計測、`INDEX.md` 生成・維持をまとめています。
- `command_runner.py` と `errors.py` はサブコマンド全体の実行制御と利用者向けエラーレポートを担います。
- `repo.py` は repo root 探索、ブランチ判定、session state、差分確認、`.cmoc` の無視保証、pathspec 単位の commit を扱います。
- `codex.py`、`indexing.py`、`subcommand_log.py`、`timestamps.py`、`timing.py` は Codex 呼び出し、INDEX 生成、tee ログ、時刻文字列、ステップ計測をそれぞれ担当します。

## Read this when

- `src/main.py` やサブコマンドから呼ぶ共通処理の置き場所と責務を確認したいとき。
- `codex exec` の共通ラッパー、Structured Output 検証、quota 待機、再試行の流れを追いたいとき。
- git リポジトリのルート探索、session / apply ブランチ判定、`.cmoc` の無視保証、未コミット差分や commit の扱いを確認したいとき。
- エラーレポート、ログ保存、タイムスタンプ、経過時間表示、`INDEX.md` の生成・維持ルールを実装・修正したいとき。

## Do not read this when

- 個別サブコマンドの引数解析や業務ロジックだけを確認したいときは、`src/sub_commands` 側を直接読むべきです。
- `cmoc` の利用手順やユーザー向けコマンド説明だけが目的なら、この共有モジュール群は優先して読む必要はありません。
- `oracles` 配下の正本仕様そのものを確認したいときは、この実装ディレクトリではなく該当する仕様文書を読むべきです。
- テストコードだけで足りる、または `src/commons/__init__.py` のパッケージ宣言だけを確認したいときは、この目次は不要です。

## hash

- 9d86b490f4830b214240c020d024532b0d5408d8a1bb52e09f0d16acdf5529dc

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

- このディレクトリには `cmoc` の各サブコマンド実装と `__init__.py` のパッケージ宣言がまとまっています。
- `apply.py` は要修正点リストの抽出、調査・修正ループ、`apply.state` 更新、レポート生成を担います。
- `apply_join.py` は完了済み apply branch を session branch へ取り込み、想定外差分や conflict を処理します。
- `apply_abandon.py` は未 join の apply run を破棄し、branch / worktree を片付けて `apply.state` を `ready` に戻します。
- `session_fork.py` は現在の local branch から session branch を作成し、session state を記録します。
- `session_join.py` は session branch を home branch へ merge し、conflict 解消と終了処理まで行います。
- `session_abandon.py` は session branch を merge せずに破棄し、状態を `abandoned` に更新します。
- `init.py` は `.cmoc` を git 追跡対象外にして初期化結果を commit します。
- `eval-oracles.py` は oracle スナップショットを評価し、部分評価または全体評価のレポートを作ります。

## Read this when

- `cmoc` の個別サブコマンド実装を修正・レビューしたいとき。
- apply 系と session 系の状態遷移や branch / worktree の違いを横断して確認したいとき。
- `init` や `eval-oracles` を含む CLI の振る舞いを実装側から追いたいとき。
- `src/sub_commands` でどのモジュールに処理があるか素早く見分けたいとき。
- `src/sub_commands` が Python パッケージとしてどう構成されているか確認したいとき。

## Do not read this when

- `cmoc` の仕様本文だけを確認したいときは、`oracles/app_specs/sub_commands` 側を読むべきです。
- 共通ユーティリティ、git 操作ヘルパー、状態ファイルの共通基盤だけを追いたいときは、`src/commons` を読むべきです。
- トップレベルの CLI ルーティングだけを知りたいときは、`src/main.py` を読むべきです。
- このディレクトリのうち特定の 1 モジュールだけを確認したいときは、`INDEX.md` ではなく該当ファイルを直接読むべきです。

## hash

- 70751717a8a9ca9642df349cc53c30117ea3bda6ad277fcc56dcc5f6d4f6149a
