# `cmoc`

## Summary

- `bin/cmoc` は cmoc CLI を起動するための POSIX shell 製ラッパースクリプトです。
- スクリプト自身の場所から `<cmoc-root>` を解決し、`<cmoc-root>/.venv/bin/python` を cmoc 実行用 Python として使用します。
- 仮想環境 Python が存在しない、または実行可能でない場合は、日本語のエラーレポート、次の対応、必要な実行ファイル、セットアップ手順、呼び出し箇所を stdout に出力して終了ステータス 1 で終了します。
- 仮想環境 Python が実行可能な場合は、`exec` により `<cmoc-root>/src/main.py` をその Python で起動し、受け取った引数をそのまま引き渡します。

## Read this when

- cmoc コマンドの実行入口がどこで、どの Python とどの main ファイルを起動するか確認したいとき。
- `.venv/bin/python` が見つからない場合のエラーメッセージ、セットアップ案内、終了ステータスを調べたいとき。
- `bin/cmoc` から `<cmoc-root>` をどのように算出しているか確認したいとき。
- cmoc の CLI 起動時にユーザー指定の引数が `src/main.py` へどう渡されるか確認したいとき。
- 仮想環境未セットアップ時の初期導線やトラブルシュート表示を修正・テストしたいとき。

## Do not read this when

- cmoc のサブコマンド本体、引数解析、業務ロジック、Codex CLI 連携など `src/main.py` 以降の実装を調べたいとき。
- cmoc の正本仕様断片、開発規約、テスト規約、アプリケーション仕様を調べたいとき。
- Python パッケージ設定、依存関係、仮想環境の作成方法そのものを詳しく調べたいとき。
- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` など個別サブコマンドの挙動を確認したいとき。
- cmoc を用いて開発する `<repo-root>` 側のファイル探索、oracle 処理、INDEX.md 生成、git 操作の詳細を調べたいとき。

## hash

- 62fe294f1a015c92004e32b18bb98eb7cb91487375005bec22aaaae6e7a7e092
