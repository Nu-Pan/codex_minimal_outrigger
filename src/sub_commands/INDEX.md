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
- cmoc 作業ブランチの検証、`.cmoc` ignore 保証、oracle 差分のコミット、`INDEX.md` メンテナンス、不整合調査、Codex CLI への実装追従依頼、変更コミット、適用レポート作成までの一連の apply 実行フローを扱う。
- oracle と実装の不整合を表す Structured Output schema と、その JSON 検証ロジックを定義する。
- 部分適用と全体適用の判定、調査対象 oracle・実装ファイルの選定、個別調査結果の整理、禁止パス変更検査を担当する。
- 不整合調査、実装追従、調査結果整理、commit message 生成、apply レポート生成のために Codex CLI へ渡す prompt を組み立てる。
- apply レポートの保存先、必須見出し、未収束時の文言、不整合件数推移、ブランチ変更内容要約の検証を行う。

## Read this when

- `cmoc apply` の実行順序や各ステップの stdout 表示を確認したいとき。
- apply が cmoc ブランチ上でのみ実行される条件や、base commit の扱いを調べたいとき。
- apply 実行前に許容される未コミット差分、oracle 差分の自動コミット、`.cmoc` ignore 保証の挙動を確認したいとき。
- `cmoc apply --repeat` や `--full` に関係する反復回数、未収束時の終了コード、部分適用と全体適用の切り替え条件を調べたいとき。
- oracle ファイル起点・実装ファイル起点の不整合調査で Codex CLI に渡す prompt や Structured Output schema を確認したいとき。
- 不整合リストの重複整理、実装追従依頼、変更後の禁止パス検査、commit message 生成の流れを追いたいとき。
- apply レポートの生成 prompt、保存場所、検証条件、未収束時に必要な記載を確認したいとき。
- `run_codex_exec`、`maintain_indexes`、`changed_paths`、`list_oracle_files`、`list_implementation_files` などの共通処理が apply からどう呼ばれるかを調べたいとき。

## Do not read this when

- `cmoc apply` 以外のサブコマンド、例えば init、branch、eval-oracles、merge の主要処理を調べたいとき。
- Codex CLI 呼び出しの低レベル実装、JSON パース、共通 command runner、git wrapper、repo 探索、タイマー、timestamp の詳細だけを確認したいとき。
- `INDEX.md` 自動メンテナンス機構そのものの対象ディレクトリ、除外規則、生成フォーマットを詳しく調べたいとき。
- oracle 正本仕様の内容や、特定仕様ファイルが要求するアプリケーション挙動そのものを確認したいとき。
- cmoc の CLI 引数定義や argparse へのサブコマンド登録だけを調べたいとき。
- テストコード、Fake Codex CLI、pytest fixture、テストデータの構造を調べたいとき。
- README、AGENTS、oracles、memo などの編集可否やリポジトリ運用ルールだけを確認したいとき。

## hash

- 7e9ee51daf0e9a379c91dbfe31bb6ba5ee6d487008aa2f0ff7ebec7d58032aa0

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
