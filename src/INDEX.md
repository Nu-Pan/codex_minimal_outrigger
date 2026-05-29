# `commons`

## Summary

- `cmoc` 全体で共有する基盤モジュール群をまとめたディレクトリです。
- Git リポジトリ判定、共通エラー処理、サブコマンドログ、経過時間計測、タイムスタンプ生成、Codex CLI 呼び出し、`INDEX.md` メンテナンスを扱います。
- 個別サブコマンドの本体ではなく、横断的に再利用される処理の入口として参照します。

## Read this when

- `src/commons` にある共通処理の役割分担をまとめて把握したいとき。
- repo ルート探索、エラー整形、ログ記録、経過時間計測、タイムスタンプ生成の共通仕様を確認したいとき。
- `codex exec` の共通ラッパーや `INDEX.md` メンテナンスなど、複数サブコマンドから使う基盤処理を追いたいとき。

## Do not read this when

- 個別サブコマンドの業務ロジックや引数定義だけを確認したいとき。
- `src/commons` 全体ではなく、`errors.py` や `repo.py` など特定モジュールだけを直接確認したいとき。
- `INDEX.md` の生成・更新ルールそのものだけを確認したいとき。

## hash

- d412d8e7485e44e88a3461976311eea87578f46b673719af6ed0781e11b80a59

# `main.py`

## Summary

- `cmoc` CLI のエントリーポイントで、Typer のルートアプリと `session` / `apply` / `review` のサブアプリを組み立てる。
- `init`、`session fork/join/abandon`、`apply fork/join/abandon`、`review oracles` のコマンド登録と引数定義をまとめる。
- サブコマンド未指定時のエラー化、Typer / Click 例外の共通エラーレポート化、`python src/main.py` 直実行の起動経路を扱う。

## Read this when

- `cmoc` の起動点やサブコマンド登録を修正・レビューしたいとき。
- `init` / `session` / `apply` / `review` のコマンド名、エイリアス、オプション既定値を確認したいとき。
- サブコマンドなし起動時の利用者向けエラー、終了コード、`--help` への誘導を確認したいとき。
- `python src/main.py` で直接起動する経路と、その例外ハンドリングを確認したいとき。

## Do not read this when

- 各サブコマンドの本体ロジックや `src/sub_commands/` 配下の業務処理だけを見たいとき。
- 共通エラー型や `format_error_report` の整形仕様だけを確認したいとき。
- `INDEX.md` の生成ルールや共有ユーティリティの設計だけを追いたいとき。

## hash

- f1f3971b766959a15809687fc7f59cd60f74eaa1bdee3c4da218fb15412853e0

# `sub_commands`

## Summary

- `src/sub_commands` は、`cmoc` の各サブコマンド実装をまとめたパッケージの入口です。
- `__init__.py` はパッケージ宣言、`init.py` は `cmoc init`、`eval_oracles.py` は `cmoc review oracles` の本体を持ちます。
- `apply/` と `session/` はそれぞれ `cmoc apply` 系と `cmoc session` 系の実装ディレクトリで、個別コマンドの詳細は各配下の `INDEX.md` に分かれています。

## Read this when

- `src/sub_commands` 配下の `cmoc` サブコマンド実装の入口と、どのモジュール・ディレクトリに進むべきかを整理したいとき。
- `init.py`、`eval_oracles.py`、`apply/`、`session/` の役割分担を俯瞰して、実装・修正・レビュー・テストの入口を確認したいとき。
- `src/sub_commands` パッケージ全体の構成を把握し、個別サブコマンドの詳細へ進む前の案内が欲しいとき。

## Do not read this when

- `cmoc init` だけの詳細な初期化手順や、`.cmoc` の ignore 保証だけを確認したいとき。
- `cmoc review oracles` の評価フロー、Structured Output スキーマ、レポート出力だけを確認したいとき。
- `cmoc apply` 系や `cmoc session` 系の個別サブコマンド仕様だけを確認したいときは、この目次ではなく各配下の `INDEX.md` を読むべきです。

## hash

- 8fbbe32e27831a91ef8f6f0a1cd1551924aedb2adf0c44fd172fd52669e7523f
