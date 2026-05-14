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

- INDEX.md 自動メンテナンス処理を実装するモジュール。
- 配置対象ディレクトリの列挙、既存 INDEX.md エントリの再利用、Codex CLI による目次 JSON 生成、Markdown エントリ組み立て、必要時の書き込みと自動コミットを扱う。
- 除外名、gitignore 判定、バイナリ判定、ファイル・ディレクトリ内容ハッシュ、Structured Output 検証、既存エントリからの hash 抽出など、INDEX.md 更新に必要な補助処理をまとめる。

## Read this when

- cmoc の `INDEX.md` 自動生成・更新処理を実装、修正、調査するとき。
- `maintain_indexes` の挙動、`commit_changes`、`.gitignore` 保守、`Maintain INDEX.md files` コミットの発生条件を確認したいとき。
- INDEX.md 配置対象から除外されるディレクトリ・ファイル名、隠しファイル、gitignore 対象、バイナリファイルの扱いを確認するとき。
- 既存 INDEX.md エントリの hash が一致する場合に Codex CLI 呼び出しを省略する再利用ロジックを調べるとき。
- INDEX 目次生成用の Codex prompt、Structured Output JSON の schema 検証、`summary`・`read_this_when`・`do_not_read_this_when` の取り扱いを変更するとき。
- ファイルまたはディレクトリ直下項目から内容ハッシュを計算する処理や、Markdown の Summary / Read this when / Do not read this when / hash ブロック生成を確認するとき。

## Do not read this when

- cmoc の各サブコマンドのユーザー向け仕様や CLI ワークフローそのものを調べたいだけのとき。
- Codex CLI の実行ラッパー、JSON パース、repo 操作、コミット処理の詳細実装を調べるときは、呼び出し先の `codex` や `repo` 系モジュールを読むべきとき。
- 特定の `INDEX.md` に書かれたルーティング内容を確認したいだけで、自動生成・更新ロジックには関心がないとき。
- README、AGENTS、oracles、memo などのリポジトリ運用ルールや編集可否だけを確認したいとき。
- 一般的なハッシュ計算、正規表現、subprocess、pathlib の使い方だけを調べたいとき。

## hash

- 819bf8e6a28ee1b2cbdd40b80746030ab465af1265b8b6a756f6b4008ce35310

# `repo.py`

## Summary

- git リポジトリルートの検出、cwd 移動、git コマンド実行、現在ブランチ名・HEAD commit hash 取得など、リポジトリ操作の共通関数を提供する。
- cmoc ブランチ名の形式判定、`.cmoc` の gitignore 追記、未コミット差分の検出・パス列挙・エラー化、指定パスの差分 commit を扱う。
- `oracles` 配下の仕様ファイル列挙、変更済み oracle ファイル抽出、cmoc ブランチ作成元 commit 記録ファイルのパス解決・読み取りを実装する。
- gitignore 判定は `git check-ignore` を優先し、git 管理外の一時テスト向けに `.gitignore` の単純 glob fallback を持つ。

## Read this when

- `<repo-root>` の git リポジトリルート検出や、コマンド実行前に cwd をリポジトリルートへ移す処理を確認・修正するとき。
- cmoc が git コマンドをどの cwd・stdout/stderr 捕捉・check 設定で実行するかを調べるとき。
- 現在ブランチ、HEAD commit、cmoc ブランチ名形式、cmoc ブランチ作成元 commit ファイルの扱いを確認するとき。
- 未コミット変更の有無、変更パス抽出、未コミット変更がある場合の `CmocError`、`oracles` 配下だけの差分制約を扱うとき。
- `.cmoc` を git 追跡対象外にする `.gitignore` 更新処理を確認・修正するとき。
- `oracles` 配下の評価対象ファイル列挙、`INDEX.md` 除外、gitignore 除外、base commit からの変更 oracle 抽出を扱うとき。
- 指定パスに差分がある場合だけ `git add` と `git commit` を行う共通処理を確認するとき。

## Do not read this when

- CLI 引数の定義、サブコマンドの dispatch、ユーザー向けヘルプ表示だけを調べたいとき。
- Codex CLI 呼び出し、プロンプト生成、Structured Output の解析、LLM 応答処理を調べたいとき。
- `INDEX.md` の本文生成、目次 JSON の構造、ルーティング文書の更新ロジックそのものを調べたいとき。
- 共通エラー型やエラー表示形式の実装だけを確認したいとき。
- ファイル読み書き一般、タイムスタンプ生成、コンソール出力、テキスト整形など git リポジトリ操作以外の共通処理を探しているとき。
- 自動テストの配置や Fake Codex CLI など、テスト支援コードの詳細だけを調べたいとき。

## hash

- 7105e24a87058244a02d2ea6b5cdddefa207f4f1d819f2039ca0f5b9c2d79818

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
