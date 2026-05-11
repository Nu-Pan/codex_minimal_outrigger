# `cmot fork`

- コマンド呼び出し時点で git 未コミット差分が有る場合はエラー終了とする
- 既に cmot feature branch をチェックアウトしている場合はエラー終了とする
- git default branch のリモート最新コミットを分岐元として、新規に cmot feature branch を作成・チェックアウトする
- cmot feature branch の命名規則は `cmot_<year>-<month>-<day>_<hour>-<minute>-<sec>` とする
