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

- `cmoc apply` サブコマンドの本体処理を実装するファイル。
- cmoc 作業ブランチ上で oracle 変更を確定し、`INDEX.md` を保守したうえで、oracle と実装の不整合調査、Codex CLI による実装修正、禁止パス検査、コミット、作業レポート生成までを反復実行する。
- 不整合調査用 Structured Output schema、oracle 起点・実装ファイル起点の調査プロンプト、不整合整理プロンプト、実装追従プロンプト、commit message 生成プロンプトを定義する。
- 部分適用と全体適用の対象ファイル判定、削除検出時の全体適用への切り替え、未収束時の専用終了コード、apply レポートの必須項目検証を扱う。
- Codex CLI から返る不整合 JSON のキー構造と型を機械的に検証する補助関数を含む。

## Read this when

- `cmoc apply` の実行フロー、4 ステップの進捗表示、反復回数、終了コード、レポート生成の挙動を確認したいとき。
- oracle と実装の不整合をどの Structured Output schema で受け取り、どのように検証・整理しているか調べたいとき。
- `--full` や削除ファイルの有無によって、部分適用と全体適用の調査対象がどう切り替わるか確認したいとき。
- Codex CLI に渡す apply 用プロンプト、調査用プロンプト、commit message 生成プロンプト、レポート生成プロンプトの内容を修正または確認したいとき。
- `cmoc apply` 実行中に `.gitignore`、`.cmoc`、`oracles`、実装差分、`INDEX.md` がどのタイミングでコミットまたは検査されるか調べたいとき。
- Codex による実装修正後、`oracles/` や `.agents/` などの編集禁止領域に差分がないことをどこで確認しているか知りたいとき。
- apply レポートの保存先、収束・未収束の表現、不整合件数推移や全変更内容の検証条件を確認したいとき。

## Do not read this when

- `cmoc apply` 以外のサブコマンド、例えば `init`、`branch`、`eval-oracles`、`merge` の詳細挙動だけを調べたいとき。
- Codex CLI 呼び出しの低レベル実装、JSON パース、共通エラー処理、git 実行ラッパー、repo 探索などの共通処理そのものを調べたいとき。
- `INDEX.md` 自動保守の対象ディレクトリ、除外規則、ハッシュ計算、目次生成の詳細実装だけを確認したいとき。
- cmoc の開発ルール、Python コーディング規約、テスト規約、依存関係など、アプリケーション実行時仕様ではない内容を調べたいとき。
- 特定の oracle 仕様断片の正本内容を確認したいだけで、`cmoc apply` がそれを実装へ反映する流れに関心がないとき。

## hash

- 4774107aae6f21b2fbab81cd36c9638332afb945e60184c68d17b5ba21bc20dc

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
- `.cmoc` の ignore 保証、`INDEX.md` メンテナンス、評価対象 oracle の選定、Codex CLI による oracle 評価、Markdown レポート保存までの一連の処理を扱う。
- `--full` 指定、cmoc ブランチ判定、ベースコミット、削除 oracle の有無に基づいて、全体評価または部分評価を選択する。
- oracle 評価用プロンプトの組み立て、評価出力に必須見出しが含まれるかの検証、`.cmoc/reports/eval-oracles` 配下への timestamp 付きレポート生成を定義する。

## Read this when

- `cmoc eval-oracles` の実行フロー、進捗表示、ステップ順序を確認したいとき。
- oracle 評価前に `.cmoc` の git ignore 保証や `INDEX.md` メンテナンスがどの順番で行われるか調べたいとき。
- `cmoc eval-oracles --full` と通常実行で、評価対象 oracle ファイルの選定条件がどう変わるか確認したいとき。
- cmoc ブランチ上での部分評価、ベースコミット、変更 oracle、削除 oracle の扱いを調べたいとき。
- Codex CLI に渡す oracle 評価プロンプトの内容、読み取り制限、ファイル編集禁止指示、必須レポート見出しを確認したいとき。
- oracle 評価結果の検証条件や、必須見出し不足時のエラー処理を確認したいとき。
- `.cmoc/reports/eval-oracles` に保存される評価レポートの frontmatter、ファイル名、本文構成を確認したいとき。

## Do not read this when

- `cmoc eval-oracles` 以外のサブコマンド本体処理を調べたいとき。
- Codex CLI 呼び出しの低レベル実装、共通 runner、repo 操作、timestamp 生成などの共通処理そのものを詳しく調べたいとき。
- `INDEX.md` 自動メンテナンスの具体的な生成・更新ロジックを調べたいとき。
- oracle ファイル列挙、変更検出、cmoc ブランチ判定、`.cmoc` ignore 保証の個別実装だけを確認したいとき。
- 評価レポートの正本仕様や、oracle 評価で何を致命的問題とみなすかの仕様断片だけを確認したいとき。
- CLI 引数の定義、サブコマンド登録、エントリーポイント側の実装を調べたいとき。

## hash

- fdcf804262512c4eceb72e1539ca583118cfd0b7414ac1b2234ee11f3aa99b56

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
