# `commons`

## Summary

- `src/commons` は `cmoc` 全体で共有する基盤モジュール群をまとめたディレクトリです。
- リポジトリ探索、エラー整形、`INDEX.md` メンテナンス、Codex 呼び出し、実行ログ、経過時間、タイムスタンプなどの共通処理を収めています。
- 各サブコマンドの個別ロジックではなく、複数機能から再利用される下支えの実装を読むための入口です。

## Read this when

- `src/commons` 配下の共通ヘルパー群の役割分担を把握したいとき。
- `repo.py`、`errors.py`、`indexing.py`、`codex.py` などの横断的な基盤処理を確認したいとき。
- サブコマンド実装の前に、共通の実行制御・ログ・時間計測・タイムスタンプ処理の入口を探したいとき。

## Do not read this when

- 個別サブコマンドの引数や状態遷移、業務ロジックだけを追いたいとき。
- `cmoc` の正本仕様や利用手順だけを確認したいとき。
- `tests` 側の回帰テストや検証コードだけを確認したいとき。

## hash

- 4c98cb34ba9b32d7e5161baf930c399d3e1350d9a3ccbecdf81eb0be5f22e52e

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

- `src/sub_commands` は cmoc の各サブコマンド実装を束ねる入口ディレクトリです。
- ここには `__init__.py`、`init.py`、`apply/`、`review/`、`session/` があり、パッケージ宣言と各サブコマンド本体への入口をまとめています。
- 個別サブコマンドへ進む前に、このディレクトリ全体の責務分担を確認するための目次です。

## Read this when

- `src/sub_commands` 配下のどのモジュールを開くべきか、入口構造を確認したいとき。
- `cmoc init`、`cmoc apply`、`cmoc review`、`cmoc session` の実装配置を俯瞰したいとき。
- サブコマンド実装・修正・テスト・レビューの前に、責務の切り分けを整理したいとき。

## Do not read this when

- 個別サブコマンドの引数、状態遷移、終了条件などの正本仕様だけを確認したいとき。
- `cmoc` の利用手順や運用フローだけを確認したいとき。
- CLI 登録や `src/main.py` の実装だけを確認したいとき。

## hash

- 94de3a618784e34fb840913ff1e2b7a2c7e952d8ae16f2534f5481cd92b98ec9
