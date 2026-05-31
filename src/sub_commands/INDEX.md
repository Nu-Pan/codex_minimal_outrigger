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

- `src/sub_commands/apply` は `cmoc apply` 系サブコマンド実装の入口ディレクトリです。
- ここには `__init__.py`、`abandon.py`、`fork.py`、`join.py` があり、apply 系のパッケージ宣言、破棄、調査・修正ループ、取り込み処理をまとめています。
- 個別の apply サブコマンド実装へ進む前に、このディレクトリ全体の責務分担を確認したいときに読む目次です。

## Read this when

- `cmoc apply` 系の実装・修正・レビュー・テストを始める前に、どのモジュールを開くべきか整理したいとき。
- apply のパッケージ入口と、`abandon` / `fork` / `join` の役割分担を素早く把握したいとき。
- apply state、worktree、merge 後始末、レポート生成など、`cmoc apply` 周辺の処理を横断して確認したいとき。

## Do not read this when

- `cmoc apply` の利用手順や正本仕様だけを確認したいときは、`oracles/docs/app_specs/sub_commands/` 側を読むべきです。
- 個別の `cmoc apply abandon`、`cmoc apply fork`、`cmoc apply join` の詳細だけを確認したいときは、対応する実装モジュールを直接読むべきです。
- `cmoc session` や `cmoc review` など、apply 以外のサブコマンドを確認したいときはこのディレクトリは対象外です。

## hash

- 94abc904b4bc4594fcf526b8a269dc5fab05e96976fd9e38bf969cec2700274c

# `init.py`

## Summary

- `src/sub_commands/init.py` は `cmoc init` の本体処理を持つモジュールです。
- `repo_root` が未指定なら `run_command()` に処理を委譲し、指定済みなら `.cmoc ignore 確認` と `初期化変更 commit` の 2 ステップで初期化を進めます。
- `.cmoc` の ignore 保証、既存 tracked `.cmoc` の追跡解除、初期化に伴う差分の commit と結果表示をまとめて扱います。

## Read this when

- `cmoc init` の実装・修正・テスト・レビューを行いたいとき。
- `.cmoc` を git 追跡対象外にする処理、`.gitignore` 更新、tracked file の解除、初期化差分の commit 規則を確認したいとき。
- `run_command()` 経由で repo root を解決しつつ、`StepTimer` と `start_step()` で 2 段階の初期化フローをどう実行するかを把握したいとき。

## Do not read this when

- `cmoc init` 以外のサブコマンドの入口や CLI 登録だけを確認したいとき。
- `.cmoc` の ignore 保証や初期化 commit の流れが論点に入っていないとき。
- 初期化後の session / apply の運用仕様だけを追いたいとき。

## hash

- b9f241adfbc212ed6bd5bdbbab857c8655a53319b89c2119409e8c3d14c59733

# `review`

## Summary

- `src/sub_commands/review` は `cmoc review` 系サブコマンドの入口ディレクトリです。
- `__init__.py` はパッケージ宣言のみを担う最小モジュールです。
- `oracles.py` は `cmoc review oracles` の本体処理を担い、snapshot 固定、評価、改善、レポート出力までを実行します。

## Read this when

- `src/sub_commands/review` が Python パッケージとして宣言されていることを確認したいとき。
- `cmoc review oracles` の本体処理、開始時点の `oracles` スナップショット固定、`INDEX.md` メンテナンス、oracle ファイルごとの評価、問題点リスト改善、レポート保存の流れを確認したいとき。
- Structured Output の検証条件や、参照してよい `oracles` 配下ファイルの制約を確認したいとき。
- 評価失敗時のエラーレポート生成や、`.cmoc/reports/review_oracles` への出力規則を確認したいとき。

## Do not read this when

- このディレクトリ全体の入口構造ではなく、`cmoc review oracles` の利用手順や引数だけを確認したいとき。
- `cmoc review oracles` ではなく、`cmoc review` の CLI 登録や hidden alias の扱いだけを確認したいとき。
- `oracles` 側の正本仕様を直接確認したいとき。

## hash

- 1e63bb590674da7f24778bc2e117c5132d0b50e58f4ce1b3048c368d5edaa25f

# `session`

## Summary

- `src/sub_commands/session` は `cmoc session` 系サブコマンドをまとめるパッケージです。
- `__init__.py` はパッケージ宣言のみを担い、`abandon.py`、`fork.py`、`join.py` がそれぞれ `cmoc session abandon`、`cmoc session fork`、`cmoc session join` の本体実装です。
- session の開始、統合、破棄に関する処理を、このディレクトリ配下で一通り扱います。

## Read this when

- `cmoc session fork`、`cmoc session join`、`cmoc session abandon` の実装や修正、レビュー、テストを行うとき。
- `src/sub_commands/session` ディレクトリ全体の役割と、どの実装ファイルへ進むべきかを把握したいとき。
- `cmoc session` 系サブコマンドの入口となる Python パッケージ構造を確認したいとき。

## Do not read this when

- `cmoc session` ではなく、`cmoc apply` や `cmoc review` など別系統のサブコマンド仕様だけを確認したいとき。
- `session` 配下の個別実装ではなく、`oracles/docs/app_specs/sub_commands/` 側の利用手順や仕様断片を直接確認したいとき。
- `src/sub_commands/session` の入口構造ではなく、一般的な git の使い方や他ディレクトリの目次だけを確認したいとき。

## hash

- ed2c7ee7987d83daf4ac9fe867871fa34ebcea43e847e62ffa5af4b802c4ac89
