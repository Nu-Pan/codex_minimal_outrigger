## oracles ファイル

## 「oracles ファイル」の定義

正本仕様中で「oracles ファイル」と言った場合、それは以下の条件をすべて満たしたファイルの事を指す

- `<repo-root>/oracles` 配下である（サブディレクトリを含む）
- `<repo-root>/.gitignore` の対象ではない
- `INDEX.md` ではない

## oracles ファイルの役割

- oracles ファイルは人間が所有し 100% の責任を負う正本仕様である
- oracles ファイルの内容について AI は提案を行うことは出来るが、実際の編集を行うのは必ず人間である
- oracles を正本仕様として実装が生成されるものとし、その逆は禁止である

## oracles ファイルと自動処理規則

- Codex CLI は oracles ファイルを読んで良いが、書き換えてはいけない
- Codex CLI は `<repo-root>/oracles` 配下の非 oracles ファイル (e.g. `INDEX.md`) を読み書きして良い
- Codex CLI の workspace-write 実行後、cmoc は  oracles ファイルに差分がないことを機械的に検査する
- oracles ファイルに差分が発生した場合、cmoc はの場でコマンドを失敗させる
