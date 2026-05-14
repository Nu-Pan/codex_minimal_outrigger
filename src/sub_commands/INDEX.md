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
- cmoc ブランチ上で oracle と実装のズレを調査し、Codex CLI に修正を依頼し、変更を commit し、apply レポートを書く一連の制御フローを扱う。
- ズレ調査用 JSON schema の検証、ズレ追従プロンプト、commit message 生成プロンプト、編集禁止パス検査、未完了時の終了コードを定義する。

## Read this when

- `cmoc apply` の実行順序、進捗表示、最大ループ回数、完了・未完了判定、終了コードを確認したいとき。
- oracle ファイルごとのズレ調査、Codex CLI 呼び出し、Structured Output の期待形式や検証ロジックを調べたいとき。
- ズレ一覧をもとに実装変更を Codex CLI へ依頼するプロンプト内容や、Codex 作業後の禁止パス検査を確認したいとき。
- `oracles` の自動 commit、`INDEX.md` メンテナンス、実装変更 commit、`.cmoc/reports/apply` へのレポート作成の流れを調べたいとき。
- `cmoc apply` が `oracles/`、`.agents/`、`memo` をどのように扱うかを実装上確認したいとき。

## Do not read this when

- `cmoc apply` ではないサブコマンドの CLI 引数定義やエントリーポイントだけを調べたいとき。
- Codex CLI 実行の低レベル実装、git 操作ラッパー、INDEX.md メンテナンス処理、タイムスタンプ生成の内部詳細だけを調べたいとき。
- oracle 正本仕様そのものや、`cmoc apply` のユーザー向け仕様だけを確認したいとき。
- ズレ調査結果の個別内容や、特定の対象リポジトリで発生した実装差分の詳細を調べたいとき。
- テストコードの構造や Fake Codex CLI を使った検証方法だけを調べたいとき。

## hash

- c330ea2c619c508107a6322916f11c862520ee826c7089cf88ed232d381e4e6e

# `branch.py`

## Summary

- `cmoc branch` subcommand implementation.
- Creates a new unique cmoc work branch from the current HEAD.
- Records the source base commit under the branch-specific cmoc metadata path.
- Ensures `.cmoc` is ignored in the target repository before writing branch metadata.
- Retries branch creation with fresh timestamps when generated branch names collide.

## Read this when

- Investigating or changing the behavior of the `cmoc branch` command.
- Need to understand how cmoc work branches are named and created.
- Need to understand when and where the base commit for a cmoc branch is recorded.
- Debugging failures around `git checkout -b`, timestamp branch name collisions, or branch creation retries.
- Changing interactions between branch creation and `.cmoc` ignore handling.

## Do not read this when

- Working on unrelated cmoc subcommands other than `branch`.
- Looking for CLI argument parsing or command dispatch wiring.
- Investigating generic git helper implementations such as `run_git`, `head_commit`, or metadata path construction.
- Looking for timestamp formatting logic.
- Working on cmoc oracle specifications or documentation outside the branch command implementation.

## hash

- 1fe2b7b1e8a34400be06674015525a21fe444a06e7117317ff243e41f92baa49

# `eval_oracles.py`

## Summary

- `cmoc eval-oracles` サブコマンドの本体処理を実装するファイル。
- `.cmoc` の ignore 確認、`INDEX.md` メンテナンス、評価対象 oracle ファイルの選択、Codex CLI による評価実行、評価レポートの保存までの一連の処理を扱う。
- cmoc ブランチでは既定で変更された oracle ファイルのみを評価し、`full` 指定時または cmoc ブランチ以外では全 oracle ファイルを評価する。

## Read this when

- `cmoc eval-oracles` の実行フロー、進捗表示、評価対象ファイル選択、partial/full モードの分岐を確認したいとき。
- oracle 評価時に Codex CLI へ渡すプロンプト内容、read-only 実行、JSON 出力を期待しない設定を確認したいとき。
- 評価結果レポートの保存先、ファイル名、front matter、oracle ごとの出力記録形式を確認・変更したいとき。
- `commons.repo`、`commons.indexing`、`commons.codex`、`commons.timestamps` と `eval-oracles` サブコマンド本体の接続部分を調べたいとき。

## Do not read this when

- `cmoc eval-oracles` の CLI 引数定義やサブコマンド登録だけを調べたいとき。
- oracle ファイル列挙、ブランチ判定、base commit 読み取り、変更 oracle 検出などの共通 repo 処理そのものの詳細を調べたいとき。
- `INDEX.md` メンテナンス処理の実装詳細だけを調べたいとき。
- Codex CLI 実行ラッパーの低レベルなコマンド組み立て、サンドボックス設定、エラーハンドリングの詳細だけを調べたいとき。
- 評価対象である oracle 仕様断片そのものの内容やルーティング情報を調べたいとき。

## hash

- 8d4e2184ab55dc533392787fc1d76f10c04efa45d0d055457265ba45a5f9b16f

# `init.py`

## Summary

- `cmoc init` の本体処理を定義する。
- `cmoc_init_impl(repo_root)` は `.cmoc` を git 追跡対象外にするため `ensure_cmoc_ignored(repo_root)` を呼ぶ。
- 初期化で `.gitignore` に変更があった場合は `commit_if_changed(repo_root, [".gitignore"], "Initialize cmoc")` でコミットする。
- 処理ステップと、コミット有無に応じた結果メッセージを標準出力へ表示する。

## Read this when

- `cmoc init` の実行時処理を調べるとき。
- 初期化時に `.cmoc` を `.gitignore` へ追加する流れを確認するとき。
- 初期化変更を `Initialize cmoc` というメッセージでコミットする挙動を変更・検証するとき。
- `ensure_cmoc_ignored` または `commit_if_changed` が `cmoc init` からどう呼ばれるかを確認するとき。

## Do not read this when

- `cmoc init` の CLI 引数定義やサブコマンド登録だけを調べるとき。
- git ignore やコミット処理の低レベル実装を調べるとき。
- `cmoc` の他サブコマンドの挙動を調べるとき。
- 正本仕様や設計ルールだけを確認するとき。

## hash

- ce04df3a0d99b9ee0e2921f47ce625c0505af8f39b84c6d3593d81107a1d17a1

# `merge.py`

## Summary

- `cmoc merge` サブコマンドの本体処理を実装するファイル。
- 対象リポジトリの作業ツリー検証、`.cmoc` ignore 確認、merge 元 cmoc ブランチの自動解決、`git merge --no-ff` 実行、merge 後のブランチ削除を扱う。
- merge conflict 発生時に Codex CLI へ conflict marker 解消を依頼し、残存 marker や unmerged path を検査して merge commit を作成する処理を含む。

## Read this when

- `cmoc merge` の実行手順、進捗表示、git merge 実行、merge 元ブランチ解決、merge 後のブランチ削除の実装を確認したいとき。
- 未マージの cmoc ブランチ候補を `git branch --no-merged` から自動判定する挙動や、候補が一意でない場合のエラーを調べたいとき。
- merge conflict 発生時に Codex CLI をどの prompt・権限で呼び出し、どのように conflict marker、unmerged path、`git add`、`git commit --no-edit` を処理するか確認したいとき。
- `assert_no_uncommitted_changes`、`ensure_cmoc_ignored`、`run_git`、`run_codex_exec` と `cmoc merge` の連携箇所を追いたいとき。

## Do not read this when

- `cmoc merge` 以外のサブコマンド、CLI 引数定義、エントリーポイント、共通エラー表示だけを調べたいとき。
- git コマンド実行ラッパー、リポジトリ検証、cmoc ブランチ判定、Codex CLI 呼び出しの共通実装そのものを調べたいとき。
- `cmoc merge` の正本仕様、ユーザー向けワークフロー、コンソール出力仕様を実装コードではなく仕様断片から確認したいとき。
- merge conflict の一般的な解消方法や Git の使い方だけを知りたいとき。

## hash

- e828cc7bef6bd07bb49e7f4095d6edc0a6c5f749abe2d69c63b6f0743b6445a3
