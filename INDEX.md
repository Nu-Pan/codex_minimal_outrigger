# `AGENTS.md`

## Summary

- Repository-level agent instructions for Codex Minimal Outrigger CLI, abbreviated cmoc.
- Defines path terminology: <cmoc-root> is this repository root, while <repo-root> is a separate repository where cmoc may be used for development.
- Warns that developing cmoc itself and using cmoc to develop another repository are distinct contexts and must not be confused.
- Specifies AI access restrictions: <cmoc-root>/memo must not be read or edited; README.md, AGENTS.md, and oracles must not be edited.
- Explains that canonical specification fragments live under <cmoc-root>/oracles and implementation should be aligned to them when conflicts arise.
- Requires reading <cmoc-root>/oracles/INDEX.md before starting work and using INDEX.md routing files to read only the minimum necessary oracle files.
- States implementation belongs in <cmoc-root>/src and automated tests belong in <cmoc-root>/tests.

## Read this when

- Starting any work in /home/happy/codex_minimal_outrigger_cli.
- Determining repository-specific AI access, edit, and routing rules.
- Working on cmoc implementation or tests.
- Needing to distinguish cmoc repository development from development performed using the cmoc command in another repository.
- Planning to consult canonical specification fragments under <cmoc-root>/oracles.

## Do not read this when

- You only need details from a specific source or test file and already know the repository-level constraints.
- You are working outside /home/happy/codex_minimal_outrigger_cli and the cmoc repository rules are irrelevant.
- You need canonical behavior details that are only specified in routed files under <cmoc-root>/oracles after AGENTS.md has already directed you there.

## hash

- 5e0ee4b1526db45849e6fb1a85e675b3da90f2113503b1af40e50137c3d2d2bf

# `README.md`

## Summary

- Codex Minimal Outrigger CLI、略称 cmoc のリポジトリ README です。
- AI 向けには詳細な作業ルールを `AGENTS.md` で確認するよう案内しています。
- cmoc は Codex CLI を用いた開発を補助する最小限度の外部ツールであることを説明しています。
- リポジトリの clone、Python 仮想環境作成、編集可能インストール、任意の PATH 設定という初期セットアップ手順を示しています。
- 基本ワークフローの詳細は `<cmoc-root>/oracles/app_specs/usage.md` を参照するよう案内しています。

## Read this when

- cmoc リポジトリの概要を短く把握したいとき。
- cmoc が何をするツールか、正式名称と略称を確認したいとき。
- cmoc の初期セットアップ手順を確認したいとき。
- clone 後に Python 仮想環境を作成し、`pip install -e .` で開発用インストールする手順を知りたいとき。
- `cmoc` コマンドを実行しやすくするために `bin` を PATH に追加する例を確認したいとき。
- cmoc の基本ワークフロー仕様がどの oracle ファイルにあるか知りたいとき。

## Do not read this when

- cmoc 自体の詳細な開発ルール、ファイルアクセス規則、編集禁止ファイル、作業時の注意点を確認したいとき。
- cmoc のサブコマンド仕様、Codex CLI 連携、出力形式、エラー処理などの正本仕様断片を調べたいとき。
- cmoc の Python 実装方針、設計規約、テスト規約、開発環境ルールを詳しく確認したいとき。
- `src` や `tests` 配下の具体的な実装・テスト構造を調べたいとき。
- cmoc を使った対象リポジトリ側の作業手順や、branch、apply、merge、oracle 評価などの詳細ワークフローを確認したいとき。
- README.md を編集する必要があるとき。

## hash

- c9f160c5a2a14b1dece67dd6f263b3b59a8e586f606eeac39d5ac2239a75d3ff

# `ROUTING.md`

## Summary

- リポジトリ直下の主要パスへのルーティング情報を箇条書きでまとめている。
- `<cmoc-root>/bin`、`<cmoc-root>/src`、`<cmoc-root>/oracles/docs` 配下の旧ドキュメント群について、用途や配置先を短く説明している。
- cmoc の公開バイナリ、ソース配置、旧仕様ドキュメントの所在を素早く把握するための入口となる。

## Read this when

- リポジトリ直下で、どのディレクトリや旧ドキュメントを見ればよいか大まかに判断したいとき。
- `bin` や `src` の役割を短く確認したいとき。
- `oracles/docs/app_spec.md`、`code_design.md`、`coding_rule.md`、`development_environment.md` など旧ドキュメント名から目的の文書を探したいとき。
- cmoc の実装ファイルや公開用バイナリの配置先を確認したいとき。

## Do not read this when

- cmoc の正本仕様を調べるために、現在の `oracles/INDEX.md` からルーティングすべきとき。
- サブコマンド仕様、Codex CLI 連携、出力、エラー処理などの詳細なアプリケーション仕様を確認したいとき。
- Python 実装規約、テスト規約、開発環境などの詳細な開発ルールを確認したいとき。
- README、AGENTS、oracles、memo などの編集可否やファイルアクセス制約だけを確認したいとき。

## hash

- 198999eb3bcc5ffd76844a04b55e0ff819f1aadb645b7d54b19c56af6b5a4bb0

# `bin`

## Summary

- Contains the repository-local executable launcher for the cmoc command.
- The `cmoc` Bash script resolves `<cmoc-root>` from its own location and execs `<cmoc-root>/.venv/bin/python` with `<cmoc-root>/src/main.py`, forwarding all CLI arguments.
- `INDEX.md` provides routing metadata for the executable launcher file in this directory.

## Read this when

- You need to understand how invoking `bin/cmoc` starts the Python implementation.
- You are debugging startup failures before `src/main.py` runs, such as incorrect root detection, missing `.venv/bin/python`, executable permissions, or argument forwarding.
- You are changing local command shim behavior, packaging assumptions, or development workflows that rely on the `bin/cmoc` launcher.
- You need routing metadata for files directly under `<cmoc-root>/bin`.

## Do not read this when

- You need the implementation of cmoc subcommands, CLI workflow logic, prompts, or runtime behavior after Python startup; read files under `<cmoc-root>/src` instead.
- You are looking for automated tests; read `<cmoc-root>/tests` instead.
- You need canonical application or development rules; use `<cmoc-root>/oracles/INDEX.md` to route to the relevant specification fragments.
- You are working on README, repository policy, or documentation unrelated to the executable launcher.

## hash

- ca4ac1558575ac1351b53f96c54f72907f00310e5a93d8ba58dd9223eb4a1006

# `codex_minimal_outrigger_cli.code-workspace`

## Summary

- VS Code workspace configuration for opening the cmoc repository root as a single workspace folder.
- Defines editor file exclusion settings for generated Python cache directories and package metadata directories.
- Contains workspace-level settings only; it does not describe cmoc runtime behavior, implementation architecture, or tests.

## Read this when

- You need to understand how the repository is configured when opened as a VS Code workspace.
- You are checking why `__pycache__` directories or `*.egg-info` paths are hidden in the editor file explorer.
- You are updating or auditing workspace-specific VS Code settings for this repository.

## Do not read this when

- You need cmoc application specifications, CLI behavior, subcommand workflows, or oracle routing information.
- You need implementation details from `src` or test details from `tests`.
- You are looking for repository development rules, file access restrictions, or authoritative specification fragments under `oracles`.
- You are not using VS Code workspace metadata or editor-specific configuration.

## hash

- 6acff2a397cd0c66553c35c5c3f0f45a551ed34bcae704aa612b4b485cce20d0

# `oracles`

## Summary

- cmoc の正本仕様断片全体への最上位ルーティング文書です。
- アプリケーション実行時仕様を扱う `app_specs` と、cmoc 自体の開発ルールを扱う `dev_rules` への入口を提供します。
- cmoc のサブコマンド仕様、Codex CLI 連携、コンソール出力、共通エラーハンドリング、`INDEX.md` 自動メンテナンスなどを調べる場合は `app_specs` に進む判断材料になります。
- Python 実装規約、設計規約、テスト規約、開発環境など、cmoc 開発者向けルールを調べる場合は `dev_rules` に進む判断材料になります。

## Read this when

- `oracles` 配下の正本仕様断片を調べ始めるとき。
- cmoc の仕様確認で、まず `app_specs` と `dev_rules` のどちらを読むべきか判断したいとき。
- cmoc のアプリケーション仕様と開発者向けルールを混同せず、読むべき仕様ディレクトリを切り分けたいとき。
- サブコマンドや実行時挙動の仕様を探しているのか、実装・テスト・開発環境のルールを探しているのかを整理したいとき。

## Do not read this when

- 読むべき個別仕様ファイルや下位ディレクトリが既に明確なとき。
- cmoc の実装コードやテストコードそのものを直接確認したいとき。
- `oracles` 以外の README、AGENTS、メモ、作業ログなど、正本仕様断片ではない文書だけを探しているとき。
- Codex CLI や git の一般的な使い方だけを調べており、cmoc 固有の仕様ルーティングが不要なとき。

## hash

- 9b0d07be6d2c916457d16c1e69f81041add13d0467dd18168ab0d1dbe310656f

# `pyproject.toml`

## Summary

- Python project metadata for cmoc, including package name, version, description, required Python version, and runtime dependencies.
- Defines the `cmoc` console script entry point as `main:app`.
- Configures setuptools build backend, `src` package layout, and `main` as a Python module.

## Read this when

- Checking or changing cmoc package metadata such as name, version, description, or supported Python version.
- Adding, removing, or reviewing project dependencies such as Typer or pytest.
- Investigating how the `cmoc` command is exposed as a console script.
- Changing build-system or setuptools configuration for the `src` layout.

## Do not read this when

- Looking for cmoc command behavior, user-facing workflow, stdout/stderr output, or subcommand specifications.
- Reading implementation details of CLI commands or shared application logic in `src`.
- Reading automated test behavior or test helper implementation in `tests`.
- Checking repository-specific AI access rules, editing restrictions, or oracle routing requirements.

## hash

- 8349bdb67cbd63691ac1238ce32ed38b23eb3e3217972652a754375e4321d4f4

# `src`

## Summary

- cmoc の Python 実装コードを収める最上位ディレクトリです。
- `main.py` は Typer ベースの CLI エントリーポイントで、`init`、`branch`、`eval-oracles`、`apply`、`merge` の各サブコマンドを登録し、リポジトリルート検出と共通エラー表示を経由して実装関数へ処理を委譲します。
- `commons` は Codex CLI 実行、Structured Output JSON 検査、共通エラー整形、`INDEX.md` 自動メンテナンス、git リポジトリ操作、タイムスタンプ生成など、サブコマンド横断の共通処理をまとめるパッケージです。
- `sub_commands` は `cmoc init`、`cmoc branch`、`cmoc eval-oracles`、`cmoc apply`、`cmoc merge` の本体処理をファイルごとに実装するパッケージです。
- `codex_minimal_outrigger_cli.egg-info` や `__pycache__` はビルド・実行に伴う生成物であり、通常の実装調査では主要な参照対象ではありません。

## Read this when

- cmoc の実装コード全体の入口を把握し、CLI エントリーポイント、共通処理、個別サブコマンド実装のどこを読むべきか判断したいとき。
- トップレベルの CLI コマンド追加・変更、サブコマンド登録、Typer 引数定義、コマンド実行時の共通例外処理を調べたいとき。
- Codex CLI 呼び出し、JSON 応答処理、`INDEX.md` メンテナンス、git 操作、タイムスタンプ生成など、複数サブコマンドから再利用される基盤処理の所在を探しているとき。
- `cmoc init`、`cmoc branch`、`cmoc eval-oracles`、`cmoc apply`、`cmoc merge` の具体的な実行フローやプロンプト生成、進捗表示、コミット・レポート生成処理の実装へ進みたいとき。
- テストや仕様断片ではなく、cmoc 自体の Python 実装配置を確認したいとき。

## Do not read this when

- cmoc の正本仕様断片を確認したいとき。まず `<cmoc-root>/oracles` 配下の該当 `INDEX.md` と仕様ファイルを読むべきです。
- 自動テストの構造、pytest、Fake Codex CLI、テストデータを調べたいだけのときは、`tests` 配下を読むべきです。
- README、AGENTS、oracles、memo などの編集可否やリポジトリ運用ルールだけを確認したいとき。
- 特定の共通処理や特定サブコマンドの読み先がすでに明確なときは、`commons` または `sub_commands` 配下の該当 `INDEX.md` や個別ファイルを直接読むべきです。
- 生成済み bytecode、egg-info、パッケージメタデータの詳細だけを調べたい場合を除き、`__pycache__` や `codex_minimal_outrigger_cli.egg-info` を読む必要はありません。

## hash

- 813d06dcba9c3320d2715640a5eb2d8550d55ae62a4a51b482a485c6fe30fdf8

# `test.sh`

## Summary

- `test.sh` は、シェル環境の `PATH` 先頭に `/home/happy/codex_minimal_outrigger_cli_stage0/bin` を追加するための短い環境設定スクリプトです。
- cmoc のテストや手動確認で、現リポジトリではなく stage0 側の `bin` 配下にあるコマンドを優先して参照したい場合の入口になります。

## Read this when

- `test.sh` を source したときに `PATH` がどのように変わるか確認したいとき。
- テスト実行や手動検証で、どの cmoc コマンド実体が優先的に呼び出されるかを確認したいとき。
- stage0 の `bin` ディレクトリを使う前提のローカル環境設定を調べたいとき。

## Do not read this when

- cmoc のサブコマンド仕様や正本仕様断片を調べたいとき。
- cmoc 本体の Python 実装、設計規約、テスト規約を調べたいとき。
- 通常のテストケース内容や pytest の期待結果を確認したいとき。
- stage0 の実装内容や `bin` 配下の個別コマンドの挙動を調べたいとき。

## hash

- 0ca9877993ee802249d52f98317a029f6b9f5e32a4ff92729fd78d983ced47a3

# `tests`

## Summary

- cmoc 自体の pytest テストスイートを集約するディレクトリです。
- pytest 実行時に `<cmoc-root>/src` を import path へ追加する `conftest.py` と、共通処理・INDEX.md メンテナンス・リポジトリ操作・主要サブコマンド・タイムスタンプ形式を検証するテストファイルを含みます。
- Codex CLI 呼び出しラッパー、Structured Output の JSON パースと意味検証リトライ、ログ保存、`--output-schema` 指定、Fake Codex CLI を使った外部依存のない検証を扱います。
- `maintain_indexes` による INDEX.md 生成・更新、gitignore 対象除外、最新 INDEX.md の再生成回避、メンテナンス対象だけのコミットなどを検証します。
- `commons.repo` の `<repo-root>` 探索、`.cmoc` ignore 保証、oracle ファイル列挙、cmoc ブランチ判定、branch base commit 記録先、oracles 外の未コミット差分拒否を検証します。
- `cmoc init`、`cmoc branch`、`cmoc eval-oracles --full`、`cmoc apply`、`cmoc merge <branch>` の主要な制御フローを、一時 git リポジトリと monkeypatch を使って確認します。
- `commons.timestamps.make_timestamp` の `YYYY-MM-DD_HH-MM_SS_mmm` 形式とミリ秒精度の期待値を検証します。

## Read this when

- cmoc 自体の自動テストを追加・修正し、既存テストの配置や対象領域を確認したいとき。
- pytest が `<cmoc-root>/src` 配下の実装をどのように import しているか確認したいとき。
- Codex CLI 呼び出しラッパー、Structured Output、JSON パース失敗時リトライ、意味検証失敗時リトライ、ログ保存、Fake Codex CLI の既存テストパターンを探すとき。
- INDEX.md メンテナンス処理のテストを確認し、gitignore 除外、hash による最新判定、Structured Output schema、Codex CLI 呼び出し抑制、自動コミット対象を調べたいとき。
- リポジトリ探索、oracle ファイル列挙、`.cmoc` ignore、未コミット差分チェック、cmoc ブランチ名、branch base commit パスなど `commons.repo` の期待挙動をテスト側から確認したいとき。
- `cmoc init`、`cmoc branch`、`cmoc eval-oracles`、`cmoc apply`、`cmoc merge` のサブコマンド実装を変更し、既存テストで期待される成功系・失敗系の制御フローを把握したいとき。
- 一時 git リポジトリ、`tmp_path`、`monkeypatch`、PATH 差し替え、疑似 Codex 応答を使うテスト実装例を参照したいとき。
- cmoc のタイムスタンプ文字列形式を変更・確認するとき。

## Do not read this when

- cmoc の実装本体を読みたいとき。実装は `<cmoc-root>/src` 配下を確認してください。
- cmoc の正本仕様断片や仕様ルーティングを確認したいとき。仕様は `<cmoc-root>/oracles` 配下を確認してください。
- README、AGENTS.md、oracles、memo などの編集可否やリポジトリ運用ルールだけを確認したいとき。
- cmoc を使って開発する対象リポジトリ側、つまり `<repo-root>` のコードやテストを調べたいとき。
- Codex CLI や git の一般的な使い方だけを調べており、cmoc 固有のテスト期待値が不要なとき。
- ユーザー向けドキュメントや CLI の利用手順だけを確認したいとき。
- 外部 LLM の実応答品質、ネットワーク連携、実 Codex CLI そのものの統合挙動を検証したいとき。

## hash

- 38dd87ff86a54dbe28f2a8dbdc57fa9baeb34c21de18a7b0a92b82b8affe74a6
