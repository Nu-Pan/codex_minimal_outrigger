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

- `src/sub_commands/review/oracles.py` は `cmoc review oracles` の本体処理を担う実装ファイルです。
- 開始時点の `oracles` ツリーを snapshot として固定し、`INDEX.md` をメンテナンスしたうえで、対象 oracle ファイルを並列に評価します。
- 評価結果の問題点リストを改善し、最終レポートまたは失敗時のエラーレポートを `.cmoc/reports/review_oracles` に保存します。

## Read this when

- `cmoc review oracles` の実行フロー全体を追いたいとき。
- oracles スナップショットの固定、部分評価・全体評価の選定、並列評価の流れを確認したいとき。
- 問題点リストの改善反復、Structured Output の検証、Markdown レポート保存とエラーレポート出力の仕様を確認したいとき。

## Do not read this when

- `cmoc review` の CLI 登録や hidden alias だけを確認したいときは、このファイルではなく `src/main.py` を読むべきです。
- `src/sub_commands/review` が Python パッケージとして宣言されていることだけを確認したいときは、同ディレクトリの `__init__.py` を読むべきです。
- `oracles` 配下の個別仕様断片そのものを確認したいときは、この実装ではなく `oracles/docs/app_specs/` 側を読むべきです。

## hash

- a644a7f70e8366099ba9123850a68f5aaedd9d716e1168c8c25a0503b58a3f6d
