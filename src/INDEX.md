# `commons`

## Summary

- `src/commons` は cmoc 全体で共有する基盤モジュール群で、CLI 起動、エラー処理、リポジトリ操作、ログ、タイムスタンプ、計測、レポート保存を担う。
- `__init__.py` は `src.commons` パッケージを宣言するだけの最小モジュール。
- `codex.py` は `codex exec` のコマンド組み立て、Structured Output の検証、再試行、実行ログ保存、`INDEX.md` 事前メンテナンスを扱う。
- `command_runner.py` は Typer サブコマンドの共通実行制御とエラー表示、終了コード処理をまとめる。
- `errors.py` は `CmocError` と stdout 向けの標準エラーレポート整形を提供する。
- `indexing.py` は `INDEX.md` の自動生成・再生成・更新判定・自動コミットを担う。
- `repo.py` は repo root 探索、branch/HEAD 取得、session/apply 状態、差分・削除検出の共通処理を担当する。
- `report_files.py` は timestamp 付き Markdown レポートを排他的に作成して保存する。
- `subcommand_log.py` はサブコマンド単位の JSON Lines ログと quota 待ち時間の管理を行う。
- `timestamps.py` は cmoc 仕様の `<time-stamp>` 文字列を生成・判定する。
- `timing.py` はサブコマンドと各ステップの経過時間計測と表示を担当する。

## Read this when

- 共通実装の入口を探したいときは `src/commons` 全体を読む。
- `codex exec` の起動、Structured Output の検証、再試行、`INDEX.md` 事前処理を確認したいときは `codex.py` を読む。
- Typer サブコマンドの共通ラッパーや終了コード処理を確認したいときは `command_runner.py` を読む。
- 共通例外や利用者向けのエラーレポート形式を確認したいときは `errors.py` を読む。
- `INDEX.md` の自動生成ロジックや更新条件を確認したいときは `indexing.py` を読む。
- repo root 探索、branch 判定、session/apply 状態、git 差分操作を確認したいときは `repo.py` を読む。
- サブコマンドの JSON Lines ログや quota 待ち時間を確認したいときは `subcommand_log.py` を読む。
- タイムスタンプ生成・判定や step 時間計測を確認したいときは `timestamps.py` と `timing.py` を読む。
- タイムスタンプ付き Markdown レポートの保存だけを確認したいときは `report_files.py` を読む。

## Do not read this when

- 個別サブコマンドの業務ロジックだけを追いたいときは、この共通層ではなく `src/sub_commands` を読む。
- `oracles` の個別仕様や操作手順を直接確認したいときは、`src/commons` ではなく該当する oracle 文書を読む。
- 実装コードの細部ではなく、CLI の使い方や作業フローだけを知りたいときは、別の案内文書を優先する。
- テストだけを修正したいときは、ここでなく `tests` 側の対象モジュールを読む。
- package 入口だけを確認したいときは `__init__.py` 以外を読む必要はない。

## hash

- 1483bfa49beb674d5b9fc0c7e5f3419bcd3638acdc7cd5c9de12e5c86aaa1a21

# `main.py`

## Summary

- cmoc CLI のエントリーポイントで、Typer のルート `app` と `session` / `apply` / `review` の各サブアプリを組み立てるファイルです。
- `init`、`session`、`apply`、`review` の各コマンド登録に加えて、`eval-oracle` / `eval-oracles` の隠し別名や、`apply fork` の繰り返し回数・`scope`、`apply join` の `--force-resolve` などの既定値をまとめています。
- サブコマンド未指定時の `CmocError` 生成、補完プローブ時の分岐、Click/Typer 例外の共通整形、`python src/main.py` 直実行の起動経路を扱います。

## Read this when

- cmoc CLI の起動点と、`session` / `apply` / `review` のサブアプリ構成を確認したいとき。
- `init`、`session fork/join/abandon`、`apply fork/join/abandon`、`review oracles` の登録名、隠し別名、既定オプションを確認したいとき。
- サブコマンド未指定時の利用者向けエラー、補完プローブ時の分岐、Click/Typer 例外の共通整形を追いたいとき。
- `python src/main.py` で直接起動する経路と、そのときの例外処理を確認したいとき。

## Do not read this when

- `src/sub_commands/` 配下の各サブコマンド本体の実装だけを追いたいとき。
- `commons.errors` のエラー型や `format_error_report()` の整形ロジックだけを確認したいとき。
- `INDEX.md` の生成ルールや `oracles` 側のルーティング方針だけを確認したいとき。

## hash

- 34ab9fdae7d4622e261437958669dd52ce211f233a2300c1c7c831efc256c365

# `sub_commands`

## Summary

- `src/sub_commands` は `cmoc` の各サブコマンド実装を束ねる入口ディレクトリです。
- `__init__.py` はパッケージ宣言のみを担い、`init.py` は `cmoc init`、`eval_oracles.py` は `cmoc review oracles` の本体です。
- `apply`、`review`、`session` は各サブコマンド群の目次ディレクトリで、さらに個別実装へ案内します。

## Read this when

- `src/sub_commands` 配下のどの実装ファイルへ進むべきかを整理したいとき。
- `cmoc init`、`cmoc review oracles`、`cmoc apply`、`cmoc session` の入口を素早く把握したいとき。
- 入口ディレクトリとしての役割分担だけを確認したいとき。

## Do not read this when

- 個別コマンドの詳細仕様、状態遷移、例外条件を確認したいときは、この目次ではなく該当ファイルを直接読むべきです。
- `apply`、`review`、`session` の内部実装や正本仕様の細部を追いたいときは、このディレクトリ全体の目次だけでは足りません。
- `src/sub_commands/__init__.py` のパッケージ宣言だけを確認したいときは、この目次ではなく `__init__.py` を直接読むべきです。

## hash

- 8e41b065faaaaf433b4bfabe1ffc0f91797eccb5f53c44df5e4268faa681fb2e
