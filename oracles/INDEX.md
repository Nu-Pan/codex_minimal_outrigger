# `app_specs`

## Summary

- `cmoc` の使用方法、主要ワークフロー、共通ルール、サブコマンド仕様の入口をまとめる。
- `branch_model`、`session_metadata`、`codex_call`、`console_and_file_log`、`error_handling`、`indexing`、`misc_specs`、`ownership_and_safety`、`usage` を扱う。
- `sub_commands/INDEX.md` から `apply` / `eval-oracles` / `init` / `session fork` / `session join` の各仕様へ分岐する起点である。

## Read this when

- `cmoc` 全体の利用フローや、各仕様ファイルの所在を確認したいとき。
- `session` / `apply` / `eval-oracles` / `init` の仕様を調べ始めるとき。
- Codex 呼び出し、ログ、エラー処理、INDEX 運用などの共通ルールを横断確認したいとき。
- `usage.md` や `sub_commands/INDEX.md` を起点に必要な仕様へ辿りたいとき。

## Do not read this when

- 個別サブコマンドの細部だけを確認したいときは、対応する各仕様ファイルを直接読む。
- `oracles` 以外の実装やテスト、設定の確認が目的のとき。
- `README.md` / `AGENTS.md` / `memo` の運用ルールだけを知りたいとき。
- `cmoc` 以外の一般的な Git 運用や別リポジトリの仕様を調べたいとき。

## hash

- 7c0a3afc63387f16da23cf48314181638ca09d47c8e3ec866452ef7004b52348

# `considered_alternatives`

## Summary

- `cmoc apply` に関する採用しなかった設計案と、その不採用理由をまとめた補足索引。
- AI-generated な改善案や記憶を次回実行へ自動注入しない方針の背景を説明している。
- 作業計画レビューよりも、`oracles` を人間が編集し AI が追従する運用を優先する理由を整理している。

## Read this when

- `cmoc apply` で事前計画や修正フローの設計判断を確認したいとき。
- AI の改善案や memory を自動継承しない方針の根拠を知りたいとき。
- `tgbt plan` や `/plan` のような計画レビューを採用しなかった理由を確認したいとき。

## Do not read this when

- `cmoc` 全体の実装コードやテストの場所を探しているだけのとき。
- 別サブコマンドの具体的な入出力仕様や操作手順だけを知りたいとき。
- INDEX.md の生成ルールや共通フォーマットそのものを確認したいとき。

## hash

- bcf28dba25d16038c99f7ffd3f93fe14a061e8da2ff82b110c1a24034e62c0e3

# `dev_rules`

## Summary

- cmoc の開発ルールをまとめたディレクトリで、コーディング規則、設計規則、開発環境、テスト規約を扱う。
- `coding_rules.md` は Python 実装のコーディング規則、型ヒント、import、docstring、コメント、非公開識別子の方針を定める。
- `design_rules.md` は CLI の配置、共通処理の置き場所、関数分割と呼び出し順の方針を定める。
- `development_environment.md` は標準環境、Python 実行環境、`.venv`、ファイルエンコードの方針を定める。
- `test_rules.md` は pytest を前提としたテスト配置と、Fake Codex CLI を用いる範囲を含むテスト方針を定める。

## Read this when

- cmoc の Python 実装におけるコーディング規則を確認したいとき。
- CLI の構成、ファイル配置、共通処理の置き場所など設計ルールを確認したいとき。
- 開発環境、Python 実行環境、仮想環境、ファイルエンコードの前提を確認したいとき。
- pytest を使ったテスト配置や、決定論的な制御ロジックの検証方針を確認したいとき。

## Do not read this when

- cmoc のユーザー向け CLI 仕様やサブコマンド仕様だけを調べたいとき。
- 開発環境、実行方法、テスト実装規約だけを確認したいとき。
- README.md、AGENTS.md、memo などのリポジトリ運用ルールだけを確認したいとき。
- `dev_rules` 以外の `oracles` 配下の正本仕様断片を調べたいとき。

## hash

- 6b574d5dd85f2314cdccf3efcdbaed7c0e5467ab46979c5c50801641b4a17ebe
