# `commons`

## Summary

- `src/commons` は、cmoc のサブコマンドから横断利用される共通処理モジュール群をまとめたディレクトリです。
- Codex CLI 呼び出し、Structured Output 検証、INDEX.md 自動メンテナンス、git リポジトリ操作、`.cmoc` ignore 保証、oracle・実装ファイル列挙、共通エラー表示、Typer 実行ラッパー、タイムスタンプ生成、ステップ時間計測を扱います。
- `codex.py` は `codex exec` 実行、ログ保存、リトライ、quota 枯渇時の resume、JSON Schema subset 検証を担当します。
- `indexing.py` は `INDEX.md` 配置対象の列挙、除外判定、内容ハッシュ比較、Codex による目次生成、INDEX メンテナンス差分の自動コミットを担当します。
- `repo.py` は `<repo-root>` 探索、git コマンド実行、ブランチ・HEAD・差分取得、`.cmoc` の追跡除外、oracle・実装ファイルの列挙と変更検出を担当します。
- `errors.py`、`command_runner.py`、`timestamps.py`、`timing.py` は、それぞれ共通エラー整形、CLI サブコマンド実行制御、`<time-stamp>` 生成、ステップ別経過時間表示を担当します。
- `__init__.py` は `src.commons` を Python パッケージとして宣言するだけで、実行時ロジックや公開 API 定義は持ちません。

## Read this when

- cmoc の複数サブコマンドで共有される実装部品の所在を判断したいとき。
- Codex CLI 呼び出し、ログ保存、Structured Output、JSON 検証、リトライ、quota resume の共通実装を探しているとき。
- `INDEX.md` の自動生成・更新、目次対象の除外規則、内容ハッシュ、Codex への目次生成依頼の実装を調べたいとき。
- `<repo-root>` の発見、カレントディレクトリ移動、git ブランチ・HEAD・差分・未コミット状態の取得処理を確認したいとき。
- `.cmoc` を git 追跡対象外に保つ処理、`.gitignore` 更新、tracked `.cmoc` の index 除去、初期化時 commit の分離処理を調べたいとき。
- oracle ファイルや実装ファイルの列挙、変更済みファイルや削除済みファイルの検出、部分評価・部分適用の対象判定を確認したいとき。
- サブコマンドの Typer エントリーポイントから共通エラー表示や終了コード変換へつながる実行フローを確認したいとき。
- `CmocError`、共通エラーレポート、次アクション表示、詳細情報、コールスタック出力の形式を調べたいとき。
- ログ名やブランチ名などで使う cmoc タイムスタンプ文字列、またはサブコマンドのステップ別タイミング表示を確認したいとき。

## Do not read this when

- 個別サブコマンドのユーザー向け仕様、CLI オプション、プロンプト本文、業務ロジックだけを調べたいとき。
- cmoc の正本仕様断片そのものを確認したいとき。仕様へのルーティングは `oracles` 配下の `INDEX.md` を読むべきです。
- cmoc 自体の開発規約、テスト規約、Python コーディング規約、依存管理や開発環境ルールだけを確認したいとき。
- README、AGENTS、memo、oracles の編集可否やアクセス制約など、リポジトリ運用ルールだけを調べたいとき。
- テストコード、pytest fixture、Fake Codex CLI、テストデータの構成だけを確認したいとき。
- Codex CLI や OpenAI モデルの一般的な使い方を調べたいだけで、cmoc 内部の共通ラッパー実装が不要なとき。
- 特定の `INDEX.md` 目次本文を読むだけで、生成・更新ロジックや共通処理の所在を知る必要がないとき。
- Python 標準ライブラリ、Typer、git、日時処理などの一般仕様を確認したいだけで、cmoc 固有の共通実装に関心がないとき。

## hash

- 62d718fdf683bbd923b144f1b4280e3c8c1d75708df036ed75095104705a2c91

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

- `src/sub_commands` は、cmoc の各サブコマンド本体処理を実装するパッケージです。
- `init.py` は `cmoc init` の処理を担当し、`.cmoc` を git 追跡対象外にする保証、初期化差分のコミット、2 段階の進捗表示、`StepTimer` による時間レポートを扱います。
- `branch.py` は `cmoc branch` の処理を担当し、`cmoc_<timestamp>` 形式の作業用ブランチ作成、作成元 commit の `.cmoc/branch` 記録、`.cmoc` ignore 保証、ブランチ名衝突時のリトライを扱います。
- `apply.py` は `cmoc apply` の処理を担当し、cmoc ブランチ検証、oracle 差分コミット、`INDEX.md` メンテナンス、oracle と実装の不整合調査、Codex CLI による実装追従、禁止パス変更検査、変更コミット、apply レポート生成を扱います。
- `eval_oracles.py` は `cmoc eval-oracles` の処理を担当し、`.cmoc` ignore 保証、`INDEX.md` メンテナンス、評価対象 oracle の選定、Codex CLI による oracle 評価、Markdown レポート保存を扱います。
- `merge.py` は `cmoc merge` の処理を担当し、未コミット差分検証、マージ元 cmoc ブランチ解決、`git merge` 実行、conflict marker 解消の Codex CLI 依頼、merge commit 作成、作業ブランチ削除を扱います。
- `__init__.py` はサブコマンド実装パッケージであることを示す最小限のパッケージ初期化ファイルです。

## Read this when

- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` のいずれかの本体実装を調べたいとき。
- 各サブコマンドが共通 runner、repo 操作、Codex CLI 呼び出し、`INDEX.md` メンテナンス、`StepTimer` をどの順序で呼ぶか確認したいとき。
- サブコマンドごとの stdout 進捗表示、ステップ数、完了時レポート、エラー条件を実装側から確認したいとき。
- `.cmoc` ignore 保証、cmoc 作業ブランチ、base commit、oracle 差分、実装差分、merge conflict などが各サブコマンド内でどう扱われるか調べたいとき。
- Codex CLI に渡す apply 不整合調査、実装追従、oracle 評価、merge conflict 解消、commit message 生成、レポート生成の prompt を確認したいとき。
- apply や eval-oracles の部分実行と全体実行の切り替え条件、対象 oracle・実装ファイルの選定条件を確認したいとき。
- サブコマンド単位のテストを書くために、直接呼び出し可能な `cmoc_*_impl` 関数や補助関数の責務を把握したいとき。

## Do not read this when

- CLI エントリーポイントで argparse サブコマンドがどう登録されるかだけを調べたいとき。
- repo root 探索、git コマンド実行、`.cmoc` パス管理、timestamp 生成、共通エラー整形、時間計測などの共通ユーティリティ実装そのものを調べたいとき。
- `INDEX.md` 自動メンテナンス機構の対象ディレクトリ、除外規則、生成フォーマット、ハッシュ判定などの共通ロジックだけを詳しく調べたいとき。
- cmoc の正本仕様断片、ユーザー向け仕様、ワークフロー説明を確認したいだけで、実装コードの流れを追う必要がないとき。
- pytest、Fake Codex CLI、fixture、テストデータなど、自動テスト側の構造を調べたいとき。
- README、AGENTS、oracles、memo などの編集可否やリポジトリ運用ルールだけを確認したいとき。
- cmoc を使って開発する `<repo-root>` 側の oracle や実装ファイルの内容を調べたいとき。

## hash

- 3e1d0c9c43a81a1db3177accbc9e20c46504f4e08c8d72e906552c768683788b
