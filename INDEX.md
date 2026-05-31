# `AGENTS.md`

## Summary

- `cmoc` リポジトリ全体の作業ルールとルーティング方針をまとめた入口です。
- `cmoc` の開発と `cmoc` を用いた開発を区別し、参照してよい・よくないファイルの扱いを示します。
- `oracles` 配下の `INDEX.md` を起点に必要最小限の仕様断片だけを読むための案内です。
- 実装は `<cmoc-root>/src`、自動テストは `<cmoc-root>/tests` に置く前提を明示します。

## Read this when

- このリポジトリで作業する前に、基本ルールと役割分担を確認したいとき。
- `cmoc` 自体の開発と `cmoc` を使った開発を区別したいとき。
- `memo` や `README.md` などの閲覧・編集制約を確認したいとき。
- `oracles` の正本仕様を読む前に、どの `INDEX.md` を起点にたどるか知りたいとき。
- 実装を `<cmoc-root>/src`、テストを `<cmoc-root>/tests` に置く前提を確認したいとき。

## Do not read this when

- 個別サブコマンドの引数や終了条件だけを確認したいとき。
- `oracles` 配下の特定仕様断片を直接確認したいとき。
- 実装コードやテストコードの内容だけを見たいとき。

## hash

- b2f93d440fb91234a2ff90e3b533ff1ba9230037690851040d4d8e5de5d0bf37

# `LICENSE`

## Summary

- このリポジトリのライセンス本文です。
- 利用、改変、配布の許可条件と、保証および責任の免責を定めています。
- 法的条件の確認が必要なときに参照する入口です。

## Read this when

- このリポジトリに適用されるライセンス条件を確認したいとき。
- 再配布、改変、サブライセンス、免責の扱いを確認したいとき。
- ソフトウェアをコピー・利用・配布する前に、権利と制約を把握したいとき。

## Do not read this when

- このリポジトリの実装方針、CLI 仕様、テスト方針を確認したいとき。
- `cmoc` の使い方や `oracles` のルーティングを調べたいとき。
- ライセンス条文そのものではなく、ファイル構成や開発手順を確認したいとき。

## hash

- a894f2547af0349f234986eb4661f0146f37b7d82f8b22a27a674d5c1236f08f

# `README.md`

## Summary

- このリポジトリの概要、初期セットアップ、基本ワークフロー、作業時の補足事項をまとめた入口です。
- `cmoc` を使い始める前に、何を最初に行うかと、次にどこを読むかを確認するための案内です。

## Read this when

- このリポジトリ全体の概要を短く把握したいとき
- 初期セットアップとして clone、仮想環境作成、`cmoc` への PATH 設定を確認したいとき
- 基本ワークフローの入口として `oracles/app_specs/usage.md` への導線を知りたいとき
- Ctrl+S によるターミナルロックなど、作業時の補足情報を確認したいとき

## Do not read this when

- cmoc の個別サブコマンドの引数や終了条件を確認したいとき
- `oracles` 配下の正本仕様を直接たどって、実装やテストの詳細を確認したいとき
- 実装ルールやテスト規約だけを確認したいとき

## hash

- 4fc977607c700055d3453298512ffdb3a3b257d876f1648f23a1b0dc79781ffc

# `bin`

## Summary

- `bin/cmoc` は cmoc コマンドのシェル製エントリーポイントで、`<cmoc-root>` を解決して `src/main.py` を起動します。
- `<cmoc-root>/.venv/bin/python` を実行 Python として使い、通常は全引数をそのまま `exec` で渡します。
- 仮想環境 Python が使えない場合は、日本語の構造化エラーを標準出力へ出し、セットアップ手順・必要な実行ファイル・簡易 Call stack を案内して終了します。
- `line_number_of` は、エラー表示内の Call stack に必要な行番号を求める補助関数です。

## Read this when

- `bin/cmoc` がどの Python で `src/main.py` を起動するか確認したいとき。
- `.venv/bin/python` が無い、または実行できないときのエラー文面、終了ステータス、復旧手順を確認したいとき。
- シェル製 CLI エントリーポイントとしての引数受け渡しや補完プローブの分岐を把握したいとき。
- エラー表示内の Call stack を組み立てる `line_number_of` の役割を確認したいとき。

## Do not read this when

- `src/main.py` 以降の Python 実装や共通処理の詳細だけを確認したいとき。
- `cmoc` の各サブコマンド本体や引数解析の仕様だけを確認したいとき。
- pytest などのテスト観点やテストケースの整理だけを確認したいとき。
- `oracles` 側の仕様断片や `INDEX.md` の生成ルールだけを確認したいとき。
- 仮想環境の作成手順そのものではなく、依存関係や Python パッケージ構成を確認したいとき。

## hash

- 6b2ad008646b163ca4bd7bd4ced6f60b6cd655c9c1d0e19d068820da0bbab7b2

# `codex_minimal_outrigger_cli.code-workspace`

## Summary

- `codex_minimal_outrigger_cli.code-workspace` は、このリポジトリ全体を単一ワークスペースとして開くための VS Code ワークスペース設定です。
- `folders` ではルート `.` を指し、`settings.files.exclude` で `**/__pycache__` と `**/*.egg-info` を非表示にします。
- このファイルの目次は、エディタ起点でリポジトリを開くときの前提設定を素早く確認するための入口です。

## Read this when

- このリポジトリを VS Code などで 1 つのワークスペースとして開く設定を確認したいとき。
- ワークスペースのルートがどこか、どのファイルが表示除外されるかを把握したいとき。
- 開発用エディタ設定の入口を素早く確認したいとき。

## Do not read this when

- cmoc の実装コードやサブコマンド仕様そのものを確認したいとき。
- `src` や `tests` の個別モジュールの役割を調べたいとき。
- `oracles` 側の正本仕様や `INDEX.md` の生成ルールだけを確認したいとき。

## hash

- 6acff2a397cd0c66553c35c5c3f0f45a551ed34bcae704aa612b4b485cce20d0

# `oracles`

## Summary

- `cmoc` の正本仕様断片をまとめる `oracles` ディレクトリの入口です。
- 配下の `docs` から、開発ルール、アプリ仕様、代替案、各種共通仕様へたどれます。
- このディレクトリ自体はルーティング用で、詳細仕様は下位の文書に分かれています。

## Read this when

- `cmoc` の正本仕様断片がどこにあるか、全体の入口を把握したいとき。
- `oracles` 配下の `docs` 以下へどの順で進むべきかを整理したいとき。
- `oracles` 全体の役割や、仕様断片の配置場所を俯瞰したいとき。

## Do not read this when

- 個別のサブコマンド仕様や設計判断だけを確認したいときは、このディレクトリではなく配下の該当文書を直接読むべきです。
- 実装コードやテストコードの作業だけで足りるときは、この目次を読む必要はありません。
- `oracles` 配下のどの仕様を読むべきか自明な場合は、入口ではなく目的のファイルへ直接進むべきです。

## hash

- fa379c76438c952476ee4ff0ca92f2a3c97fbb392e45c3043f50318524144f11

# `pyproject.toml`

## Summary

- このリポジトリの Python パッケージ定義とビルド設定がまとまっています。
- プロジェクト名、バージョン、対応 Python 版、依存パッケージ、CLI エントリポイント `cmoc` が定義されています。
- `setuptools` を使った `src` レイアウトのパッケージ探索設定が含まれています。

## Read this when

- このプロジェクトの名前、バージョン、説明、Python 要件を確認したいとき。
- 依存パッケージや `cmoc` のコンソールスクリプト定義を確認したいとき。
- ビルド方式や `setuptools` のパッケージ配置設定を確認したいとき。

## Do not read this when

- CLI の個別サブコマンドの実装や引数仕様を確認したいとき。
- テストコードや期待挙動を確認したいとき。
- `src` 配下の実装方針や内部ロジックだけを追いたいとき。

## hash

- c20014553a4e48f3a2f9f5221852179231c76594ccc1bc4c82b8dddc651b203e

# `src`

## Summary

- `src` は cmoc の実装本体を置くディレクトリで、CLI 入口、共通モジュール、サブコマンド実装をまとめる。
- `main.py` は `cmoc` の起動点で、`init` と `session` / `apply` / `review` の各コマンド登録を行う。
- `commons` はエラー整形、repo 操作、Codex 呼び出し、ログ、計測、`INDEX.md` 生成などの共通基盤を担う。
- `sub_commands` は `init`、`session`、`apply`、`review` 系の個別実装への入口をまとめる。

## Read this when

- `cmoc` の CLI 実装全体で、入口・共通基盤・サブコマンド群の配置を把握したいとき。
- `src/main.py` が Typer のルートアプリと `session` / `apply` / `review` をどう束ねているか確認したいとき。
- `src/commons` の共通処理と、`src/sub_commands` の個別実装への導線を整理したいとき。

## Do not read this when

- `oracles` 配下の正本仕様断片だけを確認したいとき。
- 個別サブコマンドの引数や状態遷移だけを確認したいとき。
- `src/commons` や `src/sub_commands` の下位モジュールを直接読む前に、この入口だけで十分なとき。

## hash

- 7403e0e836701e0073031829eca342cac77b855530285f6b5d7e7ada0cb4360a

# `test.sh`

## Summary

- `test.sh` は `<cmoc-root>` を `CMOC_ROOT` として固定し、`.venv/bin` と `bin` を `PATH` の先頭側に通すための環境初期化スニペットです。
- cmoc コマンドや関連ツールを、このリポジトリのローカル環境で実行できる状態にすることが目的です。

## Read this when

- `CMOC_ROOT` を固定し、`PATH` に `.venv/bin` と `bin` を追加する環境設定を確認したいとき。
- cmoc 関連コマンドをこのワークツリーで実行する前の最小セットアップ手順を知りたいとき。
- シェルから cmoc を使うための前提環境を素早く把握したいとき。

## Do not read this when

- `cmoc` の実装本体やサブコマンド仕様を確認したいとき。
- pytest や個別テストケースの内容を確認したいとき。
- `oracles` の正本仕様や `INDEX.md` 生成ルールだけを確認したいとき。

## hash

- 6fc07bc0dff2b064245772154c4f103ce2d3d0cbe7536ae9124eb49e183c6b44

# `tests`

## Summary

- `tests` は cmoc の回帰テスト群を集めたディレクトリです。
- `conftest.py` は pytest の import path を調整して `src` 配下の実装を直接読めるようにします。
- `test_codex.py` は Codex CLI 呼び出し基盤と Structured Output の検証を担います。
- `test_file_naming.py` は旧ルーティングファイルの残存や命名規則を検証します。
- `test_indexing.py` は `INDEX.md` メンテナンス処理の生成・更新・再利用・コミットを検証します。
- `test_repo.py` は repo root 探索、ignore 判定、変更検出、session / apply 状態管理を検証します。
- `test_report_files.py` はタイムスタンプ付きレポートの排他保存と再試行を検証します。
- `test_subcommands.py` は cmoc のサブコマンド群と共通実行基盤の横断回帰を検証します。
- `test_timestamps.py` はタイムスタンプ生成と経過時間表示の仕様を検証します。

## Read this when

- pytest 実行時に `src` 配下の cmoc 実装モジュールを import できる仕組みを確認したいときは `conftest.py` を読むべきです。
- `commons.codex` の `run_codex_exec`、Structured Output、再試行、resume、quota 復旧を確認したいときは `test_codex.py` を読むべきです。
- 旧ルーティングファイル `routing.md` / `ROUTING.md` が残っていないことや、命名規則の回帰を確認したいときは `test_file_naming.py` を読むべきです。
- `INDEX.md` の自動生成、再利用、更新判定、hash、並列化、lock などの保守挙動を確認したいときは `test_indexing.py` を読むべきです。
- `src/commons/repo.py` の repo root 検出、`.cmoc` の ignore 保証、変更検出、session / apply state の扱いを確認したいときは `test_repo.py` を読むべきです。
- タイムスタンプ付きレポートの排他作成、再試行、衝突回避の挙動を確認したいときは `test_report_files.py` を読むべきです。
- `run_command`、`main`、completion、`bin/cmoc`、各サブコマンドの横断的な制御を確認したいときは `test_subcommands.py` を読むべきです。
- `commons.timestamps.make_timestamp` と `commons.timing.format_duration` の出力形式や丸め規則を確認したいときは `test_timestamps.py` を読むべきです。

## Do not read this when

- 個別テストケースの細部や期待値だけを追いたいときは、このディレクトリ全体ではなく該当するテストファイルを読むべきです。
- cmoc の本体実装やサブコマンド仕様を確認したいときは、`tests` ではなく `src` 配下の実装と対応する `oracles` 側を読むべきです。
- `__pycache__` のような生成物やテストの実行結果ファイルを探したいときは、この目次ではなく実ファイル群を直接確認すべきです。
- `INDEX.md` 自体の生成ルールやメンテナンス仕様だけを知りたいときは、このディレクトリの個別テストではなく `oracles/docs/app_specs/indexing.md` を読むべきです。
- pytest の共通設定や import path の制御が不要で、個別モジュールの仕様だけを見たいときは `conftest.py` を優先して読む必要はありません。

## hash

- 24edc29f80387f4252ab203f33c90bdc763aad08d8fd7f53519bdee549ad913b
