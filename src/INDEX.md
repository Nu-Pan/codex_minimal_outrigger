# `commons`

## Summary

- cmoc 全体で共有する基盤処理をまとめたディレクトリです。
- Codex CLI 呼び出し、共通エラー整形、repo root 探索、session/apply 状態管理、INDEX.md 目次生成を扱います。
- サブコマンドログ、経過時間計測、タイムスタンプ生成、レポート保存などの横断処理も含みます。
- 個別サブコマンドの業務ロジックではなく、複数機能から再利用される共通部品の入口です。

## Read this when

- cmoc 全体で使う共通処理の実装や修正箇所を探したいとき。
- Codex CLI 実行、JSON/Structured Output 検証、再試行、ログ保存の流れを確認したいとき。
- git リポジトリ探索、session/apply 状態ファイル、ブランチ判定、タイムスタンプ、経過時間表示を確認したいとき。
- INDEX.md の自動生成や、サブコマンド実行ログの保存先を調べたいとき。

## Do not read this when

- 個別サブコマンドの引数や業務フローだけを追いたいときは、`src/sub_commands` 側を読むべきです。
- 共通処理のうち特定の機能だけを見たいときは、このディレクトリ全体ではなく該当モジュールを直接読むべきです。
- テストコードや仕様断片だけを確認したいときは、このディレクトリではなく `tests` や `oracles` を参照すべきです。
- cmoc の使用手順や全体ワークフローだけを知りたいときは、共通基盤の細部まで読む必要はありません。

## hash

- 8fb6ceabe81c71156e1da14822c61803f483dcb3249821b9ccaab6bbb186815c

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
- `apply/` と `session/` は、それぞれ apply 系・session 系サブコマンドをまとめたサブパッケージです。

## Read this when

- `src/sub_commands` 配下にどのサブコマンド実装が置かれているかを俯瞰したいとき。
- `cmoc init`、`cmoc review oracles`、`cmoc apply`、`cmoc session` の入口を素早く見分けたいとき。
- このディレクトリが Python パッケージとして宣言され、個別コマンド実装とサブパッケージに分かれていることを確認したいとき。

## Do not read this when

- `cmoc init` や `cmoc review oracles` の個別実装だけを確認したいときは、各モジュールを直接読むべきです。
- `cmoc apply` や `cmoc session` の配下の詳細仕様や処理順を確認したいときは、それぞれの子ディレクトリの `INDEX.md` を読むべきです。
- `src/sub_commands` のパッケージ宣言だけを確認したいときは、`__init__.py` を直接見れば足ります。

## hash

- 4a44f7ece48a1e788e7e6d51cd5391778d3ee926f1c8268b1f78143c6527a766
