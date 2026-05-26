# `apply_abandon.md`

## Summary

- `cmoc apply abandon` の仕様断片をまとめた入口です。未 join の apply run の破棄条件、破棄対象、状態遷移、cleanup 失敗時の扱いを確認するために読む文書です。

## Read this when

- 現在の session に紐づく未 join の apply run を破棄する `cmoc apply abandon` の仕様を確認したいとき
- `apply.state` の遷移、破棄対象の branch/worktree、cleanup の手順を実装・修正したいとき
- warning や report 出力、終了コードの扱いを確認したいとき

## Do not read this when

- `cmoc apply abandon` 以外の apply 系サブコマンドの仕様を確認したいとき
- session の終了や破棄、あるいは join/fork の挙動を確認したいとき
- branch model や共通エラー処理など、apply 破棄と直接関係しない仕様を確認したいとき

## hash

- 6f9d6adc8afe08c8d35332e4d1f9dd87fd90b163748360e7e2f2066b71e70c45

# `apply_fork.md`

## Summary

- `cmoc apply` の開始から完了レポートまでを扱うサブコマンド仕様。
- 調査・修正ループ、作業用ブランチ／worktree、評価対象スナップショット、レポート境界をまとめる。

## Read this when

- `cmoc apply` の引数、事前条件、実行フロー、完了条件を確認したいとき。
- `<cmoc-apply-branch>` と `<cmoc-apply-worktree>` の生成・利用・削除ルールを確認したいとき。
- 開始時点の `<oracle-snapshot-commit>` に固定した調査・修正ループや、要修正点リストの Structured Output 仕様を確認したいとき。
- 部分適用モードと全体適用モードの違い、反復回数のデフォルト値、レポート内容を確認したいとき。

## Do not read this when

- `cmoc session fork` の作成条件、ブランチ命名、session metadata 保存を確認したいとき。
- `cmoc session join` の merge 手順や session 終了処理を確認したいとき。
- `cmoc apply join` のマージ、差分検査、`--force-resolve` の挙動を確認したいとき。
- `cmoc apply abandon` の破棄手順や cleanup 挙動を確認したいとき。
- `cmoc eval-oracles` の評価モードや評価レポート仕様を確認したいとき。

## hash

- 09c59bbaac649c923ef7a64b404dc44d9053c510cf8a189fa6755123db4877aa

# `apply_join.md`

## Summary

- `cmoc apply join` は、`apply fork` で作成された成果物をセッション本流に取り込むコマンドの仕様を定義する。
- 処理対象はブランチの checkout、想定外の差分の記録または revert、`git merge --no-ff` による統合、セッション状態ファイルの更新、結果レポートである。
- マージコンフリクトは原則想定せず、発生時は解決せずにユーザーへ報告する。
- 一定条件を満たした場合にのみ、`<cmoc-apply-branch>` と `<cmoc-apply-worktree>` を削除できる。

## Read this when

- `cmoc apply join` の仕様、引数、事前条件を確認したいとき
- `<cmoc-apply-branch>` を `<cmoc-session-branch>` にマージする手順を実装・修正したいとき
- 想定外の差分の検出、通常モード/強制モードの分岐、マージ後の状態更新を扱いたいとき
- 使用済みブランチと apply worktree の削除条件を確認したいとき

## Do not read this when

- `cmoc apply join` の挙動ではなく、`cmoc apply fork` の生成処理を理解したいとき
- セッション開始・終了や abandon 系のフローを確認したいとき
- ブランチモデルや状態ファイルの基本仕様だけを確認したいとき

## hash

- 6713930f4d948ff9f97cfea0dbbe1d41e848b70ea8fb3ebc138c05f471e81753

# `eval_oracles.md`

## Summary

- 現在の `<repo-root>/oracles` スナップショットを仕様だけで評価し、致命的問題の有無を人間に報告する `cmoc eval-oracles` の仕様である。
- 部分評価・全体評価の切り替え、対象 oracle の列挙と絞り込み、1 ファイルずつの評価、レポート集約の流れを定める。
- 評価レポートの Structured Output schema、Markdown レポートの必須セクション、結果の表示方法を定める。

## Read this when

- `cmoc eval-oracles` の挙動、引数、実行モード、終了時のレポート形式を確認したいとき。
- oracles ファイル群を `oracles/INDEX.md` からたどって、どの関連仕様を評価根拠に読むべきか判断したいとき。
- 致命的問題の定義や、ファイルごとの評価結果をどの Structured Output で返すかを確認したいとき。
- 評価レポートの項目、集約順序、保存先ディレクトリの仕様を確認したいとき。

## Do not read this when

- `cmoc apply`、`cmoc session fork`、`cmoc session join`、`cmoc session abandon` など、評価以外のサブコマンド仕様を知りたいとき。
- 実装ファイルやテストファイルを読んで挙動を推測したいとき。
- oracles 自体の編集方針や内容を決めたいときは、各対象 oracle とその `INDEX.md` を読むべきであり、このファイルは読まなくてよい。
- `INDEX.md` メンテナンス処理そのものの仕様を確認したいときは、`app_specs/indexing.md` を参照すべきであり、このファイルは主目的ではない。

## hash

- c6fc1a9a9f7c102b3ebdb603e5b87fd0e8a872880670743334f0a2af949b8ab5

# `init.md`

## Summary

- `cmoc init` は `<repo-root>` を cmoc による作業が可能な状態に初期化するサブコマンドである。

## Read this when

- `cmoc init` の実装・修正・テスト・レビューを行うとき。
- `<repo-root>/.cmoc` を git 追跡対象外にする処理や、`.gitignore` 更新、`git ls-files` / `git check-ignore` による確認仕様を扱うとき。
- 初期化後に続く session/apply 系コマンドの前提条件として、リポジトリ初期化の振る舞いを確認したいとき。

## Do not read this when

- `cmoc init` 以外のサブコマンドや、その周辺の実装・テストだけを扱っているとき。
- `.cmoc` の git ignore 追加や tracked ファイルの追跡解除が論点に含まれないとき。
- 初期化後の session/apply の運用仕様だけを確認したいとき。

## hash

- b3b7cca844c91f7ba5a4e8d4592f0c2fb5510aa4ab31fbb1c114b7fd62574175

# `session_abandon.md`

## Summary

- `cmoc session abandon` は、現在の `<cmoc-session-branch>` を `<cmoc-session-home-branch>` に merge せず破棄するコマンドの仕様をまとめている。
- `cmoc session join` と異なり、session の成果物を本流へ取り込まず、既に join 済みの結果を取り消す rollback でもない。
- 実行には session が active であること、apply が ready であること、未コミット差分がないことなどの前提条件がある。

## Read this when

- 現在の `cmoc-session-branch` を merge せずに破棄したいとき。
- `session.state` や `apply.state` の前提条件、破棄対象、状態遷移を確認したいとき。
- `cmoc session abandon` を実装・修正・テストするとき。

## Do not read this when

- `cmoc session fork` の仕様だけを調べたいとき。
- `cmoc session join` の仕様や、session を merge して完了させる流れだけを確認したいとき。
- `cmoc apply abandon` など、apply run の破棄仕様だけを確認したいとき。

## hash

- 507316f4bbe764dc9e6ccf3e64c3a01db78cc820403112caad2a4e2a9ef2c6fe

# `session_fork.md`

## Summary

- `cmoc session fork` の概要と、現在の local branch を起点に session branch を作る仕様をまとめた文書
- 引数なしで実行する前提と、detached HEAD・未コミット差分・既存 active session などのエラー条件を扱う
- session start commit の取得、`.cmoc` の追跡対象外保証、session metadata 保存、標準出力への表示までの実行手順を扱う
- `cmoc/session/<session-id>` の命名規則、任意 start point を受け取らない方針、`cmoc branch` のレガシー扱いを含む

## Read this when

- `cmoc session fork` の実装方針やテスト観点を確認したいとき
- 新しい session branch の作成条件や checkout 手順を把握したいとき
- session metadata の保存先やブランチ命名規則を確認したいとき
- `cmoc branch` という旧名やレガシー要素の扱いを確認したいとき

## Do not read this when

- `cmoc session fork` 以外のサブコマンド仕様を確認したいとき
- セッションの join・abandon・apply 系の挙動だけを調べたいとき
- branch モデル全体や一般的な使用法だけを確認したいとき

## hash

- bdc848a6e1b4bd4a7b5ca68d42c99bfdce336d4712446a1df754f4c2f937df79

# `session_join.md`

## Summary

- `cmoc session join` は、現在の `<cmoc-session-branch>` を session metadata に記録された `<cmoc-session-home-branch>` へ `git merge --no-ff` するためのコマンドである。
- 主な論点は、実行可能なブランチ条件、`apply.state` の前提、home branch が進んでいた場合の扱い、merge conflict 時の解決手順、merge 後の session state 更新とブランチ削除条件である。

## Read this when

- `cmoc session join` が何をするコマンドか知りたいとき
- session ブランチを home ブランチへ戻す手順や前提条件を確認したいとき
- git merge の conflict 解決フローや、session 破棄後のブランチ削除条件を確認したいとき

## Do not read this when

- `cmoc session fork` の仕様だけを確認したいとき
- `cmoc session abandon` の仕様だけを確認したいとき
- `cmoc apply` 系の実行条件や apply run の破棄手順だけを確認したいとき

## hash

- 55fed0025c6e28cf2995d7c5cc96c23f5c53011a5e610ceacdf96ddfa2ed8379
