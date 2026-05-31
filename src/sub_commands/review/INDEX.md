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

- `src/sub_commands/review/oracles.py` は `cmoc review oracles` の本体実装です。
- oracles スナップショットの評価対象選定、部分/全体評価の分岐、並列評価、問題点リストの改善反復をまとめて扱います。
- 評価前の `INDEX.md` メンテナンス、Structured Output 検証、Codex CLI 用 prompt 構築、Markdown レポート生成と失敗時の報告処理も担います。

## Read this when

- `cmoc review oracles` の実行順、部分評価・全体評価の切り替え、評価対象の oracle ファイル選定を確認したいとき。
- 評価前の `INDEX.md` メンテナンス、開始時点の oracles tree の固定、参照可能ファイルの制約を実装・修正・レビューしたいとき。
- Structured Output の検証条件、問題点リストの改善反復、Codex CLI 向けの prompt 構築を確認したいとき。
- レポート保存、error report、stderr フォールバックまで含めて `cmoc review oracles` の挙動を把握したいとき。

## Do not read this when

- `cmoc review oracles` の CLI 引数や `main.py` への登録だけを確認したいとき。
- `cmoc apply`、`cmoc session`、`cmoc init` など、別サブコマンドの実装や仕様を追いたいとき。
- `oracles` 配下の個別仕様断片そのものを直接読みたいとき。

## hash

- 85bb6d110ac055c240ecb3d988b697e523c8414b1dcf1e392afe166968c5f6b4
