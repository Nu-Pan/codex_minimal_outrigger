## `<cmoc-session-state-file>`

## 概要

- cmo セッションの最新の状態を記録する json ファイル
- 保存先は `<repo-root>/.cmoc/sessions/<session-id>.json`
- `<cmoc-session-branch>`, `<cmoc-apply-bramch>` の状態遷移のための補助情報として用いる

## スキーマ定義

```json
{
  "session": {
    "schema_version": 1,
    "session_id": "...",
    "session_branch": "cmoc/session/...",
    "session_home_branch": "...",
    "session_start_commit": "...",
    "state": "active | joined | abandoned | error",
    "created_at": "...",
    "joined_at": null
  },
  "apply": {
    "schema_version": 1,
    "apply_id": "...",
    "apply_branch": "cmoc/apply/.../...",
    "apply_worktree": "...",
    "oracle_snapshot_commit": "...",
    "session_head_at_apply_start": "...",
    "session_head_before_merge": "...",
    "apply_head_before_merge": "...",
    "session_head_after_merge": "...",
    "merge_commit": "...",
    "state": "ready | running | completed | error",
    "pid": "...",
    "session_advanced_during_apply": true,
    "session_advanced_paths_kind": "oracles_only | oracles_not_included | none"
  }
}
```

## ステート初期値

`cmoc session fork` によってセッションが新規作成された時の初期値は以下の通り

- `session.state = active`
- `apply.state = ready`
