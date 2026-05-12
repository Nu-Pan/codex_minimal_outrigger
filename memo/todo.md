# eval_oracles の部分チェック版が欲しい

- cmot branch 上の oracles の更新内容を元に、その周辺だけチェックする軽量版が欲しい
- 修正・再チェックの反復をするのに、全チェックは重たすぎる
- cmot fork で未コミットの差分はそのまま引き継ぐ感じにしたいかも（コミットを移動するわけじゃないのだし）
- `cmot eval-oracles --full`, `cmot eval-oracles` の二本立てか

# INDEX.md

- INDEX.md の自動構築機能係を cmot に組み込む
- 機械的検査を組み合わせて、リポジトリに一切変更がなければルーティング情報生成 (`codex exec` 呼び出し) も走らないようにする
- ここらへんの仕様は `tgbt` のものをそのまま持ち込む

# 名前変える

- Codex Minimal Outrigger CLI にする
