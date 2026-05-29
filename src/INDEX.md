# `commons`

## Summary

- `cmoc` で共通利用する基盤モジュール群をまとめたディレクトリです。
- Codex CLI 呼び出し、共通エラー、git リポジトリ操作、`INDEX.md` メンテナンス、レポート保存、サブコマンドログ、タイムスタンプ、経過時間計測を扱います。
- 個別サブコマンドから横断的に使われる実装を集約しており、機能ごとの責務分離を確認する入口になります。

## Read this when

- `cmoc` 全体で共通に使う基盤処理の入口を知りたいとき。
- Codex 呼び出し、エラー整形、リポジトリ探索、ログ保存、タイムスタンプ、経過時間計測の共通仕様をまとめて追いたいとき。
- `INDEX.md` の自動生成や、サブコマンド実行前後の共通処理を確認したいとき。
- 複数モジュールにまたがる処理の役割分担を俯瞰したいとき。

## Do not read this when

- 個別サブコマンドの業務ロジックや引数定義だけを確認したいとき。
- `src/commons` 配下のうち特定の 1 モジュールの実装詳細だけを追いたいとき。
- `cmoc` のテストケースや CLI 画面表示だけを確認したいとき。
- `memo` の内容や、`oracles` 全体の更新方針そのものを確認したいとき。

## hash

- 7fba6610fe1327519de8bf508e772f675ea6fd5418831c55a0d0e5e814d82683

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
