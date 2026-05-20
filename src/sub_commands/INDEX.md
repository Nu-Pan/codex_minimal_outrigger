# `__init__.py`

## Summary

- cmoc のサブコマンド実装パッケージであることを示すパッケージ初期化ファイル。
- 実行ロジックや公開 API の定義は含まず、パッケージ用途を docstring で説明するだけのファイル。

## Read this when

- src/sub_commands 配下が何のためのパッケージかを最小限確認したいとき。
- サブコマンド実装モジュール群のパッケージ境界や概要を確認したいとき。

## Do not read this when

- 個別サブコマンドの処理内容、引数、実行フローを調べたいとき。
- cmoc のコマンドルーティング、CLI エントリポイント、サブコマンド登録方法を調べたいとき。
- 実装上の詳細な仕様やテスト対象の振る舞いを確認したいとき。

## hash

- ea4df02b820eba1ca77dfb1b2227c81dbff61cd7c4c2bf4d26d891369b57fa77

# `apply.py`

## Summary

- `src/sub_commands/apply.py` は `cmoc apply` の本体処理を実装するファイルです。
- cmoc 作業ブランチの検証、oracle 由来差分のコミット、`INDEX.md` メンテナンス、不整合調査、実装修正依頼、禁止パス検査、変更コミット、apply レポート生成までの実行フローを扱います。
- 不整合調査では oracle ファイル起点と実装ファイル起点の両方から Codex CLI を read-only Structured Output で呼び出し、`discrepancies` 配列を検証・整理します。
- 部分適用と全体適用の切り替え、変更済み oracle・実装ファイルの抽出、削除検出時の全体適用へのフォールバックを扱います。
- 実装修正では Codex CLI を workspace-write で呼び出し、`oracles`、`.agents`、`memo` などの禁止領域が変更されていないことを commit 前に検査します。
- apply レポート生成では `.cmoc/reports/apply` 配下へタイムスタンプ付き Markdown を保存し、収束・未収束、不整合件数推移、ブランチ上の全変更内容の必須記述を検証します。
- このファイルには不整合 Structured Output schema、調査・整理・修正・commit message・レポート生成用 prompt、JSON payload validator が含まれます。

## Read this when

- `cmoc apply` の全体処理順序を実装または確認したいとき。
- cmoc 作業ブランチでのみ apply を許可する条件や、base commit を使った変更範囲の扱いを調べたいとき。
- apply 実行前に未コミット差分をどのように検査し、`.gitignore`、`.cmoc`、`oracles` の保証差分を commit するか確認したいとき。
- `cmoc apply` が `INDEX.md` をいつメンテナンスするか確認したいとき。
- oracle と実装の不整合調査で Codex CLI に渡す Structured Output schema、prompt、validator を調べたいとき。
- 部分適用と全体適用の判定、変更済み oracle ファイル・実装ファイルの選別、削除検出時の挙動を確認したいとき。
- 不整合リストの重複整理や矛盾調整を Codex CLI に依頼する処理を調べたいとき。
- 不整合ごとに Codex CLI へ実装修正を依頼し、その後の禁止パス検査と commit を行う処理を確認したいとき。
- `cmoc apply` の未収束時 exit code、repeat 回数、ループごとの不整合件数記録を調べたいとき。
- apply レポートの保存先、必須見出し、収束・未収束表示、検証条件を実装または修正したいとき。

## Do not read this when

- `cmoc apply` の CLI 引数定義や argparse への接続だけを確認したいとき。
- Codex CLI 呼び出しの低レベル実装、ログ保存、リトライ、sandbox 指定の共通処理だけを調べたいとき。
- git 操作、ブランチ判定、変更ファイル列挙、commit 実行などの共通 repository helper の実装詳細だけを調べたいとき。
- `INDEX.md` メンテナンス処理そのものの対象ディレクトリ、除外規則、ハッシュ検証、生成 prompt の詳細だけを調べたいとき。
- `cmoc init`、`cmoc branch`、`cmoc eval-oracles`、`cmoc merge` の個別挙動を調べたいとき。
- cmoc の開発規約、テスト規約、Python コーディング規約など実装者向けルールだけを確認したいとき。
- oracle 正本仕様断片の内容そのものを確認したいとき。
- apply が生成したレポートの実ファイル内容や過去の実行結果だけを読みたいとき。

## hash

- 01f9fea017cf85c87dcc9a30b4d2694abc20f914d060db62567c81fa527e9862

# `branch.py`

## Summary

- `cmoc branch` サブコマンドの本体処理を実装するファイル。
- 共通 runner 経由の repo root 解決、作業用ブランチ作成、`.cmoc` の git ignore 保証、作成元 commit の `.cmoc/branch` への記録を行う。
- ブランチ名は `cmoc_<timestamp>` 形式で生成し、衝突時は最大 10 回リトライする。
- 実行中の進捗表示は `branch (1/3)` から `branch (3/3)` までの段階表示と、各ブランチ作成試行の表示で構成される。
- 処理時間の計測と完了時レポートには `StepTimer` を使用する。

## Read this when

- `cmoc branch` の実装フローを確認したいとき。
- 作業用ブランチ名の生成規則や、timestamp 衝突時のリトライ挙動を調べたいとき。
- `cmoc branch` が base commit をどのタイミングで取得し、どこへ保存するか確認したいとき。
- `.cmoc` を git 追跡対象外にする処理が `cmoc branch` 内でいつ呼ばれるか調べたいとき。
- `cmoc branch` の stdout 進捗表示や `StepTimer` による計測箇所を確認したいとき。

## Do not read this when

- `cmoc init`、`cmoc apply`、`cmoc merge`、`cmoc eval-oracles` など他サブコマンドの本体処理を調べたいとき。
- repo root 探索、git 実行、`.cmoc` パス生成、timestamp 生成、時間計測などの共通ユーティリティ実装そのものを調べたいとき。
- `cmoc branch` の正本仕様やユーザー向け仕様だけを確認したいとき。
- 自動テストの構成、Fake Codex CLI、pytest 規約を調べたいとき。
- cmoc を用いて開発する `<repo-root>` 側の oracle や `INDEX.md` 生成仕様を調べたいとき。

## hash

- 3f0f49fc6b3453d7c26dea4e5cb47b8bd0b23b7378f6d77da6eeb182a334eee7

# `eval_oracles.py`

## Summary

- `cmoc eval-oracles` サブコマンドの本体処理を実装するファイル。
- `.cmoc` の git ignore 保証、`INDEX.md` メンテナンス、評価対象 oracle ファイルの選択、Codex CLI による oracle 評価、Markdown レポート保存までの一連の処理を担当する。
- `--full` 指定、cmoc ブランチ判定、base commit、削除 oracle の有無に基づいて、部分評価と全体評価を切り替える。
- oracle 評価用プロンプトを組み立て、参照範囲、必須見出し、ファイル編集禁止、`memo` 読み書き禁止などを Codex CLI に渡す。
- 評価出力に必須見出しが含まれることを検証し、`.cmoc/reports/eval-oracles/<timestamp>.md` に frontmatter 付きで評価結果を保存する。

## Read this when

- `cmoc eval-oracles` の実行フロー、進捗表示、ステップ構成を確認したいとき。
- oracle 評価が部分評価になる条件、全体評価になる条件、`--full` の影響を調べたいとき。
- Codex CLI に渡す oracle 評価プロンプトの内容や、評価時の参照禁止範囲を確認したいとき。
- 評価レポートに要求される必須見出しや、出力検証の条件を確認したいとき。
- `.cmoc/reports/eval-oracles` に保存される評価レポートのパス、frontmatter、oracle ごとの本文構成を調べたいとき。
- `commons.codex`、`commons.indexing`、`commons.repo`、`commons.timing`、`commons.timestamps` との連携箇所を確認したいとき。

## Do not read this when

- `cmoc eval-oracles` ではなく、`init`、`branch`、`apply`、`merge` など他サブコマンドの本体処理を調べたいとき。
- Codex CLI 実行の低レベル実装、リトライ、ログ保存、Structured Output 処理などの共通処理だけを調べたいとき。
- oracle ファイル列挙、変更 oracle 検出、cmoc ブランチ判定、base commit 読み取りなどの git・repo 共通ヘルパー自体を修正したいとき。
- `INDEX.md` メンテナンス処理の詳細な対象ディレクトリ、除外規則、ハッシュ判定、目次生成処理を調べたいとき。
- 評価レポートのタイムスタンプ生成やステップ時間計測の共通実装だけを確認したいとき。
- cmoc の正本仕様断片そのものや、`cmoc eval-oracles` の仕様上の期待挙動を確認したいだけのとき。

## hash

- 831c8e5abba60851849dc02b00f8b1a6a1fdf9e33dd09e876e8952ae342efc3b

# `init.py`

## Summary

- `cmoc init` サブコマンドの本体処理を定義する実装ファイル。
- `cmoc_init_impl` は、直接呼び出し時に共通 runner へ処理を委譲し、`repo_root` 解決と共通エラー整形を受ける。
- 初期化処理として、対象リポジトリで `.cmoc` が git 追跡対象外になるよう `.gitignore` ルールや tracked file 解除を保証する。
- 初期化で発生した `.gitignore` や git index の変更だけをコミットし、変更がない場合はその旨を表示する。
- `StepTimer` により `init` の各ステップ開始と最終的な経過時間レポートを行い、stdout に 2 段階の進捗を表示する。

## Read this when

- `cmoc init` の実装本体を確認したいとき。
- `.cmoc` を git 追跡対象外にする処理の呼び出し順序を確認したいとき。
- `cmoc init` が `.gitignore` や git index の変更をどの条件でコミットするか調べたいとき。
- `cmoc init` の stdout 進捗表示、ステップ名、完了時の時間レポートを確認したいとき。
- `cmoc_init_impl` をテストから直接呼び出す際の `repo_root` 引数の扱いを確認したいとき。

## Do not read this when

- CLI エントリーポイントで `init` サブコマンドがどう登録されるかだけを調べたいとき。
- `.cmoc` ignore ルールの具体的な `.gitignore` 編集や git 操作の詳細実装を調べたいとき。
- 共通 runner の repo root 解決、例外処理、終了ステータス整形の詳細を調べたいとき。
- タイマーや経過時間表示の内部実装だけを調べたいとき。
- `cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` など他サブコマンドの挙動を調べたいとき。

## hash

- 253e20a5cd3777cd63492c0bac7fb6ed2c0dc7fdefeb5135264b7912c81b9a7a
