# `app_specs`

## Summary

- `cmoc` のアプリ仕様断片をまとめた入口です。
- branch model、Codex CLI 呼び出し、ログ出力、エラーハンドリング、`INDEX.md` 生成、雑多な基礎規約、`oracles` の扱い、利用方法を扱います。
- 個別サブコマンドの入口は `sub_commands/INDEX.md` からたどります。

## Read this when

- `cmoc` の共通仕様や、その参照先となる正本断片を確認したいとき。
- `apply`、`session`、`eval-oracles` などの前提になるルールを横断的に見直したいとき。
- どの仕様ファイルを読むべきか、`app_specs` 配下の案内から判断したいとき。
- 個別サブコマンドの入口を含めて、`branch_model`、`codex_call`、ログ、エラー処理、利用方法のどこへ進むべきか整理したいとき。

## Do not read this when

- 個別サブコマンドの手順だけを確認したいときは、`sub_commands/INDEX.md` から該当文書へ直接進むべきです。
- 実装コードやテストコードだけで足りる場合は、このディレクトリの案内を読む必要はありません。
- この配下の単独仕様の本文だけを読みたいときは、該当する `*.md` を直接参照すべきです。

## hash

- 3a42159d1c3bccbdc2941d0687a562aee823b8187ec53a69ceda04accd3cfe3a

# `dev_rules`

## Summary

- `cmoc` の開発ルールをまとめたディレクトリで、Python 実装のコーディング規約、CLI と共通機能の設計方針、開発環境の前提、テスト規約を扱います。
- `coding_rules.md` は型ヒント、import、docstring、コメント、ログメッセージ、非公開識別子などのコーディング規則を定めます。
- `design_rules.md` は `src/main.py`、`src/sub_commands`、`src/commons` の配置方針と、関数分割・並び順の考え方を定めます。
- `development_environment.md` は対象 OS、Python バージョン、`.venv` の扱い、文字コードなどの開発環境前提を定めます。
- `test_rules.md` は pytest を使った自動テストの書き方、配置先、Fake Codex CLI の扱いを定めます。

## Read this when

- `cmoc` の Python 実装やレビューで、基本的なコーディング規約を確認したいとき。
- CLI のエントリーポイント、サブコマンド配置、共有機能の置き場所、関数分割方針を決めたいとき。
- 開発環境、Python バージョン、仮想環境、文字コードなどの前提を確認したいとき。
- pytest ベースの自動テスト方針や、Fake Codex CLI を使う可否を確認したいとき。
- 実装やテストが `dev_rules` のどの規則に従うべきかを切り分けたいとき。

## Do not read this when

- `cmoc` のユーザー向けコマンド手順や各サブコマンドの仕様だけを確認したいとき。
- `branch_model`、`apply`、`eval-oracles` などの個別仕様だけを確認したいとき。
- `INDEX.md` の生成・更新ルールそのものだけを確認したいとき。
- コーディング、設計、開発環境、テストのうち特定の 1 領域だけを深掘りしたいとき。

## hash

- 1e835a1558c2fb915742b32acf8c08aaa309135736f3b7d7f98fb73c9d899318
