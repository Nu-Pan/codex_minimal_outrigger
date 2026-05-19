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

- `cmoc apply` サブコマンドの本体処理を実装するファイルです。
- cmoc 作業ブランチ上でのみ実行できることを検証し、oracle 外の未コミット差分を拒否しつつ、`.gitignore`、`.cmoc`、`oracles` の保証差分を必要に応じて commit します。
- `INDEX.md` のメンテナンス、oracle ごとの不整合調査、Codex CLI による実装修正依頼、禁止パス変更検査、変更 commit を反復実行する `cmoc apply` の主要フローを定義します。
- 不整合調査用の Structured Output schema、JSON payload 検証、調査プロンプト、実装修正プロンプト、commit message 生成プロンプトをまとめています。
- 実行結果として `.cmoc/reports/apply/<timestamp>.md` に作業レポートを保存し、完了時は `0`、指定回数内に不整合が残った場合は `2` を返す処理を扱います。

## Read this when

- `cmoc apply` の実行順序、進捗表示、終了コード、レポート出力の流れを確認したいとき。
- apply 実行前のブランチ検証、未コミット差分検査、`.cmoc` ignore 保証、oracle 差分 commit の扱いを調べたいとき。
- oracle と実装の不整合を Codex CLI に調査させる prompt、Structured Output schema、JSON 検証ロジックを確認したいとき。
- 検出された不整合を Codex CLI に実装修正させ、禁止パスの変更を検査して commit する反復処理を実装・修正したいとき。
- `cmoc apply --repeat` 相当の繰り返し回数、負数エラー、未完了時の `APPLY_INCOMPLETE_EXIT_CODE` の扱いを確認したいとき。
- apply レポートの保存先、ファイル名 timestamp、レポート生成用 prompt、完了・未完了情報の渡し方を調べたいとき。

## Do not read this when

- `cmoc init`、`cmoc branch`、`cmoc merge`、`cmoc eval-oracles` など apply 以外のサブコマンド本体だけを調べたいとき。
- Codex CLI 実行ラッパー、git 操作、repo 状態検査、INDEX メンテナンス、timestamp 生成などの共通関数そのものの実装を詳しく調べたいとき。
- cmoc のユーザー向け全体ワークフローや正本仕様を確認したいだけで、apply の Python 実装詳細が不要なとき。
- テストコードの配置、Fake Codex CLI、pytest の書き方など、テスト実装規約だけを調べたいとき。
- README、AGENTS、oracles、memo の編集可否など、リポジトリ運用ルールだけを確認したいとき。

## hash

- 8201e32dabf26119e44e5d8d954a29974a1d66cb87f8446ad97128fc6c68edf3

# `branch.py`

## Summary

- `cmoc branch` サブコマンドの本体処理を実装するファイルです。
- 作業用ブランチ作成前の HEAD commit を base commit として取得し、`cmoc_<timestamp>` 形式の一意なブランチを作成します。
- ブランチ作成後に `.cmoc` が git 追跡対象外であることを保証し、ブランチ名に対応する `.cmoc/branch` 配下のファイルへ base commit を記録します。
- ブランチ名衝突時は timestamp を作り直しながら短い sleep を挟んで最大 10 回 `git checkout -b` をリトライします。
- 進捗表示と処理時間計測には `StepTimer` を使い、`branch (1/3)` から `branch (3/3)` までの段階的な stdout 出力を行います。

## Read this when

- `cmoc branch` の実行本体、進捗表示、処理順序を確認したいとき。
- 作業用ブランチ名 `cmoc_<timestamp>` の生成や、衝突時のリトライ挙動を実装・修正したいとき。
- ブランチ作成元の HEAD commit をどのタイミングで取得し、どこへ記録するか調べたいとき。
- `.cmoc` を git 追跡対象外にする処理が `cmoc branch` 内でいつ呼ばれるか確認したいとき。
- `branch_base_commit_path`、`head_commit`、`run_git`、`ensure_cmoc_ignored` などの共通 repo ヘルパーとの接続箇所を追いたいとき。
- `run_command(cmoc_branch_impl)` による CLI 実行時の呼び出し分岐を確認したいとき。

## Do not read this when

- `cmoc branch` の正本仕様やユーザー向け仕様だけを確認したいとき。
- `cmoc init`、`cmoc apply`、`cmoc merge`、`cmoc eval-oracles` など他サブコマンドの実装を調べたいとき。
- git コマンド実行ヘルパー、リポジトリ探索、`.cmoc` パス生成などの共通処理そのものの詳細を調べたいとき。
- timestamp のフォーマットや生成規則そのものを確認したいとき。
- テスト実装、Fake Codex CLI、pytest 規約など、テスト側のルールを調べたいとき。
- `INDEX.md` 自動生成や oracle 評価など、ルーティング文書関連の仕様を調べたいとき。

## hash

- a2a1dc8602bb135cd22e9049dc55722f354c25a0dcd84d247f87cbb3480c34cc

# `eval_oracles.py`

## Summary

- `cmoc eval-oracles` サブコマンドの本体処理を実装する Python モジュール。
- `.cmoc` の git ignore 保証、`INDEX.md` メンテナンス、評価対象 oracle の選択、Codex CLI による oracle 評価、Markdown レポート保存までの一連の処理を扱う。
- cmoc 作業ブランチかつ `--full` 未指定で oracle 削除がない場合は、ブランチ基点から変更された oracle だけを部分評価し、それ以外は全 oracle を全体評価する。
- oracle 評価用プロンプトでは、実装・テスト・設定ファイルを参照せず、oracles ツリーと `INDEX.md` のルーティング情報に基づいて致命的な仕様問題を報告するよう Codex CLI に指示する。
- 評価結果は `.cmoc/reports/eval-oracles/<timestamp>.md` に、評価モード、ブランチ名、HEAD コミット、oracle 件数を frontmatter として含む Markdown レポートとして保存する。

## Read this when

- `cmoc eval-oracles` の実行ステップ、stdout 進捗表示、処理順序を確認したいとき。
- oracle 評価が部分評価になる条件と、全体評価へフォールバックする条件を調べたいとき。
- 評価対象 oracle ファイルの列挙、変更 oracle の抽出、削除 oracle 検出、ブランチ基点コミットの利用箇所を確認したいとき。
- `cmoc eval-oracles` が Codex CLI に渡す評価プロンプトの内容や、読み取り専用実行の扱いを確認したいとき。
- 評価レポートの保存先、ファイル名、frontmatter、oracle ごとの出力構造を調べたいとき。
- `commons.codex`、`commons.indexing`、`commons.repo`、`commons.timing`、`commons.timestamps` と `eval-oracles` 本体処理のつながりを把握したいとき。

## Do not read this when

- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc merge` など、`eval-oracles` 以外のサブコマンド本体だけを調べたいとき。
- Codex CLI 呼び出しの低レベル実装、コマンド実行共通処理、repo 探索や git 操作の詳細実装だけを確認したいとき。
- `INDEX.md` 自動メンテナンス処理そのものの詳細や Structured Output 目次生成ロジックだけを調べたいとき。
- oracle 正本仕様の内容や、個別 oracle ファイルの仕様レビュー観点そのものを調べたいとき。
- 評価レポートのタイムスタンプ生成ルールや `.cmoc` ignore 保証の内部実装だけを確認したいとき。
- 自動テストの構成、Fake Codex CLI、テストデータの作り方だけを調べたいとき。

## hash

- 9c24cfba3b471b2ec3d42ad3a9e2f08e07d4749d3b6637ec5f9aa1e3403e7a3b

# `init.py`

## Summary

- `cmoc init` サブコマンドの本体処理を実装するファイル。
- `repo_root` が未指定の場合は `run_command` に処理を委譲し、指定された場合は初期化処理を実行する。
- `ensure_cmoc_ignored` により `<repo-root>/.cmoc` が git 追跡対象外になる状態を保証する。
- `.gitignore` と `.cmoc` に関する初期化差分だけを対象に、`commit_if_changed` で `Initialize cmoc` コミットを作成する。
- `StepTimer` と stdout により、init の 2 ステップ進捗と完了時の時間レポートを出力する。

## Read this when

- `cmoc init` の実行本体がどの順序で処理されるか確認したいとき。
- `.cmoc` を git 追跡対象外にする処理がどこから呼ばれるか調べたいとき。
- init 実行時に `.gitignore` や `.cmoc` の変更がどのようにコミットされるか確認したいとき。
- `cmoc init` の stdout 進捗表示や `StepTimer` による時間計測を修正したいとき。
- `run_command` 経由のサブコマンド起動と、`repo_root` 指定後の実処理の分岐を確認したいとき。

## Do not read this when

- `cmoc init` の CLI 引数定義やサブコマンド登録箇所だけを探しているとき。
- `.cmoc` ignore ルールの具体的な実装や tracked file 解除の詳細だけを調べたいとき。
- 変更検出や git commit 実行の共通処理そのものを修正したいとき。
- `cmoc branch`、`cmoc apply`、`cmoc merge` など init 以外のサブコマンド処理を調べたいとき。
- cmoc の正本仕様やテストケースを確認したいだけで、init 実装コードへの入口情報が不要なとき。

## hash

- e17c7180d21c373e32c3a2292641ec0dad217fd96c2f35958b4338f54a479ca6

# `merge.py`

## Summary

- `cmoc merge` サブコマンドの本体処理を実装するファイル。
- 対象リポジトリの検出後、作業ツリーの未コミット変更確認、`.cmoc` の ignore 確認、マージ元 cmoc ブランチの解決、`git merge --no-ff` 実行、必要時の conflict 解消、マージ後のブランチ削除までを担う。
- 明示された cmoc ブランチがない場合は、未マージブランチ一覧から cmoc 命名規則に一致する候補を 1 件だけ自動選択する。
- 通常の git merge が失敗した場合、unmerged path を固定して Codex CLI に conflict marker 解消を依頼し、marker 残存確認、`git add`、`git commit --no-edit` を行う。
- Codex に conflict 解消を依頼するプロンプトでは、`oracles`、`.agents`、`memo` の編集・アクセス禁止範囲や、`git add` / `git commit` 禁止を明示する。
- merge 開始後に例外が発生した場合は、cmoc が merge state をロールバックしないことと手動解決が必要なことを stderr に表示する。

## Read this when

- `cmoc merge` の実行フロー、進捗表示、StepTimer による計測対象を確認したいとき。
- マージ元 cmoc ブランチの自動解決条件や、候補が 0 件または複数件だった場合のエラー内容を調べたいとき。
- `git merge --no-ff` 失敗時に、Codex CLI に conflict marker 解消を依頼する条件や、その後の検証・commit 手順を確認したいとき。
- conflict marker 残存検査、unmerged path 検出、merge commit 作成、マージ元ブランチ削除の実装を変更・テストしたいとき。
- merge conflict 解消用 Codex プロンプトに含める禁止事項、対象ファイル一覧、INDEX メンテナンス例外指定を確認したいとき。
- merge 開始後の例外時に表示される手動解決案内メッセージや、cmoc がロールバックしない方針を確認したいとき。

## Do not read this when

- `cmoc merge` の CLI 引数定義や argparse への登録だけを確認したいとき。
- Codex CLI 呼び出しの共通実装、サンドボックス指定、Structured Output 処理など `run_codex_exec` 側の詳細を調べたいとき。
- `run_git`、`assert_no_uncommitted_changes`、`ensure_cmoc_ignored`、`is_cmoc_branch` など git・リポジトリ共通処理の内部実装だけを確認したいとき。
- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles` など merge 以外のサブコマンド挙動を調べたいとき。
- `oracles` 配下の正本仕様そのものや、merge 仕様の設計意図を確認したいだけで、Python 実装の制御フローが不要なとき。
- 対象リポジトリ側の個別 conflict 内容や、実際のマージ結果を調査したいとき。

## hash

- e679357fc26f4c6d06e0536d8082ddd0e167b8b486183d97502699e599be74bc
