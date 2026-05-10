
# Codex Minimal Outrigger (cmot) - AGENTS.md

## 基本事項

- このリポジトリでは Codex Minimal Outrigger の開発を行う
- Codex Minimal Outrigger は cmot と略す
- cmot は Codex CLI を用いた開発を補助する外殻ツールである
- cmot が目指すこと
    - Codex CLI の機能を信用して cmot 側の実装は限りなく薄くする
    - 操作対象リポジトリの Codex CLI 挙動設定を最大限尊重し cmot では介入しない
    - 「特定の開発ワークフローに強く結びついた定型処理」のショートカットを cmot のサブコマンドとして提供する

## パス表記

- このリポジトリのルートパスは `<cmot-root>` と表記する
- cmot コマンドを使用して開発作業を行うリポジトリのルートパスは `<repo-root>` と表記する
- 「cmot 自体の開発」と「cmot を用いた開発」は文脈が全く異なるため、絶対に混同してはいけない

## AI 行動原則

- `<cmot-root>/AGENTS.md` は AI 編集禁止
- `<cmot-root>/oracles` 配下は AI 編集禁止

## `oracles`

- cmot の正本仕様断片は `<cmot-root>/oracles` 配下の `*.md` ファイルで記載する
- これはあくまで「断片」であり、 oracles に記載の無い「隙間」は AI の裁量で決めて良い

## ファイル・ディレクトリ目次

- `<cmot-root>/bin`
    - エンドユーザー公開用バイナリディレクトリ
- `<cmot-root>/oracles/docs`
    - cmot の断片的な正本仕様の文章
- `<cmot-root>/oracles/docs/app_spec.md`
    - cmot のアプリケーション仕様を述べている
- `<cmot-root>/oracles/docs/code_design.md`
    - cmot のソフトウェア的な抽象設計を述べている
- `<cmot-root>/oracles/docs/coding_rule.md`
    - cmot を実装する上での基本的なコーディング規約を述べている
- `<cmot-root>/oracles/docs/development_environment.md`
    - cmot を開発する環境について述べている
- `<cmot-root>/src`
    - ソースファイルの配置先

## テスト

- `<cmot-root>` 配下には自動テストは用意しない
