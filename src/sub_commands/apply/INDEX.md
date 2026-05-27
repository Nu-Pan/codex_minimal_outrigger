# `__init__.py`

## Summary

- - `src/sub_commands/apply/__init__.py` は `cmoc apply` 系サブコマンドのパッケージ宣言だけを担う最小モジュールです。
- - 公開 API、定数、実行ロジック、再エクスポートは持ちません。

## Read this when

- - `src/sub_commands/apply` が Python パッケージとして宣言されていることを確認したいとき。
- - `cmoc apply` 系サブコマンドの入口となるパッケージ構造を把握したいとき。

## Do not read this when

- - 個別の `cmoc apply fork/join/abandon` の実行フローや状態遷移を確認したいときは、このファイルではなく各実装モジュールを読むべきです。
- - `cmoc apply` の仕様断片や利用手順だけを確認したいときは、`oracles/app_specs/sub_commands/` 側を読むべきです。

## hash

- 5646cb02b7ca8e507d8725e2d5f87e9580881d66ce1a67505595830d53c239d6

# `abandon.py`

## Summary

- `cmoc apply abandon` の本体処理を実装します。
- apply worktree と apply branch を削除し、session state の `apply.state` を `ready` に戻します。

## Read this when

- `cmoc apply abandon` の実装・修正・レビュー・テストを行いたいとき。
- 未 join の apply run を破棄する前提条件、cleanup 対象、`apply.state` の更新、warning の扱いを確認したいとき。

## Do not read this when

- `cmoc apply fork` の調査・修正ループや要修正点一覧の生成だけを確認したいとき。
- `cmoc apply join` や `cmoc session abandon` など、別サブコマンドの終了・統合手順だけを確認したいとき。

## hash

- b1aeea9d255ad377da593edfd71750a2c0351cb774026e2d5715ccb11078e083

# `fork.py`

## Summary

- `src/sub_commands/apply/fork.py` は `cmoc apply` の本体処理を担う実装モジュールです。
- session branch の前提条件確認から、apply branch / worktree の作成、`INDEX.md` の維持、不整合調査、修正適用、コミット、レポート出力までを一連で扱います。
- Structured Output の schema 検証、対象ファイルの列挙、部分適用・全体適用の分岐、禁止領域の検査、apply state の更新とエラー時復旧も含みます。
- Codex CLI への調査依頼・要修正点改善・修正作業・commit message 生成・作業レポート生成の各 prompt もこのファイルで組み立てます。

## Read this when

- `cmoc apply fork` の全体フローを実装・修正・レビューしたいとき。
- session state の検証、apply branch / worktree の作成、調査・修正ループ、レポート生成までの実行順を確認したいとき。
- 部分適用モードと全体適用モードの切り替え、対象ファイル列挙、要修正点リストの改善ループを確認したいとき。
- Structured Output の検証、禁止領域チェック、コミット、状態遷移、apply report の YAML Front Matter 付与を確認したいとき。
- 調査対象ファイルに対する Codex CLI のプロンプト構築や、要修正点の整理・再構成の責務を確認したいとき。

## Do not read this when

- `cmoc apply join` や `cmoc apply abandon` だけの挙動を確認したいとき。
- `cmoc session fork/join/abandon` など、apply ではないサブコマンドだけを追いたいとき。
- `cmoc apply fork` の仕様断片そのものを読みたいときは、`oracles/app_specs/sub_commands/apply_fork.md` を直接読むべきです。
- Codex CLI 呼び出しや Structured Output の共通基盤だけを確認したいときは、このファイルではなく共通実装を読むべきです。

## hash

- c2ed5b844b68241da6c30ef7a8443a7e500efd4717244ad75961e5a8a9243a46

# `join.py`

## Summary

- `src/sub_commands/apply/join.py` は `cmoc apply join` の本体処理を実装します。
- 完了済み apply branch を session branch に取り込み、想定外差分の検出・強制復旧・merge conflict の報告・state 更新・後始末までを扱います。

## Read this when

- `cmoc apply join` の実装・修正・レビューで、処理順と例外条件を確認したいとき。
- 想定外差分の通常モードと `--force-resolve` の分岐、`session.state` / `apply.state` の更新条件を確認したいとき。
- merge 後の apply branch と apply worktree の削除条件、warning の出し方を確認したいとき。

## Do not read this when

- `cmoc apply fork` の調査・修正ループやレポート保存の仕様だけを確認したいとき。
- `cmoc apply abandon` の破棄手順や cleanup 条件だけを確認したいとき。
- `cmoc session join` など session 側の統合手順だけを確認したいとき。

## hash

- 873ce192533a75fbd927b6531ea8bc5aaa6d04d067c1e8e7207ee57f5de7fa66
