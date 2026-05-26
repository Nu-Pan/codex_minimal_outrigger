# `commons`

## Summary

- `cmoc` 全体で共有する共通モジュール群をまとめたディレクトリです。
- `codex exec` 呼び出し、CLI 実行ラッパー、共通エラー整形、`INDEX.md` メンテナンス、git リポジトリ操作、サブコマンドログ、タイムスタンプ、経過時間計測を扱います。
- 各サブコマンド本体から再利用する基盤処理を集約し、個別機能の実装を薄く保つための入口です。

## Read this when

- サブコマンド間で共通に使う処理やユーティリティの置き場所を確認したいとき。
- `codex exec` 呼び出し、`INDEX.md` メンテナンス、git リポジトリ探索、ログ、エラー処理を修正・レビューしたいとき。
- タイムスタンプ生成や経過時間表示など、共通の補助機能の振る舞いを確認したいとき。

## Do not read this when

- 個別サブコマンドの引数解析や業務ロジックだけを確認したいとき。
- `oracles` 配下の正本仕様や `INDEX.md` 生成ルールそのものだけを確認したいとき。
- テストコードや CLI 入口だけで用が足り、共通ユーティリティの実装を追う必要がないとき。

## hash

- 13d39382c027993b930e21f4f1c0161df0684aaab010dbb99ffd1bd54ac97711

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

- `src/sub_commands` ディレクトリの入口です。cmoc の各サブコマンド実装をまとめ、`apply`、`session`、`eval-oracles`、`init` の本体モジュールとパッケージ定義への案内を行います。
- このディレクトリでは `apply.py`、`apply_join.py`、`apply_abandon.py`、`session_fork.py`、`session_join.py`、`session_abandon.py`、`init.py`、`eval-oracles.py`、`__init__.py` が対象です。
- 各モジュールは対応するコマンドの実行本体と状態検証、cleanup、merge、report 出力などを担当します。

## Read this when

- cmoc のサブコマンド実装全体の配置や役割分担を確認したいとき。
- `apply`、`session`、`init`、`eval-oracles` のどの実装モジュールを読むべきか判断したいとき。
- パッケージ境界や `src/sub_commands` 全体のルーティングを整えたいとき。
- サブコマンド共通の入口を把握してから個別実装へ進みたいとき。

## Do not read this when

- 個別サブコマンドの詳細仕様だけを確認したいときは、このディレクトリ全体ではなく対応する `*.py` を直接読むべきです。
- `src/sub_commands` ではなく、`commons` など別ディレクトリの共通機能を調べたいときはこの目次は適していません。
- コマンドの利用方法や正本仕様だけを確認したいときは、`oracles/app_specs/sub_commands/INDEX.md` 側を参照すべきです。
- `__init__.py` のような最小モジュール単体の役割だけを確認したいときは、対象ファイルを直接読むべきです。

## hash

- caef25ce36a8d0894178865f7c06a5d19d91b7ab7573cfa1b4ce0b96f42c6525
