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

- `cmoc apply` サブコマンドの本体処理を実装するファイル。cmoc 作業ブランチの検証、oracle 差分のコミット、INDEX.md メンテナンス、不整合調査、実装追従、変更コミット、apply レポート生成までの一連の制御フローを含む。
- Codex CLI に Structured Output で oracle と実装の不整合を調査させるための schema、調査対象ファイルの選定、部分適用と全体適用の切り替え、不整合リストの整理、個別不整合への追従依頼を扱う。
- apply 実行中に編集禁止領域が変更されていないかを検査し、`.cmoc/reports/apply` へのレポート保存、レポート必須項目の検証、Codex 生成 commit message による git commit を行う補助関数群を含む。
- Codex CLI に渡す調査・整理・適用・commit message・レポート生成用プロンプトと、Structured Output の discrepancies payload を機械的に検証するバリデーション関数を定義する。

## Read this when

- `cmoc apply` の実行順序、stdout の進捗表示、終了コード、未収束時の扱いを確認したいとき。
- apply が cmoc 作業ブランチ、base commit、oracle 差分、`.gitignore`、`.cmoc`、INDEX.md をどの順番で検証・更新・コミットするか調べたいとき。
- oracle と実装の不整合調査を Codex CLI にどう依頼し、Structured Output schema をどう定義・検証しているか確認したいとき。
- `--full` や削除ファイルの有無によって、部分適用と全体適用、oracle ファイルと実装ファイルの調査対象がどう選ばれるか知りたいとき。
- 検出された不整合を Codex CLI に実装修正させる処理、修正後の禁止パス検査、INDEX.md 再メンテナンス、git commit の流れを追いたいとき。
- apply レポートの保存先、生成プロンプト、必須見出し、未収束時に必要な文言、検証失敗時のエラー処理を確認したいとき。
- apply の Codex プロンプトに含まれる読み書き禁止パス、編集禁止パス、ファイル編集禁止指示を確認したいとき。

## Do not read this when

- `cmoc init`、`cmoc branch`、`cmoc eval-oracles`、`cmoc merge` など、apply 以外のサブコマンド本体だけを調べたいとき。
- Codex CLI 呼び出しの低レベル実装、JSON パース共通処理、コマンド runner、エラー整形、タイマー、タイムスタンプ生成の詳細だけを確認したいとき。
- git 操作、ブランチ判定、変更ファイル列挙、commit 実行、禁止差分検査などの共通 repo ユーティリティの実装詳細を読みたいとき。
- INDEX.md 自動メンテナンスの対象、除外規則、ハッシュ管理、目次生成そのものの詳細仕様や実装だけを調べたいとき。
- cmoc の正本仕様断片、ユーザー向けワークフロー、開発ルール、テスト規約を確認したいだけで、apply.py の実装制御フローが不要なとき。
- apply の自動テストを探しているとき、またはテスト fixture や Fake Codex CLI の挙動だけを確認したいとき。

## hash

- 84e07dc52a7bb38615cf0f388679ac5f2dcae301995558b4792c81bd2cfce494

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
