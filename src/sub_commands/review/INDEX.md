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

- `src/sub_commands/review/oracles.py` は `cmoc review oracles` の本体処理を担い、開始時点の `oracles` ツリーを snapshot として固定したうえで、評価・改善・レポート保存までを一括で実行します。
- 部分評価 / 全体評価の切り替え、`INDEX.md` メンテナンスの反映、oracle ファイルごとの並列評価、問題点リストの反復改善を扱います。
- 評価結果とエラー時の代替レポートを `.cmoc/reports/review_oracles` に保存し、参照ファイル検証や Structured Output の妥当性確認も行います。

## Read this when

- `cmoc review oracles` の実行フロー全体を実装・修正・レビューしたいとき。
- 開始時点の `oracles` snapshot 固定、`INDEX.md` 反映、並列評価、問題点リスト改善の流れを確認したいとき。
- 評価レポートや error report の保存先、frontmatter、issue の severity 集計を確認したいとき。
- Structured Output の検証条件や、参照可能な `oracles` 配下ファイルの制約を確認したいとき。

## Do not read this when

- `cmoc review` の CLI 登録や hidden alias だけを確認したいときは、`src/main.py` を読むべきです。
- `cmoc review oracles` の利用手順や仕様断片だけを確認したいときは、`oracles/docs/app_specs/sub_commands/review_oracles.md` を読むべきです。
- 個別の `oracles` 仕様ファイルの内容だけを追いたいときは、この実装ではなく `oracles/docs/app_specs/` 側を読むべきです。
- `INDEX.md` の生成・更新ルールだけを確認したいときは、このファイルではなく `src/commons/indexing.py` を読むべきです。

## hash

- b31ccee38fb5b008834c6c8ac6569b36a2ee664257786627f8d3c4f522bd3daa
