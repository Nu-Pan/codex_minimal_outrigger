# eval_oracles の部分チェック版が欲しい

- cmot branch 上の oracles の更新内容を元に、その周辺だけチェックする軽量版が欲しい
- 修正・再チェックの反復をするのに、全チェックは重たすぎる
- cmot fork で未コミットの差分はそのまま引き継ぐ感じにしたいかも（コミットを移動するわけじゃないのだし）
- cmot eval-oracles-full, cmot eval-oracles の二本立てか

# ログ関係

- stdout には要約だけ欲しい
- サブコマンドの実行ログはファイルに tee してほしい

- 問題起きたっぽい時に

# INDEX.md

- INDEX.md の自動構築機能係を cmot に組み込む
