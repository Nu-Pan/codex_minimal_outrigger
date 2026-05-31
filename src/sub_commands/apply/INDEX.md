# `__init__.py`

## Summary

- `src/sub_commands/apply/__init__.py` は `cmoc apply` 系サブコマンドのパッケージ宣言だけを担う最小モジュールです。
- 公開 API、定数、実行ロジック、再エクスポートは持ちません。

## Read this when

- `src/sub_commands/apply` が Python パッケージとして宣言されていることを確認したいとき。
- `cmoc apply` 系サブコマンドの入口となるパッケージ構造を把握したいとき。

## Do not read this when

- 個別の `cmoc apply fork/join/abandon` の実行フローや状態遷移を確認したいときは、このファイルではなく各実装モジュールを読むべきです。
- `cmoc apply` の仕様断片や利用手順だけを確認したいときは、`oracles/docs/app_specs/sub_commands/` 側を読むべきです。

## hash

- 5646cb02b7ca8e507d8725e2d5f87e9580881d66ce1a67505595830d53c239d6

# `abandon.py`

## Summary

- `src/sub_commands/apply/abandon.py` は `cmoc apply abandon` の本体処理を実装するモジュールです。
- 現在の session に紐づく未 join の apply run を検証し、必要に応じて実行中の apply プロセスを停止したうえで、apply branch と worktree を強制削除して `apply.state` を `ready` に戻します。
- 現在の branch が apply branch の場合は cleanup 基点を session branch へ移し、破棄結果と warning を標準出力へ出力し、次回の apply に向けて session state の補助情報を初期化します。

## Read this when

- `cmoc apply abandon` の役割と責務を素早く把握したいとき。
- `session.state` / `apply.state` の前提条件、未 join の apply run の破棄条件、実行中プロセス停止の流れを確認したいとき。
- apply branch / worktree の強制削除、現在 branch から cleanup 基点を session branch へ移す処理を確認したいとき。
- 破棄結果、warning の出力、`apply.state` を `ready` に戻して補助情報を初期化する後始末を確認したいとき。
- `cmoc apply abandon` の実装・修正・レビュー・テストを始める前に、処理順と状態遷移を確認したいとき。

## Do not read this when

- `cmoc apply fork` の調査・修正ループや report 生成だけを追いたいとき。
- `cmoc apply join` の取り込み条件や merge 後 cleanup だけを確認したいとき。
- `cmoc session abandon` など、session 側の破棄処理だけを確認したいとき。
- `cmoc apply abandon` の利用手順や正本仕様だけを確認したいときは、実装ではなく `oracles/docs/app_specs/sub_commands/apply_abandon.md` を読むべきとき。

## hash

- 8e26c25997d2fb1e023a22f874a77d1a62d14bce457fe94e1f88ebda0b902ca0

# `fork.py`

## Summary

- `src/sub_commands/apply/fork.py` は `cmoc apply fork` の本体実装で、session branch 上で専用 apply branch と worktree を作成し、調査・修正ループとレポート出力までを担うモジュールです。
- 起動前の session/apply state 検証、` .cmoc` の ignore 保証、apply start のロック、worktree 作成のリトライ、`apply.state` の `running` / `completed` / `error` 更新を扱います。
- Structured Output による要修正点の収集と改善、scope に応じた対象ファイル選定、dirty path の更新、各修正ごとの禁止領域チェックと commit、さらに `INDEX.md` 保守と report 生成まで含みます。

## Read this when

- `cmoc apply fork` の本体実装の責務と処理順を確認したいとき。
- session/apply state の検証、`--repeat-investigate-and-fix`、`--repeat-improove-fixing-list`、`--scope` の挙動を追いたいとき。
- 要修正点の Structured Output、調査対象ファイルの選定、改善ループ、修正適用、commit の流れを実装・修正・レビュー・テストしたいとき。
- apply branch と専用 worktree の作成・再試行・状態更新、`running` / `completed` / `error` 遷移の実装を確認したいとき。
- 禁止領域の検査、`INDEX.md` の保守、report / error report の生成方針を追いたいとき。

## Do not read this when

- `cmoc apply join` や `cmoc apply abandon` の終了・破棄処理だけを確認したいとき。
- `cmoc apply fork` の利用手順だけを知りたいときは、実装ではなく `oracles/docs/app_specs/sub_commands/apply_fork.md` を読むべきとき。
- `src/sub_commands/apply` パッケージ全体の入口構造だけを把握したいとき。
- `INDEX.md` の生成ルールや `oracles` 全体のルーティング方針だけを確認したいとき。

## hash

- c52f543cb084e3647f228e9e51535fe14035c354e353c69a9e1ea71cbeee11a5

# `join.py`

## Summary

- `src/sub_commands/apply/join.py` は `cmoc apply join` の本体実装で、完了済みの apply branch を session branch に取り込む処理を担います。
- session/apply state の検証、現在ブランチと local branch の存在確認、未コミット差分の確認、想定外差分の `--force-resolve` 処理をまとめて扱います。
- merge 後の `apply.state=ready` への更新と、保存済み report/result を前提にした apply branch / worktree の cleanup まで含みます。

## Read this when

- `cmoc apply join` の実装・修正・レビュー・テストを行うとき。
- `--force-resolve` の有無で、想定外差分をどう扱うか確認したいとき。
- `INDEX.md` の conflict 解消条件や、merge 後の state 更新・後始末を追いたいとき。
- apply report と result の保存状況に応じて、apply branch と worktree を削除してよい条件を確認したいとき。

## Do not read this when

- `cmoc apply fork` の調査・改善ループや要修正点リストの仕様だけを確認したいとき。
- `cmoc apply abandon` や session 系サブコマンドの終了・破棄・統合だけを確認したいとき。
- `cmoc apply join` の利用手順そのものではなく、`oracles/docs/app_specs/sub_commands/apply_join.md` の正本仕様だけを読みたいとき。

## hash

- d1cc0771201cd6eb8c88405859e2a0593f5d2ad21be3cc8cff455dc97ef9a656
