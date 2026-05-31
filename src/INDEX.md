# `commons`

## Summary

- `src/commons` は、cmoc 全体で共有する基盤処理をまとめたディレクトリです。
- ここには `codex.py`、`command_runner.py`、`errors.py`、`indexing.py`、`repo.py`、`report_files.py`、`subcommand_log.py`、`timestamps.py`、`timing.py` があり、Codex 呼び出し、リポジトリ操作、エラー整形、`INDEX.md` 管理、ログ保存、時間表示を担当します。
- 個別のサブコマンドよりも先に、共通処理の入口と責務分担を確認したいときに読むディレクトリです。

## Read this when

- cmoc の共通基盤として、このディレクトリに何がまとまっているかを把握したいとき。
- リポジトリ検出、session / apply 管理、共通例外、ログ、計測、タイムスタンプの入口を探したいとき。
- `INDEX.md` のメンテナンスや、`src/commons` 配下の各モジュールへどう案内するかを確認したいとき。

## Do not read this when

- `src/commons` 全体ではなく、個別モジュールの実装や挙動だけを追いたいとき。
- `codex exec` の起動制御や Structured Output の詳細だけを確認したいとき。
- `src/commons` 以外のサブコマンド本体、引数解釈、業務ロジックを追いたいとき。

## hash

- e06c78ee7d26977916906889c8aaf6c9b12efd55e96f348f625712e446754918

# `main.py`

## Summary

- cmoc CLI のエントリーポイントで、Typer のルート `app` と `session` / `apply` / `review` の各サブアプリを組み立てるファイルです。
- `init`、`session`、`apply`、`review` の各コマンド登録に加えて、`eval-oracle` / `eval-oracles` の隠し別名や各コマンドの既定オプションをまとめています。
- サブコマンド未指定時の `CmocError` 生成、補完プローブ時の分岐、Click/Typer 例外の共通整形、`python src/main.py` 直実行の起動経路を扱います。

## Read this when

- cmoc CLI の起点と、`session` / `apply` / `review` のサブアプリ構成を確認したいとき。
- `init`、`session fork/join/abandon`、`apply fork/join/abandon`、`review oracles` の登録名や隠し別名を確認したいとき。
- `apply fork` の繰り返し回数や `scope`、`apply join` の `--force-resolve` など既定オプションを確認したいとき。
- サブコマンド未指定時の利用者向けエラー、補完プローブ時の分岐、Click/Typer 例外の共通整形を追いたいとき。
- `python src/main.py` で直接起動する経路と、そのときの例外処理を確認したいとき。

## Do not read this when

- `src/sub_commands/` 配下の個別サブコマンド本体だけを確認したいとき。
- `commons.errors` の例外型や `format_error_report()` の整形ロジックだけを確認したいとき。
- CLI 登録や補完、例外変換ではなく、各機能の業務ロジックそのものを追いたいとき。
- `INDEX.md` の生成ルールや `oracles` 側の正本仕様だけを確認したいとき。

## hash

- 1a1bb5753238e77dc6df1252d876b3fc6c7cc1706bd8b8499554963755c0a4d7

# `sub_commands`

## Summary

- `src/sub_commands` は `cmoc` のサブコマンド実装をまとめる入口ディレクトリです。
- `__init__.py` はパッケージ宣言のみを担い、`init.py` は `cmoc init` の本体処理を持ちます。
- `apply`、`review`、`session` の各サブディレクトリが、それぞれのサブコマンド群の実装入口になっています。

## Read this when

- `src/sub_commands` ディレクトリ全体の入口構造を把握したいとき。
- `cmoc init` と、`apply`・`review`・`session` の各サブコマンド群へのルーティング先を素早く選びたいとき。
- このディレクトリにある `__init__.py`、`init.py`、各サブパッケージの役割分担を確認したいとき。

## Do not read this when

- `cmoc init` の個別実装や引数・エラー条件だけを確認したいとき。
- `cmoc apply`、`cmoc review`、`cmoc session` のいずれか個別の開始・統合・破棄・評価の詳細だけを確認したいとき。
- `src.sub_commands` が Python パッケージとして存在するかどうかだけを確認したいとき。

## hash

- 7255b7f7e8290fe8ecb4363baa8af6f5ebd663a3329ea7b2298ab1f52628e43d
