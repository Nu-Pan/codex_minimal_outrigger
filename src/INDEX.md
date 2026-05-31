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

- 0cf71011795da352f88ebd84b46e50ce96193c287c5e7782178eee33e2b6602c

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

- `src/sub_commands` は cmoc のサブコマンド実装の入口で、`__init__.py`、`init.py`、`review/`、`apply/`、`session/` へ振り分ける目次です。
- `__init__.py` はパッケージ宣言のみ、`init.py` は `cmoc init`、`review/` は `cmoc review` 系、`apply/` と `session/` はそれぞれ個別の `INDEX.md` を持つ入口です。
- このディレクトリの目次は、個別サブコマンドの詳細へ入る前に、どの実装ファイルを開くべきかを素早く判断するための案内です。

## Read this when

- `src/sub_commands` 配下で、どのファイルやディレクトリがどのサブコマンドを担当するか確認したいとき。
- サブコマンド実装・修正・レビュー・テストの前に、該当モジュールや配下ディレクトリへ進む入口を整理したいとき。
- `__init__.py`、`init.py`、`review/`、`apply/`、`session/` の役割分担を素早く把握したいとき。

## Do not read this when

- 個別サブコマンドの引数、状態遷移、例外条件だけを確認したいとき。
- `apply/` や `session/` のさらに細かい仕様だけを確認したいとき。
- `src/commons` や `oracles` 全体の共通仕様だけを確認したいとき。

## hash

- 25fa5849ed06c2b67386ba01abd228a511913ff7d385869e8c3b30e0a85734a4
