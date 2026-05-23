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

- `cmoc apply` の本体処理を実装するファイルで、作業ブランチ検証、`.cmoc` の ignore 保証、oracle 差分の自動コミット、`INDEX.md` メンテナンスをまとめて扱います。
- oracle ファイルと実装ファイルを対象に、不整合調査・不整合リスト整理・不整合追従修正の反復ループを回す処理を定義します。
- 部分適用と全体適用の切り替え、変更済みファイルへの対象絞り込み、削除検出時の全体適用への切り替えを担当します。
- 不整合調査用と修正用に渡す Codex CLI プロンプト、Structured Output schema、JSON 検証ロジックを定義します。
- 作業結果レポートの生成、検証、保存先決定、未収束時の注意文言、終了コードの判定までを含みます。

## Read this when

- `cmoc apply` の実行順序、前提条件、ループ回数、終了条件を確認したいとき。
- oracle ファイル起点・実装ファイル起点で、Codex CLI に何を調査させるかを確認したいとき。
- 不整合リストの Structured Output 形式や、空配列を不整合なしとみなす判定を確認したいとき。
- 変更済み oracle・実装ファイルだけに絞る部分適用の条件を確認したいとき。
- 修正後の禁止パス検査、commit message 生成、作業レポート保存の流れを確認したいとき。

## Do not read this when

- `cmoc init`、`cmoc branch`、`cmoc eval-oracles`、`cmoc merge` など他サブコマンドの実装を調べたいとき。
- Codex CLI の低レベル実装、JSON パース、共通コマンド実行、git ラッパーなどの共通処理だけを調べたいとき。
- `INDEX.md` 自動メンテナンス機構そのものの対象範囲や生成規則を詳しく調べたいとき。
- oracle 正本仕様の内容そのものや、個別のアプリケーション仕様を確認したいとき。
- 自動テスト、Fake Codex CLI、pytest の構成やテストデータを調べたいとき。

## hash

- b027206cc87a3b30d9d0beed159cfd93532c7d5d6c2a54bef9e14a40a0808d32

# `branch.py`

## Summary

- `cmoc branch` の本体処理を実装するファイルです。
- 共通 runner 経由で `<repo-root>` を解決し、作業用ブランチ `cmoc_<time-stamp>` を作成して、作成元 commit を `.cmoc/branch/<branch>.txt` に記録します。
- ブランチ名の衝突時は最大 10 回までリトライし、`StepTimer` で 3 段階の進捗表示と経過時間レポートを行います。

## Read this when

- `cmoc branch` の実装フローや処理順を確認したいとき。
- 作業用ブランチ名の生成規則、衝突時のリトライ挙動を確認したいとき。
- base commit の取得タイミング、`.cmoc` の追跡除外保証、stdout の進捗表示や計測を確認したいとき。

## Do not read this when

- `cmoc init`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` など他サブコマンドの実装を調べたいとき。
- repo root 探索、git 実行、`timestamp` 生成、`StepTimer` など共通ユーティリティそのものを調べたいとき。
- `cmoc branch` の正本仕様や、`src/sub_commands` 以外のルーティング目次だけを確認したいとき。

## hash

- a2f0aaa3562304fd93b3e17fb51f579f2c1028009ef6ad0d22e262dfda477021

# `eval_oracles.py`

## Summary

- `cmoc eval-oracles` の本体処理を実装するモジュールです。
- `.cmoc` の ignore 保証、`INDEX.md` メンテナンス、評価対象 oracle の選定、Codex CLI による評価、Markdown レポート保存を扱います。
- `--full` と cmoc ブランチ判定、削除 oracle の有無に応じた部分評価・全体評価の切り替えを担当します。
- oracle 評価用 prompt の組み立てと、評価出力に必須見出しが含まれるかの検証も含みます。

## Read this when

- `cmoc eval-oracles` の実行フロー、進捗表示、ステップ順序を確認したいとき。
- 評価前に `.cmoc` の git 追跡除外保証と `INDEX.md` メンテナンスがどの順で行われるか調べたいとき。
- `cmoc eval-oracles --full` と通常実行で、評価対象 oracle ファイルの選定条件がどう変わるか確認したいとき。
- cmoc ブランチ上での部分評価、ベースコミット、変更 oracle、削除 oracle の扱いを確認したいとき。
- Codex CLI に渡す oracle 評価 prompt の内容、参照許可範囲、ファイル編集禁止指示、必須レポート見出しを確認したいとき。
- 評価結果の検証条件や、`.cmoc/reports/eval-oracles` に保存されるレポートの frontmatter、ファイル名、本文構成を確認したいとき。

## Do not read this when

- `cmoc eval-oracles` 以外のサブコマンド本体処理を調べたいとき。
- Codex CLI 呼び出しの低レベル実装、共通 runner、repo 操作、timestamp 生成などの共通処理だけを調べたいとき。
- `INDEX.md` 自動メンテナンスの具体的な生成・更新ロジックを調べたいとき。
- oracle ファイル列挙、変更検出、cmoc ブランチ判定、`.cmoc` ignore 保証の個別実装だけを確認したいとき。
- 評価レポートの正本仕様や、oracle 評価で何を致命的問題とみなすかの仕様断片だけを確認したいとき。
- CLI 引数の定義、サブコマンド登録、エントリーポイント側の実装を調べたいとき。

## hash

- 088f89e4fef317a82a12318c385859b044695b90dc872170aedb20696e03408c

# `init.py`

## Summary

- `cmoc init` サブコマンドの本体処理を定義する実装ファイル。
- 直接呼び出し時は共通 runner に処理を委譲し、`repo_root` の解決と共通エラー整形を受ける。
- `.cmoc` が git 追跡対象外になるよう、`.gitignore` ルールの追加と既存 tracked file の追跡解除を保証する。
- 初期化で発生した変更のみを必要に応じてコミットし、`StepTimer` で 2 段階の進捗表示と完了時の経過時間報告を行う。

## Read this when

- `cmoc init` の実装本体と処理の流れを確認したいとき。
- `.cmoc` を git 追跡対象外にする処理の呼び出し順序を確認したいとき。
- `cmoc init` がどの条件で `.gitignore` や git index の変更をコミットするか調べたいとき。
- `cmoc init` の stdout 進捗表示、ステップ名、完了時の時間レポートを確認したいとき。
- テストから `cmoc_init_impl` を直接呼び出す際の `repo_root` 引数の扱いを確認したいとき。

## Do not read this when

- CLI エントリーポイントで `init` サブコマンドがどう登録されるかだけを調べたいとき。
- `.cmoc` ignore ルールの具体的な `.gitignore` 編集や git 操作の詳細実装を調べたいとき。
- 共通 runner の `repo_root` 解決、例外処理、終了ステータス整形の詳細を調べたいとき。
- タイマーや経過時間表示の内部実装だけを調べたいとき。
- `cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` など他サブコマンドの挙動を調べたいとき。

## hash

- 766eb4ef5567a176766be2bb55dbc8f955c55af92c1ddc3f64043c1be4bda4ee

# `merge.py`

## Summary

- `src/sub_commands/merge.py` は `cmoc merge` の本体処理を実装するファイルです。
- 未コミット差分の検証、`.cmoc` の追跡除外保証、マージ元 cmoc ブランチの解決、`git merge` 実行、コンフリクト解消支援、作業ブランチ削除までを扱います。
- `cmoc_merge_impl` を中心に、`_resolve_source_branch`、`_resolve_conflicts`、`_delete_branch_if_safe`、`_files_with_conflict_markers`、`_unmerged_paths`、`_conflict_prompt` を含みます。
- `StepTimer` による 4 段階の進捗表示と時間計測もこのファイルの責務です。

## Read this when

- `cmoc merge` の実装、修正、テストを行いたいとき。
- マージ前の前提条件、マージ元ブランチの自動解決、コンフリクト時の Codex CLI 依頼内容を確認したいとき。
- merge 後に作業ブランチを削除してよい条件や、削除失敗時の warning 挙動を確認したいとき。
- conflict marker 検査や unmerged path 検査の実装を確認したいとき。

## Do not read this when

- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles` など他サブコマンドの本体処理を調べたいとき。
- CLI エントリーポイントでのサブコマンド登録や引数定義だけを調べたいとき。
- `commons` 配下の共通処理、git ラッパー、Codex CLI ラッパー、時間計測などの共通ユーティリティを調べたいとき。
- `oracles` 配下の正本仕様や、`tests` 配下の自動テストの全体構成を調べたいとき。

## hash

- 4c177d59ea4deadf724a7189e83fc7d9f07329097d251c7d842a2a731ba08066
