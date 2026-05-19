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

- Codex CLI 呼び出しに関する共通処理を提供するモジュールです。
- `run_codex_exec` により `codex exec` を実行し、read-only / workspace-write の sandbox 指定、Structured Output schema の指定、実行直前の INDEX 保守、標準出力の進捗表示、`.cmoc/logs/codex_exec` へのフルログ保存をまとめて扱います。
- Structured Output が必要な呼び出しでは、JSON parse、cmoc 側の JSON Schema subset 検査、任意の意味検査 validator を行い、失敗時は最大 3 回までリトライします。
- Codex CLI の失敗や JSON 検証失敗を `CmocError` として、ログパス、stderr、最後の stdout、schema パスなどの診断情報付きで報告します。
- `parse_json_object` は Codex CLI の応答文字列を JSON object として読み、object 以外の場合は `CmocError` に変換します。
- 内部ヘルパーとして、出力 schema ファイルの保存、Codex 実行ログの追記、JSON Schema subset の再帰検証、JSON Schema type 判定、stdout 表示用の 80 文字短縮処理を含みます。

## Read this when

- cmoc から `codex exec` を呼び出す共通経路を実装・修正したいとき。
- Codex CLI 呼び出し時の sandbox 指定、cwd、prompt 引き渡し、stdout / stderr の扱いを確認したいとき。
- Structured Output 用の JSON schema をどこに保存し、`--output-schema` にどう渡すかを調べたいとき。
- Codex CLI の JSON 応答を cmoc 側で parse・schema 検証・意味検査・リトライする流れを確認したいとき。
- `codex exec` 実行ログが `.cmoc/logs/codex_exec` 配下にどの形式で保存されるかを確認したいとき。
- `codex exec` 直前に `maintain_indexes` が呼ばれる条件や、`skip_index_maintenance` の用途を調べたいとき。
- Codex CLI 失敗時や Structured Output 検証失敗時の `CmocError` メッセージ、修正ヒント、詳細診断の内容を確認したいとき。
- Codex CLI の応答を dict として扱うための `parse_json_object` の挙動を確認したいとき。
- cmoc が対応している JSON Schema subset の `type`、`required`、`properties`、`additionalProperties`、`items` の検証範囲を調べたいとき。

## Do not read this when

- 個別サブコマンドのプロンプト内容や業務ロジックだけを調べたいとき。
- INDEX 生成・保守そのもののファイル列挙、除外規則、目次更新ロジックを詳しく調べたいとき。
- Codex CLI を使わない通常のファイル操作、git 操作、パス探索、タイムスタンプ生成だけを確認したいとき。
- `.cmoc` ディレクトリ全体の仕様や git 追跡対象外保証を調べたいとき。
- cmoc の CLI 引数定義、サブコマンド登録、エントリーポイントの構成を調べたいとき。
- テスト用 Fake Codex CLI の実装やテスト fixtures の詳細を調べたいとき。
- JSON Schema の完全な仕様や外部ライブラリによる汎用 schema 検証を調べたいとき。
- Codex CLI 自体のインストール方法、認証方法、一般的な使い方だけを確認したいとき。

## hash

- f1cd1ba9ba47409f280781903248f88be8ff681cc69c785b36e8ab7ddcbfba7f

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

- `src/commons/errors.py` は、cmoc 全体で使う実行時エラー型と、仕様で要求される stdout 向けエラーレポート整形処理を定義する共通エラーモジュールです。
- `CmocError` はユーザーに提示する要約メッセージ、次に取るべき操作の配列、詳細文、終了コードを保持する cmoc 固有の例外型です。
- `format_error_report` は `CmocError` の場合は保持された `actions`、`detail`、`message` を使い、それ以外の例外では汎用の復旧操作、例外文字列、例外クラス名を使って、`ERROR`、`Summary`、`Next actions`、`Detail`、`Call stack` からなるエラーレポート文字列を生成します。

## Read this when

- cmoc 全体で捕捉・表示する共通エラー形式を確認したいとき。
- ユーザーに次の操作を提示する cmoc 固有エラーを追加または送出したいとき。
- 例外から stdout 向けのエラーレポートを作る処理、特に `Summary`、`Next actions`、`Detail`、`Call stack` の構成を確認したいとき。

## Do not read this when

- 個別サブコマンドの引数解析、実行順序、正常系の出力仕様を調べたいとき。
- エラーをどこで捕捉して終了コードへ反映するかなど、CLI エントリーポイント側の制御フローを調べたいとき。
- 外部コマンド実行、git 操作、ファイル探索など、エラー発生元となる個別処理の実装を調べたいとき。

## hash

- 08b0686d128c1b8f2a51f93cb0e274aa9b2d34a26b2b4ccea425e88ad291b46d

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

- `src/commons/repo.py` は、cmoc が対象リポジトリを扱うための共通処理をまとめるモジュールです。
- リポジトリルートの探索と cwd 移動、現在ブランチ名・HEAD commit hash の取得、cmoc ブランチ名形式の判定を提供します。
- `.cmoc` を git 追跡対象外に保つため、root `.gitignore` への `/.cmoc/` 追加、既存 index からの除外、保証状態の検証を行います。
- 未コミット差分の有無確認、差分パス一覧の取得、差分が存在する場合のエラー化、oracles 配下だけの差分であることの検証、指定 pathspec の clean 検証を扱います。
- 指定パスに差分がある場合だけ git add と commit を行う `commit_if_changed` を提供し、`.cmoc` は新規 add 対象から除外します。
- `oracles` 配下の評価対象ファイル列挙、base commit 以降に変更された oracle ファイル列挙、削除済み oracle ファイルの有無判定を扱い、`INDEX.md` と root `.gitignore` 対象は除外します。
- cmoc branch の作成元 commit を `.cmoc/branch/<branch>.txt` から読み、対応する記録ファイルパスを組み立てます。
- git コマンド実行を `run_git` に集約し、repo root 固定の cwd、stdout/stderr capture、check オプションを統一します。
- root `.gitignore` の評価は一時 git リポジトリ上で `git check-ignore --no-index --stdin` を使って行い、必要に応じて単一パス判定や簡易 fallback 判定も提供します。

## Read this when

- cmoc の各サブコマンドから git リポジトリルートを見つけたり、処理前に cwd を `<repo-root>` へ固定したりする処理を確認したいとき。
- 現在ブランチ名、HEAD commit hash、`cmoc_<time-stamp>` 形式のブランチ名判定など、git ブランチ・commit に関する共通処理を使うとき。
- `.cmoc` ディレクトリを git 管理対象から外す保証、root `.gitignore` への `/.cmoc/` 追加、tracked な `.cmoc` の index 除外を実装・確認したいとき。
- コマンド実行前に未コミット差分がないこと、または未コミット差分が `oracles/` 配下だけであることを検証したいとき。
- `cmoc init` などで、指定 pathspec に既存の未コミット差分が混入していないことを確認したいとき。
- 対象パスに差分がある場合だけ git add と commit を作成する共通処理を確認したいとき。
- oracle 評価対象ファイルの列挙、部分評価対象となる変更済み oracle ファイルの列挙、oracle ファイル削除による評価モード切替条件を調べたいとき。
- `INDEX.md` や root `.gitignore` 対象を oracle 評価対象から除外するロジックを確認したいとき。
- cmoc branch の base commit 記録ファイル `.cmoc/branch/<branch>.txt` の読み書きパスや、記録がない場合のエラー内容を確認したいとき。
- git コマンド呼び出しの共通ラッパー、`git status --porcelain` の解釈、rename 行から新しい path だけを取り出す処理を確認したいとき。
- root `.gitignore` の pattern を Git の wildmatch semantics に近い形で評価する処理や、その失敗時のエラー処理を調べたいとき。

## Do not read this when

- cmoc の CLI 引数定義、サブコマンド登録、標準出力メッセージなど、ユーザー向けインターフェースだけを調べたいとき。
- Codex CLI の起動方法、プロンプト構築、Structured Output、ログ保存、リトライなど、Codex 連携の詳細だけを確認したいとき。
- oracle ファイルの内容評価、LLM 実行、評価結果の解釈など、oracle 評価そのもののロジックを調べたいとき。
- `README.md`、`AGENTS.md`、`oracles`、`memo` の編集可否など、リポジトリ運用ルールだけを確認したいとき。
- Python の一般的なコーディング規約、テスト規約、依存管理、開発環境など、cmoc 開発者向けルールだけを調べたいとき。
- `.cmoc` 配下に保存されるログ、実行結果、評価結果などのデータ構造そのものを調べたいとき。
- 特定サブコマンドの業務フローや仕様上の完了条件だけを知りたいとき。
- git の一般的な使い方や `gitignore` の一般仕様を知りたいだけで、cmoc の共通実装に関心がないとき。

## hash

- f2674774ece9cbb033bc716e9c67c827c5f665a0d1b5b52dbdf5ed973ae2279e

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

- `src/commons/timing.py` は、cmoc のサブコマンド実行中におけるステップ別・全体の経過時間計測を提供する共通モジュールです。
- `format_duration(duration_seconds)` は秒数を oracle 指定の `h m s` 形式へ丸め下げで整形し、負値は 0 として扱います。
- `StepTimer` はサブコマンド名、開始時刻、現在実行中ステップ、確定済みステップ時間を保持し、ステップ開始・終了・レポート出力を管理します。
- `StepTimer.start()` は直前ステップを確定してから新しいステップの計測を開始し、`finish_current()` は実行中ステップがない場合にも安全に何もしない冪等な終了処理です。
- `StepTimer.report()` は未確定ステップを確定したうえで、ステップ別時間とサブコマンド全体の経過時間を stdout に出力します。

## Read this when

- サブコマンドのステップ別経過時間や全体経過時間の表示処理を実装・修正したいとき。
- 経過時間を ` 0h  0m  0.0s` のような固定幅表示へ変換するロジックを確認したいとき。
- `StepTimer` の `start()`、`finish_current()`、`report()` の呼び出し順序や副作用を調べたいとき。
- 未終了のステップがレポート時にどう確定されるか、またステップ未実行時の終了処理がどう振る舞うかを確認したいとき。
- サブコマンド共通の stdout 時間レポート形式を使う処理やテストを書くとき。

## Do not read this when

- cmoc の個別サブコマンド仕様、引数解析、git 操作、Codex CLI 呼び出し処理を調べたいとき。
- `<repo-root>` 探索、oracle ファイル列挙、INDEX.md 生成など、時間計測以外の共通処理を確認したいとき。
- ログファイル保存、Structured Output、リトライ、サンドボックス指定など Codex 連携仕様を調べたいとき。
- テスト用 Fake Codex CLI や pytest の設定など、テスト基盤そのものを確認したいとき。
- 単に Python の `time.perf_counter` や時間フォーマットの一般的な使い方を知りたいだけのとき。

## hash

- 70ff60f908de4563216267bd427cda2ed8d216a5d4eeb235b920b161a53a54cc
