# `AGENTS.md`

## Summary

- `AGENTS.md` は、cmoc（Codex Minimal Outrigger CLI）開発リポジトリにおける作業上の基本規則を定義する文書です。
- `<cmoc-root>` と `<repo-root>` の意味を明確に分け、cmoc 自体の開発と cmoc を用いた開発を混同しないよう指示しています。
- AI が閲覧・編集してはいけないファイル、および編集してはいけないファイルを列挙しています。
- 正本仕様断片である `<cmoc-root>/oracles` の扱いと、仕様調査時に `INDEX.md` を起点として最低限必要なファイルだけを読むルーティング方針を示しています。
- 実装は `<cmoc-root>/src`、自動テストは `<cmoc-root>/tests` に置くことを定めています。

## Read this when

- このリポジトリで作業を始める前に、最初に読む必要があります。
- `<cmoc-root>`、`<repo-root>`、cmoc 自体の開発、cmoc を用いた開発の違いを確認したいときに読んでください。
- AI が読んではいけないファイル、編集してはいけないファイルを確認したいときに読んでください。
- `oracles` 配下の正本仕様断片を調べる際の入口や読み方を確認したいときに読んでください。
- 実装ファイルやテストファイルをどこに置くべきか確認したいときに読んでください。

## Do not read this when

- cmoc の詳細な仕様断片そのものを確認したいときは、ここではなく `<cmoc-root>/oracles/INDEX.md` から必要な仕様ファイルへ進んでください。
- 既に作業規則を把握しており、特定機能の実装詳細だけを確認したいときは、関連する `src` や `tests` のファイルを読んでください。
- README の利用者向け説明や導入手順を確認したいときは、この文書ではなく README を参照してください。

## hash

- b2f93d440fb91234a2ff90e3b533ff1ba9230037690851040d4d8e5de5d0bf37

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
- clone 後に Python 仮想環境を作成し、`<cmoc-root>/.venv/bin/python -m pip install -e .` で開発用インストールする手順を知りたいとき。
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

- `/home/happy/codex_minimal_outrigger_cli_stage1/oracles/INDEX.md` を読み、配下の正本仕様を調べる入口としての目次情報だけを整理します。ファイル編集と `memo` へのアクセスは行いません。

## Read this when

- `oracles` 配下の仕様断片を調べ始める前。
- どの仕様ファイルや下位ディレクトリを読むべきか判断したいとき。
- cmoc の正本仕様に基づいて実装やテスト方針を確認したいとき。

## Do not read this when

- cmoc の実装コードそのものを確認したいとき。
- `README.md` や `AGENTS.md` の編集が目的のとき。
- `memo` 配下の情報を探したいとき。

## hash

- ca462c3f2193b29fabe34123925821c5e686ced193984d6e4bd0c59678dcd4ea

# `pyproject.toml`

## Summary

- `pyproject.toml` は cmoc の Python パッケージ定義とビルド設定を記述するファイルです。
- プロジェクト名、バージョン、説明、必要 Python バージョン、依存パッケージとして `pytest` と `typer` を定義しています。
- `cmoc` コマンドのエントリーポイントを `main:main` として公開しています。
- setuptools をビルドバックエンドに使い、`src` 配下をパッケージ探索対象とし、`main` を単一モジュールとして扱う設定を含みます。

## Read this when

- cmoc の Python パッケージ名、バージョン、説明、必要 Python バージョンを確認したいとき。
- cmoc の実行コマンド `cmoc` がどの Python 関数に接続されているか確認したいとき。
- cmoc 開発環境で必要な依存パッケージやビルドバックエンドを確認したいとき。
- `src` 配下のモジュール配置と setuptools のパッケージ探索設定を確認したいとき。
- 依存追加、CLI エントリーポイント変更、Python バージョン制約変更、ビルド設定変更を行うとき。

## Do not read this when

- cmoc のサブコマンド仕様、実行時仕様、Codex CLI 連携仕様を調べたいとき。
- cmoc の実装コードやテストコードの具体的な処理内容を調べたいとき。
- README、AGENTS、oracles、memo などのリポジトリ運用ルールや編集制約だけを確認したいとき。
- cmoc を用いて開発する対象リポジトリ側の設定や仕様を調べたいとき。
- Python パッケージ設定、依存関係、ビルド設定、CLI エントリーポイントに関係しない作業をしているとき。

## hash

- f7e7dcdc72547ff9b03be0135915cb7c3ae47af0b596744238d91061acd8488e

# `src`

## Summary

- `src` は cmoc 本体の Python 実装を置くディレクトリです。
- `main.py` は Typer ベースの CLI エントリーポイントで、`init`、`branch`、`eval-oracles`、`apply`、`merge` の各サブコマンドを登録し、対応する `sub_commands` 配下の実装へ委譲します。
- `commons` は複数サブコマンドで共有する共通処理パッケージで、Codex CLI 呼び出し、Structured Output 検証、INDEX.md メンテナンス、共通エラー整形、git リポジトリ操作、タイムスタンプ生成、経過時間計測などを扱います。
- `sub_commands` は cmoc の個別サブコマンド本体を実装するパッケージで、`cmoc init`、`cmoc branch`、`cmoc eval-oracles`、`cmoc apply`、`cmoc merge` の実行フローをファイルごとに分担します。
- `codex_minimal_outrigger_cli.egg-info` や `__pycache__` はパッケージングや Python 実行時に生成される補助ファイル群であり、通常の実装調査では主要な参照先ではありません。

## Read this when

- cmoc 本体の実装入口が `main.py`、`commons`、`sub_commands` のどこにあるか判断したいとき。
- CLI のトップレベル登録、サブコマンド実装、共通処理の大まかな分担を把握したいとき。
- `cmoc init`、`cmoc branch`、`cmoc eval-oracles`、`cmoc apply`、`cmoc merge` の実装ファイルへたどるための上位ルーティングが必要なとき。
- Codex CLI 呼び出し、Structured Output、INDEX.md メンテナンス、git 操作、エラー処理、時間計測などの共通実装がどこにまとまっているか知りたいとき。
- cmoc の正本仕様ではなく、仕様を実現する Python 実装コードの配置を調べたいとき。

## Do not read this when

- cmoc のユーザー向け仕様や正本仕様断片だけを確認したいとき。
- Python コーディング規約、テスト規約、開発環境などの開発ルールだけを調べたいとき。
- 自動テスト、Fake Codex CLI、pytest fixture、テストデータなど `tests` 配下の構成を調べたいとき。
- README、AGENTS、oracles、memo の編集可否やリポジトリ運用ルールだけを確認したいとき。
- `<repo-root>` 側で cmoc を用いて開発する対象リポジトリの実装内容を調査したいとき。

## hash

- bf7f2f2e38a1159768eb196704611e83959e65c4e43e63b1ccb513bb6a37efb3

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

- `tests` は cmoc 自体の pytest 自動テストを配置するディレクトリです。
- pytest の import path 設定を行う `conftest.py` と、git リポジトリ共通処理、Codex CLI 呼び出しラッパー、INDEX.md 自動メンテナンス、タイムスタンプ・経過時間表示、主要サブコマンド制御ロジックを検証するテストファイルを含みます。
- `test_repo.py` は `<repo-root>` 探索、`.cmoc` ignore 保証、oracle ファイル列挙、oracle 差分抽出、oracle 削除検出、cmoc ブランチ名や base commit 記録先など `commons.repo` の git 連携処理を検証します。
- `test_codex.py` は `run_codex_exec` の Structured Output、JSON/schema/意味的バリデーション失敗時のリトライ、schema ファイル渡し、ログ出力、INDEX メンテナンスの事前実行とスキップ指定を検証します。
- `test_indexing.py` は `maintain_indexes` による INDEX.md 生成、gitignore 除外、空ディレクトリ、build/tmp、memo ディレクトリ、既存エントリ再生成、Structured Output リトライ、自動コミット対象の制限を検証します。
- `test_subcommands.py` は `cmoc init`、`cmoc branch`、`cmoc eval-oracles`、`cmoc apply`、`cmoc merge` と Typer エントリーポイントの決定論的な制御ロジックを検証します。
- `test_timestamps.py` は cmoc タイムスタンプ形式と stdout 用の経過時間表示形式を検証します。

## Read this when

- cmoc 自体の実装変更に対して、既存 pytest がどの挙動を保護しているか把握したいとき。
- `commons.repo`、`commons.codex`、`commons.indexing`、`commons.timestamps`、`commons.timing`、または `sub_commands` 配下の実装を変更し、対応するテストの期待値を確認したいとき。
- `.cmoc` ignore 保証、oracle ファイル列挙、gitignore pattern 解釈、oracle 差分抽出、oracle 削除検出、cmoc ブランチ判定に関するテストを探しているとき。
- Codex CLI 呼び出しの fake 化、Structured Output schema、JSON リトライ、ログ保存、`skip_index_maintenance` のテストパターンを参照したいとき。
- INDEX.md 自動生成・再生成・配置対象・除外対象・自動コミット範囲に関する回帰テストを確認したいとき。
- `cmoc init`、`cmoc branch`、`cmoc eval-oracles`、`cmoc apply`、`cmoc merge` のサブコマンド実装に対するテスト観点を確認したいとき。
- pytest で一時 git リポジトリ、fake `codex` コマンド、`monkeypatch`、`capsys`、`subprocess` を使う既存テストの書き方を参考にしたいとき。

## Do not read this when

- cmoc の正本仕様断片を確認したいとき。仕様は `oracles` 配下のルーティング情報から必要なファイルを読むべきです。
- cmoc のユーザー向け CLI 仕様、ワークフロー、出力形式を体系的に調べたいだけのとき。まず `oracles/app_specs` 側を参照してください。
- Python コーディング規約、設計規約、テスト規約、開発環境ルールそのものを確認したいとき。まず `oracles/dev_rules` 側を参照してください。
- cmoc の実装コードの詳細を読むだけで、テストの保護範囲や期待値を確認する必要がないとき。
- `README.md`、`AGENTS.md`、`oracles`、`memo` などの編集可否やリポジトリ運用ルールだけを確認したいとき。
- cmoc を用いて別の `<repo-root>` を開発する利用手順だけを知りたいとき。

## hash

- 16a52418460986fb2ecf0f6f7efd155ba4185cd36ed15ef06d21691d997fbdc1
