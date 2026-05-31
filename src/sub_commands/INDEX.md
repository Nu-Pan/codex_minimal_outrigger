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

- `src/sub_commands/apply` は `cmoc apply` 系サブコマンドの実装パッケージで、`__init__.py`、`abandon.py`、`fork.py`、`join.py` をまとめています。
- このディレクトリは `cmoc apply` の本体処理と各サブコマンドの責務分担を読むための入口です。
- 利用手順や正本仕様ではなく、実装コードを追うときの案内先として使います。

## Read this when

- `src/sub_commands/apply` 配下の実装全体を把握したいとき。
- `cmoc apply abandon` / `cmoc apply fork` / `cmoc apply join` の実装・修正・レビュー・テストを進める前に、入口を確認したいとき。
- `src/sub_commands/apply` がどのモジュールで構成されているか、パッケージとしての役割を把握したいとき。

## Do not read this when

- `cmoc apply` の利用手順や仕様断片だけを確認したいときは、このディレクトリではなく `oracles/docs/app_specs/sub_commands/apply_*.md` を読むべきです。
- `cmoc session` や `cmoc review oracles` など、別サブコマンドの実装・仕様を確認したいときは、このディレクトリは対象外です。
- `INDEX.md` の生成ルールや `oracles` 全体のルーティング方針だけを確認したいときは、このディレクトリを読む必要はありません。

## hash

- 17d02c86fda9502abcbb54c40153c11adf1d1fd8ed75740d7d47f06ffcf3ecf3

# `init.py`

## Summary

- `cmoc init` の本体処理を実装している。
- 直接呼び出し時は共通 runner に委譲し、`.cmoc` の ignore 保証と初期化差分の commit を進める。

## Read this when

- `cmoc init` の実際の処理順や、`repo_root` 未指定時に共通 runner へ委譲する流れを確認したいとき。
- `.cmoc` を git 追跡対象外にする保証や、初期化時に発生した差分の commit 処理を実装・修正・レビューしたいとき。
- `src/sub_commands/init.py` の役割と、関連する共通処理の入口を把握したいとき。

## Do not read this when

- `cmoc init` 以外のサブコマンドの処理を見たいとき。
- `.cmoc` の git ignore 追加や tracked ファイル解除、初期化差分の commit が論点に含まれないとき。
- 初期化後の session/apply の運用仕様だけを確認したいとき。

## hash

- 766eb4ef5567a176766be2bb55dbc8f955c55af92c1ddc3f64043c1be4bda4ee

# `review`

## Summary

- `src/sub_commands/review` は `cmoc review` 系サブコマンド実装の入口です。
- `__init__.py` はパッケージ宣言のみを担い、実行ロジックは持ちません。
- `oracles.py` は `cmoc review oracles` の本体実装で、oracle スナップショット評価の入口です。

## Read this when

- `src/sub_commands/review` が Python パッケージとして宣言されていることを確認したいとき。
- `cmoc review` 系サブコマンドの入口となるパッケージ構造を把握したいとき。
- `cmoc review oracles` の実行フローや評価ロジックを確認したいときは、この目次から `oracles.py` に進みたいとき。

## Do not read this when

- `cmoc apply`、`cmoc session`、`cmoc init` など別サブコマンドの実装や仕様を追いたいとき。
- `cmoc review oracles` ではなく、`oracles` 配下の個別仕様断片そのものを直接確認したいとき。
- `src/sub_commands/review` のパッケージ宣言だけを確認したいときは、`__init__.py` を直接読むべきです。

## hash

- 1f6e4bb667025e8e35cdaa458b6674cb5018bc33043fdff73836dad1e5102560

# `session`

## Summary

- `src/sub_commands/session` は `cmoc session` 系サブコマンド実装の入口で、`__init__.py` と `fork.py`、`join.py`、`abandon.py` をまとめるディレクトリです。
- この配下では `fork` が session 開始、`join` が merge による完了、`abandon` が merge せず破棄を担当します。
- 個別の実装へ進む前に、session 系の責務分担と入口構造を把握するための目次です。

## Read this when

- `cmoc session` 系サブコマンドの入口と各モジュールの担当範囲を把握したいとき。
- `cmoc session fork`、`cmoc session join`、`cmoc session abandon` のどれを読むべきか整理したいとき。
- `src/sub_commands/session` 配下の実装・修正・レビュー・テストを始める前に、関連ファイルの入口を整理したいとき。

## Do not read this when

- 個別の `cmoc session fork`、`cmoc session join`、`cmoc session abandon` の詳細仕様、状態遷移、例外条件だけを確認したいとき。
- `cmoc apply` 系の開始・統合・破棄の流れだけを確認したいとき。
- `src/sub_commands/session` のパッケージ宣言だけを確認したいときは、`__init__.py` を直接読むべきです。

## hash

- 4c9f81c6c268782fe2a63c75da67e8be4603ce48d25c5ea4823cf9b0925ff95b
