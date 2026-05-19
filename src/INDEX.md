# `commons`

## Summary

- cmoc のサブコマンド横断で使う共通実装モジュール群を収めるディレクトリ。
- Codex CLI 実行、Structured Output JSON の検査、共通エラー表示、INDEX.md 自動メンテナンス、git リポジトリ操作、タイムスタンプ生成などの基盤処理を提供する。
- 個別コマンドの業務ロジックではなく、`src` 配下の複数機能から再利用される低レベルな実行支援・状態確認・ファイル生成処理をまとめている。

## Read this when

- cmoc の共通ユーティリティがどのモジュールに分かれているか把握したいとき。
- `codex exec` の呼び出し、ログ保存、Structured Output schema、JSON パース、リトライ、バリデーション失敗時の扱いを調べたいとき。
- cmoc 全体で使う `CmocError`、ユーザー向けエラーレポート、終了コード、復旧アクション表示を確認・変更したいとき。
- `INDEX.md` の自動生成・更新、対象ディレクトリ列挙、除外条件、内容ハッシュ、既存エントリ再利用、生成後コミット処理を追跡したいとき。
- git リポジトリルート検出、cwd 移動、git コマンド実行、ブランチ名判定、未コミット差分確認、oracle ファイル列挙、`.cmoc` の ignore 設定を扱うとき。
- cmoc 仕様の `<time-stamp>` 形式や、ログ・ブランチ名・作業成果物名に使う日時文字列の生成処理を確認したいとき。

## Do not read this when

- 個別サブコマンドの CLI 引数、ユーザーワークフロー、プロンプト内容、アプリケーション固有処理だけを調べたいとき。
- 正本仕様断片を確認したいとき。まず `oracles` 配下の該当 `INDEX.md` と仕様ファイルを読むべき。
- README、AGENTS、oracles、memo などの編集可否やリポジトリ運用ルールだけを確認したいとき。
- テストコード、Fake Codex CLI、テストデータ、pytest の具体的な配置だけを調べたいとき。
- 特定機能の呼び出し元やユーザー可視のコマンド出力を知りたいだけで、共通処理の実装詳細を読む必要がないとき。

## hash

- ecfe6ddc0743e92824db1965625a665732a5c8896902c9a304cef2d87f59fc86

# `main.py`

## Summary

- Defines the Typer CLI entry point for cmoc and registers the top-level subcommands: init, branch, eval-oracles, apply, and merge.
- Maps each CLI command to its implementation function under sub_commands, passing the discovered repository root and command-specific arguments such as eval-oracles --full and merge cmoc_branch.
- Centralizes command execution in _run_command, which enters the target repo root, handles integer exit codes, converts non-Typer exceptions into formatted stdout error reports, and exits with the exception's exit_code or 1.
- Supports direct execution of src/main.py by adjusting sys.path and invoking the Typer app.

## Read this when

- You need to add, remove, rename, or change a top-level cmoc CLI command.
- You need to understand how CLI arguments and options are wired to sub_commands implementations.
- You are debugging command startup, repository-root detection before command execution, or standardized CLI error reporting and exit codes.
- You need to inspect the direct execution path for src/main.py or the Typer app configuration.

## Do not read this when

- You only need the internal behavior of a specific subcommand implementation; read the corresponding file under src/sub_commands instead.
- You are looking for low-level repository discovery logic; read commons.repo instead.
- You are looking for error formatting details; read commons.errors instead.
- You are working on oracle specifications, development rules, tests, packaging metadata, or documentation unrelated to CLI command routing.

## hash

- 69b0ed2a7787a8888653e998cdd2f87b98257cba0e1b878f7ed09096675204bb

# `sub_commands`

## Summary

- cmoc の各サブコマンド本体を実装する Python パッケージ。
- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc merge`、`cmoc eval-oracles` の実行フロー、進捗表示、Codex CLI 呼び出し、git 操作、レポート生成など、サブコマンド固有の処理をファイルごとに分けて収める。
- CLI 引数定義やコマンド登録ではなく、登録後に呼び出されるサブコマンド実装関数と、その補助関数群を調べる入口。

## Read this when

- 個別サブコマンドの本体処理がどのファイルにあるか判断したいとき。
- `cmoc init` による `.cmoc` ignore 設定と初期化コミット処理を調べたいとき。
- `cmoc branch` による cmoc 作業ブランチ作成、base commit 記録、ブランチ名衝突時のリトライ処理を調べたいとき。
- `cmoc apply` による oracle 差分検証、`INDEX.md` メンテナンス、実装とのズレ調査、Codex CLI への修正依頼、禁止パス検査、コミット、apply レポート生成を調べたいとき。
- `cmoc merge` による作業ツリー検証、merge 元 cmoc ブランチ解決、`git merge --no-ff`、conflict 解消依頼、merge 後のブランチ削除を調べたいとき。
- `cmoc eval-oracles` による oracle 評価対象選択、partial/full モード、Codex CLI 評価、評価レポート生成を調べたいとき。
- サブコマンド本体が `commons.repo`、`commons.codex`、`commons.indexing`、`commons.timestamps` などの共通処理をどう呼び出しているか確認したいとき。

## Do not read this when

- CLI エントリーポイント、argparse 設定、サブコマンド登録、ユーザー入力の振り分けだけを調べたいとき。
- git 操作、Codex CLI 実行、JSON パース、timestamp 生成、`INDEX.md` メンテナンスなどの共通ユーティリティの低レベル実装だけを調べたいとき。
- cmoc の正本仕様断片や、サブコマンドの期待挙動を実装コードではなく oracle から確認したいとき。
- cmoc 自体の開発ルール、テスト方針、環境設定、編集禁止ファイルなどのリポジトリ運用ルールだけを確認したいとき。
- 自動テストの構造、Fake Codex CLI、pytest の具体的な検証内容だけを調べたいとき。
- 生成済みの bytecode や `__pycache__` の内容を調べたいとき。

## hash

- 993f6bea62d524d6fb59dc405307a558acbc81bacd490fe7ccaf703ff4190773
