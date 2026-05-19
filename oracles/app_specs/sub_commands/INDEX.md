# `apply.md`

## Summary

- `cmoc apply` は、`<repo-root>/oracles` の正本仕様断片と実装との明確な不整合を Codex CLI で調査し、検出された不整合を修正するループを実行するサブコマンドです。
- 位置引数はなく、修正ループの最大反復回数を指定する `--repeat` / `-r` オプションを受け取り、デフォルトは 5 回です。
- 実行前に `<cmoc-branch>` 上であることと、`<repo-root>/oracles` 外に未コミット差分がないことを要求します。
- 実行時には `.cmoc` の git 追跡対象外保証、`oracles` 配下の未コミット差分の自動コミット、不整合調査、修正依頼、編集禁止領域の差分確認、変更コミット、作業レポート作成を行います。
- 不整合調査は oracle ファイルごとに独立した `codex exec` として行い、Structured Output の `discrepancies` 配列で結果を受け取ります。
- `discrepancies` が空の場合は収束、回数上限に達した場合は未収束として扱い、未収束はエラーではなく正常系の作業結果区分です。
- `cmoc apply` は修正ループの実行と判断材料のレポートを責務とし、実装が正本仕様へ完全に追従したことは保証しません。
- 作業レポートは Codex CLI に執筆させ、結果区分、不整合件数の推移、`<cmoc-branch>` 上の全変更内容の要約を含めて `<repo-root>/.cmoc/reports/apply/<time-stamp>.md` に保存し、そのフルパスを標準出力へ出します。
- 終了コードでは、収束・未収束・エラーの 3 種類を区別可能にする必要があります。

## Read this when

- `cmoc apply` の引数、`--repeat` / `-r` の意味、デフォルト反復回数を実装または確認したいとき。
- `cmoc apply` 実行前に必要なブランチ条件や未コミット差分チェックの仕様を確認したいとき。
- `oracles` 配下の未コミット差分をいつ自動コミットするか、`.cmoc` をどう git 管理から除外するかを調べたいとき。
- oracle と実装の不整合調査を Codex CLI にどの単位で依頼し、どの Structured Output schema で受け取るかを実装したいとき。
- 不整合リストが空の場合、または回数上限に達した場合に、修正ループをどう終了し、収束・未収束をどう判定するかを確認したいとき。
- Codex CLI に不整合修正作業を依頼する際、不整合リストをどのように扱うべきかを確認したいとき。
- 修正後に編集禁止領域や `oracles` などへ未コミット差分が残っていた場合の扱いを調べたいとき。
- `cmoc apply` の作業レポートに含める内容、保存先、標準出力へ流す情報を実装またはテストしたいとき。
- 収束・未収束・エラーを終了コードで区別する仕様を確認したいとき。

## Do not read this when

- `cmoc init`、`cmoc branch`、`cmoc eval-oracles`、`cmoc merge` など、`apply` 以外のサブコマンド固有仕様だけを調べたいとき。
- Codex CLI 呼び出しの共通仕様、プロンプト共通方針、サンドボックス指定、ログ保存など、サブコマンド横断の仕様だけを調べたいとき。
- `<repo-root>` の発見方法、oracle ファイル列挙、タイムスタンプ生成、`.cmoc` 管理などの共通ユーティリティ仕様だけを確認したいとき。
- `INDEX.md` 自動メンテナンスの対象、除外規則、目次生成用 Structured Output などを調べたいとき。
- cmoc 自体の Python 実装規約、CLI 構成、共通処理配置、テスト規約、開発環境など、開発者向けルールだけを確認したいとき。
- README、AGENTS、oracles、memo の編集可否やリポジトリ運用ルールだけを確認したいとき。
- 不整合が残っていないことを保証する評価やレビューの仕様を探しているとき。このファイルの `cmoc apply` は完全追従の保証ではなく、修正ループ実行とレポート作成の仕様を扱います。

## hash

- 8a124510c25b9e932db6f533a93432ec01366968fe46d15e3ec2599091ee62e9

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

- `cmoc eval-oracles` サブコマンドの仕様断片。現在の `<repo-root>/oracles` スナップショットを評価し、致命的な問題がないかを人間向けレポートとして保存・提示する挙動を定義している。
- 位置引数なし、`--full` / `-f` オプションあり。現在のブランチが `<cmoc-branch>` かどうか、`--full` の有無、作成元 commit から `HEAD` までの oracle 削除有無により、部分評価モードまたは全体評価モードを選ぶ。
- 実行手順として、`<repo-root>/.cmoc` が git 追跡対象外であることの保証、`oracles` ファイル列挙、部分評価時の変更ファイル絞り込み、ファイルごとの `codex exec` 評価、評価結果の統合レポート作成を定めている。
- 部分評価での「変更があった `oracles` ファイル」の定義、削除済みファイルの除外、rename 後パスを評価対象にすること、`<cmoc-branch>` 作成元 commit を `.cmoc/branch/<cmoc-branch>.txt` から読むことを定義している。
- 「致命的な問題」を、仕様だけから判断・実装した場合に主要ワークフローが壊れる、完了判定できない、cmoc の中核目的を満たしたと判定できない問題として定義し、この観点を `codex exec` のプロンプトへ注入する。
- 評価レポートは yaml frontmatter と本文で構成し、環境・事前条件や部分・全体評価モードなどを書いたうえで、ファイルごとの評価結果を区切りが分かるように結合する。保存先は `<repo-root>/.cmoc/reports/eval-oracles/<time-stamp>.md` で、フルパスを stdout に出力する。

## Read this when

- `cmoc eval-oracles` の引数、`--full` / `-f` オプション、事前条件を実装または確認したいとき。
- `cmoc eval-oracles` が部分評価モードと全体評価モードのどちらを選ぶべきか、ブランチ状態や oracle 削除の有無に基づく判定条件を確認したいとき。
- 部分評価で対象にする「変更があった `oracles` ファイル」の範囲、未コミット変更・staging area・ブランチ上の変更・rename・削除済みファイルの扱いを調べたいとき。
- `<cmoc-branch>` 作成元 commit の読み取り元や、作成元 commit から `HEAD` までの変更をどう解釈するかを確認したいとき。
- oracle 評価時にファイルごとに `codex exec` を呼び出す流れ、関連ファイルを読ませる方針、評価結果を統合レポートにまとめる手順を実装するとき。
- oracle 評価で何を「致命的な問題」とみなすか、`codex exec` プロンプトへ注入する汎用的な評価観点を確認したいとき。
- `eval-oracles` の評価レポートの frontmatter、本本文構成、保存先パス、stdout への提示方法を実装またはテストしたいとき。

## Do not read this when

- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc merge` など、`eval-oracles` 以外のサブコマンド仕様だけを調べたいとき。
- Codex CLI 呼び出しの共通仕様、Structured Output、リトライ、ログ保存など、サブコマンド横断の詳細だけを確認したいとき。
- `<repo-root>` の発見、oracle ファイル列挙の共通仕様、`.cmoc` の git 追跡対象外保証、タイムスタンプ生成などの共通処理だけを調べたいとき。
- `INDEX.md` 自動メンテナンスや oracle 目次生成の仕様を調べたいとき。
- cmoc 自体の Python 実装規約、CLI 設計規約、テスト規約、開発環境など、開発者向けルールだけを確認したいとき。
- 評価レポートの保存先や stdout 表示ではなく、通常のサブコマンド進捗表示・完了時時間レポート・共通エラー処理だけを調べたいとき。

## hash

- 32c17262f5488f8610f6ddd374f35a8fdfbb3cd0196a4992c2fb709a291bc282

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
