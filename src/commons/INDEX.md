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

- Codex CLI 呼び出しの共通処理を定義するモジュール。
- `run_codex_exec` により `codex exec` を read-only または workspace-write サンドボックスで実行し、標準出力・標準エラー・プロンプト・終了コード・Structured Output schema の情報を `<repo-root>/.cmoc/logs/codex_exec` 配下へ保存する。
- JSON 応答が必要な呼び出しでは最大 3 回リトライし、JSON パースや任意バリデータに失敗した場合はログ情報付きの `CmocError` を送出する。
- `parse_json_object` は Codex CLI の JSON 応答が object であることを確認し、object 以外なら `CmocError` を送出する。
- 内部ヘルパーとして、Codex 実行ログを追記する `_append_codex_log` と、Structured Output 用 JSON schema をログ配下へ書き出す `_write_output_schema` を持つ。

## Read this when

- cmoc から `codex exec` を呼び出す共通経路を確認・修正したいとき。
- Codex CLI 呼び出し時のサンドボックス指定、作業ディレクトリ、プロンプト渡し、標準出力・標準エラーの扱いを調べたいとき。
- Codex 実行ログや Structured Output schema が `<repo-root>/.cmoc/logs/codex_exec` 配下へどのように保存されるか確認したいとき。
- Structured Output 相当の JSON 応答に対するリトライ、JSON パース、バリデーション、失敗時の `CmocError` を調べたいとき。
- Codex CLI の JSON 応答を Python の辞書として扱う処理や、object 以外をエラーにする仕様を確認したいとき。

## Do not read this when

- 個別サブコマンドのプロンプト内容や業務ロジックだけを調べたいとき。
- Codex CLI を使わないファイル操作、タイムスタンプ生成、共通エラー型そのものの実装を確認したいとき。
- コンソール表示、進捗出力、ユーザー向けメッセージ全般の仕様だけを調べたいとき。
- テスト用 Fake Codex CLI の実装やテストデータの構造だけを確認したいとき。
- oracles の正本仕様や README/AGENTS など、実装コード以外のルーティング情報を調べたいとき。

## hash

- 6e34bc0ff2bbd3ed287b7a573a14541311da29f1217bdd2c076f44d9a5407cb9

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

- `INDEX.md` の自動生成・更新を担当する共通モジュール。
- 対象リポジトリ内の INDEX.md 配置対象ディレクトリを列挙し、既存エントリのハッシュ再利用、Structured Output による目次生成、必要時の書き込みとコミットを行う。
- 除外対象名、gitignore、バイナリ判定、ファイル・ディレクトリ内容ハッシュ、INDEX エントリのパースと検証など、INDEX メンテナンスに必要な内部処理をまとめている。

## Read this when

- `maintain_indexes` による INDEX.md 自動メンテナンスの全体フローを確認・変更するとき。
- INDEX.md を作成する対象ディレクトリの選定条件、除外名、gitignore 判定、バイナリ除外の仕様を調べるとき。
- Codex CLI に渡す INDEX 生成プロンプト、Structured Output schema、JSON 検証処理を確認・修正するとき。
- 既存 INDEX.md エントリの再利用条件、hash 欄の読み取り、内容ハッシュ計算、エントリ整形の挙動を調べるとき。
- INDEX.md 更新後に `.gitignore` や生成済み INDEX.md をコミット対象へ含める処理を確認するとき。

## Do not read this when

- Codex CLI 実行や JSON パースの低レベル実装そのものを調べたいとき。
- リポジトリ検出、`.gitignore` 更新、コミット作成など repo 共通処理の詳細だけを確認したいとき。
- 個別サブコマンドの CLI 仕様やユーザー向けワークフローを調べたいとき。
- INDEX.md の内容として書かれる各ディレクトリ・各ファイルの意味を知りたいだけで、自動生成処理には関心がないとき。
- cmoc の開発ルール、テスト方針、環境設定など、実装者向け規約を確認したいとき。

## hash

- b7529b83c5bc96c07a4e0e527fbcb7da7343b3bde61eaeea64891bf482e6ad9d

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
