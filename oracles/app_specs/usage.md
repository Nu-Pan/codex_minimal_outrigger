# cmot 使用方法

## エンドユーザーが cmot を呼び出す方法

- `<cmot-root>/bin` を環境変数 `PATH` に追加し `cmot` コマンドで呼び出すものとする

## 想定ワークフロー

※以下は全て `<repo-root>` 上での操作

1. 人間が分岐元となる git commit に移動する
2. 人間が git 未コミット差分が無いクリーンな状態にする
3. 人間が `cmot branch` を呼び出す
4. 記述・実装ループ
    1. 人間がやってほしいと思っている事を `<repo-root>/oracles` に反映（e.g. 正本仕様を追加）
    2. `<repo-root>/oracles` 修正ループ
        1. 人間が `cmot eval-oracles` を呼び出して、評価レポートを読む
        2. 人間が現状の `<repo-root>/oracles` で問題なしと判断したら、ここでループ終了
        3. 人間が `<repo-root>/oracles` の内容を修正
        4. ループ先頭に戻る
    3. 人間が `cmot apply` を呼び出して、作業レポートを読む
    4. 人間が現状の実装で問題なしと判断したら、ここでループ終了
    5. ループ先頭に戻る
5. 人間がマージ先 git commit に移動する
6. 人間が `cmot merge` を呼び出す
