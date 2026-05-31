# `commons`

## Summary

- `cmoc` のサブコマンド群が共通で使う基盤モジュールをまとめたディレクトリです。
- `repo.py` が repo root・branch・session/apply state・差分検査・`git` 操作補助を担当します。
- `codex.py` が `codex exec` 実行、Structured Output 検証、再試行、quota 待機、`INDEX.md` メンテナンス連携を担当します。
- `command_runner.py`、`errors.py`、`subcommand_log.py`、`timing.py`、`timestamps.py`、`report_files.py` が実行ラッパー、エラー整形、ログ、計測、時刻、レポート保存を支えます。
- `indexing.py` が `INDEX.md` の自動維持と再生成の中心になっています。

## Read this when

- `cmoc` のサブコマンド群で共通に使う基盤処理を確認したいとき。
- `repo.py` による repo root 探索、branch 判定、session/apply state、差分検査、`git` 補助の挙動を確認・修正したいとき。
- `codex.py` の `codex exec` 起動、Structured Output 検証、quota 待機、`INDEX.md` メンテナンス連携を追いたいとき。
- `command_runner.py`、`errors.py`、`subcommand_log.py`、`timing.py`、`timestamps.py`、`report_files.py` のような横断的な共通処理を理解したいとき。
- このディレクトリ配下の共通モジュールを追加・整理するときに、既存の役割分担を把握したいとき。

## Do not read this when

- 個別サブコマンドごとの業務ロジック、引数、状態遷移だけを確認したいときは、`src/sub_commands` 側を読むべきです。
- `oracles` 側のコマンド仕様や利用手順だけを確認したいときは、このディレクトリではなく `oracles/docs/app_specs/sub_commands/` 側を参照すべきです。
- 共通処理ではなくテスト実装や CLI エントリーポイントだけを追いたいときは、このディレクトリを読む必要はありません。

## hash

- eedc09290d9f5e35fb9925db75442fb006c0c2929cd8317ab94b0b0f0436d66b

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

- `src/sub_commands` は `cmoc` の個別サブコマンド実装の入口で、`apply`、`session`、`review`、`init.py` を束ねるディレクトリです。
- この配下には `__init__.py` と、`apply` 配下の `abandon.py`、`fork.py`、`join.py`、`session` 配下の `abandon.py`、`fork.py`、`join.py`、`review/oracles.py`、`init.py` があります。
- 個別実装に進む前に、各サブコマンドの責務分担と入口構造を俯瞰するための目次です。

## Read this when

- `cmoc` の個別サブコマンドの入口をまとめて確認したいとき。
- `apply`、`session`、`review`、`init` のどの仕様断片へ進むべきか整理したいとき。
- サブコマンドごとの目的、入力条件、実行手順、状態遷移、終了条件を俯瞰したいとき。
- `src/sub_commands/apply`、`src/sub_commands/session`、`src/sub_commands/review` の下位 `INDEX.md` に進む前の入口を探したいとき。

## Do not read this when

- 個別の `apply`、`session`、`review`、`init` の詳細仕様だけを確認したいときは、この目次ではなく該当する下位ディレクトリやモジュールの `INDEX.md` を直接読むべきです。
- 実装コードやテストコードの作業だけで足りるときは、この目次を読む必要はありません。
- `branch_model`、`codex_call`、ログ、エラーハンドリング、`oracles` 全体の扱いなど、別の共通仕様を確認したいときはこのディレクトリではなく他の入口文書を読むべきです。

## hash

- a39223f0a04973f3bebd1bc04d371e3b82388bb24224b1475c019208347a1b45
