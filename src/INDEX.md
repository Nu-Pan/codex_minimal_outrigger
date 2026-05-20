# `commons`

## Summary

- `src/commons` は、cmoc のサブコマンド横断で使う共通処理を集約する Python パッケージです。
- Codex CLI 呼び出し、Structured Output 検証、ログ保存、リトライ、quota 待機・resume、`INDEX.md` 自動メンテナンスなど、LLM 連携と目次保守の中核処理を含みます。
- git リポジトリ探索、repo root への移動、ブランチ・HEAD・未コミット差分確認、`.cmoc` の git 追跡対象外保証、oracle・実装ファイル列挙、指定パスだけの commit など、リポジトリ操作の共通関数を提供します。
- CLI サブコマンド用の共通実行ラッパー、利用者向けエラーレポート、復旧アクション付き `CmocError`、ステップ別時間計測、cmoc 仕様のタイムスタンプ生成を提供します。
- `__init__.py` はパッケージ宣言のみで、実処理は `codex.py`、`indexing.py`、`repo.py`、`errors.py`、`command_runner.py`、`timing.py`、`timestamps.py` に分かれています。

## Read this when

- cmoc の複数サブコマンドで共有される実装がどのモジュールにあるか判断したいとき。
- Codex CLI 呼び出し、`codex exec` の引数構築、sandbox、model、reasoning effort、Structured Output、JSON 検証、ログ保存、リトライ、quota 待機・resume の実装を探しているとき。
- `INDEX.md` の配置対象列挙、除外規則、内容ハッシュ、既存目次ブロック再利用、Codex による目次生成、INDEX 更新の自動 commit 処理を調べたいとき。
- `<repo-root>` の探索、カレントディレクトリ移動、git コマンド実行、現在ブランチ・HEAD 取得、cmoc ブランチ判定、未コミット差分チェック、`.cmoc` ignore 保証を確認したいとき。
- oracle ファイルや実装ファイルの列挙、変更済みファイルや削除ファイルの検出、root `.gitignore` や `oracles/`、`INDEX.md` などの除外条件を確認したいとき。
- サブコマンドの Typer エントリーポイントから共通実行制御へ委譲する流れ、例外を stdout の共通エラーレポートと終了コードへ変換する流れを確認したいとき。
- 利用者向けの `CmocError`、エラーレポートの見出し構成、次アクション、詳細、コールスタック出力の作り方を調べたいとき。
- サブコマンドのステップ別経過時間表示、合計時間表示、`<time-stamp>` 文字列のフォーマットを確認したいとき。

## Do not read this when

- 個別サブコマンドの CLI 引数、業務ロジック、利用者向けワークフロー、標準出力の詳細だけを調べたいとき。
- `comconfig.json` や `CMOConfig` の設定ファイル生成、補完、読み書き、設定値公開の実装だけを探しているとき。
- cmoc 自体の開発規約、設計規約、テスト規約、開発環境など、正本仕様側のルールだけを確認したいとき。
- README、AGENTS、oracles、memo の編集可否やリポジトリ運用ルールだけを確認したいとき。
- pytest、Fake Codex CLI、テストデータ、テストヘルパーなど、自動テスト側の実装だけを調べたいとき。
- Codex CLI や git、JSON Schema、Typer、日時 API の一般的な使い方だけを知りたいとき。
- 特定の `INDEX.md` の目次本文を読むだけで、目次生成・更新ロジックや共通処理の配置を調べる必要がないとき。

## hash

- a54a486a31d19fd3e4ea3eb98313840cf1b3b82718ba48d01c65abe465a0e51f

# `main.py`

## Summary

- cmoc CLI の Typer エントリーポイントを定義するファイル。
- `cmoc` アプリケーション本体を作成し、`init`、`branch`、`eval-oracles`、`apply`、`merge` の各サブコマンド名を CLI に登録する。
- 各 CLI コールバックは引数やオプションを受け取り、実処理を `sub_commands` 配下の対応する `cmoc_*_impl` 関数へ委譲する。
- `eval-oracles` は `--full` / `-f`、`apply` は `--repeat` / `-r` と `--full` / `-f`、`merge` は任意の `cmoc_branch` 引数を定義する。
- `main()` は Typer/Click の起動経路をラップし、parse error や想定外例外を `commons.errors.format_error_report` による共通エラーレポート形式で表示して終了コードを決定する。
- `python src/main.py` による直接実行時も `main()` を呼び出して cmoc CLI を起動する。

## Read this when

- cmoc のトップレベル CLI コマンド一覧やサブコマンド登録箇所を確認したいとき。
- `cmoc init`、`cmoc branch`、`cmoc eval-oracles`、`cmoc apply`、`cmoc merge` がどの実装関数へ委譲されるか調べたいとき。
- サブコマンドの Typer 引数・オプション定義、デフォルト値、短縮オプションを確認したいとき。
- Typer や Click の例外、CLI parse error、想定外例外が cmoc の共通エラーレポートと終了コードへどう変換されるか確認したいとき。
- cmoc の起動入口、`app` オブジェクト、`main()`、直接実行時の挙動を修正または調査したいとき。

## Do not read this when

- 各サブコマンドの具体的な処理内容、git 操作、ファイル生成、Codex CLI 呼び出しなどの本体実装を調べたいとき。
- 共通エラーレポートのフォーマット処理そのものを詳しく確認したいとき。
- cmoc の設定ファイル、oracle 評価、INDEX.md 生成、ログ保存などの詳細仕様や処理フローを調べたいとき。
- Typer ではなく個別モジュール内のビジネスロジックやテスト対象の詳細を確認したいとき。
- cmoc を使う対象リポジトリ側の `<repo-root>` 構造やファイル内容を調査したいとき。

## hash

- d752eef82e7384747c693c0afe234254d441d6ba098d33d86bec3b0c9e31da62

# `sub_commands`

## Summary

- `src/sub_commands` は、cmoc の各 CLI サブコマンド本体を実装するパッケージです。
- `init.py` は `cmoc init` の処理を担当し、`.cmoc` を git 追跡対象外にする保証、初期化差分のコミット、2段階の進捗表示と時間計測を扱います。
- `branch.py` は `cmoc branch` の処理を担当し、`cmoc_<timestamp>` 形式の作業ブランチ作成、作成元 commit の `.cmoc/branch` への記録、`.cmoc` ignore 保証、3段階の進捗表示を扱います。
- `apply.py` は `cmoc apply` の処理を担当し、oracle 変更の確定、`INDEX.md` メンテナンス、oracle と実装の不整合調査、Codex CLI による実装修正、禁止パス検査、コミット、apply レポート生成を反復実行します。
- `eval_oracles.py` は `cmoc eval-oracles` の処理を担当し、`.cmoc` ignore 保証、`INDEX.md` メンテナンス、評価対象 oracle の選定、Codex CLI による oracle 評価、Markdown レポート保存を扱います。
- `merge.py` は `cmoc merge` の処理を担当し、merge 前提条件検証、未マージ cmoc ブランチの解決、git merge、conflict 時の Codex CLI 解消依頼、conflict marker 検査、merge commit、作業ブランチ削除を扱います。
- `__init__.py` はサブコマンド実装パッケージであることを示すだけの初期化ファイルです。

## Read this when

- cmoc の個別サブコマンド本体実装がどのファイルにあるか判断したいとき。
- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` の実行フロー、進捗表示、終了処理、レポート生成などを調べたいとき。
- サブコマンドが共通 runner、repo 操作、Codex CLI 呼び出し、INDEX メンテナンス、時間計測、エラー処理などの共通部品をどの順序で呼び出しているか確認したいとき。
- oracle と実装の不整合調査、実装追従、oracle 評価、merge conflict 解消など、Codex CLI に渡すサブコマンド固有プロンプトや Structured Output schema を確認したいとき。
- cmoc ブランチ、base commit、部分適用と全体適用、削除検出、未収束時終了コード、レポート保存先などのサブコマンド固有ロジックを実装または修正したいとき。
- 各サブコマンドのテストを読む前に、対象となる本体関数や補助関数の配置を把握したいとき。

## Do not read this when

- CLI エントリーポイントでサブコマンドがどう登録されるかだけを調べたいとき。
- repo root 探索、git 実行ラッパー、Codex CLI 実行ラッパー、JSON パース、INDEX.md 自動保守、timestamp 生成、時間計測などの共通処理そのものを詳しく調べたいとき。
- cmoc の正本仕様断片やユーザー向け仕様だけを確認したいとき。
- Python コーディング規約、設計規約、テスト規約、開発環境など、cmoc 自体の開発ルールだけを調べたいとき。
- 自動テスト、Fake Codex CLI、pytest fixture、期待出力など、tests 配下のテスト実装だけを調べたいとき。
- `README.md`、`AGENTS.md`、`oracles`、`memo` などの編集可否やリポジトリ運用ルールだけを確認したいとき。
- cmoc を使って開発する `<repo-root>` 側の oracle や実装ファイルの内容を調べたいとき。

## hash

- 01c0e68cba63ea7bb6ef0804021daf84b2e44a81962f06cd78c80ad78d55f5f5
