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

- Codex CLI 呼び出しラッパー `commons.codex.run_codex_exec` のテストファイル。
- Fake Codex CLI を一時ディレクトリに作成し、Structured Output の JSON parse 失敗時リトライ、試行ログ保存、`--output-schema` ファイル渡し、JSON 意味検証失敗時のリトライと `CmocError` 詳細出力を検証する。
- `tmp_path`、`monkeypatch`、PATH 差し替え、`.cmoc/logs/codex_exec/*.log` の確認を使って、外部 Codex CLI を実行せずにラッパー挙動をテストする。

## Read this when

- `run_codex_exec` の Structured Output 対応、JSON パース失敗時の最大 3 回リトライ、またはリトライごとのログ記録仕様を確認したいとき。
- `output_schema` 引数が一時 JSON ファイルとして保存され、`codex exec --output-schema` に渡される挙動のテストを探すとき。
- `json_validator` による意味的検証失敗をリトライ対象にする挙動や、失敗継続時に `CmocError.detail` へ最後の JSON エラー、ログパス、最後の stdout を含める挙動を確認したいとき。
- Fake Codex CLI を使った pytest の書き方、PATH 差し替え、実行回数カウント、ログファイル検証の既存パターンを参照したいとき。

## Do not read this when

- cmoc のサブコマンド全体の統合テスト、CLI 引数解析、またはユーザー向けコマンド出力のテストを探しているとき。
- Codex CLI 呼び出しラッパーの実装そのものを読みたいとき。実装は `src` 配下の `commons.codex` 側を確認する。
- Structured Output 以外の通常実行、サンドボックス指定、権限モード、タイムアウトなど、このファイルに含まれない `run_codex_exec` 挙動を調べたいとき。
- oracle 仕様、README、AGENTS、またはリポジトリ運用ルールの正本を確認したいとき。

## hash

- fc680b14202f871c3248017f426de7a0f11cc39a15526e0d391d9b660f53e94c

# `test_indexing.py`

## Summary

- `commons.indexing.maintain_indexes` による INDEX.md メンテナンス処理の pytest テスト。
- gitignore 対象を除外して直下項目ごとのルーティング情報を生成すること、Structured Output schema が Codex CLI 呼び出しに渡されることを検証する。
- 不正な Structured Output からのリトライ、最新 INDEX.md では Codex CLI を呼ばないこと、commit_changes=True 時に INDEX.md などメンテナンス対象だけをコミットすることを確認する。
- テスト用 git リポジトリを作る `_init_repo` と、指定リポジトリ上で git コマンドを実行する `_git` ヘルパーを含む。

## Read this when

- INDEX.md 自動生成・更新処理の期待挙動を確認したいとき。
- `maintain_indexes` が gitignore、既存 INDEX.md の hash、Codex CLI 呼び出し、Structured Output schema をどう扱うべきか調べたいとき。
- INDEX.md が最新の場合に不要な Codex CLI 呼び出しを避ける仕様をテストから確認したいとき。
- INDEX.md メンテナンスの自動コミットがユーザー作業ファイルを巻き込まないことを確認したいとき。
- `commons.indexing._INDEX_OUTPUT_SCHEMA` や `run_codex_exec` のテスト上の使われ方を確認したいとき。

## Do not read this when

- cmoc の CLI サブコマンド仕様やユーザー向けワークフローだけを調べたいとき。
- INDEX.md 生成ロジックの実装本体を読みたいとき。
- Codex CLI 実行ラッパーの詳細実装やプロンプト生成処理を確認したいとき。
- git 操作全般の共通ユーティリティや本番コードでのコミット処理を調べたいとき。
- INDEX.md 以外の機能テストやサブコマンド別テストを探しているとき。

## hash

- ed3fccb8edfe74286c6a946cbb1695f64c1b669172f2f105a0d0f6cd5c7296e8

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

- cmoc の主要サブコマンド本体に対する決定論的な制御ロジックを検証する pytest ファイル。
- `cmoc init`、`cmoc branch`、`cmoc eval-oracles --full`、`cmoc apply`、`cmoc merge <branch>` の成功系と一部失敗系を、実 Git リポジトリを使って確認する。
- `cmoc apply` のズレ調査 JSON schema 検証、非 cmoc ブランチでの拒否、Codex CLI 呼び出しの monkeypatch による疑似応答など、外部依存を抑えたサブコマンド単体テストを含む。
- テスト用 Git リポジトリ作成ヘルパー `_init_repo` と、Git コマンド実行ヘルパー `_git` を同ファイル内に持つ。

## Read this when

- cmoc のサブコマンド実装を変更し、主要な制御フローが既存テストでどう期待されているか確認したいとき。
- `cmoc init` が `.gitignore` に `.cmoc` を追加し、`Initialize cmoc` commit を作る挙動のテストを確認したいとき。
- `cmoc branch` が `cmoc_` で始まるブランチを作成し、`.cmoc/branch/<branch>.txt` に base commit を記録する期待値を確認したいとき。
- `cmoc eval-oracles --full` が oracle 評価レポートを `.cmoc/reports/eval-oracles` に保存するテストを確認したいとき。
- `cmoc apply` のズレなし完了、レポート保存、Structured Output schema 指定、非 cmoc ブランチ拒否、ズレ調査 payload 検証を調べたいとき。
- `cmoc merge <branch>` が明示された cmoc ブランチを clean tree で merge し、安全ならブランチを削除するテストを確認したいとき。
- サブコマンドテストで一時 Git リポジトリを作る方法や、`monkeypatch` で `maintain_indexes` と `run_codex_exec` を差し替える既存パターンを探すとき。

## Do not read this when

- CLI 引数パース、標準出力、終了ステータス表示など、コマンドライン入口全体の挙動だけを確認したいとき。
- oracle 仕様断片そのものや、正本仕様のルーティング情報を調べたいとき。
- サブコマンド実装の詳細コードを読みたいだけで、テスト上の期待値や既存テストパターンが不要なとき。
- README、AGENTS.md、oracles、memo などのリポジトリ運用ルールや編集可否だけを確認したいとき。
- Codex CLI 実体の実行、外部 LLM 応答品質、ネットワーク連携など、mock されていない統合挙動を検証したいとき。

## hash

- 46a981833ae9798a235ffc5d372a189daee2a23797ea30706cfce37be57958e9

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
