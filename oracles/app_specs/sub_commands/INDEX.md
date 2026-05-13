# `apply.md`

## Summary

- `cmoc apply` サブコマンドの仕様を定義している。
- `<repo-root>` の実装を `<repo-root>/oracles` の正本仕様断片へ追従させるための前提条件、作業手順、ループ処理、レポート出力、終了コードを扱う。
- ズレ調査を Codex CLI に oracle ファイル単位で依頼し、Structured Output の `discrepancies` 配列として受け取る schema を定義している。
- ズレ追従作業、最大5回の反復、編集禁止領域の差分検出、コミット、作業レポート保存先の仕様を定義している。

## Read this when

- `cmoc apply` の実装、修正、テストを行うとき。
- `<repo-root>/oracles` と実装のズレを検出する処理や Structured Output schema を確認するとき。
- `cmoc apply` が Codex CLI をどのように呼び出して調査・追従・レポート作成を行うべきか確認するとき。
- `cmoc apply` の事前条件、未コミット差分の扱い、自動コミット、ループ回数上限、終了コードの仕様を確認するとき。
- `<repo-root>/.cmoc/reports/apply/<time-stamp>.md` に保存する作業レポートの内容や標準出力の仕様を確認するとき。

## Do not read this when

- `cmoc apply` 以外のサブコマンド仕様だけを調べているとき。
- cmoc 自体の開発ルール、設計ルール、環境構築手順を調べているとき。
- `oracles` のルーティング規則や INDEX.md の書き方だけを調べているとき。
- Codex CLI に依頼する一般的な実装作業の仕様で、`cmoc apply` のズレ調査・追従ループ・レポート出力に関係しないとき。

## hash

- 4653b4ae85942f593f585a36c469f6e1aa65955e886d492509844a2f6a108cc4

# `branch.md`

## Summary

- `cmoc branch` サブコマンドは、cmoc による開発作業専用の git ブランチ `<cmoc-branch>` を作成するためのショートカットである。
- 引数はなく、サブコマンド固有の事前条件もない。
- 実行手順は `git checkout -b <cmoc-branch>`、`<repo-root>/.cmoc` を git 追跡対象外にする保証、`<repo-root>/.cmoc/branch/<cmoc-branch>.txt` への作成元コミットハッシュ記録である。
- `<cmoc-branch>` は `cmoc_<time-stamp>` 形式で命名し、衝突した場合はリトライする。

## Read this when

- `cmoc branch` サブコマンドの仕様、引数、事前条件、実行手順を実装または確認するとき。
- cmoc が作成する作業用ブランチ `<cmoc-branch>` の命名規則を確認するとき。
- `<repo-root>/.cmoc/branch/<cmoc-branch>.txt` に記録する内容や、ブランチ作成元コミットの扱いを確認するとき。
- `<repo-root>/.cmoc` を git の追跡対象外にする処理が `cmoc branch` に必要か確認するとき。

## Do not read this when

- cmoc のサブコマンド全般の一覧や共通仕様だけを調べたいとき。
- `cmoc branch` 以外のサブコマンドの引数、実行手順、振る舞いを調べたいとき。
- cmoc 自体の開発ルール、コーディング規約、テスト方針、設計方針を調べたいとき。
- `<repo-root>` ではなく `<cmoc-root>` 側のリポジトリ構造や開発作業について調べたいとき。

## hash

- 9eba833d96e6456d7729e92f661147f756eba666ef19fdfd4bf269a8b69c35a9

# `eval-oracles.md`

## Summary

- `cmoc eval-oracles` subcommand specification.
- Defines that the command evaluates whether `<repo-root>/oracles` contains fatal problems and reports the results to humans.
- Documents arguments: no positional arguments, optional `--full` / `-f` flag.
- Defines partial versus full evaluation mode selection based on whether the current branch is `<cmoc-branch>` and whether `--full` is supplied.
- Specifies the execution flow: ensure `<repo-root>/.cmoc` is untracked, list oracle files, optionally narrow to changed oracle files, evaluate each file with one `codex exec` call, then aggregate a report.
- Defines changed oracle files for partial mode as the union of committed changes since the branch source commit plus unstaged and staged changes under `<repo-root>/oracles`, excluding deleted files and using post-rename paths.
- Defines fatal problems as specification issues that could break major workflows, prevent completion judgment, or prevent judging that cmoc's core purpose is met when implementing from specs alone.
- Specifies report format as YAML frontmatter with environment and prerequisites followed by concatenated per-file evaluation results.
- Specifies report output location as `<repo-root>/.cmoc/reports/eval-oracles/<time-stamp>.md` and requires printing the full report path to stdout.

## Read this when

- Implementing or modifying the `cmoc eval-oracles` subcommand.
- Working on oracle evaluation behavior, including how oracle files are selected for evaluation.
- Implementing branch-dependent partial versus full evaluation mode selection for oracle checks.
- Implementing the `--full` or `-f` option for oracle evaluation.
- Defining or changing how changed files under `<repo-root>/oracles` are detected, including staged, unstaged, committed, deleted, or renamed files.
- Building the `codex exec` prompt or execution loop used to evaluate oracle files.
- Changing the definition or handling of fatal oracle specification problems.
- Implementing or changing eval-oracles report generation, report frontmatter, report body formatting, report storage path, or stdout output.

## Do not read this when

- Working on subcommands other than `eval-oracles` with no interaction with oracle evaluation.
- Looking for general cmoc development rules, coding conventions, or environment setup.
- Looking for the overall oracle directory routing structure rather than this specific subcommand behavior.
- Working on cmoc behavior unrelated to `<repo-root>/oracles` validation or reporting.
- Needing user-facing README documentation rather than canonical application specification fragments.
- Investigating implementation details that are not governed by the eval-oracles command specification.

## hash

- 858222ca2661460b5c9c78a12d18b431b8799badbed24abe9ab2f8ccd0f4dcc5

# `init.md`

## Summary

- `cmoc init` initializes `<repo-root>` so it can be used for cmoc-based development.
- `cmoc init` takes no arguments and has no init-specific preconditions.
- The command adds `<repo-root>/.cmoc` to `<repo-root>/.gitignore` if it is not already present.
- After making the initialization change, the command commits the resulting diff with git.

## Read this when

- You are implementing, changing, or testing the `cmoc init` subcommand.
- You need to know what repository changes `cmoc init` must perform.
- You need to verify the argument behavior or preconditions for `cmoc init`.
- You need to understand whether `cmoc init` should create a git commit.

## Do not read this when

- You are working on a different cmoc subcommand and do not need `init` behavior.
- You are investigating general cmoc workflow, development rules, or design rules rather than `cmoc init`.
- You only need routing information for the broader `app_specs` or `sub_commands` directories.
- You are working on cmoc's own repository setup rather than how `cmoc init` prepares a target `<repo-root>`.

## hash

- d9a764e4ce63910f584219e4bee47ee9a3be6d016a82504f9da14d245ed66f29

# `merge.md`

## Summary

- `cmoc merge` サブコマンドの正本仕様断片。`<cmoc-branch>` を現在の `HEAD` にマージし、コンフリクト解決支援まで扱う。
- 引数として省略可能な `<cmoc-branch>` を受け取り、省略時は未マージかつ命名規則に合うローカルブランチから best effort で自動解決する。
- 実行前にマージ先へ移動済みであること、未コミット差分がないこと、`<repo-root>/.cmoc` が git 追跡対象外であることを前提・確認する。
- `git merge` がコンフリクトした場合は Codex CLI に conflict marker 解消を依頼し、cmoc 側で marker 残存確認、対象ファイルの `git add`、unmerged path 確認、merge commit 作成を行う。
- 想定外の失敗時はロールバックせず処理を打ち切り、手動解決が必要なことを stderr で通知する。
- `<cmoc-branch>` の削除は作業結果が失われない安全性の裏付けが取れた場合のみ実行し、確認失敗時は warning として残す。

## Read this when

- `cmoc merge` サブコマンドの実装・修正・テストを行うとき。
- マージ元 `<cmoc-branch>` の引数仕様、自動解決条件、候補絞り込みロジックを確認するとき。
- マージ実行前の precondition、未コミット差分チェック、`.cmoc` の git 追跡除外保証を扱うとき。
- git merge のコンフリクト発生時に Codex CLI へ依頼する範囲、cmoc 側で行う `git add` や unmerged path 確認、merge commit 作成手順を確認するとき。
- マージ失敗時や想定外エラー時のロールバックしない挙動、stderr 通知方針を実装・検証するとき。
- マージ完了後に `<cmoc-branch>` を削除してよい条件や、削除できない場合の warning 挙動を確認するとき。

## Do not read this when

- `cmoc merge` 以外のサブコマンド仕様を調べたいだけのとき。
- cmoc 全体の設計、開発ルール、ディレクトリ構成、コーディング規約を調べるとき。
- Codex CLI の一般的な起動方法、プロンプト設計全般、または merge 以外の Codex 連携仕様を調べるとき。
- git の一般的な merge 操作やコンフリクト解決方法だけを調べるとき。
- `<cmoc-branch>` の命名規則そのものの正本仕様を調べるとき。ただし merge の自動解決で命名規則を利用する文脈では読む。
- README、AGENTS、oracles の編集可否など、リポジトリ運用ルールを確認するとき。

## hash

- f8c2bba0366f1460bfe8cb568ea929626bd5d49cbd128aca62c140c2fee1a56f
