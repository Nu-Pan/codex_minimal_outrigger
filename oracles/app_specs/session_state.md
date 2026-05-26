## `<cmoc-session-state-file>`

## 概要

- cmoc ワ―フロー上発生する fork, join の挙動を一意に定めるための情報をファイル永続化するための json ファイル
- 保存先は `<repo-root>/.cmoc/sessions/<session-id>.json`

## スキーマ定義

※ファイル永続化しなくてもその場その場で解決可能な情報は持たせない方針

```json
{
  "session": {
    "state": "active | joined | abandoned | error",
    "session_home_branch": "...",
    "session_start_commit": "..."
  },
  "apply": {
    "state": "ready | running | completed | error",
    "apply_branch": "cmoc/apply/.../...",
    "oracle_snapshot_commit": "..."
  }
}
```

## ステート初期値

`cmoc session fork` によってセッションが新規作成された時の初期値は以下の通り

- `session.state = active`
- `apply.state = ready`

## `apply.state` が `ready` に遷移した時の初期化処理

- `apply.state` が `ready` に遷移した時、 `apply` セクションの `state` を除く各フィールドは null で初期化する
