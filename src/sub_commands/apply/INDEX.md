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

- bec22b07eb9dbd4f65bd37ab36391efed571f1ee57ee2d0b1f7ed706fb6b9a18

# `fork.py`

## Summary

- `cmoc apply fork` の本体実装で、session branch 上の apply run を開始し、不整合調査から修正反復、レポート出力までを担います。
- state 検証、apply worktree の作成、`running` / `completed` / `error` への状態遷移、終了コードの分岐をまとめています。

## Read this when

- `cmoc apply fork` の処理順や責務を追いたいとき。
- session/apply state の検証、` .cmoc` の ignore 保証、apply worktree 作成、排他制御の流れを確認したいとき。
- 要修正点の Structured Output、調査・修正ループ、`INDEX.md` の自動メンテナンスを確認したいとき。
- 途中失敗時の error report と、収束・未収束の終了コードを確認したいとき。

## Do not read this when

- `cmoc apply join` や `cmoc apply abandon` の終了・破棄処理だけを確認したいとき。
- `src/sub_commands/apply/__init__.py` など、パッケージ宣言や入口構造だけを確認したいとき。
- `oracles/docs/app_specs/sub_commands/apply_fork.md` の利用手順や引数仕様だけを確認したいとき。

## hash

- 5b7f1ac57be0122785aefb693a21b42b39d2d9cccd1c72cd4075e057285c8c25

# `join.py`

## Summary

- `src/sub_commands/apply` は `cmoc apply` 系サブコマンド実装の入口ディレクトリです。
- ここには `__init__.py`、`abandon.py`、`fork.py`、`join.py` があり、パッケージ宣言、破棄、調査・修正ループ、取り込み処理をまとめています。
- 個別の `cmoc apply` 実装へ進む前に、このディレクトリ全体の責務分担を確認するための目次です。

## Read this when

- `src/sub_commands/apply` 配下のどのモジュールを開くべきか、入口構造を確認したいとき。
- `cmoc apply` 系の破棄・調査修正・取り込みの責務分担を俯瞰したいとき。
- `cmoc apply` 系サブコマンドの実装・修正・テスト・レビューの前に、ディレクトリ全体の役割を整理したいとき。

## Do not read this when

- `cmoc apply` の個別サブコマンド `abandon` / `fork` / `join` の実装詳細だけを確認したいときは、対応するモジュールを直接読むべきです。
- `cmoc apply` の利用手順や正本仕様だけを確認したいときは、`oracles/docs/app_specs/sub_commands/` 側を参照すべきです。
- `src/sub_commands/apply` のパッケージ宣言だけで足りるときは、`__init__.py` だけを確認すれば十分です。

## hash

- 74bb0729c59be3763e62ed38de51dc709793ee0e7dead37aee8432a57e147c12
