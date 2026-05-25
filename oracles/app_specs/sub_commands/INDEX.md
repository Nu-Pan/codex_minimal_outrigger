# `apply.md`

## Summary

- `cmoc apply` の目的、前提条件、反復ループ、マージ、レポート、終了コードを定義する。
- 調査対象ファイルの列挙から要修正点の抽出・改善・修正作業までの流れと、その責務境界を扱う。
- apply 用ブランチ・worktree・metadata・成果レポートの扱いも含めた実行仕様をまとめている。

## Read this when

- `cmoc apply` の実行順序や各段階の役割を確認したいとき。
- 部分適用モードと全体適用モード、反復回数、要修正点リストの Structured Output 仕様を知りたいとき。
- merge 条件、`<cmoc-apply-branch>` の削除条件、作業レポートの出力要件を確認したいとき。

## Do not read this when

- `cmoc init` や `cmoc eval-oracles` など、`apply` 以外のサブコマンド仕様を調べたいとき。
- セッション管理やセッション metadata の詳細仕様だけを知りたいとき。
- 個別の実装修正方針や設計判断を先に詰めたいだけで、`apply` の実行フローは不要なとき。

## hash

- 43f72e4b091016507373f35d71a1a5fb62ca248cf9d800129fa44c1b92565057

# `eval_oracles.md`

## Summary

- `cmoc eval-oracles` の正本仕様で、現在の oracles スナップショットを評価し、人間向けレポートを生成するコマンドの全体像をまとめている。
- 位置引数なし・`--full` あり、部分評価と全体評価の切り替え条件、実行手順、読み取り可能な oracles 範囲を扱っている。
- 致命的問題の定義、ファイル単位評価の前提、Structured Output の期待形、レポート本文の必須構成と出力先まで含めている。

## Read this when

- `cmoc eval-oracles` が何を評価し、どのような結果を人間に報告するかを確認したいとき。
- 部分評価モードと全体評価モードの切り替え条件を確認したいとき。
- `fatal` / `inconclusive` / `warning` の判定基準や、致命的問題の定義を確認したいとき。
- 評価レポートの構成、集約方法、出力先を確認したいとき。

## Do not read this when

- `cmoc eval-oracles` の評価対象の選び方や、レポートの必須形式を知りたいだけではないとき。
- `cmoc apply` や `cmoc session fork` / `cmoc session join` など、別サブコマンドの仕様を調べたいとき。
- oracles 配下の一般的な設計方針やコーディング規約、開発環境ルールを確認したいとき。
- `cmoc` 全体の運用ルールやファイル編集可否だけを確認したいとき。

## hash

- faba60e5a605660a4def461307c56cc70bdd5d1839ed347448ed01d958a938a4

# `init.md`

## Summary

- `cmoc init` の仕様を定める文書である。
- `<repo-root>` を cmoc 利用可能な状態に初期化し、`.cmoc` を git 追跡対象外にしたうえで、ここまでの差分を commit する手順が書かれている。
- 引数なしで実行すること、`<repo-root>/.cmoc` の ignore 判定と tracked ファイル解除の考え方が記載されている。

## Read this when

- `cmoc init` が何をするコマンドかを確認したいとき。
- `<repo-root>` を `cmoc` による作業が可能な状態へ初期化する流れを知りたいとき。
- 初回セットアップとして `.cmoc` を git の追跡対象外にする必要があるか確認したいとき。
- `cmoc init` の実行後にどの差分を commit するのかを確認したいとき。

## Do not read this when

- `cmoc init` の実装方針やコード配置ではなく、他のサブコマンドの仕様を調べたいとき。
- `cmoc session fork`、`cmoc session join`、`cmoc apply` など、初期化以外のワークフロー仕様を確認したいとき。
- `.cmoc` を git 追跡対象外にするための詳細な判定条件ではなく、リポジトリ全体の開発ルールや設計規約だけを知りたいとき。
- `cmoc` のユーザー向け使用方法全体を広く把握したいだけで、初回の初期化手順が不要なとき。

## hash

- b3b7cca844c91f7ba5a4e8d4592f0c2fb5510aa4ab31fbb1c114b7fd62574175

# `session_fork.md`

## Summary

- `cmoc session fork` の正本仕様断片で、現在の `<local-branch>` を session の home branch として記録し、その HEAD から新しい session branch を作成して checkout する手順を定義している。
- 引数なしで実行し、detached HEAD や managed branch 上での実行、未コミット差分の存在、既存の active session との重複を禁止する。
- 作成した session branch の名前を `cmoc/session/<session-id>` 形式とし、session metadata を `.cmoc/sessions/<session-id>/session.json` に保存して標準出力へ branch 名と home branch 名を表示する。

## Read this when

- `cmoc session fork` の仕様、入出力、事前条件、実行手順を確認したいとき。
- 現在のローカルブランチを session の起点として記録し、新しい `cmoc/session/...` ブランチを作る振る舞いを実装・修正したいとき。
- session metadata の生成や、`<cmoc-session-home-branch>` と `<cmoc-session-branch>` の関係を確認したいとき。
- session fork のブランチ命名規則や、active な session の重複禁止条件を確認したいとき。

## Do not read this when

- `cmoc session join`、`cmoc apply`、`cmoc eval-oracles` など、別サブコマンドの仕様だけを調べたいとき。
- `cmoc init` や開発環境など、セッション開始以外の作業フローを調べたいとき。
- `cmoc` 全体の設計方針、コーディング規約、テスト規約だけを確認したいとき。
- legacy な `cmoc branch` の扱いだけを知りたいとき。

## hash

- bdc848a6e1b4bd4a7b5ca68d42c99bfdce336d4712446a1df754f4c2f937df79

# `session_join.md`

## Summary

- `cmoc session join` の仕様をまとめた文書で、現在の `<cmoc-session-branch>` を session metadata に記録された `<cmoc-session-home-branch>` へ merge する手順を扱う。
- 引数なしで実行し、`<cmoc-session-branch>` 上でのみ動作すること、同一 session に running / merge_pending / merge_conflict の apply run がある場合は失敗することを示す。
- `git switch` と `git merge --no-ff` を使った join 手順、conflict 発生時の解決フロー、`session metadata` の `state=merged` 更新、必要に応じた session ブランチ削除の条件を含む。
- `<repository-default-branch>` は特別扱いせず、常に session metadata の `<cmoc-session-home-branch>` を merge 先にする方針を明示している。

## Read this when

- 現在 checkout している session ブランチを home branch へ merge して session を完了させたいとき。
- session metadata の `state` を `merged` に更新する条件や、join の完了後処理を確認したいとき。
- `git merge --no-ff` 実行時の conflict 扱い、Codex CLI への解消依頼、手動解決手順を確認したいとき。
- `session_home_branch` が session 作成後に進んでいた場合の join 挙動を確認したいとき。

## Do not read this when

- `cmoc session fork` の仕様や session 作成時のブランチ命名規則を調べたいとき。
- `cmoc apply` の実行手順や調査・修正ループの仕様を知りたいとき。
- `cmoc init` や `cmoc eval-oracles` など、別サブコマンドの仕様を調べたいとき。
- `cmoc` 全体の開発ルールやファイルアクセス規則だけを確認したいとき。

## hash

- 63d29a0134de7a6184e58b43be243b8d43694dcba516583c2ac66194d58f9aa8
