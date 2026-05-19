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

- `bin` は、cmoc コマンドの実行入口を置くディレクトリです。
- 主要な手書き対象は `bin/cmoc` で、リポジトリルートを自身の位置から解決し、利用可能なら `<cmoc-root>/.venv/bin/python` で `<cmoc-root>/src/main.py` を再実行します。
- 仮想環境 Python で既に実行中、または `.venv/bin/python` が存在しない場合は、`<cmoc-root>/src` を import path に追加して `main.main` を呼び出します。
- `bin/cmoc` は CLI 本体のサブコマンド実装ではなく、ユーザーが実行する `cmoc` コマンドから Python 実装へ制御を渡す薄いランチャーです。
- `bin/__pycache__` は Python のバイトコードキャッシュであり、通常の仕様確認や実装確認では読む必要がありません。

## Read this when

- `cmoc` 実行ファイルがどのように Python 実装へ処理を渡すか確認したいとき。
- `.venv/bin/python` が存在する場合の再実行ロジックや、`src/main.py` が起動される流れを調べたいとき。
- 仮想環境がない場合、または既に仮想環境 Python で実行中の場合に、`main.main` がどのように呼び出されるか確認したいとき。
- PATH に置かれる `cmoc` コマンドの shebang、ランチャー構造、import path 追加処理を確認したいとき。
- CLI 起動時の問題が、サブコマンド本体ではなくランチャーや Python インタープリタ選択に関係している可能性があるとき。

## Do not read this when

- cmoc のサブコマンドの具体的な挙動、オプション、業務ロジックを調べたいとき。
- Typer アプリケーション本体、コマンド定義、共通処理、各サブコマンド実装を確認したいとき。
- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` の仕様や詳細実装を調べたいとき。
- Codex CLI 呼び出し、Structured Output、ログ保存、リトライ、サンドボックス指定などの実行時仕様を確認したいとき。
- cmoc 自体の開発規約、テスト規約、コーディング規約、依存管理方針を確認したいとき。
- `<repo-root>` 側に生成される `INDEX.md`、oracle 評価結果、作業ブランチなど、cmoc が対象リポジトリ内で扱う成果物について調べたいとき。
- Python の実行時キャッシュである `__pycache__` や `.pyc` ファイルの中身を通常の仕様確認として読もうとしているとき。

## hash

- 6dfe0c2d9010f26a4858f47e270adde4d1e76e9249406cb87a2f7b695e43a525

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
- CLI エントリーポイントの `main.py`、共通ユーティリティ群の `commons`、個別サブコマンド実装の `sub_commands` が主要な読み先です。
- `main.py` は Typer アプリを定義し、`init`、`branch`、`eval-oracles`、`apply`、`merge` の各 CLI callback から `sub_commands` 配下の実装へ処理を委譲します。
- `commons` は Codex CLI 呼び出し、Structured Output 検証、`INDEX.md` 自動メンテナンス、repo root・git 操作、共通エラー整形、実行ラッパー、タイムスタンプ、ステップ時間計測など、複数サブコマンドで共有する処理をまとめます。
- `sub_commands` は `cmoc init`、`cmoc branch`、`cmoc eval-oracles`、`cmoc apply`、`cmoc merge` の本体フローをファイル別に実装します。
- `codex_minimal_outrigger_cli.egg-info` や `__pycache__` はビルド・実行時の生成物であり、通常の仕様調査や実装修正の主要対象ではありません。

## Read this when

- cmoc の実装コード全体で、CLI 入口、共通処理、個別サブコマンドのどこを読むべきか判断したいとき。
- `cmoc` コマンドのサブコマンド登録、Typer/Click の例外処理、CLI 引数から実装関数への委譲関係を確認したいとき。
- Codex CLI 呼び出し、Structured Output、ログ保存、リトライ、`INDEX.md` 自動メンテナンス、repo root 探索、git 操作、共通エラー処理などの共有実装を探しているとき。
- `cmoc init`、`cmoc branch`、`cmoc eval-oracles`、`cmoc apply`、`cmoc merge` の具体的な実行フローや前提条件検査、進捗表示、レポート保存、commit・merge 処理を調べたいとき。
- cmoc 自体の実装を変更する前に、`main.py`、`commons`、`sub_commands` の責務分担を把握したいとき。
- テスト対象の実装ファイルが `src` 配下のどこにあるかを切り分けたいとき。

## Do not read this when

- cmoc の正本仕様断片を確認したいとき。その場合は `oracles` 配下の `INDEX.md` から必要な仕様ファイルへ進むべきです。
- cmoc 自体の開発ルール、コーディング規約、テスト規約、環境ルールだけを調べたいとき。その場合は `oracles/dev_rules` 側を読むべきです。
- cmoc を使って開発する対象リポジトリの `<repo-root>` 側の oracle、`.cmoc` 作業データ、生成レポートだけを確認したいとき。
- README、AGENTS、oracles、memo などのリポジトリ運用ルールや編集可否だけを確認したいとき。
- Python の一般的な Typer、git、JSON Schema、subprocess、日時処理の使い方だけを知りたいとき。
- ビルド生成物や Python キャッシュの内容を確認したいだけのとき。

## hash

- 301074652a5bc9d5e3d4b9fb49aaae1d8e3b837402544cd9b0a935866b3a5be0

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

- `tests` は cmoc 自体の pytest ベース自動テストをまとめるディレクトリです。
- `conftest.py` で `<cmoc-root>/src` を import path に追加し、インストールなしで `commons`、`sub_commands`、`main` などをテストできるようにしています。
- `test_codex.py` は `commons.codex.run_codex_exec` の Codex CLI 呼び出し、Structured Output、JSON/schema/意味的バリデーションのリトライ、ログ保存、stdout 進捗表示、INDEX メンテナンス連携を検証します。
- `test_indexing.py` は `commons.indexing.maintain_indexes` による `INDEX.md` 自動生成・再生成、gitignore 除外、空ディレクトリ、build/tmp、nested memo、Structured Output schema、自動コミット対象の切り分けを検証します。
- `test_repo.py` は `commons.repo` の repo root 探索、`.cmoc` ignore 保証、oracle ファイル列挙、変更 oracle 抽出、oracle 削除検出、oracle 外差分拒否、cmoc ブランチ判定、base commit 記録パスを検証します。
- `test_subcommands.py` は `cmoc init`、`cmoc branch`、`cmoc eval-oracles`、`cmoc apply`、`cmoc merge` と Typer エントリーポイントの決定論的な制御ロジックを検証します。
- `test_timestamps.py` は cmoc timestamp と経過時間表示の固定フォーマットを検証します。
- `__pycache__` は Python 実行時のキャッシュであり、テスト仕様や実装判断のために読む対象ではありません。

## Read this when

- cmoc 自体の自動テスト全体の配置と、どのテストファイルがどの機能を検証しているかを把握したいとき。
- `src` 配下の実装変更に対して、関連する既存 pytest を探したいとき。
- Codex CLI 呼び出し、Structured Output、ログ保存、stdout 進捗表示、INDEX メンテナンス連携のテストを探しているとき。
- `INDEX.md` 自動メンテナンス、gitignore 対象除外、空ディレクトリ、build/tmp、memo、hash 最新性、Structured Output schema、自動コミット対象のテストを確認したいとき。
- git repo 共通処理、oracle ファイル列挙、変更 oracle 抽出、oracle 削除検出、cmoc ブランチ判定、`.cmoc` ignore 保証のテストを確認したいとき。
- `cmoc init`、`cmoc branch`、`cmoc eval-oracles`、`cmoc apply`、`cmoc merge` のサブコマンド制御ロジックに関するテストを確認したいとき。
- timestamp 生成やサブコマンド完了時の経過時間表示フォーマットのテストを探しているとき。
- 一時 git repository、fake `codex` コマンド、`monkeypatch`、`capsys` を使った既存テストパターンを参考にしたいとき。

## Do not read this when

- cmoc の正本仕様断片を確認したいとき。この場合は `<cmoc-root>/oracles` 配下の該当 `INDEX.md` と仕様ファイルを読むべきです。
- cmoc の実装コードそのものを読みたいとき。この場合は `<cmoc-root>/src` 配下を読むべきです。
- README、AGENTS、oracles、memo などのリポジトリ運用ルールや編集可否だけを確認したいとき。
- cmoc を使って別リポジトリを開発する `<repo-root>` 側の仕様や作業手順だけを調べたいとき。
- pytest の実行キャッシュや生成物を確認したいだけのとき。`tests/__pycache__` は通常読む必要がありません。
- Codex CLI や git の一般的な使い方を調べており、cmoc 固有のテスト期待値が不要なとき。

## hash

- 53e851d75d9a1fd4ea0ffe37587af13e0b94d916cb5b54890ed9fdca213d1ae5
