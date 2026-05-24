# `branch_model.md`

## Summary

- `cmoc` の branch model を定義している。通常の local branch を起点に session branch を作り、必要に応じて apply branch を作る流れを説明する。
- `<cmoc-session-home-branch>`、`<cmoc-session-branch>`、`<cmoc-apply-branch>`、`<cmoc-managed-branch>` などの種類と命名規則を整理している。
- 1 つの home branch に対して active な session branch は高々 1 つという原則と、detached HEAD や remote-tracking branch を home branch として扱わないルールを定めている。
- `cmoc apply` は開始時点の session branch HEAD を snapshot として固定し、実行中に session branch が進んでも取り込まないという判定原則を定めている。

## Read this when

- `cmoc session fork` で作る session branch の命名・生成・意味を決めるとき
- `cmoc apply` がどの branch からどの branch を作るか、snapshot をどう固定するかを確認するとき
- session の home branch と managed branch の関係、同時に active になれる session 数の制約を確認するとき

## Do not read this when

- 通常の Git 操作だけを確認したいとき
- `cmoc` の session / apply / branch 管理に関係しない機能を実装・修正するとき
- `<repository-default-branch>` 固有の扱いだけを確認したいとき

## hash

- c87504ed9e45a7ad221b1a6882ab786e193548937aced2a660570093094edac8

# `codex_call.md`

## Summary

- `cmoc` から Codex CLI を呼び出す際の基本方針をまとめた仕様です。
- プロンプトはロール、作業内容、完了条件、任意の詳細という構成にすること、本文は `stdin` で渡すこと、`argv` には載せないことが定められています。
- モデル選択、推論強度、サンドボックス設定、`--json` と `--output-last-message` の必須化、Structured Output の扱い、失敗時のリトライと待機方針も含まれます。

## Read this when

- `codex exec` を呼び出す実装を追加・修正するとき。
- Codex CLI に渡すプロンプトの構成、入力経路、出力形式、失敗時の扱いを確認するとき。

## Do not read this when

- `codex exec` の呼び出し規約やプロンプト生成を変更しないとき。
- Codex CLI ではなく、別の実行基盤や別コマンドの仕様を確認したいとき。

## hash

- bd838ad821fa22f2c811f51ef3663e5235af9a23c9e1f3ca2da0fd043c3bcf08

# `console_and_file_log.md`

## Summary

- サブコマンド実行時のコンソール出力とファイルログ出力の規則を定めている。
- ログはサブコマンド呼び出しと 1 対 1 で対応し、標準出力と `<repo-root>/logs/sub_commands/<time-stamp>.log` の両方へ tee する前提である。
- ステップ開始通知、Codex CLI 呼び出し通知、各種経過時間、サブコマンド戻り値など、運用追跡に必要な項目の出し方を扱っている。
- 時間表示のフォーマットと、途中経過と作業完了レポートを見分けやすくする表示上の要件も含んでいる。

## Read this when

- サブコマンド実行時のコンソール出力とファイルログの両方への出力ルールを確認したいとき。
- `<repo-root>/logs/sub_commands/<time-stamp>.log` のようなログ保存先や、tee の扱いを確認したいとき。
- ステップ開始通知、Codex CLI 呼び出し通知、経過時間表示、戻り値表示のフォーマットを確認したいとき。
- 途中経過レポートと作業完了レポートの境目を見やすくする表示要件を確認したいとき。

## Do not read this when

- `cmoc` のコマンド全体の実行手順や、個別サブコマンドの仕様だけを調べたいとき。
- `oracles` や `INDEX.md` の構成ではなく、エラー処理や設計ルールそのものを確認したいとき。
- コンソール出力やログ出力の細かな表示要件ではなく、別の開発ルールだけを確認したいとき。

## hash

- 7eb84e1d97b41b7321cd2db126adaa399cd400cfb7cba464c2e161acaed1f7ae

# `error_handling.md`

## Summary

- 各仕様に特別な記載がない場合の共通エラーハンドリング規則を定める断片である。
- エラー時はその場で処理を中断し、簡単な説明・次に取るべきアクション・詳細説明・コールスタックを stdout に出力する。
- 終了コードはエラー終了であることがわかる値を返し、個別仕様に指示がある場合はそれに従う。

## Read this when

- 個別仕様に書かれていないエラー時の共通動作を確認したいとき。
- エラー報告で stdout に何を出すべきかを確認したいとき。
- 共通ルールと個別仕様のどちらを優先するかを整理したいとき。

## Do not read this when

- 特定サブコマンドの入出力や実行手順そのものを調べたいとき。
- すでに対象仕様に固有のエラー処理が書かれていて、この共通規則を参照する必要がないとき。
- エラー処理ではなく、設計ルールやコーディング規約だけを確認したいとき。

## hash

- bfaceea1701755cbe1f24db75ea9044ad4d4ed7dc98edef844bc94e39c3bbdf8

# `indexing.md`

## Summary

- `<repo-root>` 上の `INDEX.md` の配置対象ディレクトリ、目次作成対象、除外条件を定義する。
- 各項目の `Summary`、`Read this when`、`Do not read this when`、`hash` のフォーマットと生成ルールをまとめている。
- `INDEX.md` メンテナンス処理の対象、処理順、更新判定、Codex CLI による生成方法、実行タイミングを定義している。

## Read this when

- `<repo-root>` 配下の `INDEX.md` をどのディレクトリに配置し、どう維持するかを確認したいとき
- `INDEX.md` の目次情報のフォーマット、除外対象、ハッシュ更新条件を実装・修正したいとき
- `INDEX.md` 生成時に Codex CLI をどう呼び出し、Structured Output をどう扱うかを確認したいとき
- `INDEX.md` メンテナンスをいつ実行し、いつスキップするかの条件を確認したいとき

## Do not read this when

- `cmoc` の `apply`、`eval-oracles`、`session fork`、`session join` など、`INDEX.md` のメンテナンス以外のサブコマンド仕様を知りたいとき
- `INDEX.md` の内容そのものではなく、実装コードやテストの細部だけを確認したいとき
- `oracles` 全体の設計方針や開発ルールだけを確認したいとき

## hash

- fb9796719c76b94a16efdcb08e7dcb839fcb5754e409f6c9bca0900cd2de47c0

# `misc_specs.md`

## Summary

- `oracles` ファイルと実装ファイルをどう列挙するかの機械的なルールをまとめている。
- `<repo-root>` の仮定、cmoc 実行時のルート探索、カレントディレクトリ変更の規則を扱う。
- `.cmoc` を git 管理から外す理由と、タイムスタンプ形式、`<cmoc-managed-branch>` の定義を整理している。

## Read this when

- `oracles` ファイル列挙の機械的なルールを確認したいとき
- 実装ファイル列挙の対象範囲と除外条件を決めたいとき
- `<repo-root>` の探索方法や、作業時にどこへカレントを移すかを確認したいとき
- `.cmoc` を git 追跡対象外にする必要や、その意図を確認したいとき
- タイムスタンプのフォーマットや、`<cmoc-managed-branch>` の定義を参照したいとき

## Do not read this when

- `cmoc apply`、`cmoc eval-oracles`、`cmoc init`、`cmoc session fork`、`cmoc session join` など個別サブコマンドの手順や引数だけを調べたいとき
- `INDEX.md` の配置対象や目次作成ルールそのものを確認したいときは、`indexing.md` を読むべきであり、この断片は主対象ではないとき
- `oracles` の所有権や編集禁止ルールだけを確認したいときは、`ownership_and_safety.md` を優先したいとき
- cmoc 以外の一般的な Git 運用や実装方針を知りたいだけで、このファイルの前提規則は不要なとき

## hash

- 141025692ce4dfbeee21c77fe3db31b5d2eaa6404da0a8fd3c369f56fc9d30d4

# `ownership_and_safety.md`

## Summary

- `oracles` 配下の `INDEX.md` を除く `*.md` は人間が所有する正本仕様である。
- Codex CLI は `oracles` を読んでよいが、書き込んではいけない。
- cmoc は workspace-write 後に `oracles` の差分がないことを機械的に検査し、差分があれば commit せず失敗する。

## Read this when

- `oracles` ファイルの所有権と編集禁止ルールを確認したいとき。
- workspace-write 後の `oracles` 差分検査と失敗条件を知りたいとき。
- 人間と AI の責務境界や、安全な実装・レビューの前提を確認したいとき。

## Do not read this when

- `oracles` 配下の個別ファイルの仕様内容を知りたいとき。
- `cmoc` の各サブコマンドの入出力や実行手順を調べたいとき。
- 開発環境やコーディング規約など、所有権・安全性以外の共通ルールだけを確認したいとき。

## hash

- 2f45dde9ad4c5abbe5bf884f3c3d3057c08a754ad81cca70ca4285be29ee6cd1

# `session_metadata.md`

## Summary

- session と apply_run に関する metadata の正本仕様断片をまとめた文書。
- session の識別子、ブランチ名、開始 commit、状態、作成時刻、join 時刻、および apply run の識別子、作業ブランチ、各種 commit、状態遷移を扱う。
- session 管理や apply の実装で、metadata の構造とライフサイクルを確認するために参照する。

## Read this when

- `session.json` と `apply` 実行結果に記録される metadata の構造を確認したいとき。
- `session` / `apply_run` の各 `schema_version`、`state`、ブランチ名、commit ID、時刻の意味を確認したいとき。
- `cmoc session fork`、`cmoc session join`、`cmoc apply` の実装で、session metadata の読み書きや状態遷移を扱うとき。

## Do not read this when

- `cmoc init` や `cmoc eval-oracles` など、セッション metadata 以外のサブコマンド仕様だけを確認したいとき。
- `cmoc` 全体のコーディング規約、設計規約、テスト規約だけを調べたいとき。
- `README.md`、`AGENTS.md`、`memo` の運用ルールや編集可否だけを確認したいとき。

## hash

- a707e7b7d7a39d9403d8d6ed4ae5a99d47596697d90f44c76a17bcae2b711fd7

# `sub_commands`

## Summary

- `cmoc apply` の目的、前提条件、反復ループ、マージ、レポート、終了コードを扱う。
- `cmoc eval-oracles` の評価モード、致命的問題の定義、評価レポート生成を扱う。
- `cmoc init` の初期化手順と `.cmoc` を追跡対象外にする保証を扱う。
- `cmoc session fork` の session 開始、ブランチ命名、metadata 保存を扱う。
- `cmoc session join` の session 終了、home branch への merge、conflict 解消を扱う。

## Read this when

- `cmoc apply` の実行順序、要修正点リスト、マージ条件を確認したいとき。
- `cmoc eval-oracles` の評価モード、致命的問題の定義、レポート構成を確認したいとき。
- `cmoc init` で `.cmoc` を git 追跡対象外にする手順を確認したいとき。
- `cmoc session fork` の開始条件、ブランチ命名規則、session metadata 保存を確認したいとき。
- `cmoc session join` の merge 先、conflict 解消手順、session 完了後処理を確認したいとき。

## Do not read this when

- `cmoc apply` 以外のサブコマンド仕様を調べたいとき。
- `cmoc eval-oracles` 以外の評価・レポート仕様を調べたいとき。
- `cmoc init` 以外の初期化やセッション関連仕様を調べたいとき。
- `cmoc session fork` 以外の session 作成系仕様を調べたいとき。
- `cmoc session join` 以外の session  समाप्त了や merge 仕様を調べたいとき。

## hash

- 3a291812279cac808108e2b536a0a2298304b39f97f25b8e6a7c306c9aab15cb

# `usage.md`

## Summary

- `cmoc` は `<cmoc-root>/bin` を `PATH` に追加して `cmoc` コマンドとして呼び出す。
- 最初に 1 回だけ `cmoc init` を実行する前提がある。
- 通常の作業は、ローカルブランチへ移動してから `cmoc session fork` で session branch を作り、`oracles` を更新しつつ `cmoc eval-oracles` で評価し、必要に応じて修正と commit を重ねたうえで `cmoc apply` を実行し、最後に `cmoc session join` で home branch へ merge する流れである。

## Read this when

- `cmoc` をどのように呼び出すか、利用開始の前提を確認したいとき。
- 初回の `cmoc init` と、その後の session ベースの作業手順を把握したいとき。
- `cmoc session fork`、`cmoc eval-oracles`、`cmoc apply`、`cmoc session join` を含む基本ワークフローを確認したいとき。

## Do not read this when

- `cmoc` の各サブコマンドの個別仕様を詳しく確認したいとき。
- `cmoc` の実装方針、設計ルール、テスト規約を調べたいとき。
- `cmoc` の利用方法全体ではなく、特定のサブコマンドだけの入出力や内部手順を知りたいとき。

## hash

- 1acb8c34c04e0211c05442f2a1753897cdb9c7ce8c5849112fdaff932bcc4dba
