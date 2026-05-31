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

- `src/sub_commands/apply` は `cmoc apply` 系サブコマンドの実装入口です。
- `__init__.py` はパッケージ宣言のみで、本体ロジックは `fork.py`、`join.py`、`abandon.py` に分かれています。
- この目次は、開始・統合・破棄のどの実装ファイルへ進むべきかを素早く振り分けるためのものです。

## Read this when

- `src/sub_commands/apply` の実装入口と、各モジュールの担当範囲を確認したいとき。
- `cmoc apply fork`、`cmoc apply join`、`cmoc apply abandon` のどれを読むべきか整理したいとき。
- 実装・修正・レビュー・テストを始める前に、関連ファイルの入口を把握したいとき。
- 開始・統合・破棄の役割分担を俯瞰して、目的の実装ファイルへ素早く進みたいとき。

## Do not read this when

- 個別の `cmoc apply fork`、`cmoc apply join`、`cmoc apply abandon` の詳細な実装フローや状態遷移だけを確認したいとき。
- `src/sub_commands/apply` のパッケージ宣言だけを確認したいとき。
- 利用手順や正本仕様の断片だけを確認したいときは、実装ではなく `oracles/docs/app_specs/sub_commands/` 側を読むべきとき。
- `src/sub_commands/apply` 全体ではなく、`src/commons` や他のサブコマンドの共通仕様を確認したいとき。

## hash

- c1e45d07798f0b39f6d765f9e24859e0dec24992f2280884d66bee99b0205a76

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
- `__init__.py` はパッケージ宣言のみを担う最小モジュールです。
- `oracles.py` は `cmoc review oracles` の本体処理を担い、snapshot 固定、評価、改善、レポート出力までを実行します。

## Read this when

- `src/sub_commands/review` が Python パッケージとして宣言されていることを確認したいとき。
- `cmoc review oracles` の本体処理、開始時点の `oracles` スナップショット固定、`INDEX.md` メンテナンス、oracle ファイルごとの評価、問題点リスト改善、レポート保存の流れを確認したいとき。
- Structured Output の検証条件や、参照してよい `oracles` 配下ファイルの制約を確認したいとき。
- 評価失敗時のエラーレポート生成や、`.cmoc/reports/review_oracles` への出力規則を確認したいとき。

## Do not read this when

- `cmoc review oracles` の実行手順、引数、評価モードの仕様だけを確認したいときは、`oracles.py` 側の入口ではなく仕様断片を読むべきです。
- `cmoc review` の CLI 登録や hidden alias の扱いだけを確認したいときは、`src/main.py` を読むべきです。
- `src/sub_commands/review` ディレクトリ全体の入口構造ではなく、個別の実装ロジックや仕様断片だけを確認したいときは、この目次ではなく該当ファイルを直接読むべきです。

## hash

- 73e808270f2261d242d616c7dc6e57d3bec6a0f0c78b16467409bb2df6297a67

# `session`

## Summary

- `src/sub_commands/session` は `cmoc session` 系サブコマンドをまとめるパッケージです。
- `__init__.py` はパッケージ宣言のみを担い、`abandon.py`、`fork.py`、`join.py` がそれぞれ `cmoc session abandon`、`cmoc session fork`、`cmoc session join` の本体実装です。
- session の開始、統合、破棄に関する処理を、このディレクトリ配下で一通り扱います。

## Read this when

- `cmoc session fork`、`cmoc session join`、`cmoc session abandon` の実装や修正を行うとき。
- `session` サブコマンド群のパッケージ構成と、各実装ファイルの役割を把握したいとき。
- `cmoc session` の起点となる Python パッケージの中身を確認したいとき。

## Do not read this when

- `cmoc apply` 系の実装や状態遷移だけを確認したいとき。
- `cmoc review oracles` や `cmoc init` など、`session` 以外のサブコマンドの仕様を確認したいとき。
- `src/sub_commands/session` 配下の個別実装ではなく、`oracles` 側の正本仕様だけを確認したいとき。

## hash

- 9bed792e17287b8a3555168bd6af83b076231b3dcbfafecba5297707b96adaef
