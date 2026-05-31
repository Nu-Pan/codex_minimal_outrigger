# `__init__.py`

## Summary

- `src/sub_commands/__init__.py` は `src.sub_commands` パッケージを宣言するだけの最小モジュールです。
- 公開 API、定数、実行ロジック、再エクスポートは持ちません。

## Read this when

- `src.sub_commands` が Python パッケージとして宣言されていることを確認したいとき。
- `src/sub_commands` ディレクトリの入口として、最小限の役割だけを把握したいとき。
- パッケージとしての存在確認だけで足り、追加の公開 API や実行処理が不要なとき。

## Do not read this when

- `src.sub_commands` 配下の個別サブコマンド実装や実行フローを確認したいとき。
- `apply`、`session`、`review`、`init` などの各モジュールの仕様を追いたいとき。
- `src.sub_commands` のパッケージ宣言ではなく、実際の業務ロジックや CLI 入口を見たいとき。

## hash

- ea4df02b820eba1ca77dfb1b2227c81dbff61cd7c4c2bf4d26d891369b57fa77

# `apply`

## Summary

- `src/sub_commands/apply` は `cmoc apply` 系実装の入口ディレクトリです。
- `__init__.py` はパッケージ宣言のみを担い、`abandon.py` は破棄、`fork.py` は調査・修正ループ、`join.py` は取り込み処理を担います。
- 個別モジュールへ進む前に、この配下全体の責務分担を把握するための目次です。

## Read this when

- `src/sub_commands/apply` 配下でどのモジュールを開くべきか迷っているとき。
- `cmoc apply` の破棄・調査修正・取り込みの責務分担を俯瞰したいとき。
- `cmoc apply` 系実装・修正・テスト・レビューの前に、入口構造を整理したいとき。

## Do not read this when

- `cmoc apply` の利用手順や正本仕様だけを確認したいとき。
- 個別の `abandon` / `fork` / `join` の実装詳細だけを確認したいとき。
- `src/sub_commands/apply` のうち、特定の単一モジュールだけを確認すれば足りるとき。

## hash

- ad19e58c01251850726756ff430066d69c675d2f8a72293a4946bad890827a13

# `init.py`

## Summary

- `src/sub_commands/init.py` は `cmoc init` の本体処理を持つモジュールです。
- `repo_root` が未指定なら共通 runner に委譲し、指定済みなら `.cmoc` の ignore 確認と初期化変更の commit という 2 段階で処理します。
- `.cmoc` の ignore 保証、既存 tracked `.cmoc` の追跡解除、初期化に伴う差分 commit と結果表示をまとめて扱います。

## Read this when

- `cmoc init` の実装・修正・テスト・レビューを行いたいとき。
- `.cmoc` を git 追跡対象外にする処理、`.gitignore` 更新、tracked file の解除、初期化差分の commit 規則を確認したいとき。
- `run_command()` 経由で repo root を解決しつつ、`StepTimer` と `start_step()` で 2 段階の初期化フローをどう実行するかを把握したいとき。

## Do not read this when

- `cmoc init` 以外のサブコマンドの入口や CLI 登録だけを確認したいとき。
- `.cmoc` の ignore 保証や初期化 commit の流れが論点に入っていないとき。
- 初期化後の session / apply の運用仕様だけを追いたいとき。

## hash

- d521f2e6b339670dceeea2ae04fae5971c16a7ac9760586977de57e4f82240e6

# `review`

## Summary

- `src/sub_commands/review` は `cmoc review` 系サブコマンドの入口ディレクトリです。
- `__init__.py` はパッケージ宣言だけを担う最小モジュールです。
- `oracles.py` は `cmoc review oracles` の本体処理を担い、スナップショット固定、評価、改善、レポート出力までを実行します。

## Read this when

- `src/sub_commands/review` が Python パッケージとして宣言されていることを確認したいとき。
- `cmoc review` 系サブコマンドの入口構造や、`oracles.py` の役割を把握したいとき。
- `cmoc review oracles` の本体処理、開始時点の `oracles` スナップショット固定、評価、改善、レポート出力の流れを確認したいとき。

## Do not read this when

- `cmoc review oracles` の利用手順や引数だけを確認したいときは、`oracles/docs/app_specs/sub_commands/review_oracles.md` を読むべきです。
- `cmoc review` の CLI 登録や hidden alias だけを確認したいときは、`src/main.py` を読むべきです。
- `INDEX.md` の生成・更新ルールや、`oracles` 全体のルーティング方針だけを確認したいときは、このディレクトリを読む必要はありません。

## hash

- 85794ff51a4f9a190c00cedff044aa30985d0fa29a59ff9ca6121f5d889e709d

# `session`

## Summary

- `src/sub_commands/session` は `cmoc session` 系サブコマンドの実装入口です。
- `__init__.py` はパッケージ宣言だけを担う最小モジュールです。
- `abandon.py` は session branch を merge せず破棄して home branch へ戻す本体実装です。
- `fork.py` は local branch から session branch を作成し、session state を記録する本体実装です。
- `join.py` は session branch を home branch へ `git merge --no-ff` で取り込み、session を完了する本体実装です。

## Read this when

- `src/sub_commands/session` が Python パッケージとして宣言されていることを確認したいとき。
- `cmoc session abandon` の前提条件、cleanup 順序、rollback を確認したいとき。
- `cmoc session fork` の作成条件、branch 名、state 保存、retry を確認したいとき。
- `cmoc session join` の merge 手順、state 検証、conflict 解消、後始末を確認したいとき。

## Do not read this when

- `cmoc session` 以外の `cmoc` サブコマンドの実装だけを確認したいとき。
- `cmoc apply` 側の破棄や取り込みの仕様だけを確認したいとき。
- `oracles/docs/app_specs/sub_commands/` 側の正本仕様だけを確認したいとき。
- パッケージ宣言だけ、または一般的な git branch 操作だけを確認したいとき。

## hash

- 8abe880028a57337b24282d378c5dfa41d632400551b61888b63c54ff9589522
