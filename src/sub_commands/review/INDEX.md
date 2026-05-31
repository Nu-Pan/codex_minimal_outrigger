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

- `src/sub_commands/review/oracles.py` は `cmoc review oracles` の実行本体で、oracle 仕様ファイル群の評価とレポート作成をまとめて担当します。
- 評価開始時点の `oracles` tree を snapshot として固定し、その後に `INDEX.md` をメンテナンスしてから評価を進めます。
- 対象 oracle ファイルを選定し、各ファイルを並列に評価したうえで、問題点リストの改善反復を行います。
- 最終結果を Markdown レポートとして保存し、異常時にはエラーレポートとフォールバック出力も行います。

## Read this when

- `src/sub_commands/review/oracles.py` が `cmoc review oracles` の本体として何をしているか把握したいとき。
- 開始時点の oracles tree の snapshot 固定、評価対象ファイル選定、並列評価の流れを確認したいとき。
- 問題点リストの改善反復、Structured Output 検証、Markdown レポート出力の実装を確認したいとき。
- 評価前の `INDEX.md` メンテナンスや、失敗時のエラーレポート生成の流れを追いたいとき。

## Do not read this when

- `cmoc review oracles` の CLI 引数や `main.py` への登録だけを確認したいとき。
- `cmoc apply`、`cmoc session`、`cmoc init` など別サブコマンドの実装や仕様を追いたいとき。
- `oracles` 配下の個別仕様断片そのものを直接読みたいとき。

## hash

- 1440c8a39b0ef7a272026f272b5671c8e2038dd72e3574b1742133311bd3e8a4
