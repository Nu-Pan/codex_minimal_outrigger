# `cmoc`

## Summary

- `bin/cmoc` は、cmoc コマンドを起動するための実行可能 Python ランチャースクリプトです。
- リポジトリルートを自身の配置場所から解決し、`.venv/bin/python` が存在する場合はその Python で `src/main.py` を再実行します。
- 仮想環境 Python で既に実行中、または `.venv/bin/python` が存在しない場合は、`src` を import path に追加して `main.main` を呼び出します。
- このファイルは CLI 本体の実装ではなく、ユーザーが実行する `cmoc` コマンドから Python 実装へ制御を渡す薄い入口です。

## Read this when

- `cmoc` 実行ファイルがどの Python インタープリタで `src/main.py` を起動するか確認したいとき。
- `.venv/bin/python` が存在する場合の再実行ロジックや `os.execv` の引数構成を調べたいとき。
- `bin/cmoc` から `src/main.py` や `main.main` へ処理が渡る流れを追いたいとき。
- cmoc の CLI 起動時に `src` がどのように import path へ追加されるか確認したいとき。
- 実行可能ファイルとしての shebang、ランチャーの `main()`、`if __name__ == "__main__"` の構造を確認したいとき。

## Do not read this when

- cmoc のサブコマンドの具体的な挙動、オプション、業務ロジックを調べたいとき。
- Typer アプリケーション本体や CLI コマンド定義を確認したいとき。
- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` の仕様や実装詳細を調べたいとき。
- Codex CLI 呼び出し、Structured Output、ログ保存、リトライ、サンドボックス指定などの実行時仕様を調べたいとき。
- cmoc 自体の開発規約、テスト規約、コーディング規約、依存管理方針を確認したいとき。
- `<repo-root>` 側に生成される `INDEX.md` や oracle 評価結果など、cmoc が扱う対象リポジトリ内の成果物について調べたいとき。

## hash

- 45e1e7701b636a1983b642c490a05707855e028005f80723dfefc26685946e8a
