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
- `run_codex_exec` で `codex exec` を起動し、必要に応じて INDEX 保守、Structured Output schema の保存、stdout 進捗表示、`.cmoc/logs/codex_exec` へのフルログ保存、最終メッセージ読み取り、JSON またはテキスト検証、最大 3 回のリトライを行う。
- Codex CLI の model と reasoning effort を検査し、既定値、INDEX 生成用モデル、quota 疎通確認用モデルなどの定数を定義する。
- quota 枯渇らしい非 0 終了を検出した場合、session id を抽出して `--resume` 付きコマンドを組み立て、低コストの疎通確認を定期実行して quota 復活後に元セッションを再開する。
- `parse_json_object` で Codex CLI 応答を JSON object として読み、object 以外は `CmocError` に変換する。
- Codex CLI コマンド構築、1 回分の起動、`--output-last-message` ファイル読み取り、ログ追記、Structured Output schema ファイル書き出しを小さな内部関数に分けている。
- cmoc が利用する JSON Schema subset の再検証を実装し、object の required、properties、additionalProperties、array の items、基本 type を再帰的に検査する。
- ユーザー向け stdout 進捗表示用に prompt/output の先頭 80 文字を切り詰め、改行をエスケープする補助関数を含む。

## Read this when

- cmoc から Codex CLI を呼び出す共通経路、`codex exec` の引数、sandbox、model、reasoning effort、`--json`、`--output-last-message` の扱いを確認したいとき。
- Codex CLI 実行前に INDEX 保守が走る条件や、`skip_index_maintenance` の意味を調べたいとき。
- Codex CLI 呼び出しログ、schema ファイル、last-message ファイルが `.cmoc/logs/codex_exec` 配下にどのように作られるか確認したいとき。
- Structured Output を使う呼び出しで、schema 指定、JSON parse、cmoc 側 schema subset 検証、追加の validator、リトライ条件を調べたいとき。
- Codex CLI が quota 枯渇で失敗した場合の検出、待機、疎通確認、session resume の流れを実装または修正したいとき。
- Codex CLI の非 0 終了や不正な JSON 応答が、どのような `CmocError` と診断情報に変換されるか確認したいとき。
- Codex CLI 応答を dict として扱うための `parse_json_object` の責務を確認したいとき。
- cmoc 内で使う JSON Schema subset の対応範囲や検証エラーの出し方を確認したいとき。

## Do not read this when

- 個別サブコマンドの業務ロジックや CLI 引数定義だけを調べたいとき。
- リポジトリ探索、oracle ファイル列挙、実装ファイル列挙など、Codex CLI 呼び出し以外の共通処理を調べたいとき。
- INDEX.md の生成対象ディレクトリ探索や目次ファイルの更新処理そのものを調べたいとき。
- タイムスタンプ生成、経過時間表示、例外クラス定義など、別モジュールに分離された小さな共通機能だけを確認したいとき。
- Codex CLI や JSON Schema の一般仕様だけを知りたいとき。
- テストコードの構成、Fake Codex CLI の実装、pytest の使い方を調べたいとき。

## hash

- 478ef94765ad80132f178f8c2bd853b0e3273c5f85ef100511f7ad9ac0ea547b

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

- `INDEX.md` の自動メンテナンス処理を実装する共通モジュール。
- `maintain_indexes` は `<repo-root>` 配下の配置対象ディレクトリへ `INDEX.md` を生成・更新し、必要な差分だけを自動コミットする。
- 配置対象ディレクトリの列挙、除外条件、gitignore 判定、バイナリ判定、既存目次ブロックの再利用、子項目ハッシュに基づく更新判定を担う。
- 目次情報の新規生成時は Codex CLI を Structured Output schema 付きで呼び出し、返却 JSON を検証して固定形式の Markdown ブロックへ変換する。
- `<repo-root>/memo`、隠し項目、gitignore 対象、バイナリらしいファイル、特定の除外ディレクトリを INDEX 対象から外すロジックを含む。

## Read this when

- `cmoc` 実行時に `INDEX.md` がどのディレクトリへ配置され、どの項目が目次生成対象になるかを確認したいとき。
- `maintain_indexes` による `.cmoc` ignore 保証、INDEX 更新、変更パス限定コミットの流れを調べたいとき。
- 既存 `INDEX.md` ブロックがハッシュ一致時に再利用される条件や、固定フォーマット検証の仕様を実装・修正したいとき。
- ファイルやディレクトリの内容ハッシュ計算、ディレクトリハッシュに含める子項目の除外条件を確認したいとき。
- INDEX 生成用 Codex CLI プロンプト、Structured Output schema、JSON 検証、Markdown 変換処理を変更したいとき。
- `memo`、隠しディレクトリ、`build`、`tmp`、`__pycache__`、gitignore 対象、バイナリファイルの扱いを調査したいとき。

## Do not read this when

- 個別サブコマンドの CLI 引数、ユーザー向け出力、終了ステータスなどの仕様だけを調べたいとき。
- Codex CLI 呼び出しの汎用ラッパー、JSON パース、モデル定数そのものの詳細を調べたいとき。
- git コミット処理、`.gitignore` 更新、リポジトリ検出など、INDEX 以外の repo 共通処理だけを確認したいとき。
- 特定の `INDEX.md` 目次本文の内容を読みたいだけで、生成・更新ロジックを調べる必要がないとき。
- cmoc 自体の開発規約、テスト規約、環境構築ルールなど、実装方針の正本仕様を探しているとき。
- README、AGENTS、oracles、memo の編集可否やアクセス制約だけを確認したいとき。

## hash

- 0783b777023b73c54db00dd6b067439f1c31998faa51974bdcbb289bc9bb8ef8

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
