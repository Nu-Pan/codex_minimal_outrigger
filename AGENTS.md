
# Codex Minimal Outrigger (cmot) - AGENTS.md

## 基本事項

- このリポジトリでは Codex Minimal Outrigger の開発を行う
- Codex Minimal Outrigger は cmot と略す

## パス表記

- このリポジトリのルートパスは `<cmot-root>` と表記する
- cmot コマンドを使用して開発作業を行うリポジトリのルートパスは `<repo-root>` と表記する
- 「cmot 自体の開発」と「cmot を用いた開発」は文脈が全く異なるため、絶対に混同してはいけない

## ファイルアクセス規則

以下のファイルは AI 閲覧・編集禁止

- `<cmot-root>/memo`

以下のファイルは AI 編集禁止

- `<cmot-root>/README.md`
- `<cmot-root>/AGENTS.md`
- `<cmot-root>/oracles`

## `<cmot-root>/oracles`

- cmot の正本仕様断片は `<cmot-root>/oracles` 配下のファイルで述べている
- これはあくまで「断片」であり、 `oracles` に記載の無い「隙間」は実装者である AI の裁量で決めて良い
- `oracles` とそれ以外とがズレている場合は実装の方を合わせる

## ルーティング

- `<cmot-root>/oracles` 配下の各ディレクトリには `INDEX.md` が存在する
- `INDEX.md` には、同階層のファイル・ディレクトリへのルーティング情報が記載されている
- `<cmot-root>/oracles` 配下の正本仕様を調べる際は、 `INDEX.md` のルーティング情報を手がかりに、最低限必要なファイルだけを読むこと
- 作業を始める前に `<cmot-root>/oracles/INDEX.md` を必ず読むこと

## 実装・テスト

- cmot の実装は `<cmot-root>/src` に書く
- cmot の自動テストは `<cmot-root>/tests` に書く
