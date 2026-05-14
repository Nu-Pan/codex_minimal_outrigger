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

# `REAMDE.md`

## Summary

- cmoc のリポジトリ概要を短く示すトップレベル文書。
- cmoc が Codex CLI を用いた開発を補助する最小限度の外部ツールであることを説明する。
- 詳細情報の参照先として AGENTS.md を案内する。

## Read this when

- リポジトリ直下の README 相当ファイルとして、cmoc のごく短い概要だけを確認したいとき。
- cmoc が何をするツールなのかを一文レベルで把握したいとき。
- 詳細な開発ルールや仕様を見る前に、参照先が AGENTS.md であることを確認したいとき。

## Do not read this when

- cmoc の実装方針、テスト方針、ファイルアクセス規則、編集禁止ファイルなどの開発ルールを詳しく確認したいとき。
- cmoc の正本仕様断片やサブコマンドごとの挙動を調べたいとき。
- src や tests 配下の具体的なコード構造、実装詳細、自動テスト内容を確認したいとき。

## hash

- 5755d7fef8c24837d821eaf097531d8b84684ac1b1b911f31bd28a17de89a7ad

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

- cmoc の正本仕様断片を収める oracles 直下の最上位ルーティング情報。
- アプリケーション実行時仕様を扱う app_specs と、cmoc 自体の開発ルールを扱う dev_rules への導線を示す。
- cmoc の仕様調査を始める際に、ユーザー向け CLI 挙動を読むべきか、実装・テスト・開発環境ルールを読むべきかを切り分ける入口。

## Read this when

- cmoc の正本仕様断片を調べ始めるとき。
- どの oracles 配下ディレクトリまたは仕様ファイルを読むべきか判断したいとき。
- cmoc の CLI ワークフロー、サブコマンド、Codex CLI 連携、出力、エラーハンドリングなどのアプリケーション仕様への入口を探すとき。
- cmoc 自体の src 実装、tests 自動テスト、Python 開発環境、コーディング規約、設計規約への入口を探すとき。
- app_specs と dev_rules のどちらが現在の作業に関係するかを確認したいとき。

## Do not read this when

- 読むべき個別仕様ファイルまたは下位 INDEX.md が既に明確なとき。
- oracles 配下の正本仕様ではなく、実装コードやテストコードそのものだけを読みたいとき。
- README.md、AGENTS.md、memo、oracles の編集可否など、リポジトリ運用ルールだけを確認したいとき。
- cmoc を使って開発する対象リポジトリ <repo-root> 側の独自仕様だけを調べたいとき。
- 外部ツール、Codex CLI 本体、LLM 一般の仕様だけを調べたいとき。

## hash

- 951575d6cb2edce374031efc2adc86eeb06c177e64c3cb45c3154627d8fd38fc

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

- cmoc の Python 実装コードを置くトップレベルディレクトリ。
- Typer ベースの CLI エントリーポイントである `main.py`、サブコマンド実装を集める `sub_commands`、複数サブコマンドから再利用される共通処理を集める `commons` への入口になる。
- `main.py` は `init`、`branch`、`eval-oracles`、`apply`、`merge` の CLI 登録、引数受け渡し、リポジトリルート移動、共通エラー表示を担当する。
- `sub_commands` は各サブコマンド固有のワークフロー、Codex CLI へのプロンプト、レポート出力、git 操作の呼び出し順序を実装する。
- `commons` は Codex CLI 実行、Structured Output 検証、INDEX.md 自動メンテナンス、git リポジトリ操作、共通エラー、タイムスタンプ生成などの横断的な補助処理を提供する。

## Read this when

- cmoc の実装コード全体の入口を把握し、`main.py`、`sub_commands`、`commons` のどこを読むべきか判断したいとき。
- トップレベル CLI コマンドの登録、Typer 引数定義、サブコマンド実装への dispatch、共通エラー処理の流れを確認したいとき。
- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` の実装ファイルへの導線を探すとき。
- Codex CLI 呼び出し、git 操作、oracle ファイル列挙、INDEX.md メンテナンス、タイムスタンプ、共通エラーなどの共有処理がどのパッケージにあるか調べたいとき。
- cmoc 自体の src 配下を変更する前に、実装の大まかな責務分担と読むべき下位 INDEX.md を確認したいとき。

## Do not read this when

- cmoc の正本仕様断片やユーザー向け CLI 挙動を確認したいだけのときは、まず `oracles` 配下の該当ルーティングを読むべきとき。
- Python コーディング規約、テスト方針、開発環境などの開発ルールだけを確認したいとき。
- 特定サブコマンドの実装ファイルが既に明確で、この src 全体のルーティング情報が不要なとき。
- git 実行、Codex CLI 実行、INDEX.md 生成、エラー整形など、読むべき共通モジュールが既に明確なとき。
- テストコード、pytest fixture、Fake Codex CLI、テスト期待値だけを調べたいとき。
- README、AGENTS、oracles、memo など、src 外の文書・運用ルール・編集可否だけを確認したいとき。

## hash

- 7b0716ef0733a9648798f3ab9b3c5e000b9bdfae0f814d0c51548b08dae13d6c

# `tests`

## Summary

- cmoc 自体の自動テストを配置する pytest テストディレクトリ。
- commons.codex、commons.indexing、commons.repo、commons.timestamps と、主要 sub_commands の決定論的な制御ロジックを検証する。
- conftest.py により <cmoc-root>/src を import path に追加し、tmp_path 上の一時 git リポジトリ、fake Codex CLI、monkeypatch を使って外部依存を抑えたテストを構成する。
- INDEX.md 自動メンテナンス、Codex CLI Structured Output リトライ、git リポジトリ共通処理、timestamp 形式、init/branch/eval-oracles/apply/merge の基本挙動への導線をまとめる。

## Read this when

- cmoc の自動テスト全体の配置を把握し、どの test_*.py を読むべきか判断したいとき。
- commons.codex.run_codex_exec、commons.indexing.maintain_indexes、commons.repo、commons.timestamps.make_timestamp のテスト期待値を確認したいとき。
- cmoc init、cmoc branch、cmoc eval-oracles、cmoc apply、cmoc merge のサブコマンド挙動を pytest 側から確認・変更したいとき。
- pytest で <cmoc-root>/src のモジュールを import する仕組み、tmp_path 上の git リポジトリ作成、fake Codex CLI、monkeypatch の使い方を参照したいとき。
- INDEX.md 生成・更新、gitignore 対象除外、Structured Output 不正時リトライ、自動コミット対象限定など、回帰テストで守られている境界条件を調べたいとき。

## Do not read this when

- cmoc の正本仕様断片そのものを調べたいときは <cmoc-root>/oracles 配下の該当 INDEX.md と仕様ファイルを読む。
- cmoc の実装コード本体や内部アルゴリズムを直接追いたいだけで、pytest 上の期待挙動や回帰テストが不要なとき。
- README.md、AGENTS.md、oracles、memo などのリポジトリ運用ルールやファイルアクセス制約だけを確認したいとき。
- cmoc を用いて開発する対象リポジトリ <repo-root> 側の仕様やテストを探しているとき。
- 外部の Codex CLI、Git、pytest 自体の一般的な使い方を調べたいだけで、このリポジトリ固有のテスト構成が不要なとき。

## hash

- a06f076e7c7458b9f8e6ae72eae32f7a3a6fcd07d26e48938942f46485dd0098
