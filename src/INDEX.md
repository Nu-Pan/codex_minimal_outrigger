# `commons`

## Summary

- cmoc 全体で共有する共通ユーティリティ群をまとめるディレクトリです。
- Codex CLI の実行基盤、repo/worktree 解析、例外整形、サブコマンドログ、時間計測、タイムスタンプ、レポート保存、`INDEX.md` メンテナンスを担います。
- 個別サブコマンド本体ではなく、複数コマンドから再利用する基盤処理が集まっています。

## Read this when

- `codex exec` の呼び出し、Structured Output 検証、再試行、`resume` を追いたいとき。
- `<repo-root>` 検出、session/apply state、branch や commit の判定、差分抽出を確認したいとき。
- サブコマンドログ、経過時間表示、レポート保存、タイムスタンプ生成の共通仕様を確認したいとき。
- `INDEX.md` の自動更新や共通例外 `CmocError` の整形規則を確認したいとき。

## Do not read this when

- 個別サブコマンドの引数解釈や業務ロジックだけを追いたいとき。
- `src/sub_commands` 側の実装や `oracles` の個別仕様を直接確認したいとき。
- テストや CLI エントリポイント以外の、共有基盤を経由しない処理を確認したいとき。

## hash

- 937cf452011b901aa13d2b04282a23af6f59d08307b84bfe2cf424481015deb0

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

- 6e901618816baad8b120b3ae4510536b615dd1b5fcedd832d2b23483c1cdb418
