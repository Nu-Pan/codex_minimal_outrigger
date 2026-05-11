# cmot 使用方法

## エンドユーザーが cmot を呼び出す方法

- `<cmot-root>/bin` を環境変数 `PATH` に追加し `cmot` コマンドで呼び出すものとする

## 想定ワークフロー

1. 人間が `<repo-root>` の git 未コミット差分が無いクリーンな状態にする
2. 人間が `cmot fork` を実行
3. 人間がやってほしいと思っている事を `<repo-root>/oracles` に反映（e.g. 正本仕様を追加）
4. `<repo-root>/oracles` 修正ループ
    1. 人間が `cmot eval-oracles` を呼び出して、評価レポートを読む
    2. 人間が現状の `<repo-root>/oracles` で問題なしと判断したら、ここでループ終了
    3. 人間が `<repo-root>/oracles` の内容を修正
    4. ループ先頭に戻る
5. 人間が `cmot apply` を呼び出して、作業レポートを読む
6. 現状の実装に人間が満足しなければ「4. `<repo-root>/oracles` 修正ループ」に戻る
7. 人間が `cmot merge` を呼び出す
