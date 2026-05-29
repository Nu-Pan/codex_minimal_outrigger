# `commons`

## Summary

- `src/commons` は、cmoc 全体で使う共通基盤モジュール群をまとめたディレクトリです。
- `codex.py` は Codex CLI 呼び出し、Structured Output の JSON 解析と検証、リトライ、ログ保存、`INDEX.md` 事前メンテナンスを担います。
- `command_runner.py` はサブコマンドの共通実行ラッパー、`errors.py` は共通例外と stdout 向けエラーレポート整形を担います。
- `indexing.py` は `INDEX.md` の自動生成・更新・自動コミットを扱い、`repo.py` は git リポジトリと `.cmoc` の状態管理を扱います。
- `subcommand_log.py` は JSON Lines ログ、`timestamps.py` は `<time-stamp>` 生成、`timing.py` はステップ経過時間計測を扱います。
- `__init__.py` は `src.commons` パッケージを宣言する最小モジュールです。

## Read this when

- 共通処理の役割分担をまとめて把握したいとき。
- repo root 探索、branch 判定、session/apply 状態管理などの git 共通処理を確認したいとき。
- Codex CLI 呼び出し、エラー整形、サブコマンドログ、タイムスタンプ、経過時間計測、`INDEX.md` メンテナンスの実装を追いたいとき。

## Do not read this when

- cmoc の個別サブコマンドの引数、状態遷移、実行手順だけを確認したいとき。
- `INDEX.md` の生成・維持ルールそのものを確認したいとき。
- `src/commons` の外にある CLI 本体やテストコードだけを確認したいとき。

## hash

- 5f832824aa560db29f71412404bd99a6e9066928d50b8b830f9ecca3d878584f

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

- `src/sub_commands` 配下の各サブコマンド実装への入口をまとめるパッケージ目次です。
- `cmoc init`、`cmoc review oracles`、`cmoc apply` 系、`cmoc session` 系の実装ファイルと下位ディレクトリへの案内を担います。
- `src/main.py` のコマンド分岐から各本体処理へ進むときの起点です。

## Read this when

- `src/sub_commands` にどのサブコマンド実装があるか確認したいとき。
- `cmoc init`、`cmoc review oracles`、`cmoc apply`、`cmoc session` の入口ファイルを素早く辿りたいとき。
- サブコマンド全体の構成と責務の分け方を把握したいとき。

## Do not read this when

- 個別サブコマンドの引数、状態遷移、終了条件などの詳細仕様を確認したいときは、各実装ファイルを直接読むべきです。
- `oracles` の正本仕様や作業手順だけを確認したいときは、この目次ではなく `oracles` 側を読むべきです。
- `src/commons` の共通処理やテスト実装だけを確認したいときは、このディレクトリを読む必要はありません。

## hash

- 1b97e249c5b0a0d04ffb00a388339464fabdb2f4df7d291562439a88180f30c3
