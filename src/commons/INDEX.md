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

- `INDEX.md` の自動メンテナンス処理を実装するモジュールです。
- 配置対象ディレクトリの列挙、既存目次ブロックの再利用、直下項目のハッシュ計算、Codex CLI Structured Output による目次情報生成、Markdown 形式への変換を扱います。
- `.cmoc` の ignore 保証、gitignore 対象や `memo`・隠し項目・バイナリらしきファイルの除外、深い階層から親へ向かう更新順序、自動コミット対象の限定を担います。
- INDEX 生成用 JSON schema と payload 検証、既存 `INDEX.md` ブロックの hash・固定フォーマット検証、箇条書き出力などの補助関数を含みます。

## Read this when

- `maintain_indexes` による `INDEX.md` 自動生成・更新の全体フローを確認したいとき。
- どのディレクトリやファイルが `INDEX.md` 配置対象・目次対象から除外されるかを調べたいとき。
- `memo`、隠しファイル、`build`、`tmp`、`__pycache__`、gitignore 対象、バイナリらしきファイルの扱いを確認したいとき。
- INDEX 生成時に Codex CLI へ渡すプロンプト、Structured Output schema、JSON 検証、hash を返させない方針を調べたいとき。
- 既存 `INDEX.md` の目次ブロックをいつ再利用し、いつ再生成するかの判定条件を確認したいとき。
- 直下項目の hash 計算、ディレクトリ hash の子 hash 連結、親目次へ最新の子目次状態を反映する更新順序を理解したいとき。
- INDEX メンテナンス結果を `.gitignore` や `.cmoc` とともに自動コミットする条件を確認したいとき。

## Do not read this when

- cmoc の個別サブコマンドのユーザー向け仕様や実行ワークフローだけを調べたいとき。
- Codex CLI 呼び出しの低レベル実装、JSON 抽出、コマンド実行共通処理そのものを調べたいとき。
- リポジトリ探索、`.cmoc` ignore 保証、コミット処理の詳細実装だけを確認したいとき。
- `INDEX.md` の出力内容を編集したいが、自動メンテナンスの実装ロジックには関心がないとき。
- Python の一般的なファイル I/O、正規表現、hashlib、subprocess の使い方だけを知りたいとき。
- テストコードの構成や Fake Codex CLI の実装方針を調べたいとき。

## hash

- 2ec828f5a583d8de4a4e1224328cd97ce28b558cc5e86cb32cb234ed2c1e2554

# `repo.py`

## Summary

- git リポジトリと cmoc 作業ディレクトリに関する共通処理をまとめたモジュール。
- リポジトリルート探索と cwd 移動、現在ブランチ名・HEAD commit hash の取得、cmoc ブランチ名形式の判定を提供する。
- `.cmoc` を git 追跡対象外にするため、root `.gitignore` への `/.cmoc/` 追加、既存 tracked `.cmoc` の index 解除、保証状態の検証を行う。
- 未コミット差分の有無や対象パスの clean 検査、oracles 配下だけに差分が限定されているかの検査など、サブコマンド実行前の git 状態検証を扱う。
- `cmoc init` が発生させた `.gitignore` と `.cmoc` 関連の差分だけを安全に stage・commit する補助処理を含む。
- 指定 pathspec に差分がある場合だけ add・commit する汎用 commit 補助処理を提供する。
- oracle ファイルの全列挙、base commit からの変更 oracle ファイル列挙、oracle ファイル削除有無の判定を行い、`INDEX.md` と root `.gitignore` 対象は除外する。
- cmoc ブランチの作成元 commit 記録ファイルの読み取りと、その `.cmoc/branch/<branch>.txt` パス生成を扱う。
- git status porcelain から変更パスを抽出し、rename 行では新しい path だけを返す。
- root `.gitignore` だけを Git の ignore semantics で評価するため、一時 git repository を使った ignore 判定を実装している。
- すべての git 実行は `run_git()` に集約され、repo root を cwd として stdout/stderr を捕捉する。

## Read this when

- cmoc のサブコマンド実装で `<repo-root>` を探索し、処理中の cwd を git リポジトリルートへ固定したいとき。
- 現在の git ブランチ名、HEAD commit hash、cmoc ブランチ名形式の判定が必要なとき。
- `.cmoc` ディレクトリを root `.gitignore` と git index の両面から追跡対象外に保証する処理を確認・修正したいとき。
- 実行前に未コミット差分がないこと、または未コミット差分が oracles 配下だけであることを検査する処理を探しているとき。
- `cmoc init` の初期化差分を、既存ユーザー差分と混ぜずに commit する実装を確認したいとき。
- 指定パスに差分がある場合だけ commit を作る共通処理を使いたいとき。
- `oracles` 配下の評価対象ファイルを列挙し、`INDEX.md` や root `.gitignore` 対象を除外するロジックを調べたいとき。
- 部分 oracle 評価のため、base commit 以降に追加・変更・rename・copy された oracle ファイルや未コミット oracle ファイルを集める処理を確認したいとき。
- oracle ファイル削除がある場合に full 評価へ切り替えるための判定を調べたいとき。
- cmoc ブランチ作成時に保存した base commit の読み取り場所や `.cmoc/branch` 配下のファイル名規則を確認したいとき。
- root `.gitignore` の pattern だけを使って oracle 列挙対象を除外する実装を確認したいとき。
- git コマンド実行の共通ラッパー、エラー時の `CmocError` 化、stdout/stderr の扱いを追いたいとき。

## Do not read this when

- cmoc の CLI 引数定義、サブコマンド登録、エントリーポイントだけを調べたいとき。
- Codex CLI の呼び出し、プロンプト生成、Structured Output、ログ保存、リトライ処理を調べたいとき。
- oracle の本文仕様や `oracles/INDEX.md` などの正本仕様ファイルそのものを読みたいとき。
- `INDEX.md` 目次生成のプロンプト内容や出力 JSON schema の詳細だけを調べたいとき。
- cmoc のエラー表示フォーマットや `CmocError` クラス定義そのものを確認したいとき。
- ファイルコピー、テンプレート生成、時刻フォーマットなど、git リポジトリ状態と直接関係しない共通ユーティリティを探しているとき。
- テストコードの書き方、Fake Codex CLI、pytest fixture など、テスト実装規約だけを確認したいとき。
- README、AGENTS、memo、oracles の編集可否など、リポジトリ運用上のアクセス制約だけを確認したいとき。
- cmoc を用いて開発する `<repo-root>` 側の業務コードや仕様を調べており、cmoc 自体の git 共通処理が不要なとき。

## hash

- 2b9c0428634571cfc028293de22a18f2fba3dec9d1012166f1e1cddc0e4ac7f3

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
