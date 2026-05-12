# `cmot branch`

## 概要

- これから cmot による開発作業を行うことになる専用 git ブランチである `<cmot-branch>` を作成する
- 実態は git によるブランチ操作のショートカットである。

## 事前条件

- サブコマンド呼び出し時点で満たすべき `cmot branch` 固有の事前条件は無い

## 実行手順

以下のような手順で処理を行う。

```
git checkout -b <cmot-branch>
```

## `<cmot-branch>` の命名規則

- `cmot_<time-stamp>` とする
- ブランチ名が衝突（どう考えても有りえないが）した場合はリトライする
