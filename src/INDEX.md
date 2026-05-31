# `commons`

## Summary

- `src/commons` は cmoc 全体で共有する基盤モジュール群をまとめたディレクトリです。
- リポジトリ検出、実行制御、Codex CLI 呼び出し、エラー整形、ログ、計測、日時、レポート保存、`INDEX.md` 生成などの横断処理を集約しています。
- 個別サブコマンド本体ではなく、複数機能から再利用される共通実装を読む入口です。

## Read this when

- リポジトリルート探索、branch / commit 判定、session/apply の state 管理を確認したいとき。
- `codex exec` の起動、Structured Output 検証、quota 待機、再試行、`INDEX.md` メンテナンスの流れを追いたいとき。
- 共通例外 `CmocError`、利用者向けエラーレポート整形、JSON Lines ログ、ステップ計測、日時文字列、Markdown レポート保存の実装を確認したいとき。
- `src/commons` 配下の各モジュールを役割ベースで素早く振り分けたいとき。

## Do not read this when

- 個別サブコマンドの引数解析や業務ロジックだけを追いたいとき。
- `cmoc session` や `cmoc apply` の使い方、ユーザー向け操作手順だけを確認したいとき。
- `src/commons` 以外のモジュールやテストの詳細を調べたいとき。
- 必要な対象ファイルがすでに分かっているなら、このディレクトリの索引ではなく該当モジュールを直接読みたいとき。

## hash

- 8c047a899e5fcaba10bac7abc31ac0462c9c90c256bf757e976fb939bc326e9a

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

- `src/sub_commands` は `cmoc` のサブコマンド実装をまとめる入口ディレクトリで、`__init__.py` がパッケージ宣言、`init.py` が `cmoc init`、`apply/`・`session/`・`review/` が各系統の実装入口です。
- このディレクトリは、個別実装へ進む前に責務ごとの読み先を振り分けるためのルーティング目次として使います。

## Read this when

- `cmoc` のどのサブコマンド実装がこの配下にあるかを俯瞰したいとき。
- `init`、`apply`、`session`、`review` のうち、どの入口ファイルや配下ディレクトリを読むべきか振り分けたいとき。
- `src/sub_commands` が Python パッケージとして成立していることや、各サブコマンドの入口構造を確認したいとき。

## Do not read this when

- 個別サブコマンドの引数、状態遷移、終了条件などの詳細仕様だけを確認したいときは、各実装ファイルか `oracles/docs/app_specs/sub_commands/` 側を読むべきです。
- `cmoc` 全体の使い方や開発ルールだけを確認したいときは、このディレクトリではなく上位の案内文書を参照すべきです。
- `src/sub_commands` のパッケージ宣言だけを確認したいときは、この目次ではなく `__init__.py` を直接読むべきです。

## hash

- f109f2013d9a92257e7b0e5f698ef7b6a6a21fc186abe76f742ce30a280847f7
