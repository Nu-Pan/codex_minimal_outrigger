# `cmoc`

## Summary

- `bin/cmoc` は cmoc コマンドのシェル版エントリーポイントです。
- スクリプト自身の位置から `<cmoc-root>` を解決し、`<cmoc-root>/.venv/bin/python` を実行用 Python として固定します。
- 仮想環境の Python が実行可能でない場合は、作成手順と `pip install -e .` の案内を stderr に出力して終了ステータス 1 で失敗します。
- 仮想環境が存在する場合は、受け取った引数をそのまま渡して `<cmoc-root>/src/main.py` を `exec` します。
- このファイル自体にはサブコマンド実装や業務ロジックはなく、実処理は `src/main.py` 以下に委譲されます。

## Read this when

- cmoc コマンド起動時に、どの Python とどの main ファイルが実行されるか確認したいとき。
- `.venv/bin/python` が見つからない、または実行できない場合のエラーメッセージや終了挙動を調べたいとき。
- cmoc のインストール直後や開発環境で、仮想環境作成手順の案内がどこから出ているか確認したいとき。
- CLI 引数が `src/main.py` にどのように渡されるかを確認したいとき。
- cmoc のシェルラッパーとしての入口だけを確認し、Python 側の実装に入る前の挙動を把握したいとき。

## Do not read this when

- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` などのサブコマンド仕様や実装詳細を調べたいとき。
- Codex CLI 連携、Structured Output、ログ保存、リトライ、INDEX.md 生成などのアプリケーション仕様を確認したいとき。
- Python 側のルーティング、引数解析、共通エラーハンドリング、サブコマンド実装を読みたいとき。
- 自動テスト、Fake Codex CLI、テスト規約など、cmoc 開発者向けのテスト情報を探しているとき。
- README、AGENTS.md、oracles、memo などのリポジトリ運用ルールや編集可否だけを確認したいとき。

## hash

- a4a6f66b4b3c43b63b77dcaa43620430179b9707ded9a408ef455a4956cb7795
