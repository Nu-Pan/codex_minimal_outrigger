# `commons`

## Summary

- `src/commons` は、cmoc のサブコマンド群から共有される Python 共通処理を集約するパッケージです。
- Codex CLI 呼び出し、Structured Output 検証、ログ保存、INDEX.md 自動メンテナンス、共通エラー整形、Typer 実行ラッパー、git リポジトリ操作、タイムスタンプ生成、ステップ時間計測を扱います。
- `codex.py` は `codex exec` 実行、sandbox 指定、schema 保存、JSON parse・検証・リトライ、`.cmoc/logs/codex_exec` へのログ保存を担当します。
- `indexing.py` は `INDEX.md` の配置対象列挙、除外規則、内容ハッシュ、既存目次再利用、Codex CLI による目次生成、Markdown ブロック生成、自動コミットを担当します。
- `repo.py` は `<repo-root>` 探索、cwd 固定、git コマンド実行、`.cmoc` ignore 保証、未コミット差分検査、oracle ファイル列挙、cmoc ブランチ base commit 記録の読み取りを担当します。
- `command_runner.py`、`errors.py`、`timestamps.py`、`timing.py` はそれぞれサブコマンド共通実行制御、cmoc 固有エラーとエラーレポート、仕様タイムスタンプ、経過時間レポートを提供します。
- `__init__.py` は `src.commons` を Python パッケージとして示すだけで、実行時ロジックや公開 API の再エクスポートは持ちません。

## Read this when

- cmoc の複数サブコマンドで共有される実装部品の入口を探しているとき。
- サブコマンドの Typer エントリーポイントから本体処理へ入る共通ラッパー、例外捕捉、終了コード変換の流れを確認したいとき。
- `codex exec` の呼び出し方法、read-only / workspace-write sandbox、Structured Output schema、JSON 検証、リトライ、ログ保存の共通実装を調べたいとき。
- `INDEX.md` の自動生成・更新、対象ディレクトリや除外項目、内容ハッシュ、既存ブロック再利用、Codex CLI への目次生成依頼を確認したいとき。
- `<repo-root>` の探索、カレントディレクトリ変更、git status / diff / add / commit、`.cmoc` の git 追跡対象外保証を実装または修正したいとき。
- oracle 評価対象ファイルや変更済み oracle ファイルの列挙、削除済み oracle の検出、`INDEX.md` や `.gitignore` 対象の除外ロジックを調べたいとき。
- cmoc ブランチ名の形式判定や `.cmoc/branch/<branch>.txt` に保存された base commit の扱いを確認したいとき。
- cmoc 全体で使う `CmocError`、stdout 向けエラーレポート、復旧操作の表示形式を確認したいとき。
- ログ名・ブランチ名などに使う `<time-stamp>` 形式や、サブコマンドのステップ別・全体経過時間レポートを確認したいとき。

## Do not read this when

- 個別サブコマンドのユーザー向け仕様、引数、プロンプト内容、正常系ワークフローだけを調べたいとき。
- cmoc のアプリケーション仕様断片そのものを確認したい場合で、実装ではなく正本仕様を読むべきとき。
- Python コーディング規約、テスト規約、依存管理、開発環境など、開発者向けルールだけを確認したいとき。
- README、AGENTS、oracles、memo の編集可否やリポジトリ運用ルールだけを調べたいとき。
- テストコード、Fake Codex CLI、pytest fixture、テストデータの具体的な構成を調べたいとき。
- Codex CLI や git の一般的な使い方だけを知りたい場合で、cmoc 固有の共通実装に関心がないとき。
- `.cmoc` 配下に保存される個別コマンド結果や評価結果のデータ内容だけを調べたいとき。
- UI、ドキュメント、配布設定、パッケージ設定など、`src/commons` の共通実行ロジック以外の領域を確認したいとき。

## hash

- 27227d7de68a957277faeecb7d695c64c39f8f4c0dbb767faac5f2ea5e3bacc4

# `main.py`

## Summary

- cmoc の Typer ベースの CLI エントリーポイントを定義するファイル。
- `init`、`branch`、`eval-oracles`、`apply`、`merge` の各サブコマンドを登録し、それぞれ対応する `sub_commands` 配下の実装関数へ委譲する。
- `eval-oracles` では `--full` / `-f` オプション、`apply` では `--repeat` / `-r` オプション、`merge` では任意の `cmoc_branch` 引数を受け取る。
- `main()` は Typer/Click の例外や想定外例外を `commons.errors.format_error_report` による共通エラーレポート形式へ変換し、適切な終了コードで終了する。
- スクリプトとして直接実行された場合は `src` ディレクトリを `sys.path` に追加してから `main()` を起動する。

## Read this when

- cmoc CLI のトップレベルコマンド一覧やサブコマンド名を確認したいとき。
- 各 CLI コマンドがどの `sub_commands` 実装関数へ委譲されるか調べたいとき。
- `eval-oracles`、`apply`、`merge` の CLI 引数やオプション定義を確認したいとき。
- Typer/Click の parse error や実行時例外が、cmoc の共通エラーレポートへどう変換されるか確認したいとき。
- `bin/cmoc` などから直接起動される際のエントリーポイント処理を調べたいとき。

## Do not read this when

- 個別サブコマンドの詳細な処理内容や仕様を調べたいとき。
- `init`、`branch`、`eval-oracles`、`apply`、`merge` の内部実装ロジックを修正したいとき。
- 共通エラーレポートの具体的な整形ルールや例外クラス定義を調べたいとき。
- Codex CLI 呼び出し、ログ保存、oracle 評価、ブランチ操作、マージ処理などの実装詳細を確認したいとき。
- テストコード、開発環境、コーディング規約など cmoc 開発ルール全般を調べたいとき。

## hash

- 94aa9dcc576677bc140d61d6c7aaa19ae18ff8b875a40faa38c4d3517611adca

# `sub_commands`

## Summary

- `src/sub_commands` は、cmoc の各 CLI サブコマンド本体を実装する Python パッケージです。
- `init.py`、`branch.py`、`apply.py`、`eval_oracles.py`、`merge.py` に、`cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` の実行フロー、進捗表示、共通ヘルパー呼び出し、レポート保存、git 操作、Codex CLI 呼び出しの接続が分かれて配置されています。
- `apply.py` は oracle と実装の不整合調査、Structured Output schema、Codex CLI による実装修正依頼、禁止パス検査、変更 commit、apply レポート生成を扱います。
- `eval_oracles.py` は oracle 評価対象の選択、部分評価と全体評価の切り替え、Codex CLI による読み取り専用評価、評価レポート生成を扱います。
- `merge.py` は cmoc ブランチの解決、`git merge --no-ff`、conflict 発生時の Codex CLI 依頼、marker 検査、merge commit、作業ブランチ削除を扱います。
- `init.py` と `branch.py` は `.cmoc` の git 追跡対象外保証、初期化 commit、cmoc 作業ブランチ作成、base commit 記録など、cmoc ワークフロー開始時の処理を扱います。
- `__init__.py` はサブコマンド実装パッケージであることを示すだけで、実行ロジックは含みません。

## Read this when

- cmoc の個別サブコマンド本体がどのファイルに実装されているか判断したいとき。
- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` の処理順序、stdout 進捗表示、終了コード、レポート出力、git 操作を確認したいとき。
- サブコマンド実装から `commons.command_runner`、`commons.repo`、`commons.codex`、`commons.indexing`、`commons.timing`、`commons.timestamps` などの共通処理がどう呼ばれているか追いたいとき。
- oracle 不整合調査、Structured Output schema、Codex CLI への prompt、実装修正依頼、禁止パス検査、commit message 生成など `cmoc apply` 固有の制御を調べたいとき。
- oracle 評価の部分評価条件、全体評価へのフォールバック、評価 prompt、`.cmoc/reports/eval-oracles` へのレポート保存形式を確認したいとき。
- cmoc ブランチ作成、base commit 記録、未マージ cmoc ブランチ解決、merge conflict 解消依頼、conflict marker 検査、ブランチ削除の実装を確認したいとき。
- サブコマンドの挙動を変更するために、実装入口となるモジュールを選びたいとき。

## Do not read this when

- argparse へのサブコマンド登録、CLI エントリポイント、トップレベルのコマンド分岐だけを調べたいとき。
- git 実行、repo 探索、`.cmoc` パス生成、Codex CLI 呼び出し、INDEX メンテナンス、timestamp 生成などの共通ヘルパー内部だけを詳しく調べたいとき。
- cmoc の正本仕様断片やユーザー向け仕様だけを確認したいとき。
- pytest、Fake Codex CLI、テストデータ、テスト実装規約など tests 側の構成だけを調べたいとき。
- README、AGENTS、oracles、memo の編集可否やリポジトリ運用ルールだけを確認したいとき。
- `<repo-root>` 側で cmoc を使う開発作業の対象ファイルや、利用者リポジトリ固有の実装内容を調査したいとき。
- 個別サブコマンドではなく、cmoc 全体の設計方針、開発環境、コーディング規約だけを確認したいとき。

## hash

- 39805e011391acc371d557b3d17c5f93123fa07017db7036f9bd0008fd17c5b4
