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

- `cmoc` のサブコマンド実装をまとめたパッケージの入口です。`__init__.py` と、`apply.py`、`apply_abandon.py`、`apply_join.py`、`eval-oracles.py`、`init.py`、`session_abandon.py`、`session_fork.py`、`session_join.py` への案内をまとめます。
- 各モジュールは `cmoc apply`、`cmoc session`、`cmoc eval-oracles`、`cmoc init` などの本体実装を担当し、この目次から目的の実装へ直接進めます。
- サブコマンドごとの実行フローや前提条件を確認する前段として、どのファイルに仕様・実装があるかを整理するための入口です。

## Read this when

- `src/sub_commands` 配下にどのサブコマンド実装があるかをひと目で把握したいとき。
- `apply`、`session`、`eval-oracles`、`init` など、各サブコマンドの実装ファイルへどれを開けばよいか判断したいとき。
- パッケージレベルの入口として、`__init__.py` と各コマンド実装の役割分担を確認したいとき。
- このディレクトリ全体の構成を起点に、個別モジュールへ順番にたどりたいとき。

## Do not read this when

- 個別のサブコマンド実装を確認したいときは、この目次ではなく該当する `*.py` を直接読むべきです。
- `cmoc` 全体の共通仕様や `oracles` 側の正本仕様だけを確認したいときは、このディレクトリの入口ではなく対応する仕様文書を読むべきです。
- 共有処理や `commons` 配下のユーティリティだけを追いたいときは、このパッケージの目次は遠回りです。
- `INDEX.md` の生成ルールそのものだけを確認したいときは、`oracles/app_specs/indexing.md` を読むべきです。

## hash

- 1051289e1ea695fe09f64f5257e3856651f029a1bcdbb0d824e12d97205ef8ab
