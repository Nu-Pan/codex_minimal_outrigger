# `commons`

## Summary

- `src/commons` は cmoc 全体で共有する基盤モジュール群をまとめたディレクトリです。
- リポジトリ検出、実行制御、Codex CLI 呼び出し、エラー整形、ログ、計測、日時、レポート保存、`INDEX.md` 生成などの横断処理を集約しています。
- 個別サブコマンド本体ではなく、複数機能から再利用される共通実装を読む入口です。

## Read this when

- リポジトリルート探索、`cmoc/session/*` と `cmoc/apply/*` の判定、worktree 復元の共通処理を確認したいとき。
- `codex exec` の起動、Structured Output 検証、quota 待機、capacity 再試行、`INDEX.md` メンテナンスの流れを追いたいとき。
- 共通例外 `CmocError` の定義や、利用者向けエラーレポートの整形規則を確認したいとき。
- サブコマンド実行の共通ラッパー、JSON Lines ログ、ステップ計測、日時文字列、Markdown レポート保存の実装を確認したいとき。
- このディレクトリ配下の各共通モジュールを、役割ベースで素早く振り分けたいとき。

## Do not read this when

- 個別サブコマンドの引数解析や業務ロジックだけを追いたいとき。
- `cmoc session` / `cmoc apply` の操作手順や CLI 全体のユーザー向け説明だけを見たいとき。
- `src/commons` 以外のモジュールやテストの詳細を調べたいとき。
- 必要な対象ファイルが既に分かっているなら、このディレクトリの索引ではなく該当モジュールを直接読むべきです。

## hash

- 068905a26a30fe70b6e2f8ad33749a0b3791eba2b396474429c8935971ca8f80

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

- `src/sub_commands` は `cmoc` の CLI サブコマンド実装をまとめる入口ディレクトリです。
- `__init__.py` によるパッケージ宣言のほか、`init.py`、`apply/`、`session/`、`review/` を束ねます。
- この配下から各サブコマンド本体へ進み、個別の処理順や状態遷移を確認できます。

## Read this when

- `src/sub_commands` 配下でどの実装ファイルを読むべきか整理したいとき。
- `cmoc init`、`cmoc apply`、`cmoc session`、`cmoc review oracles` の入口構造を俯瞰したいとき。
- サブコマンド実装の責務分担や、パッケージとしての構成を確認したいとき。

## Do not read this when

- 個別サブコマンドの引数や状態遷移だけを確認したいときは、各 `apply_*`、`session_*`、`review/oracles.py`、`init.py` を直接読むべきです。
- Python の一般的なパッケージ作法だけを確認したいときは、この目次ではなく実装コードを読むべきです。
- `oracles` 配下の正本仕様や `INDEX.md` 生成ルールだけを確認したいときは、別の仕様文書を読むべきです。

## hash

- e69f386803376cc51b2959b6e0b820455b71875c9e1c34c35a2cfd8f07a4cceb
