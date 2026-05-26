# `commons`

## Summary

- `cmoc` 全体で共通利用するユーティリティ群をまとめたディレクトリです。
- エラー処理、サブコマンド実行制御、git リポジトリ操作、tee ログ、経過時間計測、タイムスタンプ生成、Codex CLI ラッパー、INDEX 生成処理を収録します。
- 各サブコマンドから横断的に使う機能をここに集約し、個別コマンド本体を薄く保つ役割を持ちます。

## Read this when

- サブコマンド間で共通に使う処理を実装・修正したいとき。
- エラー整形、実行制御、リポジトリ探索、ログ、経過時間計測、タイムスタンプ、Codex CLI 呼び出し、INDEX 管理の共通基盤を確認したいとき。
- 複数モジュールから参照される共通関数や定数の置き場所を探したいとき。

## Do not read this when

- 個別サブコマンドの業務ロジックや引数処理だけを確認したいとき。
- `app_specs` 配下のユーザー向け仕様や、`oracles` の正本断片だけを追いたいとき。
- `INDEX.md` の生成ルールそのものを確認したいとき。

## hash

- 9dbb3e1b1f3f2b7c32823d1e1971f975f74dc695ffebe2f0bea0ca5f588255f4

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

- `src/sub_commands` は `cmoc` のサブコマンド実装を集めたディレクトリで、`apply`、`session`、`eval-oracles`、`init` の各本体モジュールと `__init__.py` を含みます。
- `apply.py` は `cmoc apply` の入口で、`apply_abandon.py` と `apply_join.py` は `apply` の破棄・結合処理を分担します。
- `session_fork.py`、`session_join.py`、`session_abandon.py` は session 系の開始・統合・破棄を担い、`eval-oracles.py` と `init.py` は評価実行と初期化を担当します。

## Read this when

- `cmoc` の個別サブコマンドの実装本体を探したいとき。
- `apply` 系と `session` 系の処理を分けて把握したいとき。
- `eval-oracles` や `init` の入口モジュールの場所と役割を確認したいとき。
- `src/sub_commands` 配下で新しいサブコマンド実装や関連モジュールを追加・整理したいとき。

## Do not read this when

- 共通ルールや仕様断片だけを確認したいときは、`oracles/app_specs/INDEX.md` か該当の仕様本文を読むべきです。
- CLI の利用方法や作業手順だけを知りたいときは、`oracles/app_specs/usage.md` を優先すべきです。
- `INDEX.md` の生成・更新ルールそのものを確認したいときは、`oracles/app_specs/indexing.md` を読むべきです。
- 実装コードではなくテストや共通ライブラリだけを追いたいときは、このディレクトリの案内より該当箇所を直接見るべきです。

## hash

- 6d9d02380062d83131c0d9b60ffa383258f599bec99fc6533b5ec318c3be3d23
