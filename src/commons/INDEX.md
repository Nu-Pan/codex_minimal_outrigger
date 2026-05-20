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

- Codex CLI 呼び出しの共通処理を提供するモジュール。
- `run_codex_exec` は `codex exec` のコマンド構築、実行前の INDEX 保守、ログ保存、Structured Output schema ファイル作成、stdout 進捗表示、JSON/text 検証、最大 3 回のリトライ、quota 枯渇時の待機と resume、失敗時の `CmocError` 生成をまとめて扱う。
- `parse_json_object` は Codex CLI の最終応答文字列を JSON object として読み、object 以外なら `CmocError` にする。
- model と reasoning effort の既定値、禁止 reasoning effort、quota 疎通確認用の軽量 model/effort、quota poll 間隔を定義する。
- `_build_codex_command`、`_run_codex_command`、`_read_last_message`、`_append_codex_log`、`_write_output_schema` など、Codex CLI 実行とログ・成果物管理の内部ヘルパーを含む。
- quota 枯渇判定、session id 抽出、`--resume` 付きコマンド生成、低コスト疎通確認後の再開処理を含む。
- cmoc 側で使う JSON Schema subset の再検証として、object/array/string/integer/boolean/null、required、properties、additionalProperties、items を検査する内部実装を含む。

## Read this when

- cmoc から Codex CLI を呼び出す共通経路、`codex exec` の引数、sandbox、model、reasoning effort、`--json`、`--output-last-message` の扱いを確認したいとき。
- Codex CLI 実行前に INDEX 保守が走る条件や、`skip_index_maintenance` の意味を調べたいとき。
- Codex CLI 呼び出しログ、last message ファイル、Structured Output schema ファイルが `.cmoc/logs/codex_exec` 配下へどのように保存されるか確認したいとき。
- Codex CLI の JSON 応答、Structured Output、text validator、json validator、リトライ回数、検証失敗時の診断情報を調べたいとき。
- quota 枯渇らしい失敗を検出して待機し、session id を抽出して `codex exec --resume` で再開する処理を調べたいとき。
- Codex CLI の model/reasoning effort 制約、特に high/xhigh 禁止や low/medium のみ許可する実装を確認したいとき。
- cmoc 内部の簡易 JSON Schema 検証がどの keyword と型をサポートしているか確認したいとき。
- Codex CLI の最終応答を dict として扱うための `parse_json_object` のエラー処理を確認したいとき。

## Do not read this when

- 個別サブコマンドの業務ロジックやユーザー向けワークフローだけを調べたいとき。
- Codex CLI 呼び出しではなく、通常のファイル列挙、git 操作、設定ファイル読み書きなどの共通処理を探しているとき。
- INDEX 生成・保守そのものの実装詳細を調べたいとき。ただし Codex 実行直前に INDEX 保守を呼ぶ接点だけ知りたい場合は読む。
- `CmocError` のクラス定義やエラー表示形式そのものを調べたいとき。
- タイムスタンプ文字列の生成仕様そのものを調べたいとき。
- テストコード、Fake Codex CLI、またはテスト用 fixture の実装だけを確認したいとき。
- Codex CLI や JSON Schema の一般仕様を調べたいだけで、cmoc 固有の呼び出し・検証・ログ保存の実装が不要なとき。

## hash

- a467f4d5b4dfc2effbe04da36cc1ccb562ff76a59b9a7eb7df9496c9fabaa948

# `command_runner.py`

## Summary

- CLI サブコマンドの Typer 関数から呼び出される共通実行ラッパーを定義するファイルです。
- `run_command(handler)` が `<repo-root>` の解決とカレントディレクトリ移動を `enter_repo_root()` に委ね、解決後の `Path` をサブコマンド本体の `handler` に渡します。
- `handler` が整数を返した場合はその値を終了コードとして `typer.Exit` を送出します。
- `typer.Exit` はそのまま再送出し、それ以外の例外は `format_error_report()` で表示してから、例外の `exit_code` 属性または既定値 `1` を使って `typer.Exit` に変換します。

## Read this when

- サブコマンドの Typer エントリーポイントを薄く保ち、共通の実行制御をどこに委譲しているか確認したいとき。
- 各サブコマンド本体が `<repo-root>` の `Path` をどのように受け取るか調べたいとき。
- 例外発生時の共通エラー表示、終了コード決定、`typer.Exit` への変換処理を確認したいとき。
- `enter_repo_root()` や `format_error_report()` とサブコマンド実行フローの接続箇所を探しているとき。

## Do not read this when

- 個別サブコマンドの具体的な処理内容やオプション定義を調べたいとき。
- `<repo-root>` の探索ロジック自体や `.cmoc` の扱いを詳しく確認したいとき。
- エラーメッセージの整形内容や例外クラスの定義を詳しく確認したいとき。
- Codex CLI 呼び出し、プロンプト生成、oracle 評価、INDEX.md 生成などの実処理を調べたいとき。

## hash

- ef44b0b6b838c51a601783bd80e15d97049be1e17cd4771609ed747e30a45b6d

# `errors.py`

## Summary

- cmoc 全体で使う共通エラー型とエラーレポート整形処理を定義するモジュール。
- `CmocError` は利用者に提示するメッセージ、複数の次アクション、詳細、終了コードを保持する実行時エラーで、次アクションは最低 2 件を必須にしている。
- `format_error_report` は任意の例外を stdout 向けの共通エラーレポート文字列へ変換し、`ERROR`、`Summary`、`Next actions`、`Detail`、`Call stack` の形式で出力内容を組み立てる。
- `CmocError` の場合は保持済みの利用者向け情報を使い、それ以外の例外では汎用的な確認・再実行アクションと例外クラス名・例外文字列を使う。

## Read this when

- cmoc の共通エラーハンドリング、エラー表示、例外から stdout レポートへの変換を実装または修正するとき。
- サブコマンドや共通処理から利用者向けの復旧アクション付きエラーを投げたいとき。
- `CmocError` に渡す `message`、`actions`、`detail`、`exit_code` の意味や制約を確認したいとき。
- 仕様で要求される `ERROR` レポートの見出し構成、次アクション一覧、詳細、コールスタック出力の組み立て方を確認したいとき。
- 通常の Python 例外が cmoc の共通エラーレポート上でどのように扱われるか確認したいとき。

## Do not read this when

- 個別サブコマンドの業務ロジック、引数解析、git 操作、Codex CLI 呼び出し処理を調べたいとき。
- エラー表示ではなく、ログ保存、リトライ、Structured Output、サンドボックス指定などの Codex 連携仕様を調べたいとき。
- テスト用ヘルパー、Fake Codex CLI、pytest 設定など、テスト実装の詳細だけを確認したいとき。
- cmoc のユーザー向けワークフローや `<repo-root>` 側に配置される `INDEX.md` の生成仕様を調べたいとき。
- 例外クラスやエラーレポート形式ではなく、ファイルシステム探索、oracle 読み込み、タイムスタンプ生成などの補助処理を探しているとき。

## hash

- 08942dd418269062be5b2ed6bad95b8f070d9a37fbc0c65ea870a33fd66a06f4

# `indexing.py`

## Summary

- `INDEX.md` の自動メンテナンス処理を実装するモジュールです。
- リポジトリ配下の配置対象ディレクトリを列挙し、直下項目ごとの目次ブロックを生成・再利用・更新します。
- `INDEX.md` 生成用の Structured Output schema、Codex CLI へのプロンプト生成、JSON payload 検証を定義します。
- 目次対象から除外するディレクトリ名、ドット始まり項目、`memo`、gitignore 対象、バイナリらしいファイルの判定を扱います。
- ファイル内容またはディレクトリ直下項目の hash から更新要否を判定し、必要に応じて `INDEX.md` を書き換え、自動コミット対象パスをまとめます。
- 既存 `INDEX.md` ブロックのパース、hash 抽出、固定フォーマット検証、Markdown bullet への変換を行う補助関数群を含みます。

## Read this when

- `maintain_indexes` による `INDEX.md` の作成・更新・自動コミット条件を確認したいとき。
- `INDEX.md` 配置対象ディレクトリや目次作成対象項目の除外規則を実装・修正したいとき。
- `memo`、ドット始まり項目、`build`、`tmp`、`__pycache__`、gitignore 対象、バイナリ判定の扱いを調べたいとき。
- 目次情報生成時に Codex CLI へ渡すプロンプト、read-only 実行、Structured Output schema、JSON 検証の流れを確認したいとき。
- 既存 `INDEX.md` の目次ブロックを hash とフォーマットに基づいて再利用する条件を調べたいとき。
- `INDEX.md` の Markdown ブロック形式、`Summary`、`Read this when`、`Do not read this when`、`hash` セクションの生成規則を確認したいとき。
- INDEX メンテナンス処理が `.gitignore` の `.cmoc` ignore 保証や `commit_if_changed` とどう連携するか確認したいとき。

## Do not read this when

- 個別サブコマンドの CLI 仕様やユーザー向け挙動だけを調べたいとき。
- Codex CLI 実行ラッパーそのもの、JSON パースの詳細、リポジトリ共通処理の実装を調べたいとき。
- `INDEX.md` のルーティング文書としての内容を読みたいだけで、自動生成・更新ロジックに関心がないとき。
- cmoc の全体ワークフロー、oracle 評価、branch、apply、merge などの仕様を調べたいとき。
- Python パッケージ構成、CLI エントリーポイント、テスト規約など、INDEX メンテナンス以外の開発ルールを探しているとき。
- 特定ファイルの内容 hash を確認・再計算したいだけのとき。

## hash

- 65d87fde3b9ccbf060cd681882097d7555d2bbdc3fdfd66b85494fb73143b30f

# `repo.py`

## Summary

- `src/commons/repo.py` は、git リポジトリ検出、カレントブランチ・HEAD 取得、cmoc ブランチ名判定、未コミット差分検査、`.cmoc` の git 追跡対象外保証を扱う共通モジュールです。
- `cmoc init` や pathspec commit 用に、既存 staged 差分を分離しながら初期化差分・指定パス差分だけを commit し、index を復元する処理を提供します。
- oracle ファイル、実装ファイル、変更済み oracle、変更済み実装ファイルを仕様上の除外規則と root `.gitignore` に従って列挙し、削除有無の判定も行います。
- `.cmoc/branch/<branch>.txt` に保存された cmoc ブランチ作成元 commit の読み取り、未コミットパス一覧の抽出、git name-status 出力の path 変換など、サブコマンド横断の補助処理を含みます。
- git コマンド実行は `run_git` に集約され、失敗時に `CmocError` へ変換する箇所では利用者向けの復旧ヒントと詳細情報を付けます。

## Read this when

- `<repo-root>` の探索や `os.chdir` による repo root への移動処理を確認・修正したいとき。
- 現在ブランチ、HEAD commit、`cmoc_<timestamp>` 形式のブランチ名判定、cmoc ブランチの base commit 記録ファイルを扱う処理を調べたいとき。
- `.cmoc` を root `.gitignore` に追加し、tracked な `.cmoc` を index から外し、追跡対象外保証を検証する挙動を確認したいとき。
- 未コミット差分の有無、未コミット差分が oracle 配下だけか、特定 pathspec が clean かを判定する共通チェックを使う・直すとき。
- `cmoc init` の初期化差分 commit や、指定パスだけを commit する処理で、既存 staged 差分を混ぜずに一時 index を使う仕組みを理解したいとき。
- oracle ファイル列挙、実装ファイル列挙、変更済みファイル列挙、削除ファイル検出の対象・除外条件を確認したいとき。
- `oracles/`、`.git/`、`INDEX.md`、root `.gitignore` 対象ファイルが列挙から除外されるかを調べたいとき。
- git の `status`、`diff`、`log --name-status`、`check-ignore`、`commit-tree`、`update-ref` などの呼び出しラッパーやエラー処理を確認したいとき。

## Do not read this when

- CLI 引数定義、サブコマンドの argparse 構成、エントリーポイントだけを調べたいとき。
- Codex CLI 呼び出し、プロンプト生成、Structured Output、ログ保存、リトライなど LLM 連携仕様を調べたいとき。
- `comconfig.json` や `CMOConfig` の読み書き、設定値補完、設定プロパティの詳細だけを確認したいとき。
- oracle 目次 `INDEX.md` の本文フォーマット、Codex への目次生成依頼、内容ハッシュ管理だけを調べたいとき。
- 個別サブコマンドの利用者向け標準出力、進捗表示、終了時レポート、コマンド全体のワークフローだけを確認したいとき。
- git 以外のファイル入出力ユーティリティ、時刻生成、一般的な文字列処理など、このモジュールにない共通処理を探しているとき。

## hash

- b075d68d5381adb8b7ae342b2127cb443b03391aedc4cb7a289f2a4fce70dfad

# `timestamps.py`

## Summary

- cmoc 仕様で使う `<time-stamp>` 文字列を生成する共通モジュールです。
- `make_timestamp(now: datetime | None = None) -> str` は、指定された `datetime` または現在のローカル時刻からタイムスタンプを作ります。
- 出力形式は `YYYY-MM-DD_HH-MM_SS_mmm` で、年月日時分秒をゼロ埋めし、ミリ秒は `microsecond // 1000` により 3 桁で表現します。

## Read this when

- cmoc のログ名、ファイル名、ディレクトリ名などに使うタイムスタンプ文字列の生成処理を確認したいとき。
- `<time-stamp>` の実装上のフォーマット、ゼロ埋め、ミリ秒の扱いを確認したいとき。
- テストで固定時刻を渡してタイムスタンプ生成を検証したいとき。
- 現在ローカル時刻を使う場合と、呼び出し側が `datetime` を明示する場合の挙動を確認したいとき。

## Do not read this when

- cmoc のサブコマンド別のタイムスタンプ利用箇所や保存先仕様を調べたいとき。
- タイムゾーン変換、UTC 固定、日時パースなど、タイムスタンプ生成以外の日時処理を探しているとき。
- `INDEX.md` 自動メンテナンスや内容ハッシュ計算の実装を調べたいとき。
- コンソール出力、Codex CLI 呼び出し、エラー処理などの共通実行制御を確認したいとき。

## hash

- 19f63db93ff1ae561f750e9a5b22b1d9869679523ef84672607bdf96fda0491b

# `timing.py`

## Summary

- サブコマンドのステップ時間計測を提供する共通モジュール。
- `StepTimer` はサブコマンド全体の開始時刻、実行中ステップ、確定済みステップ別 duration を保持し、`start()` で直前ステップを確定して新ステップを開始する。
- `StepTimer.report()` は未確定ステップを確定したうえで、ステップ別経過時間とサブコマンド全体の経過時間を stdout に出力する。
- `StepTimer.finish_current()` は実行中ステップがある場合だけ duration を保存して状態をクリアし、実行中ステップが無い場合は何もしない。
- `format_duration()` は秒数を 0.1 秒単位に切り捨て、負値を 0 として扱い、` 0h  0m  0.0s` 形式の経過時間文字列へ変換する。

## Read this when

- サブコマンド処理のステップ別タイミング表示や総経過時間表示を実装・修正するとき。
- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` などから共通の時間計測器を使う方法を確認したいとき。
- ステップ開始時に直前ステップを自動的に確定する挙動、または最後のステップを report 時に確定する挙動を確認したいとき。
- 経過時間の表示フォーマット、0.1 秒単位への切り捨て、負値の扱いを確認したいとき。
- タイミングレポートの stdout 出力行や `command_name` の使われ方を確認したいとき。

## Do not read this when

- タイマーを使う側の各サブコマンド固有の処理順序や業務ロジックを調べたいとき。
- Codex CLI 呼び出し、Structured Output、ログ保存、リトライなどの実行時仕様全体を調べたいとき。
- oracle ファイル列挙、repo-root 探索、INDEX.md 生成など、時間計測以外の共通処理を調べたいとき。
- pytest や Fake Codex CLI など、テスト基盤の規約だけを確認したいとき。
- Python の一般的な時間計測 API や `perf_counter` の詳細仕様を調べたいだけのとき。

## hash

- 37186b8a149f9438526632ae6e3619364cfc49e91b6157a8b55db52ff3af8126
