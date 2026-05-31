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
- この配下には `__init__.py`、`abandon.py`、`fork.py`、`join.py` があり、各モジュールの責務分担をたどるための目次です。
- 個別実装に進む前に、apply 系の入口構造と担当範囲を俯瞰できます。

## Read this when

- `src/sub_commands/apply` が `cmoc apply` 系サブコマンドの実装パッケージであることを確認したいとき。
- `__init__.py` がパッケージ宣言だけを担い、`abandon.py`、`fork.py`、`join.py` がそれぞれ何を担当するか整理したいとき。
- `cmoc apply fork`、`cmoc apply join`、`cmoc apply abandon` のどの実装ファイルを読むべきか切り分けたいとき。

## Do not read this when

- `cmoc session`、`cmoc review`、`cmoc init` など、`apply` 以外のサブコマンドの入口だけを確認したいとき。
- 個別の `fork` / `join` / `abandon` の詳細仕様や実行フローを直接追いたいとき。
- `cmoc apply` の利用手順や仕様断片そのものを確認したいときは、`oracles/docs/app_specs/sub_commands/` 側を読むべきです。

## hash

- 8e4ff4f12009882d4c672e5634f60a4fe1216546c8b0423125d665e8977439b4

# `init.py`

## Summary

- `cmoc init` の本体処理を定義する Python モジュールです。
- `run_command()` 経由で repo root を解決し、`.cmoc` の ignore 保証と tracked file の解除を行ったうえで、初期化に伴う変更をコミットします。
- `StepTimer` と `start_step()` を使って、`.cmoc` の ignore 確認から初期化変更の commit までを 2 段階で実行し、結果を標準出力に表示します。

## Read this when

- `cmoc init` の実装・修正・テスト・レビューを行いたいとき。
- `<repo-root>/.cmoc` を git 追跡対象外にする処理や、`.gitignore` 更新、`git ls-files` / `git check-ignore` による確認仕様を確認したいとき。
- 初期化後に続く session / apply 系コマンドの前提条件として、リポジトリ初期化の振る舞いを把握したいとき。

## Do not read this when

- `cmoc init` 以外のサブコマンドの実装や CLI 登録だけを確認したいとき。
- `.cmoc` の追跡解除や `.gitignore` 更新が論点に入っていないとき。
- 初期化後の session / apply の運用仕様だけを追いたいとき。

## hash

- 49282f4cf811268918e12479be371a9a72bb21ad66319b738e5d27f3a0a4d00c

# `review`

## Summary

- `src/sub_commands/review` は `cmoc review` 系サブコマンドの入口ディレクトリです。
- `__init__.py` はパッケージ宣言のみを担い、`oracles.py` は `cmoc review oracles` の本体処理を担います。
- この目次は、レビュー系の入口と oracles 評価本体の役割分担を整理するための案内です。

## Read this when

- `src/sub_commands/review` が Python パッケージとして宣言されていることを確認したいとき。
- `cmoc review` 系サブコマンドの入口構造を把握したいとき。
- `cmoc review oracles` の実行フロー全体を追いたいとき。
- oracles スナップショットの固定、`INDEX.md` のメンテナンス、部分評価・全体評価の切り替え、並列評価、レポート保存の流れを確認したいとき。

## Do not read this when

- パッケージ宣言だけを確認したいときは `__init__.py` を直接読むべきです。
- `cmoc review oracles` の本体ロジックや評価手順を追いたいときは `oracles.py` を直接読むべきです。
- `cmoc review` の CLI 登録や hidden alias だけを確認したいときは `src/main.py` を読むべきです。

## hash

- 22163c54c069ebfbd25baa83e33afd14a2deb11dbf27a06be7f3bd46a5539bb8

# `session`

## Summary

- `src/sub_commands/session` は `cmoc session` 系サブコマンド実装の入口ディレクトリで、`__init__.py`、`fork.py`、`join.py`、`abandon.py` をまとめています。
- `fork.py` は session 開始、`join.py` は merge による完了、`abandon.py` は merge せず破棄を担当します。
- 個別実装へ進む前に、session 系の責務分担と各モジュールの位置関係を俯瞰するための目次です。

## Read this when

- `cmoc session` 系サブコマンドの入口構造を把握したいとき。
- `fork`、`join`、`abandon` のどの実装ファイルを読むべきか整理したいとき。
- `cmoc session fork`、`cmoc session join`、`cmoc session abandon` の実装・修正・レビュー・テストを始める前に、関連ファイルの位置関係を確認したいとき。

## Do not read this when

- `cmoc apply` や `cmoc init` など、session 以外のサブコマンドを確認したいとき。
- 個別の `fork` / `join` / `abandon` の手順、状態遷移、例外条件だけを確認したいときは、それぞれの実装モジュールを直接読むべきです。
- このディレクトリのパッケージ宣言だけで足りるときは、`__init__.py` を直接読めば十分です。

## hash

- 449f30d4ff4e943ae621908ae3b755154660ff6e2b8f5d23e781b5aa66158c5d
