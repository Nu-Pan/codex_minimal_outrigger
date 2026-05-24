## oracle ownership

- `<repo-root>/oracles` 配下の `oracles` ファイル (`INDEX.md` を除く `*.md` ファイル) は人間が所有する正本仕様である。
- Codex CLI は `<repo-root>/oracles` を読んでよい
- Codex CLI は `oracles` ファイルに書き込んではいけない
- cmoc は Codex CLI の workspace-write 実行後 `oracles` ファイルに差分がないことを必ず機械的に検査する。
- `oracles` ファイルに差分が発生した場合、cmoc はその差分を commit せず、コマンドを失敗させる。
