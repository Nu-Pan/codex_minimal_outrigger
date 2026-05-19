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

- `<cmoc-root>/bin` は、cmoc コマンドの実行入口を置くディレクトリです。
- 主な実体は `bin/cmoc` で、シェルラッパーとして `<cmoc-root>` を解決し、`<cmoc-root>/.venv/bin/python` で `<cmoc-root>/src/main.py` を起動します。
- `bin/cmoc` は受け取った CLI 引数をそのまま Python 側へ渡し、サブコマンドの実装やアプリケーションロジックは `src/main.py` 以下に委譲します。
- 仮想環境の Python が実行可能でない場合、`bin/cmoc` は仮想環境作成と `pip install -e .` の手順を stderr に出力し、終了ステータス 1 で失敗します。
- `bin/__pycache__` は Python 実行時に生成されるキャッシュ領域であり、通常の仕様確認や実装理解では読む必要はありません。

## Read this when

- cmoc コマンドを実行したとき、最初にどのファイルが呼ばれるか確認したいとき。
- `bin/cmoc` が `<cmoc-root>`、仮想環境 Python、`src/main.py` をどのように解決しているか調べたいとき。
- `.venv/bin/python` が存在しない、または実行できない場合のエラーメッセージや終了ステータスを確認したいとき。
- cmoc の PATH 設定や開発環境で使う実行用ラッパーの挙動を確認したいとき。
- CLI 引数がシェルラッパーから Python のメイン処理へどのように渡されるか知りたいとき。

## Do not read this when

- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` など個別サブコマンドの仕様や実装を調べたいとき。
- Codex CLI 呼び出し、Structured Output、ログ保存、リトライ、INDEX.md 自動生成などのアプリケーション実行時仕様を調べたいとき。
- Python 側の引数解析、共通エラーハンドリング、サブコマンド分岐、業務ロジックの詳細を読みたいとき。
- cmoc 自体の Python コーディング規約、設計規約、テスト規約、開発環境ルールを確認したいとき。
- 自動テスト、Fake Codex CLI、pytest の使い方やテスト配置を調べたいとき。
- 生成済みキャッシュやバイトコードの内容を確認する目的で `__pycache__` を読もうとしているとき。

## hash

- dc808c234dd01ff9f971f14eed683eba9e933a49f673c4b2006094d56b848b82

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

- `src` は cmoc 自体の Python 実装を置くディレクトリです。
- CLI エントリーポイントである `main.py`、共通処理を集約する `commons` パッケージ、各サブコマンド本体を実装する `sub_commands` パッケージで構成されています。
- `main.py` は Typer アプリケーションを定義し、`init`、`branch`、`eval-oracles`、`apply`、`merge` の CLI サブコマンドを登録して、実処理を `sub_commands` 配下へ委譲します。
- `commons` は Codex CLI 呼び出し、Structured Output 検証、`INDEX.md` 自動メンテナンス、共通エラー表示、git リポジトリ操作、oracle ファイル列挙、タイムスタンプ生成、ステップ時間計測など、複数サブコマンドから利用される共通ユーティリティを扱います。
- `sub_commands` は `cmoc init`、`cmoc branch`、`cmoc eval-oracles`、`cmoc apply`、`cmoc merge` の実行フロー、進捗表示、Codex CLI 連携、git 操作、レポート生成などの個別ロジックを実装します。

## Read this when

- cmoc 自体の実装コードが `src` 配下でどのように分かれているか把握したいとき。
- CLI の入口、サブコマンド登録、Typer/Click 例外の共通エラー変換、各サブコマンド実装への委譲関係を確認したいとき。
- `init`、`branch`、`eval-oracles`、`apply`、`merge` の処理本体がどのモジュールにあるか判断したいとき。
- Codex CLI 呼び出し、Structured Output、ログ保存、リトライ、`INDEX.md` メンテナンス、repo root 探索、git 操作、タイムスタンプ、時間計測などの共通処理の入口を探しているとき。
- サブコマンド実装を修正する前に、トップレベル CLI、共通ユーティリティ、個別サブコマンドのどこを読むべきか切り分けたいとき。
- cmoc の自動テストを書くために、実装側の責務分担や対象モジュールを確認したいとき。

## Do not read this when

- cmoc の正本仕様断片を読みたいとき。仕様のルーティングは `oracles/INDEX.md` から確認するべきです。
- cmoc 自体の開発規約、設計規約、テスト規約、環境ルールだけを調べたいとき。該当する `oracles/dev_rules` 配下の仕様を読むべきです。
- README、AGENTS、memo、oracles の編集可否など、リポジトリ運用ルールだけを確認したいとき。
- cmoc を用いて開発する別リポジトリ側の `<repo-root>` の業務コード、oracle 内容、生成済みレポートを調べたいとき。
- pytest fixture、Fake Codex CLI、テストデータなど、テストコード側の詳細だけを調べたいとき。
- Codex CLI や git の一般的な使い方だけを知りたく、cmoc 固有の実装配置やラッパーを確認する必要がないとき。

## hash

- 4f6cf60a9f93d62789fafff286bdbdd288a29b989f565629dc3f36802d13534f

# `test.sh`

## Summary

- `test.sh` は、cmoc 開発リポジトリのルートパスを `CMOC_ROOT` として設定し、ローカルの仮想環境 `.venv/bin` と `bin` を `PATH` の先頭に追加するためのシェル設定断片です。
- このファイル自体はテスト実行ロジックを含まず、cmoc のローカル開発・検証で使用するコマンド探索パスを整える役割を持ちます。

## Read this when

- cmoc のローカル開発環境で、どのパスが `PATH` に追加されるか確認したいとき。
- `cmoc` コマンドや仮想環境内の実行ファイルが、テストや手元実行時にどの順序で解決されるか調べたいとき。
- 開発リポジトリの絶対パスを前提にした簡易的な環境設定スクリプトの内容を確認したいとき。

## Do not read this when

- cmoc のサブコマンド仕様、Structured Output、oracle 評価、マージ処理などのアプリケーション仕様を調べたいとき。
- cmoc の Python 実装、設計規約、テスト規約、個別テストケースの内容を調べたいとき。
- 実際の自動テストの手順、pytest の設定、Fake Codex CLI の挙動を確認したいとき。
- リポジトリ運用上の編集禁止ファイルや AI アクセス制限を確認したいとき。

## hash

- 6fc07bc0dff2b064245772154c4f103ce2d3d0cbe7536ae9124eb49e183c6b44

# `tests`

## Summary

- `tests` は cmoc 自体の pytest ベースの自動テストを配置するディレクトリです。
- pytest の import path 設定を行う `conftest.py` と、Codex CLI 呼び出し、INDEX.md メンテナンス、git リポジトリ共通処理、主要サブコマンド、タイムスタンプ・経過時間表示を検証するテストファイルを含みます。
- `test_codex.py` は `commons.codex.run_codex_exec` の Structured Output、JSON リトライ、schema 検証、ログ保存、stdout 進捗表示、INDEX メンテナンス呼び出しを検証します。
- `test_indexing.py` は `commons.indexing.maintain_indexes` による INDEX.md 生成、gitignore 除外、空ディレクトリ、build/tmp、memo、既存エントリ再生成、Structured Output リトライ、自動コミット対象を検証します。
- `test_repo.py` は `commons.repo` の repo root 探索、`.cmoc` ignore 保証、oracle ファイル列挙、oracle 差分抽出、oracle 削除検出、cmoc ブランチ判定、base commit 記録パスを検証します。
- `test_subcommands.py` は `cmoc init`、`cmoc branch`、`cmoc eval-oracles`、`cmoc apply`、`cmoc merge` と Typer 表層・ランチャーに関する決定論的な制御ロジックを検証します。
- `test_timestamps.py` は cmoc timestamp と stdout 用経過時間表示のフォーマットを検証します。
- `__pycache__` は Python 実行時生成物であり、テスト設計や仕様確認のために読む対象ではありません。

## Read this when

- cmoc 自体の自動テストの全体構成を把握したいとき。
- どのテストファイルが Codex CLI 呼び出し、INDEX.md メンテナンス、git 共通処理、サブコマンド、タイムスタンプのどれを担当しているか判断したいとき。
- `src` 配下の実装変更に対して、影響しそうな既存 pytest を探したいとき。
- Structured Output、fake Codex CLI、tmp_path 上の一時 git repo、monkeypatch を使ったテストパターンを探しているとき。
- `cmoc apply`、`cmoc merge`、`cmoc eval-oracles` など主要サブコマンドの回帰テスト範囲を確認したいとき。
- oracle ファイル列挙、gitignore pattern、変更 oracle 抽出、oracle 削除検出の期待値をテストから確認したいとき。
- INDEX.md 自動生成や目次メンテナンス処理の既存テストを調べたいとき。

## Do not read this when

- cmoc の正本仕様を確認したいとき。正本仕様断片は `oracles` 配下を読むべきです。
- cmoc の実装コードそのものを確認・修正したいとき。対象は `src` 配下です。
- README、AGENTS、oracles、memo などの編集可否やリポジトリ運用ルールだけを確認したいとき。
- cmoc を使って別リポジトリを開発するための `<repo-root>` 側の情報だけが必要なとき。
- pytest 実行で生成された `__pycache__` や `.pyc` ファイルの内容を調べようとしているとき。
- 外部利用者向けの導入手順や CLI の使い方だけを知りたいとき。

## hash

- b7da802d4c6a40cb5ef4878a1f5d92a255447c1a1ee3c06efa46f9e58e3c1c83
