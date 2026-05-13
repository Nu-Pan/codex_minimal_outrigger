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

- Implements the core `cmoc apply` workflow that reconciles oracle specifications with repository implementation by delegating investigation, implementation, commit-message generation, and report writing to Codex CLI.
- Validates that `cmoc apply` runs only on a cmoc branch, ensures only oracle files are initially uncommitted, updates `.gitignore` state, commits oracle changes, maintains oracle `INDEX.md` files, then runs up to five discrepancy-resolution loops.
- For each oracle file, invokes Codex CLI in read-only JSON mode to collect discrepancy objects, applies accumulated discrepancies with write-enabled Codex CLI, rejects forbidden changes under `oracles/` or `.agents/`, commits implementation changes, and writes an apply report under `.cmoc/reports/apply/`.
- Defines prompts used for discrepancy auditing, discrepancy application, commit-message generation, and reporting, including restrictions against reading or editing `memo` and against editing protected paths.

## Read this when

- You need to understand or modify the behavior of the `cmoc apply` subcommand.
- You are changing how cmoc detects discrepancies between oracle files and implementation.
- You are changing how Codex CLI is invoked during apply, including read-only JSON investigation, write-enabled implementation, commit-message generation, or report generation.
- You are debugging `cmoc apply` failures involving branch validation, dirty working trees, forbidden path edits, automatic commits, discrepancy loop limits, or exit code 2 for incomplete application.
- You are changing report output for apply runs under `.cmoc/reports/apply/`.

## Do not read this when

- You only need command-line argument parsing or subcommand registration, not the implementation body of `cmoc apply`.
- You are working on unrelated cmoc subcommands such as branch creation or oracle editing workflows.
- You only need generic Git helper behavior, repository state helpers, timestamp formatting, indexing internals, or Codex CLI wrapper implementation; read the corresponding `commons` modules instead.
- You are looking for oracle specification text itself; use the routed files under `oracles/` instead of this implementation file.
- You are documenting or changing files that are explicitly AI-edit-prohibited, such as `README.md`, `AGENTS.md`, or `oracles` contents.

## hash

- d535afdfef0d21ef903bb741c6149fc7068b0c589bc76e522120f5ae65bcab97

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

- Implements the `cmoc eval-oracles` subcommand body that evaluates oracle specification fragments with Codex CLI and writes a report.
- Ensures `.cmoc` is ignored, maintains oracle `INDEX.md` files, selects either changed oracle files on cmoc branches or all oracle files, runs read-only Codex evaluations, and saves results under `.cmoc/reports/eval-oracles/<timestamp>.md`.
- Contains helper logic for constructing the oracle-review prompt and formatting the markdown report metadata and per-oracle evaluation output.

## Read this when

- You need to understand or modify how `cmoc eval-oracles` chooses between partial and full oracle evaluation.
- You are changing how oracle files are evaluated through `run_codex_exec`, including prompt content, read-only behavior, or report collection.
- You are working on eval-oracles report generation, report path conventions, report front matter, or printed progress steps.

## Do not read this when

- You are working on unrelated subcommands that do not invoke oracle evaluation or report writing.
- You only need the low-level implementations of repository helpers such as branch detection, oracle file listing, or `.cmoc` ignore handling.
- You are looking for the canonical oracle specifications themselves rather than the command that evaluates them.

## hash

- 750fe696b31e4fee63028a58f9dda853a4df77238eef1a4b0b402f0132e63330

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

- Implements the `cmoc merge` subcommand, merging a cmoc branch into the current HEAD with a no-fast-forward merge.
- Validates repository state before merging by requiring no uncommitted changes and ensuring cmoc metadata is ignored.
- Resolves the source branch from an explicit argument or by auto-selecting exactly one unmerged cmoc branch.
- On merge conflicts, delegates conflict-marker resolution to Codex CLI, verifies markers and unmerged paths are gone, stages resolved files, and creates the merge commit.
- Attempts safe deletion of the merged source branch with `git branch -d` and warns if Git refuses.

## Read this when

- You need to understand or change `cmoc merge` behavior.
- You are working on cmoc branch auto-detection for unmerged branches.
- You are modifying how merge conflicts are delegated to Codex CLI or how conflict resolution is validated.
- You are changing repository cleanliness checks, cmoc ignore enforcement, merge commit creation, or post-merge branch deletion.
- You need to know which files Codex is instructed not to edit while resolving merge conflicts.

## Do not read this when

- You are working on unrelated subcommands such as init, branch creation, status, or command-line argument parsing without touching merge execution.
- You only need the generic Git helper functions or repository utility behavior; read the commons modules instead.
- You are looking for cmoc canonical specification fragments; use the routed files under `oracles` instead.
- You are changing documentation or routing metadata only and do not need implementation details of merge conflict handling.

## hash

- eab24f2fdfd113601cd7e858bed0e1eac8d89e9cb9c0dfacbfe8a6bc079f0909
