# `__init__.py`

## Summary

- Declares the src.commons package with a short module docstring.
- Contains no imports, exports, runtime logic, constants, or public API definitions.

## Read this when

- You need to confirm that src.commons is a Python package.
- You are documenting or routing the commons package at a package-level overview.

## Do not read this when

- You need implementation details for shared utilities; inspect the concrete modules under src/commons instead.
- You are looking for command behavior, workflow logic, configuration handling, or tests.

## hash

- ff1b23adb7b4c5a75686ac97283d2065d5cacc8861143f25677b559abeb6e2d0

# `codex.py`

## Summary

- Provides shared helpers for invoking `codex exec` from cmoc workflows.
- `run_codex_exec` builds the Codex CLI command with read-only or workspace-write sandboxing, runs it in the target repository root, and stores full invocation logs under `.cmoc/logs/codex_exec`.
- When JSON output is expected, `run_codex_exec` retries up to three times, parses stdout as JSON, optionally applies a validator, and raises `CmocError` with log details if validation never succeeds.
- `parse_json_object` parses Codex CLI output and enforces that the result is a JSON object.
- `_append_codex_log` appends each Codex CLI attempt, prompt, return code, stdout, and stderr to the per-run log file.

## Read this when

- You need to understand or change how cmoc calls `codex exec`.
- You are working on Codex CLI sandbox selection, including read-only versus workspace-write execution.
- You are debugging `.cmoc/logs/codex_exec` log creation or the contents written for each Codex execution attempt.
- You are changing retry behavior for expected JSON responses from Codex CLI.
- You are adding or modifying validation of Codex CLI JSON output.
- You are investigating `CmocError` messages raised after Codex CLI command failures or invalid JSON output.

## Do not read this when

- You only need command-line argument parsing, subcommand routing, or top-level CLI entrypoint behavior.
- You are working on timestamp formatting without needing to know where Codex execution logs are named.
- You are changing domain-specific prompt text or oracle routing rules but not the shared Codex invocation mechanism.
- You need implementation details for non-Codex subprocesses or general filesystem operations outside Codex execution logging.
- You are looking for tests or fixtures rather than the production helper that invokes Codex CLI.

## hash

- cf766cddefb179fe47bf6973fc886f9be493ec480e89aa6cb021d6801f5536a1

# `errors.py`

## Summary

- Defines CmocError, the shared runtime error type for cmoc failures that should present user-facing next actions.
- Stores an error message, recovery actions, detail text, and process exit code for structured CLI error handling.
- Provides format_error_report(error), which converts CmocError and unexpected exceptions into the stdout error report format with summary, next actions, detail, and call stack.

## Read this when

- You need to raise or handle cmoc-specific runtime errors that include actionable recovery steps for the user.
- You are changing the CLI-wide error report format printed for failures.
- You need to understand how unexpected exceptions are converted into generic user-facing error reports.
- You are wiring command execution paths to return or display structured error details and exit codes.

## Do not read this when

- You are looking for command-specific validation rules or domain-specific error messages; inspect the relevant command module instead.
- You are investigating logging, tracing, or debug output unrelated to user-facing CLI error reports.
- You need application specification details for when errors should be raised; consult the relevant oracle specification route instead.
- You are working on non-error commons utilities or normal command output formatting.

## hash

- e22fea18c95c0c9b16b8e8e53049f6f3e9ee78a9ec719ac82d59b92a02c3131e

# `indexing.py`

## Summary

- Maintains generated INDEX.md routing files for a target repository by scanning eligible directories, generating per-entry metadata through Codex structured JSON output, and optionally committing changes.
- Defines index target selection, ignored-name and gitignore filtering, binary-file exclusion, stable hash generation, prompt construction, payload validation, and Markdown entry formatting for INDEX.md files.

## Read this when

- You need to understand or modify how cmoc creates, updates, or commits INDEX.md files across a repository.
- You are changing rules for which files or directories are excluded from indexing, including memo, build, tmp, __pycache__, hidden paths, gitignored paths, or binary-looking files.
- You are debugging INDEX.md generation prompts, structured output validation, hash calculation, or Markdown formatting of summary/read-this-when/do-not-read-this-when sections.

## Do not read this when

- You only need the high-level CLI command routing or user-facing behavior and do not need INDEX.md maintenance internals.
- You are working on unrelated repository utilities, Codex execution wrappers, or git commit helpers except where they are called by index maintenance.
- You are looking for the canonical specification fragments under oracles rather than the implementation of generated repository index maintenance.

## hash

- 602d58e535fe198c1e10c90f35fc3847c7b751507a8186778de8f99932ddb042

# `repo.py`

## Summary

- Provides shared helpers for locating and entering a Git repository root, running Git commands with a fixed cwd, and reading current branch or HEAD commit information.
- Defines cmoc branch recognition for `cmoc_<timestamp>` names and manages `.cmoc` ignore handling in `.gitignore`.
- Checks working tree state, extracts changed paths from `git status --porcelain`, and raises `CmocError` for disallowed uncommitted changes.
- Lists oracle files and changed oracle files while excluding `INDEX.md` and Git-ignored paths, including committed, staged, unstaged, and untracked oracle changes.
- Reads and builds paths for cmoc branch base commit records under `.cmoc/branch`, with Git ignore detection backed by `git check-ignore` plus a simple `.gitignore` glob fallback.

## Read this when

- You need to understand how cmoc finds `<repo-root>` from the current directory or switches process cwd to the repository root.
- You are changing Git command execution, branch detection, HEAD commit lookup, or cmoc branch naming rules.
- You are working on commands that require a clean working tree or only allow uncommitted changes under `oracles/`.
- You need to know how cmoc enumerates all oracle files or detects which oracle files changed since a branch base commit.
- You are debugging `.cmoc` ignore insertion, Git-ignored oracle filtering, or `.cmoc/branch/<branch>.txt` base commit files.

## Do not read this when

- You are looking for CLI argument parsing, subcommand dispatch, or user-facing command definitions.
- You need oracle specification content or routing metadata under `oracles`; this file only contains implementation helpers.
- You are working on non-Git filesystem utilities that do not depend on repository root discovery, working tree status, or oracle file enumeration.
- You need prompt construction, AI evaluation logic, or documentation generation behavior outside repository and Git plumbing.
- You are investigating tests or fixtures unless the failure is specifically about Git state handling, oracle path collection, or cmoc branch base commit records.

## hash

- 9c20123a58e16b99ee798d60a654b08485c63bc69788a53c187ee14f7ceb99a5

# `timestamps.py`

## Summary

- cmoc 仕様の `<time-stamp>` 文字列を生成する共通ユーティリティを定義している。
- `make_timestamp(now: datetime | None = None) -> str` は、指定された `datetime` または現在のローカル時刻から `YYYY-MM-DD_HH-MM_SS_mmm` 形式の文字列を返す。
- ミリ秒部分は `microsecond // 1000` により 3 桁ゼロ埋めで出力される。

## Read this when

- cmoc 内で生成されるタイムスタンプ文字列の形式を確認・変更したいとき。
- `<time-stamp>` を含むファイル名、ディレクトリ名、ログ、作業成果物名の生成処理を追跡するとき。
- タイムスタンプ生成のテストで固定時刻を渡す方法を確認したいとき。

## Do not read this when

- タイムスタンプを使う側のワークフローや保存先ディレクトリ構造を調べたいだけのとき。
- CLI 引数解析、サブコマンド実装、設定読み込みなど、日時文字列のフォーマットに関係しない処理を調べているとき。
- 正本仕様そのものを確認したいときは、まず `oracles` 配下の該当仕様断片を読むべき。

## hash

- 191db72c912ef0587bb2d6521fa8e4151c14102328c551868854aa7fa632edcc
