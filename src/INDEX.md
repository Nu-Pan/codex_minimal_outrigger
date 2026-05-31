# `commons`

## Summary

- `src/commons` は cmoc で共有する基盤モジュール群をまとめたディレクトリです。
- `errors.py` は共通例外とエラーレポート整形、`repo.py` は Git リポジトリや cmoc 作業領域の判定と state 管理を担当します。
- `codex.py` は Codex CLI 実行基盤、`indexing.py` は `INDEX.md` の自動メンテナンス、`subcommand_log.py` はサブコマンド単位のログ管理を担当します。
- `command_runner.py` と `timing.py` はサブコマンドの実行制御と時間計測を、`timestamps.py` と `report_files.py` はタイムスタンプ生成とレポート保存を担当します。
- `__init__.py` は `src.commons` を Python パッケージとして宣言します。

## Read this when

- cmoc 全体で共有する基盤処理を把握したいときに読む。
- repo root 探索、branch / commit 判定、session / apply state、worktree パス復元など Git 周りの共通処理を確認したいときに読む。
- `codex exec` の呼び出し、Structured Output の検証、quota / capacity の再試行、`INDEX.md` メンテナンスや oracle 保護を確認したいときに読む。
- サブコマンドの共通実行制御、エラー整形、JSON Lines ログ、ステップ計測、timestamp 生成、タイムスタンプ付きレポート保存の実装を確認したいときに読む。
- 共通モジュール同士の依存関係や、どの責務をどのファイルが持つかを最短で見たいときに読む。

## Do not read this when

- 個別のサブコマンド実装や引数解析だけを追いたいときは、このディレクトリではなく `src/sub_commands` 側を読む。
- `codex exec` の詳細な起動・再試行・Structured Output 仕様だけを確認したいときは、`codex.py` だけを読む。
- Git リポジトリ状態や cmoc の作業ブランチ・state の仕様だけを確認したいときは、`repo.py` を読む。
- `INDEX.md` の配置ルールやメンテナンス方針の正本仕様だけを確認したいときは、`oracles/docs/app_specs/indexing.md` を読む。
- テストコードや他のパッケージの実装を探したいときは、このディレクトリではなく対象の `tests` や別モジュールを読む。

## hash

- e1dc6b06c7369e21bc2481d8a73423e009f5c88c2eb120ef21c0e8bf261e2d01

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

- `src/sub_commands` は `cmoc` のサブコマンド実装をまとめる入口ディレクトリです。
- `__init__.py` はパッケージ宣言のみを担い、`init.py` は `cmoc init`、`apply/` は `cmoc apply` 系、`review/` は `cmoc review` 系、`session/` は `cmoc session` 系の実装入口です。
- この目次は、個別実装へ進む前に読むべきファイルを切り分けるためのルーティング情報を提供します。

## Read this when

- `src/sub_commands` 配下のどの実装ファイルを読むべきかを素早く振り分けたいとき。
- `cmoc` の各サブコマンド実装の入口構造を俯瞰したいとき。
- `apply`、`session`、`review`、`init` の実装・修正・レビュー・テストを始める前に関連ディレクトリの役割分担を確認したいとき。

## Do not read this when

- `src/sub_commands/__init__.py` のパッケージ宣言だけを確認したいとき。
- `cmoc apply`、`cmoc session`、`cmoc review`、`cmoc init` の個別仕様や実装詳細だけを追いたいとき。
- `oracles/docs/app_specs/` 側の正本仕様だけを読みたいとき。

## hash

- 18c6dd7ba80bee50de0cbe51a535e6373e1dfc81d27e8647a64612d76a21ee20
