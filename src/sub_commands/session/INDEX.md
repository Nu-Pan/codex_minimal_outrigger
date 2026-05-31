# `__init__.py`

## Summary

- `src/sub_commands/session/__init__.py` は `cmoc session` 系サブコマンドのパッケージ宣言だけを担う最小モジュールです。
- 公開 API、定数、実行ロジック、再エクスポートは持ちません。

## Read this when

- `src/sub_commands/session` が Python パッケージとして宣言されていることを確認したいとき。
- `cmoc session` 系サブコマンドの入口となるパッケージ構造を把握したいとき。

## Do not read this when

- 個別の `cmoc session fork/join/abandon` の実行フローや状態遷移を確認したいときは、このファイルではなく各実装モジュールを読むべきです。
- `cmoc session` の仕様断片や利用手順だけを確認したいときは、`oracles/docs/app_specs/sub_commands/` 側を読むべきです。

## hash

- cae1fe2deaf0b783c45fb2b0cb686d48eb34f14259fb35febfc5cb7ed819653a

# `abandon.py`

## Summary

- `src/sub_commands/session/abandon.py` は `cmoc session abandon` の本体実装で、現在 checkout 中の session branch を merge せずに破棄して home branch へ戻します。
- 実行前に現在 branch、session/apply state、記録済み home branch の存在、`.cmoc` の ignore/clean 状態を確認し、必要な退避情報を保持します。
- 失敗時は session state と branch HEAD を元に戻して再実行可能な状態へ復旧し、詳細付きの `CmocError` を投げます。

## Read this when

- `cmoc session abandon` の実装・修正・レビュー・テストを行うとき。
- session branch を merge せずに破棄する前提条件や、`session.state` / `apply.state` の検証条件を確認したいとき。
- `.cmoc` の ignore 保証、home branch への切り替え、session branch 削除、`session.state=abandoned` 更新の順序を追いたいとき。
- cleanup 失敗時の rollback と、再実行前に手動復旧が必要な箇所を確認したいとき。

## Do not read this when

- `cmoc session fork` や `cmoc session join` の開始・統合処理だけを確認したいとき。
- `cmoc apply abandon` など、apply 側の破棄仕様だけを確認したいとき。
- `src/sub_commands/session` パッケージ全体の入口構造だけを確認したいとき。
- `cmoc session abandon` の利用手順ではなく、`oracles/docs/app_specs/sub_commands/session_abandon.md` の仕様断片を直接確認したいとき。

## hash

- 42100c686956ebb06fb98dd7a9cea0330d5185697558b863c204a0bf2759fdcd

# `fork.py`

## Summary

- `src/sub_commands/session/fork.py` は `cmoc session fork` の本体実装で、現在 checkout 中の local branch を session home branch とみなし、その HEAD から `cmoc/session/<session-id>` を作成します。
- detached HEAD、local branch 以外、cmoc 管理 branch、未コミット差分、既存 active session を検査し、`.cmoc` の非追跡保証も確認します。
- session 作成の直列化、timestamp ベースの一意な branch 名生成、session state の保存、保存失敗時の rollback までを扱います。

## Read this when

- `cmoc session fork` の実装・修正・レビュー・テストを行うとき。
- 現在 checkout 中の local branch を session home branch とみなす条件を確認したいとき。
- detached HEAD、remote-tracking branch、未コミット差分、cmoc 管理 branch、既存 active session の扱いを確認したいとき。
- session branch 名の生成、`.cmoc` の保証、state 保存失敗時の rollback や再実行性を確認したいとき。

## Do not read this when

- `cmoc session join` や `cmoc session abandon` の終了・破棄処理だけを確認したいとき。
- `cmoc apply` 系サブコマンドの開始・統合・破棄だけを確認したいとき。
- 一般的な git の branch 作成手順や、`src/sub_commands/session` パッケージ全体の入口構造だけを確認したいとき。
- `cmoc session fork` の利用手順ではなく、`oracles/docs/app_specs/sub_commands/session_fork.md` の仕様断片だけを確認したいとき。

## hash

- b9614b8a7b0f202921401390479ccedcba42b79e0e4fdedbddd3f0252276bf20

# `join.py`

## Summary

- `src/sub_commands/session/join.py` は `cmoc session join` の本体実装です。
- 現在の session branch を記録済みの session home branch に `git merge --no-ff` で取り込み、join 完了までの後始末を行います。
- 状態検証、`.cmoc` の ignore 保証、conflict 時の Codex 依頼、merge state の保護、session state 更新、branch 削除可否の判断をまとめて扱います。

## Read this when

- `cmoc session join` の前提条件、merge 手順、後始末を実装・修正・レビュー・テストしたいとき。
- session branch から記録済みの home branch へ戻す流れや、`session.state` / `apply.state` の検証条件を確認したいとき。
- merge conflict 発生時に、Codex CLI へ依頼してよい範囲と、`oracles` / `README.md` / `AGENTS.md` / `memo` / `.agents` の扱いを確認したいとき。
- merge 後の `session.state=joined` 更新や、安全な場合だけ branch を削除する条件を追いたいとき。

## Do not read this when

- `cmoc session fork` や `cmoc session abandon` の挙動だけを確認したいとき。
- `cmoc apply` 系サブコマンドの開始・統合・破棄だけを確認したいとき。
- `cmoc session join` の利用手順や仕様断片だけを確認したいときは、実装ではなく `oracles/docs/app_specs/sub_commands/session_join.md` を読むべきとき。
- 一般的な `git merge` の説明だけで足り、cmoc 独自の session state 管理や conflict 保護が不要なとき。

## hash

- afa182bff0d20972666b527766f16bb565a600f11aef2451396c6717a2b95615
