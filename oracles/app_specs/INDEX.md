# `codex_call.md`

## Summary

- cmoc が外部の Codex CLI を呼び出す際の正本仕様を定める。
- `codex exec` の使用、サンドボックス指定、`.agents` 配下を編集できない制約とその緩和方針を扱う。
- Codex CLI に渡すプロンプトの構成、具体パスの埋め込み、ファイルシステム制約指示、汎用性、自走可能性の要件を定める。
- `codex exec` 呼び出しログの保存先、Structured Output パース失敗時の最大3回リトライ、想定外エラー時の即時失敗を扱う。
- Codex CLI で扱う自然言語部分は原則として日本語にする、という言語規約と例外を定める。

## Read this when

- cmoc から Codex CLI をどのコマンド・引数・サンドボックス設定で実行するか実装または確認するとき。
- `codex exec` に渡すプロンプトの構成、ロール、作業内容、完了条件、詳細指示の書き方を決めるとき。
- `<repo-root>` や `<cmoc-root>` などの抽象表記を Codex CLI プロンプトに含めてよいか判断するとき。
- Codex CLI に渡すプロンプトへ読み書き禁止・編集禁止などのファイルアクセス制約をどう含めるか確認するとき。
- `.agents` 配下が `codex exec` から編集できない制約を前提に、プロンプトや実装方針を決めるとき。
- `codex exec` のフルログ保存先やログ出力実装を確認するとき。
- Structured Output のパース失敗、Codex CLI の想定外エラー、リトライ上限、コマンド全体の失敗条件を実装または確認するとき。
- Codex CLI への入力プロンプト、作業レポート、評価レポート、エラー説明などの自然言語を日本語にすべきか判断するとき。

## Do not read this when

- cmoc の個別サブコマンドである `init`、`branch`、`apply`、`merge`、`eval-oracles` の詳細仕様だけを調べたいとき。
- stdout の進捗表示、共通エラー表示、終了ステータスなど、Codex CLI 呼び出し以外のユーザー可視挙動だけを調べたいとき。
- `INDEX.md` の自動生成・更新、oracle ファイル列挙、`.cmoc` ディレクトリ、タイムスタンプなどの共通アプリケーション仕様だけを調べたいとき。
- cmoc 自体の Python コーディング規約、CLI 構成、テスト規約、開発環境などの開発ルールを調べたいとき。
- Codex CLI や LLM そのものの外部仕様、モデル性能、一般的な使い方を調べたいとき。
- README、AGENTS、memo、oracles などのリポジトリ運用上の編集可否やアクセス制約だけを確認したいとき。

## hash

- 25cb6164140b1c8dd21d68c79b31bdbe8c7b095e50a7def66568177aff84250a

# `console_output.md`

## Summary

- cmoc の各サブコマンドが標準出力へ流す進捗表示の基本方針を定義する。
- 出力は詳細ログではなく、コマンドが動いていることを確認できる程度の簡潔な情報とする。
- ステップ名・ステップ数、codex exec に渡したプロンプトや回収した出力、ステップ別および全体の実行時間レポートを出力例として示す。

## Read this when

- サブコマンド実行中に stdout へ表示する進捗メッセージの粒度や内容を決めるとき。
- cmoc apply などの処理ステップ名、ステップ番号、実行中表示を実装・調整するとき。
- codex exec への入力プロンプトや実行結果から回収した出力を、コンソールへどの程度表示するか確認するとき。
- ステップ別の経過時間やサブコマンド全体の経過時間レポートを実装・確認するとき。

## Do not read this when

- サブコマンドの詳細な処理順序、引数、終了ステータス、エラー条件などを調べたいとき。
- Codex CLI 呼び出しそのものの仕様やプロンプト生成の詳細を調べたいとき。
- 構造化データ、oracle、INDEX.md、.cmoc など、コンソール表示以外の入出力仕様を調べたいとき。
- cmoc 自体の開発ルール、テスト規約、コード配置規約を確認したいとき。

## hash

- 4107a532f0a23299cb9c9733f55ee05fb43608415b1140fa226cd524c3123d8d

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
