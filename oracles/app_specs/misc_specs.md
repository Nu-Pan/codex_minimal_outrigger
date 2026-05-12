
# cmot の雑多な仕様

## `oracles` ファイルの列挙方法

- 「`oracles` ファイルを列挙」と言った場合、以下の方法で機械的に列挙する
    - `<repo-root>/oracles` 配下の全てのファイルを glob する（拡張子で制限しない）
    - `<repo-root>/.gitignore` の対象は除外
    - `INDEX.md` は除外

## `<repo-root>` に対する仮定

cmot による操作対象リポジトリである `<repo-root>` は以下の要件を満たすものと仮定する

- git で管理されている
- `<repo-root>/oracles` 配下に断片的な正本情報が記載されている（`<cmot-root>` 配下がそうであるように）
- `<repo-root>` に固有の作業のノウハウは全てリポジトリ上で実装済みである
    - 言い換えれば cmot が無くても Codex CLI の直接利用でも作業を完遂出来るように `<repo-root>` がメンテナンスされている事を仮定する
    - e.g.
        - 「`<repo-root>/oracles` 配下のファイル別に `codex exec` セッションを起動する責任」は cmot が負う
        - 「開発必要な特定のツールの使用方法を説明する責任」は cmot ではなく `<repo-root>/.agents/skills` が担う

## cmot 実行時のカレントディレクトリ

- cmot が呼び出された時のカレントを起点に、ルートに向けて「直下に `.git` ファイル・ディレクトリを持つディレクトリ」を探索する
- 最初に見つかったディレクトリを `<repo-root>` とする
- cmot 実行時のカレントは必ず `<repo-root>` に変更する

## `<repo-root>/.cmot`

- `<repo-root>/.cmot` は git の追跡対象外とする
- このことは `cmot init` で保証される
- `<repo-root>/.cmot` 配下のログファイルが未コミット差分として現れて、各サブコマンドの処理が狂ってしまう可能性を排除するための仕様である

## タイムスタンプのフォーマット

- タイムスタンプ `<time-stamp>` はフォーマット `<year>-<month>-<day>_<hour>-<minute>_<sec>_<msec>` に従うものとする
- month/day/hour/minute/sec/msec はゼロ埋めする
- timezone はそのマシンのローカルとする
