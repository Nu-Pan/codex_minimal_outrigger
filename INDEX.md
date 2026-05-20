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

- `bin` は cmoc コマンドの起動用ファイルを置くディレクトリです。
- 主な実体は `bin/cmoc` で、シェル製の CLI エントリーポイントとして `<cmoc-root>` を解決し、`<cmoc-root>/.venv/bin/python` で `<cmoc-root>/src/main.py` を実行します。
- `bin/cmoc` は仮想環境 Python が存在し実行可能な場合、受け取った全引数を `src/main.py` に渡して `exec` します。
- 仮想環境 Python が見つからない、または実行できない場合は、日本語の構造化エラー、復旧用セットアップ手順、必要な実行ファイル、簡易 Call stack を表示して終了ステータス 1 で終了します。
- `bin/INDEX.md` は `bin/cmoc` へのルーティング情報を記載する目次ファイルです。
- `bin/__pycache__` は Python 実行時に生成されるキャッシュ領域であり、通常の仕様確認や実装確認では読む必要はありません。

## Read this when

- cmoc コマンドを起動したときに、最初にどのファイルが実行されるか確認したいとき。
- `bin/cmoc` から `<cmoc-root>/src/main.py` へどのように処理が渡るか調べたいとき。
- cmoc が使用する Python 実行ファイルとして `<cmoc-root>/.venv/bin/python` が前提になっているか確認したいとき。
- 仮想環境が未作成、削除済み、または実行不能な場合のエラー表示や終了ステータスを確認したいとき。
- cmoc の PATH 配置や CLI ラッパーとしての `bin/cmoc` の役割を調べたいとき。
- `bin` 配下で読むべき通常のファイルが `bin/cmoc` であることを判断したいとき。

## Do not read this when

- cmoc の各サブコマンドの具体的な仕様や処理内容を調べたいとき。
- Python 側のコマンドディスパッチ、共通処理、サブコマンド実装を調べたいとき。
- cmoc の自動テスト、Fake Codex CLI、pytest の規約やテストケースを確認したいとき。
- `<repo-root>` 側に生成される `INDEX.md`、`.cmoc`、oracle 評価結果などの仕様を調べたいとき。
- Python パッケージ構成、依存関係、仮想環境作成以外の開発環境ルールを確認したいとき。
- Python キャッシュや生成物の中身を調べたいだけのとき。

## hash

- 670c4146f37c39ca4785c462cbfb31ad730ef6d03952fdf7e4b91474fa2a6264

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

- `oracles/INDEX.md` は、cmoc の正本仕様断片ディレクトリ直下にある最上位ルーティング文書です。
- `app_specs` は cmoc のアプリケーション実行時仕様、Codex CLI 連携、設定、共通挙動、各サブコマンド仕様、利用者向けワークフローへの入口です。
- `dev_rules` は cmoc 自体の開発ルール、Python 実装規約、設計規約、開発環境、テスト規約への入口です。
- cmoc の仕様調査を始める際に、アプリケーション仕様を読むべきか、開発者向けルールを読むべきかを切り分けるための目次です。

## Read this when

- `oracles` 配下の正本仕様断片を調べ始めるとき。
- cmoc のアプリケーション実行時仕様と、cmoc 自体の開発ルールのどちらを読むべきか判断したいとき。
- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` などのサブコマンド仕様への入口を探しているとき。
- Codex CLI 連携、設定ファイル、stdout 表示、エラーハンドリング、ログ、Structured Output、`INDEX.md` 自動生成などの仕様を探しているとき。
- src や tests を修正する前に、cmoc 自体の実装規約、設計規約、テスト規約、開発環境ルールへの入口を確認したいとき。

## Do not read this when

- 読むべき個別仕様ファイルやサブディレクトリが既に明確で、最上位のルーティング判断が不要なとき。
- cmoc の実装コードやテストコードだけを直接確認すれば足りるとき。
- `README.md`、`AGENTS.md`、`memo`、`oracles` などの編集可否やリポジトリ運用ルールだけを確認したいとき。
- Codex CLI、git、Python、pytest などの一般的な使い方だけを調べており、cmoc 固有の仕様断片が不要なとき。

## hash

- b1e5bf65266186f38c0d1b61a4ad6f431bf179cf6b85a5834cdd0f611701da5b

# `pyproject.toml`

## Summary

- Python プロジェクト `codex-minimal-outrigger-cli` のパッケージメタデータ、実行環境、依存関係、CLI エントリーポイント、ビルドバックエンド、setuptools のパッケージ探索設定を定義するファイル。
- Python 3.12.3 以上を要求し、依存関係として `pytest` と `typer` を指定している。
- `cmoc` コマンドを `main:main` に対応付け、`src` 配下をパッケージ配置場所として扱う設定を含む。

## Read this when

- cmoc の Python パッケージ名、バージョン、説明、要求 Python バージョンを確認したいとき。
- cmoc の実行時または開発時に使う Python 依存関係を確認したいとき。
- `cmoc` コマンドがどの Python 関数をエントリーポイントとして呼び出すか調べたいとき。
- ビルドシステム、setuptools 設定、`src` レイアウト、`main` モジュールの扱いを確認したいとき。
- 依存追加、CLI エントリーポイント変更、パッケージング設定変更に関わる作業をするとき。

## Do not read this when

- cmoc のサブコマンドの詳細仕様や正本仕様断片へのルーティングを調べたいとき。
- `src` 配下の実装コードの具体的な処理内容を確認したいとき。
- `tests` 配下のテストケースや Fake Codex CLI の詳細を調べたいとき。
- README、AGENTS、oracles、memo などのリポジトリ運用ルールや編集可否だけを確認したいとき。
- cmoc を使って開発する別リポジトリ側の `<repo-root>` の設定やファイル構成を調べたいとき。

## hash

- f7e7dcdc72547ff9b03be0135915cb7c3ae47af0b596744238d91061acd8488e

# `src`

## Summary

- `src` は cmoc 本体の Python 実装を置くディレクトリです。
- トップレベルの `main.py` は Typer ベースの CLI エントリーポイントで、`init`、`branch`、`eval-oracles`、`apply`、`merge` の各サブコマンドを登録し、実処理を `src/sub_commands` 配下へ委譲します。
- `src/sub_commands` は個別サブコマンドの本体実装パッケージで、初期化、作業ブランチ作成、oracle 評価、oracle 変更の実装反映、cmoc ブランチのマージ処理を扱います。
- `src/commons` はサブコマンド横断の共通処理パッケージで、Codex CLI 呼び出し、Structured Output 検証、ログ保存、リトライ、quota 待機、`INDEX.md` 自動メンテナンス、git リポジトリ操作、エラー整形、時間計測、タイムスタンプ生成を提供します。
- CLI の入口、サブコマンド固有ロジック、共通ユーティリティが `main.py`、`sub_commands`、`commons` に分離されています。

## Read this when

- cmoc 本体の実装コード全体の配置を把握し、どのファイルやサブディレクトリを読むべきか判断したいとき。
- cmoc CLI のトップレベル入口、サブコマンド登録、Typer/Click の例外処理、各サブコマンド実装への委譲関係を確認したいとき。
- `cmoc init`、`cmoc branch`、`cmoc eval-oracles`、`cmoc apply`、`cmoc merge` の本体実装がどこにあるか探しているとき。
- Codex CLI 呼び出し、Structured Output、ログ保存、リトライ、quota 待機、`INDEX.md` 自動保守など、複数サブコマンドで共有される処理の入口を探したいとき。
- git リポジトリ探索、ブランチや HEAD の取得、`.cmoc` の git 追跡対象外保証、oracle・実装ファイル列挙、指定パス commit などの共通 repo 操作を調べたいとき。
- 共通エラー型、利用者向けエラーレポート、サブコマンドの共通実行ラッパー、ステップ別時間計測、cmoc 用タイムスタンプ生成の配置を確認したいとき。
- tests 配下の自動テストを読む前に、対応する実装モジュールや責務分担を把握したいとき。

## Do not read this when

- cmoc の正本仕様断片を確認したいだけのとき。その場合は `oracles` 配下の該当 `INDEX.md` から辿ってください。
- cmoc 自体の開発ルール、設計規約、テスト規約、開発環境などを確認したいだけのとき。
- README、AGENTS、oracles、memo の編集可否やリポジトリ運用ルールだけを確認したいとき。
- 自動テスト、pytest fixture、Fake Codex CLI、期待出力など、tests 配下のテスト実装だけを調べたいとき。
- cmoc を用いて開発する対象リポジトリ側の `<repo-root>` の oracle や実装ファイルの内容を調査したいとき。
- Typer、Click、git、Codex CLI、JSON Schema、日時 API などの一般的な使い方だけを知りたいとき。
- 特定の個別モジュールを読むべきことが既に明確で、src 全体のルーティング情報が不要なとき。

## hash

- bc888907c1acb0aa352614b9c499b539f7b202cbbdb2a19f1458931eeecf08a4

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

- `tests` は cmoc 自体の自動テストを置くディレクトリです。
- pytest 共通設定の `conftest.py` により、テスト実行時に `<cmoc-root>/src` が import path の先頭へ追加されます。
- `test_codex.py` は `commons.codex.run_codex_exec` の Codex CLI 呼び出しラッパーを検証し、Structured Output、schema 検証、意味的バリデーション、3 回リトライ、ログ保存、stdout 進捗表示、quota 枯渇時の resume、INDEX メンテナンス呼び出しを扱います。
- `test_indexing.py` は `commons.indexing.maintain_indexes` による `INDEX.md` メンテナンスを検証し、gitignore 対象除外、空ディレクトリ、`build`/`tmp`、非 UTF-8 バイナリ、repo 直下以外の `memo`、既存 INDEX の再生成、Structured Output 不正時のリトライ、最新 INDEX での Codex 非呼び出し、自動コミット対象の限定を扱います。
- `test_repo.py` は `commons.repo` の git リポジトリ共通処理を検証し、repo root 探索、`.cmoc` ignore 保証、oracle・実装ファイル列挙、root `.gitignore` semantics、cmoc ブランチ判定、base commit 記録、変更検出、削除検出、oracle 外未コミット差分拒否を扱います。
- `test_subcommands.py` は `cmoc init`、`cmoc branch`、`cmoc eval-oracles`、`cmoc apply`、`cmoc merge`、Typer エントリーポイント、`bin/cmoc` ランチャーの決定論的な制御ロジックを検証します。
- `test_timestamps.py` は cmoc timestamp と経過時間表示の出力形式を検証します。
- 各テストファイルには一時 git リポジトリ、fake Codex CLI、monkeypatch、capsys、subprocess を使った決定論的なテストパターンが含まれます。

## Read this when

- cmoc 自体の自動テスト全体の配置と、どのテストファイルを読むべきか判断したいとき。
- pytest で `src` 配下の実装を import できる理由や、テスト共通設定を確認したいとき。
- Codex CLI 呼び出し、Structured Output、schema 検証、リトライ、ログ保存、quota resume、INDEX メンテナンス連携のテストを探しているとき。
- `INDEX.md` 自動生成・メンテナンスの除外規則、再生成条件、Codex 呼び出し条件、自動コミット範囲のテストを確認したいとき。
- git repo 共通処理、oracle ファイル列挙、実装ファイル列挙、cmoc ブランチ、base commit、変更・削除検出、gitignore pattern の期待挙動をテストから確認したいとき。
- `cmoc init`、`cmoc branch`、`cmoc eval-oracles`、`cmoc apply`、`cmoc merge` のサブコマンド実装を変更し、既存テストの期待値を把握したいとき。
- Typer の `main.py` command 関数、`cmoc --help` の Usage、サブコマンドエラー時の終了コード、`bin/cmoc` の仮想環境 Python 必須チェックに関するテストを探しているとき。
- タイムスタンプや経過時間表示のフォーマットを変更する前に、既存テストの期待値を確認したいとき。
- 一時 git リポジトリ、fake `codex` 実行ファイル、monkeypatch、capsys を使うテスト実装例を参照したいとき。

## Do not read this when

- cmoc の正本仕様断片を確認したいだけのとき。仕様の入口は `<cmoc-root>/oracles` 配下の `INDEX.md` です。
- cmoc の本体実装コードを直接読みたいとき。実装は `<cmoc-root>/src` 配下を確認してください。
- cmoc のユーザー向け README、利用手順、インストール手順だけを確認したいとき。
- `README.md`、`AGENTS.md`、`oracles`、`memo` の編集可否など、リポジトリ運用ルールだけを確認したいとき。
- pytest、git、Typer、Codex CLI の一般的な使い方だけを調べており、cmoc 固有のテスト期待値が不要なとき。
- cmoc を使って別リポジトリを開発する `<repo-root>` 側の作業手順を知りたいとき。
- 外部 Codex CLI や実際の LLM 出力品質を検証したいとき。このディレクトリの多くは fake や monkeypatch による決定論的テストです。
- `__pycache__` 配下の `.pyc` ファイルを調べたいとき。テストの意味を理解するには対応する `.py` ファイルを読むべきです。

## hash

- 19203ccbb9c230b0b745cf3068a9c466dc10c2b51712112fa200a8cbf3db3e9b
