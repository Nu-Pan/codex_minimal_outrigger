# `commons`

## Summary

- `src/commons` は `cmoc` 全体で共有する Python パッケージで、共通基盤をまとめる入口です。
- `codex.py` は `codex exec` 呼び出しの共通制御、Structured Output の扱い、再試行、oracle 保護を担います。
- `command_runner.py`、`errors.py`、`indexing.py`、`repo.py`、`report_files.py`、`subcommand_log.py`、`timestamps.py`、`timing.py` は、それぞれサブコマンド実行、共通例外、`INDEX.md` 保守、git リポジトリ処理、レポート保存、ログ、タイムスタンプ、経過時間計測を提供します。
- `__init__.py` は `src.commons` パッケージを宣言するだけの最小構成です。

## Read this when

- `cmoc` 全体で共有する共通処理を探していて、CLI 実行・例外整形・git 操作・ログ・時刻処理のどこに何があるか整理したいとき。
- `codex exec` の共通制御、Structured Output、JSON スキーマ検証、再試行、oracle 保護の実装を確認したいとき。
- `INDEX.md` の自動生成・再生成・更新、サブコマンド実行ラッパー、レポート保存、サブコマンドログ、時間計測の実装を確認したいとき。
- `repo.py` で session/apply 状態や git リポジトリ判定を追いたいとき、または `timestamps.py` や `report_files.py` のような共通ユーティリティだけを読みたいとき。

## Do not read this when

- 個別サブコマンドの業務ロジックや CLI 引数の詳細だけを確認したいときは、この配下ではなく `src/sub_commands` を読むべきです。
- `oracles` の正本仕様や利用手順を確認したいときは、この配下ではなく `<cmoc-root>/oracles` を辿るべきです。
- pytest の期待値や回帰テストを確認したいときは、この配下ではなく `tests` を読むべきです。
- パッケージ宣言だけを確認したいときは `__init__.py` で足りるので、他の共通モジュールまで広げて読む必要はありません。

## hash

- 6148e3612f8fa419d8f9c6522e9523c02902bd54532fa61639e117d5d3768ad0

# `main.py`

## Summary

- cmoc CLI のエントリーポイントで、Typer のルート app と `session` / `apply` / `review` のサブアプリを組み立てます。
- `init`、`session fork/join/abandon`、`apply fork/join/abandon`、`review oracles` の登録と、それぞれのオプション既定値やエイリアスをまとめます。
- サブコマンド未指定時の利用者向けエラー、Click/Typer 例外の共通整形、`python src/main.py` 直実行の起動経路を扱います。

## Read this when

- cmoc の起動点やサブコマンド登録を修正・レビューしたいとき。
- `init` / `session` / `apply` / `review` のコマンド名、エイリアス、オプション既定値を確認したいとき。
- サブコマンドなし起動時の利用者向けエラー、終了コード、`--help` への誘導を確認したいとき。
- `python src/main.py` で直接起動する経路と、その例外ハンドリングを確認したいとき。

## Do not read this when

- 各サブコマンドの本体ロジックや `src/sub_commands/` 配下の処理だけを確認したいとき。
- 共通エラー型や `format_error_report` の整形仕様だけを確認したいとき。
- `INDEX.md` の生成ルールや共通ユーティリティの設計だけを追いたいとき。

## hash

- 725244cd04649c14efdc472340862818b2eabfb76416af919258408edf3121cc

# `sub_commands`

## Summary

- `src/sub_commands` は cmoc のサブコマンド実装の入口で、`__init__.py`、`init.py`、`eval_oracles.py`、`apply/`、`session/` を含みます。
- `init.py` は `cmoc init`、`eval_oracles.py` は `cmoc review oracles` を担当します。
- `apply/` と `session/` は、それぞれ apply 系・session 系サブパッケージです。

## Read this when

- `src/sub_commands` 配下にどのサブコマンド実装が置かれているかを俯瞰したいとき。
- `cmoc init`、`cmoc review oracles`、`cmoc apply`、`cmoc session` の入口を素早く見分けたいとき。
- このディレクトリが Python パッケージとして宣言され、個別コマンド実装とサブパッケージに分かれていることを確認したいとき。

## Do not read this when

- 個別サブコマンドの詳細仕様だけを確認したいときは、各モジュールを直接読むべきです。
- `cmoc apply` や `cmoc session` 配下の詳細だけを確認したいときは、それぞれの子ディレクトリの `INDEX.md` を読むべきです。
- `src/sub_commands` のパッケージ宣言だけを確認したいときは、`__init__.py` を直接見れば足ります。

## hash

- eb599cb48d326c6a3a9d236be3cd568a9d42c56614e3f8bcb80b57a8aa3c8b21
