# `cmot apply`

## サブコマンド仕様

- cmot feature branch 上に居なければエラー終了とする
- `<repo-root>` の実装を `<repo-root>/oracles` で記述している仕様断片に追従させる
- 作業開始前に...
    - 未コミット差分が `<repo-root>/oracles` 配下だけなら自動コミットして続行
    - `<repo-root>/oracles` の外の未コミット差分があればエラー終了する
- 具体的には以下の手順を最大３回繰り返す
    1. `<repo-root>/oracles` と実装との明確なズレを調査
    2. ズレがなければこの時点でループ終了
    3. 「`<repo-root>` の実装を `<repo-root>/oracles` に追従させてください。」を codex にやらせる（この時、ズレ調査結果を一緒に渡す）
    4. 発生した差分を git にコミット（コミットメッセージは codex で適切なものを生成）
    5. 1. に戻る
- 作業完了後、結果をレポートする
    - レポートは「現状の cmot feature branch を default branch のリモート最新コミットにマージした時の変更内容の要約」を書く（この `cmot apply` で行った作業内容の要約ではない）
    - レポート本体は `<repo-root>/.cmot/reports/apply/<time-stamp>.md` にファイルに保存する
    - レポート執筆は codex にやらせる
    - レポートのフルパスを標準出力に流す

## `<repo-root>/oracles` と実装との明確なズレを調査する方法

- `<repo-root>/oracles` ファイルごとに「`<repo-root>/oracles` ファイルと実装との明確な差異が無いかを確認して、差異とその説明を報告してください」を codex にやらせる
- 確認結果を１つのファイルにして、これを「`<repo-root>/oracles` と実装の差異」とする
