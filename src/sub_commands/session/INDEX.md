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
- 実行前に current branch、session/apply state、local home branch の存在、`.cmoc` の ignore/clean 状態を検証し、rollback 用に branch HEAD と state を退避します。
- 途中失敗時は session state と branch HEAD を元に戻し、再実行可能な状態へ復旧したうえで詳細付きの `CmocError` を投げます。

## Read this when

- `cmoc session abandon` の実装・修正・レビュー・テストを行うとき。
- session branch を merge せず破棄する前提条件や、`session.state` / `apply.state` の検証条件を確認したいとき。
- .cmoc の ignore 保証、home branch への switch、session branch 削除、`session.state=abandoned` 更新の順序を追いたいとき。
- cleanup 失敗時の rollback と、再実行前に手動復旧が必要な箇所を確認したいとき。

## Do not read this when

- `cmoc session fork` や `cmoc session join` の開始・統合処理だけを確認したいとき。
- `cmoc apply abandon` など、apply 側の破棄仕様だけを確認したいとき。
- `src/sub_commands/session` パッケージ全体の入口構造だけを確認したいとき。
- `cmoc session abandon` の利用手順ではなく、`oracles` 側の仕様断片を直接確認したいとき。

## hash

- 73180913e5250dbe8f3ddf0b5aba739c7130c8fb806670476d02053fd4f9ce35

# `fork.py`

## Summary

- `src/sub_commands/session/fork.py` は `cmoc session fork` の本体実装で、現在 checkout 中の local branch を session home branch とみなし、その HEAD から session branch を作成します。
- detached HEAD、local branch 以外、`cmoc` 管理 branch、未コミット差分、既存 active session を検査し、`.cmoc` の非追跡保証も確認します。
- session 作成の直列化、timestamp ベースの一意な branch 名生成、session state の保存、失敗時の rollback までを扱います。

## Read this when

- `cmoc session fork` の実装・修正・レビュー・テストを行うとき。
- 現在 checkout 中の local branch を session home branch とみなす条件を確認したいとき。
- detached HEAD、remote-tracking branch、未コミット差分、既存 active session の扱いを確認したいとき。
- session branch 名の生成、`.cmoc` の保証、state 保存失敗時の rollback を確認したいとき。

## Do not read this when

- `cmoc session join` や `cmoc session abandon` の終了処理だけを確認したいとき。
- `cmoc apply` 系の開始・統合・破棄だけを確認したいとき。
- 一般的な git の branch 作成手順だけを確認したいとき。
- `src/sub_commands/session` パッケージ全体の構造確認だけが目的のとき。

## hash

- b40681fa7743dc1b58feb5647ae1b232074b7017ff1c30cdb2fd00462efd2d1c

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
- `cmoc session join` の利用手順や仕様断片だけを確認したいときは、実装ではなく `oracles/docs/app_specs/sub_commands/session_join.md` を読むべきです。
- 一般的な `git merge` の説明だけで足り、cmoc 独自の session state 管理や conflict 保護が不要なとき。

## hash

- 8f0c9f70ee5b256ae84b2cb0ce2ab6a53e6066b9031e5051d6b1b686184f1f83
