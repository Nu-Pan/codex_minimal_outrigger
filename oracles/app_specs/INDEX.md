# `codex_call.md`

## Summary

- `codex_call.md` は、cmoc から Codex CLI を `codex exec` で呼び出す際の実行規約、プロンプト構成、Structured Output、ログ保存、失敗時の扱い、使用言語を定義する仕様断片です。
- Codex CLI 呼び出しでは、必要に応じてサンドボックスモードを読み取り専用にし、`.agents` 配下を直接編集できない制約をプロンプトで緩和する方針を説明しています。
- Codex CLI に渡すプロンプトは、エージェントのロール、作業概要、完了条件、任意の詳細作業内容で構成し、`<cmoc-root>` や `<repo-root>` のような cmoc 固有の抽象表記ではなく具体的なパスを埋め込むことを求めています。
- Structured Output を要求する場合は `codex exec --output-schema <schema.json>` を使い、cmoc 側でも機械的検証を行うこと、また意味的な失敗は最大 3 回リトライすることを定めています。
- `codex exec` のフルログ保存先や、想定外エラー時に即時失敗させる方針、Codex CLI が扱う自然言語部分を原則日本語にする方針も含みます。

## Read this when

- cmoc から Codex CLI を起動する処理や `codex exec` の引数組み立てを実装・変更するとき。
- Codex CLI に渡すプロンプトの構成、禁止表現、具体パスの埋め込み、ファイルシステムアクセス制限指示を確認したいとき。
- 読み取り専用実行や書き込み可能実行で、プロンプトに含めるべき編集禁止・読み書き禁止ルールを判断するとき。
- Structured Output を Codex CLI に要求する実装で、`--output-schema` の使用、cmoc 側検証、パース失敗時のリトライ方針を確認するとき。
- `codex exec` のフルログ保存先や、Codex CLI 呼び出し失敗時のコマンド全体の扱いを確認するとき。
- Codex CLI に渡す入力プロンプト、作業レポート、評価レポート、エラー説明、INDEX.md 目次情報などの自然言語の使用言語を確認するとき。

## Do not read this when

- cmoc のサブコマンドごとのユーザー向け仕様やワークフローだけを調べたいとき。
- Codex CLI 呼び出しと関係しないコンソール出力、共通エラーハンドリング、実行時間表示、終了ステータスだけを確認したいとき。
- cmoc 自体の Python コーディング規約、テスト規約、開発環境、実装ファイル配置を調べたいとき。
- `<cmoc-root>/README.md`、`AGENTS.md`、`oracles`、`memo` などのリポジトリ運用上の編集可否だけを確認したいとき。
- 対象が Codex CLI 連携ではなく、oracle ファイルの列挙、`.cmoc` ディレクトリ管理、タイムスタンプ、INDEX.md 自動更新の詳細仕様に限られるとき。

## hash

- dd8a1da333895c51bfe2808eb00e76afbb28f83ebfafaca44f94bffa5d0bc9fd

# `console_output.md`

## Summary

- cmoc の各サブコマンドが標準出力へ流す進捗表示の仕様を定義する文書。
- 全サブコマンド共通で必ず出力するステップ名・ステップ数、入れ子ループの表示、`codex exec` 呼び出し時のプロンプト先頭 80 文字と回収出力先頭 80 文字、完了時の時間レポートを扱う。
- 標準出力に表示する経過時間のフォーマットとして、時・分・秒の桁幅、スペースパディング、小数 1 桁表示と切り捨て規則を定める。

## Read this when

- サブコマンド実行中に stdout へ表示する進捗メッセージの内容や粒度を実装・確認するとき。
- ステップ名、ステップ数、入れ子ループの進捗表示をどのように出すべきか確認したいとき。
- `codex exec` 呼び出し時に、渡したプロンプトや回収した出力をどの範囲までコンソール表示するか調べたいとき。
- サブコマンド完了時に、ステップ別経過時間と全体経過時間を標準出力へ出す処理を実装・検証するとき。
- 経過時間表示を `<hour>h <minute>m <sec>.<msec>s` 形式で整形する際の桁幅、スペースパディング、小数桁の扱いを確認するとき。

## Do not read this when

- 詳細ログの保存先、ログファイル形式、永続化ルールなど、標準出力ではないログ仕様だけを調べたいとき。
- 特定サブコマンドの処理手順、入力、成果物、終了条件など、コンソール表示以外の個別仕様を確認したいとき。
- 共通エラーハンドリング、例外時の stderr 表示、終了ステータスなど、エラー報告仕様だけを調べたいとき。
- Codex CLI 呼び出しの引数、サンドボックス、Structured Output、リトライなど、実行制御の詳細仕様を調べたいとき。
- cmoc 自体の Python 実装規約、テスト規約、ファイル配置など、開発者向けルールだけを確認したいとき。

## hash

- 6b4f937d8b273ed346e887253cec0852ef1adef17a9e3bd8857ab74a00481fad

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

- cmoc が `<repo-root>` 配下に自動配置・自動メンテナンスする `INDEX.md` の仕様を定めるファイル。
- `INDEX.md` の配置対象ディレクトリ、目次作成対象ファイル・ディレクトリ、除外対象、フォーマットを説明している。
- 目次情報の生成を Codex CLI に依頼する手順、Structured Output schema、ハッシュの責任分担、深い階層から処理するメンテナンス順序を定めている。
- Codex CLI 実行前に `INDEX.md` メンテナンスを行うタイミングと、目次生成・merge コンフリクト解決時の例外を説明している。

## Read this when

- `<repo-root>` 配下の `INDEX.md` をどのディレクトリに配置するか実装・確認するとき。
- `INDEX.md` の目次対象から `.gitignore` 対象、ドット始まり、`memo`、`INDEX.md` 自身、バイナリファイルなどを除外する規則を確認したいとき。
- `INDEX.md` の目次情報に含める Summary、Read this when、Do not read this when、hash の形式を実装・検証するとき。
- `INDEX.md` メンテナンス処理で新規作成、欠落目次の追加、存在しない対象の削除、ハッシュ不一致時の再生成、自動コミットを扱うとき。
- Codex CLI に目次情報生成を依頼する Structured Output の schema や、ファイル名・ハッシュなどを cmoc 側で扱う責務分担を確認するとき。
- Codex CLI 実行前に `INDEX.md` メンテナンスを走らせるべきか、または例外として除外すべきか判断するとき。

## Do not read this when

- cmoc 自体の Python コーディング規約、CLI 実装配置、テスト規約など開発者向けルールだけを確認したいとき。
- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc merge`、`cmoc eval-oracles` の個別コマンド挙動だけを調べたいとき。
- Codex CLI の一般的な呼び出し方法、サンドボックス指定、プロンプト生成、ログ保存など、`INDEX.md` メンテナンス以外の連携仕様を調べたいとき。
- `<cmoc-root>` 側の `oracles/INDEX.md` ルーティング運用や AGENTS.md のファイルアクセス禁止規則だけを確認したいとき。
- 対象が `<repo-root>` の自動生成 `INDEX.md` ではなく、通常のアプリケーション機能やユーザー向け出力仕様に限られるとき。

## hash

- 15984367fe9fbecd03996ac286f423461d24ce983143582a1b47f2b96f462ee1

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

- `oracles/app_specs/sub_commands/init.md`、`branch.md`、`apply.md`、`eval_oracles.md`、`merge.md` に分かれた cmoc サブコマンド個別仕様へのルーティング文書です。
- `cmoc init` は `<repo-root>` を cmoc 作業可能な状態に初期化し、`<repo-root>/.cmoc` を git 追跡対象外にする具体的な操作と完了判定を扱います。
- `cmoc branch` は cmoc 作業用ブランチ `<cmoc-branch>` の作成、`cmoc_<time-stamp>` 形式の命名規則、作成元コミットの記録、`.cmoc` の git 追跡対象外保証を扱います。
- `cmoc apply` は `<repo-root>/oracles` の正本仕様断片と実装の明確な不整合を Codex CLI で調査・修正する反復ループ、`--repeat` / `-r`、収束・未収束・エラーの区分、作業レポート作成を扱います。
- `cmoc eval-oracles` は現在の `<repo-root>/oracles` スナップショットを部分評価または全体評価し、致命的な問題の有無を人間向けレポートとして保存・提示する仕様を扱います。
- `cmoc merge` は `<cmoc-branch>` を現在の `HEAD` にマージし、省略可能なマージ元ブランチ指定、自動解決、Codex CLI によるコンフリクト解決支援、merge commit 作成、ブランチ削除条件を扱います。

## Read this when

- cmoc のサブコマンド別仕様のうち、どのファイルを読むべきか判断したいとき。
- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` の引数、事前条件、実行手順、終了時の扱いを調べたいとき。
- `<repo-root>/.cmoc` を git 追跡対象外にする処理が各サブコマンドでどのように関わるか確認したいとき。
- `<cmoc-branch>` の作成、作成元コミット記録、作業用ブランチ上での apply、最終的な merge までのサブコマンド単位の流れを追いたいとき。
- Codex CLI を使った不整合調査・修正、oracle 評価、マージコンフリクト解決支援など、サブコマンド固有の Codex 連携仕様を確認したいとき。
- `apply` の収束・未収束レポート、`eval-oracles` の評価レポート、`merge` の失敗時通知など、個別コマンドのレポート・出力・結果区分を実装またはテストしたいとき。
- `cmoc apply` の不整合調査用 Structured Output schema や、`cmoc eval-oracles` の部分評価・全体評価の選択条件など、特定サブコマンドに閉じた詳細仕様を探したいとき。

## Do not read this when

- Codex CLI 呼び出し、プロンプト構成、サンドボックス指定、Structured Output、ログ保存、リトライなど、サブコマンド横断の共通仕様だけを調べたいとき。
- stdout 進捗表示、共通エラーハンドリング、終了ステータス方針、タイムスタンプ生成、`<repo-root>` 発見、oracle ファイル列挙などの共通処理だけを確認したいとき。
- `INDEX.md` 自動メンテナンスの対象、除外規則、目次生成用 Structured Output、更新タイミングなどを調べたいとき。
- cmoc 自体の Python コーディング規約、CLI 構成、共通処理配置、テスト規約、開発環境など、開発者向けルールだけを調べたいとき。
- README、AGENTS、oracles、memo の編集可否や、`<cmoc-root>` 側のリポジトリ運用ルールだけを確認したいとき。
- git や Codex CLI の一般的な使い方だけを調べており、cmoc の各サブコマンド固有仕様が不要なとき。

## hash

- 5e90c50ead69ee471083bb8d8d1328a857a129b41e90b46b2f821f5f91f9d8ce

# `usage.md`

## Summary

- cmoc のエンドユーザー向け利用手順を説明する仕様断片。
- `cmoc` コマンドの呼び出し前提として、`<cmoc-root>/bin` を `PATH` に追加することを示す。
- 初回セットアップとして人間が `cmoc init` を一度実行する流れを定義する。
- 通常利用の想定ワークフローとして、分岐元ブランチでの `cmoc branch`、`<repo-root>/oracles` の記述・評価、`cmoc apply` による実装反映、マージ先ブランチでの `cmoc merge` までの全体手順をまとめる。
- `<repo-root>/oracles` の修正ループでは、`cmoc eval-oracles` による評価レポート確認と、人間による仕様修正を繰り返すことを示す。

## Read this when

- cmoc をエンドユーザーがどの順番で実行するか確認したいとき。
- `cmoc init`、`cmoc branch`、`cmoc eval-oracles`、`cmoc apply`、`cmoc merge` を使った全体ワークフローを把握したいとき。
- cmoc コマンドを呼び出すために `<cmoc-root>/bin` を `PATH` に追加する前提を確認したいとき。
- `<repo-root>/oracles` を人間が更新し、評価レポートを読みながら仕様を改善する利用フローを確認したいとき。
- cmoc による実装作業を開始してから、最終的にマージ先ブランチへ反映するまでの利用者視点の手順を調べたいとき。

## Do not read this when

- 各サブコマンドの詳細な引数、入出力、エラー処理、内部処理を調べたいとき。
- cmoc 自体の実装方針、Python コーディング規約、テスト規約、開発環境ルールを確認したいとき。
- Codex CLI 呼び出し、Structured Output、サンドボックス、ログ保存などの詳細仕様を調べたいとき。
- `INDEX.md` 自動生成・更新や oracle ファイル列挙など、cmoc の内部的な共通処理仕様を調べたいとき。
- 既に特定のサブコマンド仕様ファイルを読むべきことが分かっており、利用者向けの全体手順が不要なとき。

## hash

- 8b06fc15b6b50983c7695a9aa351c4bbf8df7b262059233fe5f2bc941612e17f
