# `apply.md`

## Summary

- `cmoc apply` は、`<repo-root>/oracles` の正本仕様断片と実装の明確な不整合を Codex CLI で調査し、最大反復回数の範囲で修正・コミット・レポート生成を行うサブコマンド仕様である。
- 位置引数はなく、`--repeat`/`-r` で不整合修正ループの最大反復回数、`--full`/`-f` で全体適用モードを指定する。
- 実行前には `<cmoc-branch>` 上にいることと、`<repo-root>/oracles` 外に未コミット差分がないことを要求する。
- 適用モードは部分適用と全体適用があり、`--full` 指定時または `<cmoc-branch>` 上で oracle ファイル・実装ファイルの削除がある場合は全体適用、それ以外は部分適用となる。
- 処理は `.cmoc` の git 追跡対象外保証、oracle 差分の自動コミット、不整合リストアップ、不整合リスト整理、Codex CLI への修正依頼、編集禁止領域の差分検査、全差分コミット、作業レポート生成で構成される。
- `cmoc apply` は仕様追従の完全保証を責務とせず、指定回数内で調査・修正ループを実行し、人間が判断できる作業結果を報告することを責務とする。
- 不整合リストアップとリスト整理はいずれも Structured Output の `discrepancies` 配列 schema を用い、空配列の場合のみ検出不整合なしとして扱う。
- 不整合追従作業は、整理済み不整合リストの各項目ごとに Codex CLI を1回起動して修正を依頼する。
- 回数上限に達してもエラーではなく作業結果区分は「未収束」となり、検出不整合リストが空になった場合は「収束」となる。
- 作業レポートは Codex CLI に執筆させ、結果区分、不整合件数の推移、`<cmoc-branch>` 上の全変更内容の意味論的要約を含め、`<repo-root>/.cmoc/reports/apply/<time-stamp>.md` に保存してパスを標準出力する。
- 終了コードは、収束・未収束・エラーの3種類を区別可能である必要がある。

## Read this when

- `cmoc apply` サブコマンドの引数、事前条件、部分適用・全体適用モードの判定条件を確認したいとき。
- `cmoc apply` がどの順番で `.cmoc` 保護、oracle 差分コミット、不整合調査、修正依頼、コミット、レポート作成を行うか把握したいとき。
- `cmoc apply` の責務が、正本仕様への完全追従保証ではなく、最大回数内の不整合調査・修正ループと判断材料のレポートであることを確認したいとき。
- 不整合リストアップを Codex CLI に依頼する際の対象ファイル列挙、for each 実行、Structured Output schema を実装・確認したいとき。
- ファイル別に得た不整合リストを連結し、重複や矛盾を整理する Codex CLI 呼び出しの仕様を確認したいとき。
- 整理済み不整合リストを要修正項目として扱い、各不整合ごとに Codex CLI へ修正作業を依頼する仕様を確認したいとき。
- ループの収束条件、回数上限到達時の未収束扱い、エラーではない終了の扱いを確認したいとき。
- `cmoc apply` の作業レポートに含める内容、保存先、標準出力へ流すパスを実装・確認したいとき。
- 収束・未収束・エラーを区別する終了コードの仕様を調べたいとき。

## Do not read this when

- `cmoc init`、`cmoc branch`、`cmoc eval-oracles`、`cmoc merge` など、`cmoc apply` 以外のサブコマンド仕様だけを調べたいとき。
- Codex CLI 呼び出し、プロンプト構成、ログ保存、リトライ、Structured Output の共通仕様など、サブコマンド横断の実行時仕様だけを確認したいとき。
- `<repo-root>` の発見、oracle ファイル列挙、実装ファイル列挙、タイムスタンプ形式、`.cmoc` の git 追跡対象外保証など、共通補助仕様の詳細だけを調べたいとき。
- cmoc 自体の Python 実装規約、設計規約、テスト規約、開発環境など、開発者向けルールだけを確認したいとき。
- `<repo-root>/oracles` 配下の `INDEX.md` 自動生成・更新仕様だけを調べたいとき。
- cmoc のエンドユーザー向け全体ワークフローや PATH 設定、初期化からマージまでの流れだけを把握したいとき。
- README、AGENTS、oracles、memo などの編集可否やリポジトリ運用ルールだけを確認したいとき。

## hash

- 404005a40a1a2e7cc6dbb38676fa5c187b1c76554ae5bd3a1ce70f1e8347304b

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

# `eval_oracles.md`

## Summary

- `oracles/app_specs/sub_commands/eval_oracles.md` は、`cmoc eval-oracles` サブコマンドの正本仕様断片です。
- 現在の `<repo-root>/oracles` の仕様スナップショットに致命的な問題がないかを評価し、人間向けレポートとして保存・提示する挙動を定義しています。
- 部分評価と全体評価の切り替え条件、`codex exec` によるファイル単位評価、評価時に読んでよい範囲、致命的問題の定義、レポート本文と yaml frontmatter、保存先と stdout 出力を扱います。

## Read this when

- `cmoc eval-oracles` の実装・修正・テストを行うとき。
- `cmoc eval-oracles` が部分評価モードと全体評価モードをどの条件で切り替えるか確認したいとき。
- oracle ファイル評価時に `codex exec` へ渡す制約、読み取り可能ファイル、参照禁止ファイル、評価観点を確認したいとき。
- 評価レポートの構成、保存先、標準出力に表示する内容を確認したいとき。

## Do not read this when

- `cmoc eval-oracles` 以外のサブコマンド仕様を調べているとき。
- oracles の仕様評価ではなく、実装コードやテストコードを直接検証する処理を調べているとき。
- cmoc 自体ではなく、cmoc を用いて開発する `<repo-root>` 側の個別アプリケーション仕様を調べているとき。
- `INDEX.md` 自動生成や目次フォーマットそのものの仕様だけを確認したいとき。

## hash

- 4e236a20ed84f93e0eaae87213fb935f329b58a66bd51e48a3ff71cabbd15a5b

# `init.md`

## Summary

- `cmoc init` サブコマンドの正本仕様断片。
- `<repo-root>` を cmoc で作業可能な状態に初期化するための引数、事前条件、実行手順を定義する。
- `<repo-root>/.cmoc` を git 追跡対象外にする具体的な操作と完了判定を定義する。

## Read this when

- `cmoc init` の仕様を実装・修正・確認するとき。
- `cmoc init` が引数なしで動作することや、固有の事前条件がないことを確認したいとき。
- `<repo-root>/.cmoc` を `.gitignore` に追加し、既に tracked な `.cmoc` 配下ファイルを追跡解除する処理を実装するとき。
- `.cmoc` 追跡対象外保証の完了判定として、`git ls-files -- .cmoc` と `git check-ignore -q .cmoc/.__cmoc_ignore_probe__` を使う仕様を確認するとき。
- 初期化処理の最後に、ここまでの作業で発生した差分を git commit する必要があるか確認するとき。

## Do not read this when

- `cmoc init` 以外のサブコマンド仕様を調べたいとき。
- cmoc 自体の開発ルール、コーディング規約、テスト規約、開発環境だけを調べたいとき。
- Codex CLI 呼び出し、Structured Output、コンソール出力、共通エラーハンドリングなど、サブコマンド横断の共通仕様だけを調べたいとき。
- `<repo-root>/.cmoc` の git ignore 保証や init 時の commit に関係しない機能を実装するとき。

## hash

- b3b7cca844c91f7ba5a4e8d4592f0c2fb5510aa4ab31fbb1c114b7fd62574175

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
