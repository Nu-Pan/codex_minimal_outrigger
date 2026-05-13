# `commons`

## Summary

- Contains shared cmoc utility modules used across commands and workflows.
- Provides common error reporting, Codex CLI invocation and JSON parsing, repository and Git helpers, timestamp generation, and INDEX.md maintenance logic.
- The package-level INDEX.md routes to concrete modules such as codex.py, repo.py, errors.py, timestamps.py, indexing.py, and __init__.py.

## Read this when

- You need a package-level overview of common implementation helpers under src/commons.
- You are deciding which shared module to inspect for Codex execution, Git repository handling, structured error reports, timestamps, or generated INDEX.md maintenance.
- You are changing cross-cutting infrastructure that multiple cmoc commands rely on.
- You are documenting or updating routing metadata for the commons package.

## Do not read this when

- You need command-specific behavior, CLI argument parsing, or subcommand dispatch; inspect the relevant command or entrypoint modules instead.
- You need canonical product specifications; use the routed files under oracles rather than shared implementation helpers.
- You are looking for tests or fixtures; inspect tests instead.
- You only need one concrete utility implementation and already know the target module, such as repo.py for Git helpers or codex.py for Codex CLI execution.

## hash

- 958c0f4bf343c2160caadddcb71963e536a2fc1a1993410f57820d59e10eecf9

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
- `cmoc init` は `.cmoc` の ignore 設定と初期化コミット、`cmoc branch` は cmoc 作業ブランチ作成と base commit 記録を担当する。
- `cmoc apply` は oracle と実装の差分調査、Codex CLI による追従実装、禁止パス検査、コミット、apply レポート作成を担当する。
- `cmoc eval-oracles` は oracle `INDEX.md` 保守、評価対象 oracle の選択、Codex CLI による read-only 評価、評価レポート作成を担当する。
- `cmoc merge` は cmoc ブランチの no-fast-forward merge、未マージ cmoc ブランチの自動解決、Codex CLI による conflict marker 解消、merge commit、作業ブランチ削除を担当する。

## Read this when

- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` の実行時処理を理解または変更するとき。
- サブコマンドが `commons.repo`、`commons.codex`、`commons.indexing`、`commons.timestamps` などの共通処理をどの順序で呼ぶか確認するとき。
- cmoc ブランチ作成、base commit 記録、oracle 変更のコミット、oracle 評価、実装追従ループ、merge conflict 解消、`.cmoc/reports` 出力の挙動を調査するとき。
- Codex CLI へ渡す prompt、read-only/write-enabled の使い分け、JSON 期待有無、禁止パス指定を変更または検証するとき。
- サブコマンド実装に起因するエラー、進捗表示、終了コード、git 操作、レポート生成の不具合をデバッグするとき。

## Do not read this when

- CLI 引数定義、サブコマンド登録、コマンド dispatch のみを調べたいとき。
- git 実行、ブランチ判定、変更ファイル列挙、`.cmoc` ignore、oracle ファイル列挙、timestamp 生成、Codex CLI ラッパーなどの低レベル共通処理だけを調べたいとき。
- cmoc の正本仕様断片そのものを確認したいとき。
- テストコードの期待値や fixture のみを調べたいとき。
- README、AGENTS、oracles、memo など、閲覧または編集制限のある文書・仕様・メモを扱う作業をしているとき。

## hash

- 36df25dccb02d1869b01ec09775ca7ef4df4eb742a1be3c6e8a0c3d4651b791b
