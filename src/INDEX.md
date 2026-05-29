# `commons`

## Summary

- `src/commons` は cmoc 全体で共有する基盤処理をまとめたディレクトリです。
- Codex CLI 呼び出し、共通エラー整形、git と session state の取り回し、INDEX.md 生成、レポート保存、サブコマンドログ、時刻・経過時間処理を扱います。
- 個別サブコマンドの業務ロジックではなく、他モジュールから再利用される共通ユーティリティへの入口です。

## Read this when

- cmoc の共通処理の実装や修正箇所を探したいとき。
- `codex exec` 呼び出し、Structured Output、`INDEX.md` メンテナンス、リポジトリ管理、ログ、レポート保存の共通仕様を確認したいとき。
- 個別サブコマンドの前に、どの共通モジュールを読むべきか判断したいとき。

## Do not read this when

- 個別サブコマンドの引数や業務フローだけを確認したいとき。
- `src/commons` 以外の CLI 本体やテスト実装だけを追いたいとき。
- `oracles` 全体のルーティング方針や `INDEX.md` の生成ルールだけを確認したいとき。

## hash

- 67c5bef68fb3e97589a97c927f69a03b2febfa0eaf383c3dfd0ad99781ef60f7

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
