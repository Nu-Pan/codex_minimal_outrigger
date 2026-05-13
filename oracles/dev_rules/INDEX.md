# `coding_rules.md`

## Summary

- cmoc の Python 実装における基本的なコーディング規則を定義している。
- PEP 8、明確な命名・責務・入出力、最小限の変更、適切なコメントと NOTE コメントの使い方を定めている。
- 型ヒント必須、Any の抑制、from __future__ import annotations の禁止を定めている。
- src をルートとした import 前提、可能な限り相対 import を使う方針、循環参照回避と TYPE_CHECKING 使用条件を定めている。
- 関数・クラスの Google style docstring、コメントは基本日本語、ログメッセージは英語、非公開識別子は先頭アンダースコアとする規則を定めている。

## Read this when

- cmoc の src 配下に Python コードを実装・修正するとき。
- 型ヒント、import、docstring、コメント、ログメッセージ、非公開識別子の書き方を確認したいとき。
- 実装方針が過剰設計になっていないか、または既存の開発ルールに合っているか確認したいとき。
- コードレビューやテスト追加時に、cmoc のコーディングスタイル上の期待値を確認したいとき。

## Do not read this when

- cmoc のユーザー向け CLI 仕様、サブコマンド仕様、ワークフロー仕様だけを調べたいとき。
- 開発環境のセットアップ、実行方法、テストコマンドなどの環境情報だけを調べたいとき。
- アーキテクチャや設計判断など、コードスタイル以外の設計ルールを調べたいとき。
- README や AGENTS など、リポジトリ全体の運用ルールやファイルアクセス規則だけを確認したいとき。

## hash

- dd1b5890cf9682753d5854bd2e45baf97a54534fbb194bb7dd5867965d6b0c21

# `design_rules.md`

## Summary

- cmoc のコード設計方針を定める開発ルール。
- CLI 実装では typer を使い、エントリーポイントと引数解釈を src/main.py、各サブコマンド本体を src/sub_commands/<sub command name>.py に置く。
- 複数サブコマンドで共有する機能は src/commons 配下に置く。
- 関数分割は基本的に許容するが、1 箇所からしか呼ばれない関数の安易な抽出は避け、同一ファイル内の関数順は caller first, callee last とする。

## Read this when

- cmoc の CLI エントリーポイント、typer 定義、引数解釈、サブコマンド実装の配置を決めるとき。
- src/main.py、src/sub_commands、src/commons 配下の設計や実装方針を確認するとき。
- 新しいサブコマンドを追加するとき、または既存サブコマンドの本体処理をどこに置くか判断するとき。
- 共通ユーティリティ、定数、エラー処理などをどこに実装するか判断するとき。
- 関数分割の粒度や、同一ファイル内での caller/callee の並び順を確認するとき。

## Do not read this when

- cmoc のユーザー向けコマンド仕様、ワークフロー、出力形式などアプリケーション仕様だけを調べたいとき。
- 開発環境、依存関係、テスト実行方法などの環境構築ルールを調べたいとき。
- 特定機能の詳細な正本仕様やサブコマンドの振る舞いを調べたいとき。
- README、AGENTS、oracles などのファイルアクセス制約やリポジトリ運用ルールだけを確認したいとき。

## hash

- d697ddb85156a45dbace4170dc59d13710f941b8db621e38dd5e8e50013d50e9

# `development_environment.md`

## Summary

- cmoc 開発に使う標準環境として、WSL2 Ubuntu 24.04 on Windows 11、VS Code Remote Development、指定 workspace、Codex CLI 利用可能環境を定義している。
- ファイルエンコードは原則 UTF-8 BOM なしで統一し、ツール都合がある場合のみ例外を認める。
- Python は 3.12.3 以上を前提とし、システムワイドの python3 直接使用は venv 作成時以外禁止する。
- Python 仮想環境は <cmoc-root>/.venv を使い、インタプリタは <cmoc-root>/.venv/bin/python、pip は <cmoc-root>/.venv/bin/python -m pip を使う。
- <cmoc-root>/.venv の作成、editable install、依存追加時の pyproject.toml 更新と再インストール手順を定めている。

## Read this when

- cmoc 自体の開発環境、前提 OS、エディタ、workspace、Codex CLI 利用前提を確認したいとき。
- Python コマンド、pip コマンド、仮想環境パス、システム Python 使用可否を判断するとき。
- .venv を新規作成するとき、または .venv に cmoc をインストールするとき。
- 新しい Python 依存パッケージを追加する手順を確認するとき。
- ファイル作成・編集時の文字コード方針を確認するとき。

## Do not read this when

- cmoc のサブコマンド仕様、ワークフロー仕様、CLI 挙動仕様を調べたいとき。
- 実装方針、設計ルール、コーディング規約など、開発環境以外の開発ルールを調べたいとき。
- 特定機能のテスト仕様、入出力仕様、エラー仕様を調べたいとき。
- README、AGENTS、oracles の編集可否やリポジトリ全体のファイルアクセス規則を確認したいとき。

## hash

- 18bc19e57ac055a39bbf07444976bae25fee0421e8f94826e57686d03f076a74

# `test_rules.md`

## Summary

- cmoc のテスト実装規約を定義している。
- pytest を使用し、テストは `<cmoc-root>/tests` に実装する。
- 正規の Codex CLI の正常動作に依存するテストは禁止し、Fake Codex CLI を使うテストは許可する。
- cmoc の決定論的な制御ロジックを仕様どおり検証することをテスト目的とする。
- Codex CLI や LLM 自体の挙動や出力品質は自動テストの対象外とする。

## Read this when

- cmoc の自動テストを追加・修正するとき。
- テスト対象を cmoc の制御ロジックにするべきか、Codex CLI や LLM の挙動にするべきか判断するとき。
- Fake Codex CLI を使ったテスト設計の可否を確認するとき。
- pytest や `<cmoc-root>/tests` に関するテスト配置ルールを確認するとき。

## Do not read this when

- cmoc のプロダクト仕様やサブコマンド仕様だけを調べたいとき。
- テストではなく本体実装のコーディング規約や設計規約を確認したいとき。
- README、AGENTS、oracles の編集可否などリポジトリ運用ルールを確認したいとき。
- Codex CLI や LLM の実際の出力品質を評価する手順を探しているとき。

## hash

- 3e08d595cf86d05cce430fb097a721a58e5618a082bd861900a276713c1c2783
