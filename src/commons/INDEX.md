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

- `codex exec` 呼び出しの共通処理を定義するファイルです。
- 実行前の `INDEX.md` 保守、サンドボックス指定、Structured Output 用 schema ファイル生成、`.cmoc/logs/codex_exec` へのフルログ保存、stdout 進捗表示、JSON 応答のリトライと検証をまとめています。
- `run_codex_exec` は Codex CLI 実行の入口で、通常出力または schema 検証済み JSON 文字列を返し、Codex CLI 失敗や JSON 検証失敗時は `CmocError` を送出します。
- `parse_json_object` は Codex CLI の JSON 応答が object であることを保証して辞書として返します。
- 内部 helper として、Codex 実行ログ追記、Structured Output schema 保存、cmoc が使う JSON Schema subset の再帰検証、JSON Schema type 判定、prompt/stdout の先頭 80 文字切り詰めを実装しています。

## Read this when

- cmoc から `codex exec` を呼び出す処理、引数構築、作業ディレクトリ、サンドボックス指定を確認したいとき。
- Codex CLI 呼び出し前に `INDEX.md` 保守がいつ実行され、どの条件でスキップされるかを調べたいとき。
- Structured Output を使う呼び出しで、schema ファイルの保存場所、`--output-schema` 指定、最大 3 回の JSON リトライ、検証順序を確認したいとき。
- Codex CLI の stdout 進捗表示と `.cmoc/logs/codex_exec` 配下のフルログ保存内容を実装または確認したいとき。
- Codex CLI の失敗、JSON parse 失敗、schema 不一致、意味検査失敗がどのように `CmocError` や `ValueError` へ変換されるかを確認したいとき。
- cmoc 内部で対応している JSON Schema subset、`required`、`properties`、`additionalProperties`、`items`、`type` の検証挙動を確認したいとき。
- Codex CLI の JSON 応答を dict として扱う前に `parse_json_object` の保証内容を確認したいとき。

## Do not read this when

- 個別サブコマンドの CLI 仕様、引数、利用者向けワークフローだけを調べたいとき。
- `INDEX.md` の目次生成対象、除外規則、フォーマット、処理順序など、インデックス保守そのものの詳細を調べたいとき。
- タイムスタンプ生成の形式や実装だけを確認したいとき。
- cmoc の共通エラー型やエラーメッセージ表示の実装だけを確認したいとき。
- Codex CLI を使わない処理、git 操作、ファイルコピー、oracle 評価、merge conflict 解消などの実装を調べたいとき。
- 外部の JSON Schema ライブラリ互換性や JSON Schema 全仕様への対応状況を調べたいとき。

## hash

- ffba4a682429b2c6954b1dd42078c883c976fbbee26479e204bfee8e508e5650

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

- `INDEX.md` の自動メンテナンス処理を実装する共通モジュールです。
- 配置対象ディレクトリの列挙、除外条件の適用、既存目次ブロックの再利用、内容ハッシュ比較、必要時の `INDEX.md` 書き込みを扱います。
- Codex CLI に Structured Output schema 付きで目次生成を依頼し、返却 JSON を検証して Markdown の目次ブロックへ変換します。
- `.cmoc` の gitignore 保証、INDEX 更新差分だけを対象にした自動コミット、gitignore 判定、バイナリ判定、`memo` 除外などの補助処理を含みます。
- ハッシュ欄、見出し、Summary、Read this when、Do not read this when の固定フォーマット検証と既存 `INDEX.md` の項目単位パースを行います。

## Read this when

- `INDEX.md` の生成・更新・自動コミットの流れを確認したいとき。
- どのディレクトリに `INDEX.md` を配置し、どの名前やパスを除外するかを調べたいとき。
- 既存の目次情報をハッシュ一致時に再利用する条件や、再生成される条件を確認したいとき。
- Codex CLI に目次情報生成を依頼するプロンプト、Structured Output schema、JSON 検証処理を変更したいとき。
- `memo`、ドットパス、`build`、`tmp`、`__pycache__`、gitignore 対象、バイナリファイルの扱いを確認したいとき。
- `INDEX.md` の Markdown ブロック形式、hash セクション、既存エントリのパースやフォーマット検証に関わる不具合を調査するとき。

## Do not read this when

- 個別サブコマンドの CLI 仕様やユーザー向け挙動だけを調べたいとき。
- Codex CLI 実行ラッパーそのもの、JSON パースの低レベル実装、リトライやログ保存の詳細だけを確認したいとき。
- リポジトリ探索、`.cmoc` の ignore 保証、コミット処理などの共通 git/repo 操作の本体実装だけを読みたいとき。
- 生成された `INDEX.md` の内容そのものを確認したいだけで、生成ロジックが不要なとき。
- cmoc のテスト規約、開発環境、Python コーディング規約など、開発者向けルールだけを調べたいとき。

## hash

- 911fa78749629cf1ca97f70502bca882cdf6c53952df7a7ebfa62f175f4d60cb

# `repo.py`

## Summary

- `src/commons/repo.py` は、cmoc が対象リポジトリを扱うための共通処理をまとめたモジュールです。
- リポジトリルート探索と cwd 移動、現在ブランチ・HEAD commit 取得、cmoc ブランチ名判定、git コマンド実行ラッパーを提供します。
- `.cmoc` を git 追跡対象外に保つため、`.gitignore` への `/.cmoc/` 追加、既存 index からの `.cmoc` 除去、保証状態の検証を行います。
- 未コミット差分の検査、指定パスの clean 確認、oracles 配下だけの差分確認、変更パス抽出など、サブコマンド実行前の作業ツリー検証を扱います。
- `cmoc init` 用に、初期化差分だけを一時 index で commit し、既存の staged 差分を復元する処理を含みます。
- oracle ファイルの全列挙、base commit 以降に変更された oracle ファイルの列挙、oracle ファイル削除有無の判定を行い、`INDEX.md` と root `.gitignore` 対象を除外します。
- cmoc ブランチの作成元 commit 記録ファイル `.cmoc/branch/<branch>.txt` のパス生成と読み取りを提供します。
- root `.gitignore` だけを Git の ignore semantics で評価するため、一時 git repository を作って `git check-ignore --no-index --stdin` を実行する補助処理を持ちます。

## Read this when

- cmoc の各サブコマンドから共通利用される git 操作、リポジトリルート探索、cwd 固定の実装を確認したいとき。
- `.cmoc` ディレクトリを git 追跡対象外に保証する処理、`.gitignore` 更新、tracked な `.cmoc` の index 除去を調べたいとき。
- 未コミット差分がある場合の検査、oracles 配下だけの差分許可、指定 pathspec の clean 確認など、作業ツリー状態チェックを実装または修正したいとき。
- `cmoc init` が生成した差分だけを commit し、既存 staged 差分を混ぜずに復元する一時 index 処理を理解したいとき。
- oracle ファイルの列挙条件、変更済み oracle ファイルの部分評価対象判定、削除済み oracle ファイルによる評価モード切替を確認したいとき。
- root `.gitignore` のみを基準に oracle ファイルや削除パスを除外する仕様の実装箇所を探しているとき。
- cmoc ブランチ名の形式判定や、cmoc branch 作成元 commit ファイルの保存場所・読み取りを確認したいとき。
- git コマンド失敗時の `CmocError` 変換箇所や、利用者向け復旧ヒント付きエラーを確認したいとき。

## Do not read this when

- 個別サブコマンドの CLI 引数、stdout 表示、処理順序など、ユーザー向け仕様そのものだけを知りたいとき。
- Codex CLI 呼び出し、プロンプト構成、Structured Output、ログ保存、リトライ方針を調べたいとき。
- oracle ファイル本文の評価ロジックや、LLM に渡すプロンプト内容だけを確認したいとき。
- `src/commons/errors.py` など、共通エラー型そのものの定義だけを確認したいとき。
- テストの構成、Fake Codex CLI、pytest の使い方など、テスト実装規約だけを調べたいとき。
- README、AGENTS、oracles、memo の編集可否やリポジトリ運用ルールだけを確認したいとき。
- cmoc を用いて開発される別リポジトリ側の業務ロジックやアプリケーションコードを調べたいとき。

## hash

- c55c1d8beea41b3e56a5dd7b543a907d8ec3daa5730748af183d1e42c8635237

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
