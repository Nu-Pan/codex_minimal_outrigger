# `commons`

## Summary

- `src/commons` は、cmoc 全体で共有する基盤モジュール群をまとめたパッケージです。
- repo root の探索と git 関連処理、共通エラー整形、CLI サブコマンドの実行ラッパー、Codex CLI 呼び出し、`INDEX.md` の維持管理、サブコマンドログ、タイムスタンプ、経過時間計測、レポート保存を扱います。
- 個別機能の本体というより、各サブコマンドや自動メンテナンス処理が依存する横断的な共通部品が集まっています。

## Read this when

- `cmoc` 全体で共通に使う基盤処理の入口を確認したいとき。
- repo root の解決、共通エラー整形、`codex exec` 呼び出し、`INDEX.md` メンテナンス、サブコマンドログ、タイムスタンプ、経過時間計測、レポート保存の関係を把握したいとき。
- 各サブコマンドや自動メンテナンス処理が依存する横断的な共通部品をまとめて追いたいとき。

## Do not read this when

- 個別サブコマンドの引数や業務ロジックだけを追いたいとき。
- `cmoc` の CLI エントリーポイントや `session` / `apply` / `review` の登録構成だけを確認したいとき。
- `oracles` 側の正本仕様だけを確認したいとき。
- `src/commons` のうち 1 つのモジュールだけの実装や詳細を見たいとき。

## hash

- cc77e1f1628a8421251cc26fb601e595d2f7829c9c534ca0fffc8ef7597cde20

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
- `__init__.py` はパッケージ宣言のみを担い、`init.py` は `cmoc init` の本体です。
- `apply/` は `cmoc apply` 系、`session/` は `cmoc session` 系、`review/` は `cmoc review` 系の実装入口です。
- この `INDEX.md` は、個別モジュールへ進む前に責務分担を把握するための目次です。

## Read this when

- `src/sub_commands` 配下で、どのモジュールやサブディレクトリを開くべきか迷っているとき。
- `cmoc init`、`cmoc apply`、`cmoc session`、`cmoc review` の実装入口を俯瞰したいとき。
- `src/sub_commands` 配下の責務分担を整理してから、個別実装やテストに進みたいとき。
- `src/sub_commands` が Python パッケージとして成立していることと、各サブコマンド本体の入口を確認したいとき。

## Do not read this when

- `cmoc init` だけの仕様や実装を確認したいときは、`src/sub_commands/init.py` を直接読むべきです。
- `cmoc apply` 系だけを追いたいときは、`src/sub_commands/apply/INDEX.md` を起点に読むべきです。
- `cmoc session` 系だけを追いたいときは、`src/sub_commands/session/INDEX.md` を起点に読むべきです。
- `cmoc review` 系だけを追いたいときは、`src/sub_commands/review/INDEX.md` を起点に読むべきです。
- `oracles/docs/app_specs/sub_commands/` 側の正本仕様だけを確認したいときは、この実装目次ではなく仕様側の INDEX を読むべきです。

## hash

- de5894b8b9ae02816177d8085710004eaa76c769a26efc97f522ff5a509426e9
