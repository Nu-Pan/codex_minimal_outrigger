# `__init__.py`

## Summary

- `src/sub_commands/review/__init__.py` は `cmoc review` 系サブコマンドのパッケージ宣言だけを担う最小モジュールです。
- 公開 API、定数、実行ロジック、再エクスポートは持ちません。

## Read this when

- `src/sub_commands/review` が Python パッケージとして宣言されていることを確認したいとき。
- `cmoc review` 系サブコマンドの入口となるパッケージ構造を把握したいとき。

## Do not read this when

- `cmoc review oracles` の実行フローや評価ロジックを確認したいときは、このファイルではなく `oracles.py` を読むべきです。
- `cmoc review oracles` の CLI 引数や hidden alias 登録だけを確認したいときは、`src/main.py` を読むべきです。

## hash

- d432dc21ecc8d2cabf968eac490bb998f303e6d3e7411b90260759ccd587f07d

# `oracles.py`

## Summary

- `cmoc review oracles` の実行本体で、oracles 仕様ファイル群の評価とレポート生成を担当します。
- 開始時点の oracles ツリーを snapshot として固定し、その後に `INDEX.md` をメンテナンスしてから評価を進めます。
- 対象 oracle の選定、並列評価、問題点リストの改善反復、Markdown レポート保存、失敗時のエラーレポート出力までをまとめて扱います。

## Read this when

- `cmoc review oracles` の実行フロー全体を追いたいとき。
- oracles スナップショットの固定、評価対象の選定、並列評価、Structured Output 検証を確認したいとき。
- 問題点リストの改善反復や、最終レポート・エラーレポートの生成仕様を確認したいとき。

## Do not read this when

- CLI へのコマンド登録や hidden alias だけを確認したいときは、`src/main.py` を読むべきです。
- パッケージ宣言だけで足りるときは、同ディレクトリの `__init__.py` を読むべきです。
- `oracles` 配下の個別仕様断片そのものを確認したいときは、このファイルではなく `oracles/docs/app_specs/` 側を読むべきです。

## hash

- 964729b33c9d366e132d532dbcbe1851339e1025b795a8b0182bcdc52f4125ba
