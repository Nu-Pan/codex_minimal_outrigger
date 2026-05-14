# `commons`

## Summary

- cmoc の複数サブコマンドから共有される Python 共通実装を集めたパッケージ。
- Codex CLI 呼び出し、Structured Output JSON の検証、Codex 実行ログ保存、共通エラー整形、INDEX.md 自動メンテナンス、git リポジトリ操作、oracle ファイル列挙、タイムスタンプ生成を扱う。
- CLI 引数定義やサブコマンド固有の業務ロジックではなく、src/sub_commands などから再利用される横断的な補助処理の入口となる。

## Read this when

- cmoc のサブコマンド間で共有する処理をどの commons モジュールに置くか、または既存の共通関数を再利用できるか判断したいとき。
- Codex CLI を `codex exec` で呼び出す処理、read-only/workspace-write sandbox、リトライ、JSON パース、Structured Output 検証、`.cmoc/logs/codex_exec` のログ出力を調べるとき。
- cmoc 全体で使う `CmocError`、復旧アクション付きエラー、stdout 向けエラーレポート形式を確認・修正するとき。
- `INDEX.md` の自動生成・更新、既存エントリ再利用、hash 比較、除外対象、gitignore 判定、Codex prompt 生成、自動コミット処理を扱うとき。
- git リポジトリルート検出、cwd 移動、git コマンド実行、現在ブランチや HEAD commit、未コミット差分検査、`.cmoc` の gitignore 追記、指定パス commit を扱うとき。
- `oracles` 配下の仕様ファイル列挙、変更済み oracle ファイル抽出、cmoc ブランチ作成元 commit ファイルのパス解決・読み取りを調べるとき。
- cmoc 仕様の `<time-stamp>` 形式でファイル名、ブランチ名、ログ名、成果物名を生成する処理を確認したいとき。

## Do not read this when

- CLI エントリーポイント、typer 定義、引数解釈、サブコマンド dispatch だけを調べたいとき。
- `init`、`branch`、`apply`、`merge`、`eval-oracles` など、特定サブコマンド固有のワークフロー実装やプロンプト本文を調べたいとき。
- cmoc のユーザー向け仕様、正本仕様断片、出力仕様、ワークフロー仕様を確認したいだけのときは、まず `oracles` 配下の該当ルートを読むべきとき。
- テストコード、pytest  fixtures、Fake Codex CLI、テストデータ配置だけを調べたいとき。
- README、AGENTS、oracles、memo などのリポジトリ運用ルールや編集可否だけを確認したいとき。
- 共通処理ではない画面表示文言、サブコマンド固有の入力検証、ドメイン固有のエラー条件だけを調べたいとき。
- Python 標準ライブラリ、git、pathlib、subprocess、JSON の一般的な使い方だけを確認したいとき。

## hash

- 977b735b8d1ea719a520551894d9307115297e8e00a2720aaac9003502958114

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
- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` の実行時処理をファイルごとに分けて扱う。
- `init.py` は `.cmoc` の ignore 設定と初期化コミット、`branch.py` は cmoc 作業ブランチ作成と base commit 記録を実装する。
- `apply.py` は oracle と実装のズレ調査、Codex CLI による追従実装、禁止パス検査、コミット、apply レポート作成を実装する。
- `eval_oracles.py` は oracle `INDEX.md` 保守、評価対象 oracle の選択、Codex CLI による read-only 評価、評価レポート作成を実装する。
- `merge.py` は cmoc ブランチの no-fast-forward merge、未マージ cmoc ブランチの自動解決、Codex CLI による conflict 解消、merge commit、作業ブランチ削除を実装する。

## Read this when

- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` の実行時処理を理解または変更するとき。
- サブコマンドが `commons.repo`、`commons.codex`、`commons.indexing`、`commons.timestamps` などの共通処理をどの順序で呼ぶか確認するとき。
- cmoc ブランチ作成、base commit 記録、oracle 変更のコミット、oracle 評価、実装追従ループ、merge conflict 解消、`.cmoc/reports` 出力の挙動を調査するとき。
- Codex CLI へ渡す prompt、read-only と workspace-write の使い分け、JSON 期待有無、禁止パス指定を変更または検証するとき。
- サブコマンド実装に起因するエラー、進捗表示、終了コード、git 操作、レポート生成の不具合をデバッグするとき。
- このディレクトリ内のどのサブコマンド実装ファイルを読むべきか判断したいとき。

## Do not read this when

- CLI 引数定義、サブコマンド登録、コマンド dispatch のみを調べたいとき。
- git 実行、ブランチ判定、変更ファイル列挙、`.cmoc` ignore、oracle ファイル列挙、timestamp 生成、Codex CLI ラッパーなどの低レベル共通処理だけを調べたいとき。
- cmoc の正本仕様断片そのものを確認したいとき。
- テストコードの期待値や fixture のみを調べたいとき。
- README、AGENTS、oracles、memo など、閲覧または編集制限のある文書・仕様・メモを扱う作業をしているとき。
- 個別サブコマンドの対象ファイルが既に明確で、このディレクトリ全体のルーティング情報が不要なとき。

## hash

- 71d3cb5320f2e3e5f30acb930898d9ca6e2a29a8d672da6080d3f7ab78aece98
