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

- cmoc の正本仕様断片を集約する最上位ディレクトリ。
- アプリケーション実行時仕様を扱う app_specs と、cmoc 自体の開発ルールを扱う dev_rules へのルーティング入口。
- cmoc の仕様調査を始める際に、ユーザー向け CLI 挙動・サブコマンド仕様・Codex CLI 連携・INDEX 自動メンテナンス・エラー処理・開発規約・テスト規約のどこを読むべきか判断するためのメタデータ。

## Read this when

- cmoc の正本仕様断片を調べ始める前に、どの下位ディレクトリや仕様ファイルへ進むべきか判断したいとき。
- cmoc のアプリケーション仕様と、cmoc 自体の開発ルールのどちらを参照すべきか切り分けたいとき。
- Codex CLI 連携、コンソール出力、エラーハンドリング、INDEX.md 自動メンテナンス、利用フロー、各サブコマンド仕様の所在を探したいとき。
- Python 実装、CLI 構成、共通処理配置、開発環境、pytest による自動テストなど、cmoc 開発ルールの所在を探したいとき。
- <cmoc-root>/oracles 配下の仕様断片を読む必要があるが、最小限どのファイルだけを読むべきかまだ明確でないとき。

## Do not read this when

- 読むべき下位 INDEX.md または個別仕様ファイルが既に明確で、この最上位ルーティング情報が不要なとき。
- cmoc の実装コードそのものやテストコードそのものを直接調査したいだけのとき。
- README.md、AGENTS.md、memo、oracles などのリポジトリ運用上の編集可否だけを確認したいとき。
- cmoc を用いて作業する対象リポジトリ <repo-root> 側の独自仕様を調べたいとき。
- Codex CLI や外部ツールそのものの一般仕様を調べたいとき。

## hash

- cc6c9f948ce973d4c0f64a1eada45c0c1f7c5c6c96b411e13303731f1200d0cc

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

- cmoc の実装コード全体を収める Python ソースディレクトリ。
- Typer ベースの CLI エントリーポイントである main.py、サブコマンド実装をまとめる sub_commands、コマンド横断の共通処理をまとめる commons で構成される。
- init、branch、eval-oracles、apply、merge の各 CLI コマンドの登録、実行時エラー処理、Git・Codex CLI・INDEX.md 保守・タイムスタンプなどの実装入口を提供する。

## Read this when

- cmoc 自体の実装コードの全体構造を把握し、どのファイルやパッケージを読むべきか判断したいとき。
- トップレベル CLI コマンドの登録や dispatch を調べる必要があるとき。
- cmoc init、branch、eval-oracles、apply、merge のいずれかの実行時処理を変更またはデバッグするとき。
- 複数サブコマンドで共有される Git 操作、Codex CLI 呼び出し、エラー整形、timestamp 生成、INDEX.md 自動保守の実装を探すとき。
- tests 側の失敗から、対応する production code の配置を特定したいとき。

## Do not read this when

- cmoc の正本仕様断片そのものを確認したいときは、まず oracles 配下のルーティング情報を読むべき。
- cmoc 自体の開発ルール、設計規約、テスト方針、環境ルールだけを確認したいときは、oracles/dev_rules 側を読むべき。
- 自動テスト、fixture、期待値だけを調べたいときは tests 配下を読むべき。
- README.md、AGENTS.md、oracles、memo など、リポジトリ運用文書やアクセス制限対象の内容を確認したいだけのとき。
- cmoc を用いて開発する対象リポジトリ側の仕様やアプリケーションコードを調べたいとき。

## hash

- 7861a53aee9d4d91c835f364afe77e3ff601d5f5dfd03c76e72283a33321001a

# `tests`

## Summary

- pytest-based automated test suite for cmoc implementation under <cmoc-root>/src.
- Covers Codex CLI execution wrapper behavior, INDEX.md maintenance, git repository utilities, timestamp formatting, and deterministic subcommand implementation logic.
- Uses temporary git repositories, fake Codex CLI executables, monkeypatching, and direct calls into implementation functions rather than full shell-level integration tests.

## Read this when

- Adding, updating, or debugging cmoc automated tests.
- Changing src behavior in commons.codex, commons.indexing, commons.repo, commons.timestamps, or sub_commands and needing the corresponding test expectations.
- Investigating pytest setup, import path bootstrapping, temporary git repository helper patterns, fake Codex CLI behavior, or monkeypatched deterministic test flows.
- Verifying expected behavior for Codex Structured Output retries, INDEX.md generation, oracle file discovery, cmoc branch metadata, init/branch/eval-oracles/apply/merge control logic, or timestamp formatting.

## Do not read this when

- You need the canonical application specification; start from <cmoc-root>/oracles/INDEX.md and route to the relevant oracle files instead.
- You are looking for production implementation details only; read <cmoc-root>/src before consulting tests.
- You are changing README.md, AGENTS.md, or repository operation rules without touching tested implementation behavior.
- You need user-facing CLI documentation or broad workflow explanation rather than executable pytest assertions.

## hash

- 65d0cbe3a7118e8c9fc855faae16059a6fe2b5abc1b4d6bdec28e3731e4dd83f
