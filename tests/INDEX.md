# `conftest.py`

## Summary

- pytest execution helper that prepends the repository's src directory to sys.path so tests can import cmoc source modules without installation.
- Defines SRC as the repository root's src path relative to tests/conftest.py and inserts it at the front of Python's import search path.

## Read this when

- Investigating how tests import modules from <cmoc-root>/src.
- Debugging pytest import errors, module resolution order, or test environment setup.
- Changing the test suite's Python path/bootstrap behavior.

## Do not read this when

- Looking for individual test cases or assertions for cmoc behavior.
- Investigating application runtime import behavior outside pytest.
- Changing cmoc implementation code under <cmoc-root>/src.

## hash

- 32bfe11389fb732e9ac0cc6ecb2e14bf9722d848696fc618e360ef72c19633e7

# `test_codex.py`

## Summary

- Tests the commons.codex.run_codex_exec wrapper around the codex CLI.
- Covers Structured Output JSON retry behavior for parse failures and semantic validation failures.
- Verifies codex execution attempt logs are written under .cmoc/logs/codex_exec and include all retry attempts.
- Verifies repeated JSON semantic validation failure raises CmocError with diagnostic detail including the last JSON error, log path, and last stdout.

## Read this when

- Changing commons.codex.run_codex_exec behavior, especially expect_json or json_validator handling.
- Changing retry counts, retry conditions, or error reporting for codex CLI Structured Output execution.
- Changing codex exec logging location, log format, or per-attempt log content.
- Debugging tests or regressions related to CmocError details from failed codex execution.

## Do not read this when

- Working on unrelated CLI subcommands or workflow behavior that does not call run_codex_exec.
- Changing oracle routing metadata, README content, packaging, or project configuration unrelated to codex execution.
- Investigating non-Codex test suites or behavior outside the commons.codex wrapper.
- Looking for broad cmoc application specifications rather than tests for the codex CLI invocation wrapper.

## hash

- 78fa2bcb09792f7acb33ca486c6ae3265510ad3b92179e66c6ceecb87617036c

# `test_indexing.py`

## Summary

- Tests INDEX.md maintenance for repository indexing, including routing entry generation for non-ignored files and exclusion of .gitignore-matched paths.
- Verifies invalid structured JSON output from the Codex CLI is retried until schema-valid routing metadata is produced.
- Defines git-backed temporary repository helpers used by the indexing tests.

## Read this when

- Changing commons.indexing.maintain_indexes behavior for INDEX.md generation, gitignore filtering, or changed-state reporting.
- Changing run_codex_exec structured-output validation or retry behavior for routing metadata JSON.
- Investigating failures in indexing tests that create temporary git repositories and fake Codex CLI responses.

## Do not read this when

- Working on application command behavior unrelated to INDEX.md maintenance or routing metadata generation.
- Looking for production implementation details of indexing; read commons.indexing instead.
- Updating documentation content manually without touching automated INDEX.md generation or structured-output retry behavior.

## hash

- a0a4f9baa41c97a6292bca4b8c013ef22e2386e4f32288c5866be8e65503d57d

# `test_repo.py`

## Summary

- Tests shared git repository utilities in commons.repo.
- Covers repository root discovery, .cmoc gitignore setup, oracle file enumeration, changed oracle detection, uncommitted-change validation, cmoc branch naming, and branch base commit path construction.
- Uses temporary git repositories and local helper functions to exercise behavior against real git commands.

## Read this when

- Changing commons.repo functions such as find_repo_root, ensure_cmoc_ignored, list_oracle_files, changed_oracle_files, assert_only_oracles_uncommitted, is_cmoc_branch, or branch_base_commit_path.
- Modifying cmoc behavior around oracle file discovery, gitignored oracle files, or partial evaluation targets from base..HEAD plus working tree changes.
- Changing cmoc branch naming rules or .cmoc/branch base commit record paths.
- Debugging test failures related to git repository setup, temporary repositories, or subprocess-based git assertions.

## Do not read this when

- Working on CLI argument parsing, command dispatch, or user-facing output that does not affect repository utility behavior.
- Changing oracle specification routing metadata or documentation unrelated to tests or commons.repo behavior.
- Investigating non-git application logic, prompt generation, or AI execution workflows outside repository and oracle-file handling.

## hash

- fb1e54af197513c88a70be5adc0e8b98e481bce65fb58be6f869fc7ae7b91850

# `test_subcommands.py`

## Summary

- Tests deterministic control logic for cmoc subcommand implementation functions using temporary Git repositories.
- Covers cmoc init creating and committing the .cmoc ignore rule, cmoc branch creating a cmoc_ branch and recording the base commit, eval-oracles report generation with fake Codex output, apply completion behavior when discrepancy JSON is empty, and merge behavior for explicitly named cmoc branches.
- Defines shared test helpers for initializing a minimal Git repository and running Git commands with captured output.

## Read this when

- Changing or debugging tests for subcommand implementation functions in src/sub_commands.
- Modifying cmoc init, branch, eval-oracles, apply, or merge behavior that affects Git state, .cmoc metadata, or report creation.
- Needing examples of how tests monkeypatch run_codex_exec or maintain_indexes for deterministic subcommand tests.
- Looking for the local test helper pattern for creating temporary Git repositories in pytest.

## Do not read this when

- Investigating CLI argument parsing, command dispatch wiring, or terminal output formatting rather than subcommand implementation behavior.
- Working on oracle INDEX routing metadata or documentation generation tests unrelated to subcommand execution.
- Changing README, AGENTS, or oracle specification prose without touching the tested subcommands.
- Looking for integration tests that execute the installed cmoc command through the shell instead of calling implementation functions directly.

## hash

- 718ddc2b660c8057c8dbf4afdd60c786edeaa8ccd20a55bdc09dea892e7b1c68

# `test_timestamps.py`

## Summary

- Tests the cmoc timestamp formatting helper `commons.timestamps.make_timestamp`.
- Verifies that a `datetime` value is formatted as `YYYY-MM-DD_HH-MM_SS_mmm` with zero-padded date/time fields and millisecond precision.
- Uses a fixed datetime value with microseconds to confirm truncation or conversion to a three-digit millisecond suffix.

## Read this when

- You are changing timestamp generation or formatting behavior.
- You are modifying `commons.timestamps.make_timestamp` or related timestamp utilities.
- You need to understand the expected cmoc timestamp string format used by tests.

## Do not read this when

- You are working on CLI argument parsing, command routing, or unrelated command behavior.
- You are changing filesystem operations, repository discovery, or process execution logic unrelated to timestamps.
- You only need broad test suite structure and do not need timestamp-specific expectations.

## hash

- 04907b2d4b3124b790c583ea06e2afecdf812378b4b933143c989e15ecfb0373
