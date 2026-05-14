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

- commons.indexing.maintain_indexes の INDEX.md 自動生成・更新処理を検証する pytest テスト。
- 直下項目ごとのルーティング項目生成、.gitignore 対象の除外、Structured Output 不正時のリトライ、INDEX.md が最新のときの Codex CLI 呼び出し抑止、自動コミット対象の限定を扱う。
- 一時 git リポジトリ、fake Codex CLI、monkeypatch、ハッシュ付き既存 INDEX.md を使って INDEX メンテナンスの主要な境界条件を確認する。

## Read this when

- maintain_indexes の挙動を変更し、INDEX.md 生成・更新ロジックの既存テスト期待値を確認したいとき。
- INDEX.md 目次項目の生成対象、gitignore されたファイルの除外、最新判定、content hash による再生成スキップを検証したいとき。
- Codex CLI の Structured Output が schema 不一致だった場合のリトライ挙動をテストしたいとき。
- INDEX.md メンテナンス時の commit_changes=True が、ユーザー作業ファイルではなくメンテナンス対象パスだけをコミットすることを確認したいとき。
- tests 内で一時 git リポジトリを初期化する _init_repo や git コマンド実行ヘルパー _git の使い方を参照したいとき。

## Do not read this when

- cmoc の INDEX.md 自動メンテナンス仕様そのものを知りたいだけで、テスト実装の詳細が不要なとき。
- branch、apply、merge、init、eval-oracles など、INDEX メンテナンス以外のサブコマンド挙動を調べたいとき。
- commons.indexing の実装コードを直接修正するために、関数本体や内部アルゴリズムを読みたいとき。
- README、AGENTS、oracles、memo などのリポジトリ運用ルールやファイルアクセス制約だけを確認したいとき。
- Codex CLI 一般の利用方法や外部コマンド仕様を調べたいとき。

## hash

- 5692abccc4571bf53548a2b906d82697ea20919c739e5712aafabdc7bdf320a8

# `test_repo.py`

## Summary

- commons.repo の git リポジトリ共通処理を検証する pytest テストファイル。
- find_repo_root、ensure_cmoc_ignored、list_oracle_files、changed_oracle_files、assert_only_oracles_uncommitted、is_cmoc_branch、branch_base_commit_path の挙動を扱う。
- 一時 git リポジトリを作成するヘルパーを使い、`.git` 探索、`.cmoc` ignore 追記、oracle ファイル列挙、部分評価対象の差分検出、非 oracle 差分拒否、cmoc ブランチ名判定、branch base commit 記録先を確認する。

## Read this when

- commons.repo のリポジトリ探索、gitignore 更新、oracle ファイル列挙、差分検出、ブランチ関連パスの仕様をテスト側から確認したいとき。
- `cmoc apply` の事前条件として oracles 外の未コミット差分を拒否する挙動を確認・変更するとき。
- cmoc ブランチ命名規則や `.cmoc/branch/<branch>.txt` の記録先に関するテストを追加・修正するとき。
- gitignore 対象ファイルや `INDEX.md` を oracle 列挙・部分評価対象から除外する挙動を確認するとき。
- tmp_path 上に git リポジトリを作るテストヘルパー `_init_repo` や `_git` の使い方を確認したいとき。

## Do not read this when

- cmoc の CLI サブコマンド全体のユーザー向け仕様や stdout 表示仕様だけを調べたいとき。
- Codex CLI 呼び出し、プロンプト生成、Structured Output、サンドボックスなど LLM 連携部分のテストを探しているとき。
- oracle 正本仕様そのものの内容や `oracles/INDEX.md` のルーティング仕様を調べたいとき。
- README、AGENTS、memo、oracles などリポジトリ運用上の編集可否ルールだけを確認したいとき。
- git リポジトリ共通処理ではないサブコマンド固有の実装テストを探しているとき。

## hash

- dc42a69418cfe6c904f477510dce201eaa38df69192340858a7f71e68b6b409a

# `test_subcommands.py`

## Summary

- cmoc の主要サブコマンド実装に対する決定論的な制御ロジックの pytest テストをまとめる。
- `cmoc init` の `.cmoc` ignore 追加と初期化コミット、`cmoc branch` の cmoc ブランチ作成と base commit 記録を検証する。
- `cmoc eval-oracles --full`、`cmoc apply`、`cmoc merge <branch>` について、Codex 呼び出しを monkeypatch したレポート保存、ブランチ制約、discrepancy JSON schema 検証、merge 後のブランチ削除を確認する。
- テスト用 git リポジトリ作成と git コマンド実行のための `_init_repo`、`_git` ヘルパーを含む。

## Read this when

- `sub_commands.init`、`sub_commands.branch`、`sub_commands.eval_oracles`、`sub_commands.apply`、`sub_commands.merge` のサブコマンド本体の基本挙動をテストで確認したいとき。
- cmoc サブコマンドが git リポジトリ上で作成するブランチ、コミット、`.cmoc` 配下の記録・レポート、`.gitignore` 変更をどう検証しているか知りたいとき。
- Codex CLI 実行や INDEX メンテナンスを monkeypatch して、サブコマンドの決定論的な制御フローだけをテストする方法を探すとき。
- `cmoc apply` の cmoc ブランチ制約、ズレなし JSON の完了扱い、discrepancy payload の必須項目検証に関するテストを調べるとき。
- `cmoc merge <branch>` が clean tree 前提で cmoc ブランチを merge し、成功後に対象ブランチを削除する挙動のテストを確認したいとき。

## Do not read this when

- CLI の引数パース、エントリーポイント、stdout/stderr の表示形式だけを調べたいとき。
- Codex CLI との実際の外部プロセス連携、プロンプト内容、サンドボックス設定、Structured Output の詳細仕様そのものを確認したいとき。
- oracle 正本仕様ファイルの内容や INDEX.md 自動生成ルーティング仕様を読みたいとき。
- 個別サブコマンドの実装コードを直接追いたいだけで、pytest 上の期待挙動や回帰テストを参照する必要がないとき。
- ファイルアクセス制約、README/AGENTS/oracles/memo の編集可否など、リポジトリ運用ルールだけを確認したいとき。

## hash

- 163a0b34c233afe7f777808513e50b841903ce0890bf031a4f4cec49323f81cc

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
