# `commons`

## Summary

- `src/commons` は、cmoc 全体で共有する基盤モジュール群をまとめたパッケージです。
- repo root の探索と git 関連処理、共通エラー整形、CLI サブコマンドの実行ラッパー、Codex CLI 呼び出し、`INDEX.md` の維持管理、サブコマンドログ、タイムスタンプ、経過時間計測、レポート保存を扱います。
- 個別機能の本体というより、各サブコマンドや自動メンテナンス処理が依存する横断的な共通部品が集まっています。

## Read this when

- `cmoc` 全体で共通に使う基盤処理の入口を確認したいとき。
- repo root の解決、共通エラー整形、サブコマンド実行制御、`codex exec` 呼び出し、`INDEX.md` メンテナンスの関係を把握したいとき。
- タイムスタンプ、実行時間計測、サブコマンドログ、レポートファイル作成などの横断的な共通処理を追いたいとき。

## Do not read this when

- 個別サブコマンドの引数や業務ロジックだけを追いたいとき。
- テストコード、CLI エントリーポイント、`oracles` 側の仕様だけを確認したいとき。
- `src/commons` ではなく、特定の機能モジュール 1 つだけの実装や詳細を確認したいとき。

## hash

- b46e880a40b4a892f521cbd299af02816f5ab594ccdd201e28eea58086b7b4c2

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

- `src/sub_commands` は cmoc の個別サブコマンド実装の入口ディレクトリです。
- `__init__.py` はパッケージ宣言のみを担い、`apply/` は `cmoc apply` 系、`init.py` は `cmoc init`、`review/` は `cmoc review` 系、`session/` は `cmoc session` 系の本体実装を含みます。
- 個別モジュールへ進む前に、この配下全体の責務分担を把握するための目次です。

## Read this when

- `src/sub_commands` 配下でどのモジュールを開くべきか迷っているとき。
- `cmoc apply`、`cmoc session`、`cmoc review`、`cmoc init` の実装構造を俯瞰したいとき。
- CLI サブコマンドの入口構成と、各実装ファイル・サブディレクトリの責務分担を整理したいとき。

## Do not read this when

- 個別の `apply` / `session` / `review` / `init` 実装だけを確認したいときは、この目次ではなく該当モジュールを直接読むべきです。
- `src/sub_commands/__init__.py` のようなパッケージ宣言だけを確認したいときは、このディレクトリ全体の目次は不要です。
- 実装コードではなく `oracles/docs/app_specs/sub_commands/` 側の正本仕様だけを確認したいときは、このディレクトリを読む必要はありません。

## hash

- ba09bbcdbcf2968e0bd2a044d5539f110569e2975d74a163b0e3b5a8455ffffe
