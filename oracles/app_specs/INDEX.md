# `codex_call.md`

## Summary

- cmoc から Codex CLI を呼び出す際は、すべて `codex exec` を使うことを定める仕様。
- 読み取り専用で足りる作業では Codex CLI のサンドボックスを read-only にし、`.agents` 配下は `codex exec` から編集できない前提で扱う。
- Codex CLI に渡すプロンプトは、ロール、作業概要、完了条件、任意の詳細作業内容の順で構成する。
- Codex CLI に渡すプロンプトでは `<cmoc-root>` や `<repo-root>` などの cmoc 固有概念を使わず、具体的なパスを埋め込む必要がある。
- 呼び出された AI エージェントがプロンプト単体で自走でき、特定リポジトリや cmoc 由来のメタ認知に依存しない汎用的な内容にする。
- Codex CLI へのプロンプトには、実行時のサンドボックスに応じたファイルアクセス制限指示を含める。
- `codex exec` のフルログは `<repo-root>/.cmoc/logs/codex_exec/<time-stamp>.log` に保存する。
- `codex exec` の失敗時は、Structured Output の意味的失敗のみ最大3回リトライし、それ以外の想定外エラーや3回失敗後は即時にコマンド全体を失敗させる。

## Read this when

- cmoc から Codex CLI をどのコマンド形式で起動するかを実装・確認するとき。
- `codex exec` に渡すプロンプトの構成、禁止表現、必要な前提情報、完了条件の書き方を確認するとき。
- 読み取り専用作業と書き込み可能作業で、Codex CLI に渡すサンドボックス設定やファイルアクセス制限指示を決めるとき。
- `.agents` 配下を Codex CLI 経由で扱う際の制約や、プロンプト側での緩和方針を確認するとき。
- `codex exec` 呼び出しログの保存先やログ出力仕様を実装・確認するとき。
- Structured Output のパース失敗や Codex CLI 実行エラーに対するリトライ・失敗処理を実装・確認するとき。

## Do not read this when

- cmoc のサブコマンド全体の一覧やユーザー向け CLI 仕様を調べたいだけのとき。
- Codex CLI 呼び出しではなく、cmoc 内部の通常処理、データ構造、設定ファイル仕様を調べているとき。
- `oracles` 配下の仕様断片のルーティング規則や INDEX の書き方を調べたいとき。
- cmoc 自体のコーディング規約、テスト方針、開発環境ルールを調べたいとき。
- Codex CLI を呼び出さない処理のログ保存先やエラーハンドリングだけを調べているとき。

## hash

- 554bde700e2a8f4c8e8e86e649c33b18f0b675c05e4b7443e3ad42a3fca62f5e

# `console_output.md`

## Summary

- Defines cmoc console output requirements for subcommands.
- Subcommands should emit lightweight progress information to stdout so users can tell work is active, without requiring detailed logs.
- Examples include step names and counts, prompts passed to `codex exec`, outputs collected from execution results, and elapsed-time reports per step and per subcommand.

## Read this when

- Designing or changing stdout/progress output behavior for cmoc subcommands.
- Implementing reporting of subcommand steps, step counts, execution prompts, collected command output, or elapsed-time summaries.
- Checking what level of console logging is expected during cmoc command execution.

## Do not read this when

- Working on command routing, CLI argument parsing, or subcommand semantics unrelated to user-visible console output.
- Investigating coding style, repository development rules, or test environment setup.
- Looking for complete specifications of individual subcommands beyond their progress/output reporting behavior.

## hash

- aadad6359ed1b4af58ac47902b69675df12858a7ccc363aca173ca551052e80d

# `error_handling.md`

## Summary

- cmoc の仕様で個別指定がない場合の標準エラーハンドリング規則を定義する。
- 処理中断、stdout へのエラーレポート出力、エラー終了を示すステータスコード返却を要求する。
- エラーレポートに含める内容として、簡単な説明、次に取るべきアクション、詳細説明、コールスタックを定める。
- 個別仕様に特別なエラー処理指定がある場合は、その指定を優先することを定める。

## Read this when

- cmoc 全体で共通のエラー終了時の挙動を実装または確認するとき。
- 個別仕様にエラー処理の明記がないケースで、どのように処理を中断し報告するべきか判断するとき。
- エラー時に stdout へ出力するレポート項目や終了ステータスの扱いを設計するとき。
- 例外や想定外状態の扱いについて、個別仕様と共通規則の優先関係を確認するとき。

## Do not read this when

- 特定サブコマンドの正常系フローや入出力仕様だけを調べたいとき。
- 開発環境、コーディング規約、設計規約などアプリケーション実行時エラー以外の開発ルールを調べたいとき。
- 個別仕様に明記された専用のエラー処理だけで判断でき、共通フォールバック規則を確認する必要がないとき。
- README や CLI の利用者向け説明文を更新するための情報だけが必要なとき。

## hash

- bfaceea1701755cbe1f24db75ea9044ad4d4ed7dc98edef844bc94e39c3bbdf8

# `indexing.md`

## Summary

- `cmoc` が `<repo-root>` 配下に自動配置・自動メンテナンスする `INDEX.md` の仕様を定義している。
- `INDEX.md` の配置対象ディレクトリ、目次作成対象、除外対象、フォーマット、ハッシュ管理、生成方法を説明している。
- メンテナンス処理の順序、差分検出、削除・再生成、自動コミット、実行タイミングを定義している。

## Read this when

- `cmoc` による `<repo-root>` の `INDEX.md` 自動生成・更新処理を実装または修正するとき。
- ルーティングメタデータの Structured Output schema、目次情報フォーマット、hash 欄の扱いを確認するとき。
- `INDEX.md` の配置対象・除外対象や、`.gitignore`、隠しファイル、memo、バイナリファイルの扱いを判断するとき。
- Codex CLI 実行前に行う `INDEX.md` メンテナンスの実行タイミングや例外条件を確認するとき。

## Do not read this when

- `cmoc` 自体のコマンドライン引数、サブコマンド、UI、ワークフローなど、`INDEX.md` メンテナンス以外のアプリ仕様を調べるとき。
- `<cmoc-root>/oracles` 配下の正本仕様ルーティングそのものを調べるだけで、`<repo-root>` 側の `INDEX.md` 仕様に触れないとき。
- 開発環境、コーディング規約、設計ルールなど、実装上の一般ルールを確認したいだけのとき。
- README や AGENTS.md など、AI 編集禁止ファイルの取り扱いルールだけを確認したいとき。

## hash

- 0dc8c091f82725c8298f9a3748b6c80bf57701d562ac7b43aabb413dab20d9e9

# `misc_specs.md`

## Summary

- Defines miscellaneous cmoc application behavior not specific to a single subcommand or workflow.
- Specifies how to mechanically enumerate oracle files under `<repo-root>/oracles`, excluding gitignored files and `INDEX.md`.
- States assumptions about the target `<repo-root>` repository, including git management, fragmented oracle documentation, and repository-local implementation of task-specific knowledge.
- Defines how cmoc discovers and switches to `<repo-root>` by walking upward from the invocation directory to find a directory containing `.git`.
- Specifies that `<repo-root>/.cmoc` is untracked by git and that `cmoc init` guarantees this.
- Defines the timestamp format `<year>-<month>-<day>_<hour>-<minute>_<sec>_<msec>` using zero-padded local time components.

## Read this when

- Implementing or testing oracle-file enumeration behavior.
- Implementing or testing target repository root discovery from the current working directory.
- Working on behavior that depends on cmoc changing its current directory to `<repo-root>` before execution.
- Implementing or testing `.cmoc` directory creation, gitignore handling, or log isolation in target repositories.
- Clarifying what assumptions cmoc may make about repositories it operates on.
- Implementing or testing timestamp generation or parsing for cmoc artifacts.

## Do not read this when

- You only need detailed behavior for a specific cmoc subcommand covered by another app_specs file.
- You are looking for development rules, coding conventions, design rules, or local development environment setup.
- You need cmoc implementation source code rather than canonical specification fragments.
- You need test code organization or test implementation details.
- You are investigating README-facing documentation wording rather than canonical runtime behavior.

## hash

- 8c01e5cb96806de404ea5df9c4fc4fbcef81b6f90cb257ddf666f0c558fa6b73

# `sub_commands`

## Summary

- `cmoc` のサブコマンド仕様断片を集約するディレクトリ。
- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc merge`、`cmoc eval-oracles` の各仕様ファイルへのルーティング情報を扱う。
- 各サブコマンドの概要、読むべき状況、読まないべき状況を把握し、必要な個別仕様ファイルへ誘導するためのメタデータ。

## Read this when

- `cmoc` のサブコマンド仕様のうち、どの個別ファイルを読むべきか判断したいとき。
- `init`、`branch`、`apply`、`merge`、`eval-oracles` のいずれかの実装・修正・テストに着手する前に、関連する正本仕様断片を探すとき。
- サブコマンドごとの責務、引数、事前条件、実行手順、レポート出力、終了コード、git 操作、Codex CLI 連携などの仕様所在を確認したいとき。
- `<repo-root>` に対して cmoc が実行するアプリケーション動作の仕様を調べており、対象がサブコマンド単位であるとき。

## Do not read this when

- cmoc 自体の開発ルール、コーディング規約、設計ルール、開発環境を調べているとき。
- サブコマンドではない cmoc のアプリケーション仕様、ワークフロー仕様、その他の misc 仕様を調べているとき。
- `<cmoc-root>` の README、AGENTS、oracles の編集可否など、リポジトリ運用ルールだけを確認したいとき。
- 特定サブコマンドの詳細仕様ファイルが既に分かっており、このディレクトリ全体のルーティング情報が不要なとき。

## hash

- 100a6c8ec64ce3bbb99921506bc330ff386e62e343dd252574f5ebd92153e730

# `usage.md`

## Summary

- cmoc の利用者向け起動方法と、初回セットアップから branch/apply/merge までの想定利用フローを定義する仕様。
- PATH に <cmoc-root>/bin を追加して cmoc コマンドを呼び出すこと、初回に cmoc init を実行することを述べる。
- 開発対象リポジトリ側の <repo-root>/oracles を修正し、eval-oracles と apply を繰り返してから merge する人間主導ワークフローを述べる。

## Read this when

- cmoc のエンドユーザー向け利用手順、初期化手順、全体ワークフローを確認したいとき。
- cmoc init、branch、eval-oracles、apply、merge の呼び出し順序や役割を実装・テスト・文書化するとき。
- cmoc 自体の <cmoc-root> と、cmoc で作業する対象リポジトリの <repo-root> の関係を利用フロー上で確認したいとき。

## Do not read this when

- 個別サブコマンドの詳細な引数、入出力、内部処理仕様だけを調べたいとき。
- cmoc の開発ルール、コーディング規約、設計方針、テスト方針を調べたいとき。
- 実装ファイルやテストファイルの配置、具体的なコード構造、ライブラリ選定を調べたいとき。

## hash

- 8df46802f7432949a4f4f4ebbdd433a6ba5fc63f3297f68839ee53d338110391
