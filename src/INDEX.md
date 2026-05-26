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

- このディレクトリは、`cmoc` の各サブコマンド実装をまとめた配置先で、CLI から呼ばれる本体処理が集まっています。
- `apply.py` は `cmoc apply` の本体で、`apply_abandon.py` と `apply_join.py` が破棄と取り込みの処理を担当します。
- `session_fork.py`、`session_join.py`、`session_abandon.py` は session の開始・統合・破棄を担当します。
- `eval-oracles.py` は `oracles` 断片の評価処理、`init.py` は初期化処理、`__init__.py` はパッケージ入口です。

## Read this when

- `cmoc` のサブコマンド実装がどのファイルにあるかを確認したいとき。
- `apply`、`session`、`eval-oracles`、`init` の本体処理を実装・修正・レビューしたいとき。
- サブコマンド間の責務分割や、新しいコマンド追加時の配置方針を整理したいとき。
- `__init__.py` を含むこのディレクトリ配下の役割をまとめて把握したいとき。

## Do not read this when

- 利用方法や操作順だけを確認したいときは、このディレクトリではなく `oracles/app_specs/usage.md` を読むべきです。
- 個別サブコマンドの詳細仕様だけを確認したいときは、対応する `oracles/app_specs/sub_commands/*.md` を直接読むべきです。
- branch 管理、ログ出力、エラーハンドリング、INDEX 生成ルールなどの共通仕様だけを確認したいときは、このディレクトリではなく上位の仕様文書を読むべきです。
- `INDEX.md` の生成・更新ルールだけを確認したいときは、`oracles/app_specs/indexing.md` を読むべきです。

## hash

- 2b1e12b9cc6aa77376d7e541771ebf9870a753e2175624b008151faf36d14f19
