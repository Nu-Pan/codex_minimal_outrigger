## session metadata

```json
{
  "session": {
    "schema_version": 1,
    "session_id": "...",
    "session_branch": "cmoc/session/...",
    "session_home_branch": "...",
    "session_start_commit": "...",
    "state": "active | joined | abandoned",
    "created_at": "...",
    "joined_at": null
  },
  "apply_run": {
    "schema_version": 1,
    "session_id": "...",
    "apply_run_id": "...",
    "apply_branch": "cmoc/apply/.../...",
    "apply_worktree": "...",
    "oracle_snapshot_commit": "...",
    "session_head_at_apply_start": "...",
    "session_head_before_merge": "...",
    "apply_head_before_merge": "...",
    "session_head_after_merge": "...",
    "merge_commit": "...",
    "state": "running | apply_completed | merged | merge_pending | merge_conflict | failed",
    "session_advanced_during_apply": true,
    "session_advanced_paths_kind": "oracle_only | non_oracle_included | none"
  }
}
```
