# `cmoc apply fork`

## 概要

- `cmoc apply fork` は、Codex CLI による調査・修正ループを開始する
- この調査・修正ループは以下の状態を目標とする
    - `<repo-root>` の実装を `<repo-root>/oracles` の正本仕様断片と一致している
    - `<repo-root>` の実装が最低限度の品質を満たしている
- `cmoc apply fork` が正常に実行完了したからといって、目標達成が保証されるわけではない
    - あくまで、調査・修正ループの実行し、目標達成のために努力する所までが `cmoc apply fork` の責任範囲である
    - i.e. ベストエフォート的な振る舞いで良い
- `cmoc apply fork` は `<cmoc-session-branch>` と作業用コピーを直接汚すことはしない
    - `<cmoc-apply-branch>` を作成し、そこにコミットを積み上げる

## 引数

- 位置引数なし
- オプション引数 `--repeat-investigate-and-fix` を受け取る
- オプション引数 `--repeat-improove-fixing-list` を受け取る
- オプション引数 `--full` (`-f`) を受け取る

## 事前条件

以下の場合はエラー終了する。

- 現在のブランチが `<cmoc-session-branch>` ではない
- 対応する `<cmoc-session-state-file>` が存在しない
- 対応する `<cmoc-session-state-file>` の `session.state` が `active` ではない
- 対応する `<cmoc-session-state-file>` の `apply.state` が `ready` ではない
- git 未コミット差分が存在する

## 実行作業

1. `<repo-root>/.cmoc` が git の追跡対象外であることを保証する
2. 現在の `<cmoc-session-branch>` HEAD を `<oracle-snapshot-commit>` として取得する
3. 一意な `<apply-run-id>` を生成する
4. `<oracle-snapshot-commit>` から `<cmoc-apply-branch>` を作成する
5. `<cmoc-apply-branch>` を checkout した専用 `<cmoc-apply-worktree>` を作成する
6. `<cmoc-session-state-file>` の状態を更新
7. `<cmoc-apply-worktree>` 上で調査・修正ループを実行する
    1. 調査対象となる oracles ファイル・実装ファイルを列挙する
    2. Codex CLI に、列挙したファイルリストを元に要修正点をリストアップさせる
    3. 要修正点リスト改善ループ (最大 M 回)
        1. Codex CLI に、要修正点リストを改善させる
        2. 改善点がなければここで要修正点リスト改善ループを抜ける
        3. 要修正点リスト改善ループ先頭に戻る
    4. 改善後の要修正点リストが空であれば、要修正点が検出されなかったものとしてループを終了する
    5. 修正作業ループ（改善後の要修正点リストに対する for-each）
        1. 要修正点 1 つに対する修正作業を Codex CLI に依頼する
        2. `<repo-root>/oracles` などの編集禁止ディレクトリに未コミット差分が有る場合はエラー終了
        3. 全ての未コミット差分を git にコミット（コミットメッセージは Codex CLI で適切なものを生成）
    6. 調査・修正ループ先頭に戻る
8. `<cmoc-session-state-file>` の状態を更新
9. 作業結果をレポートする

## `cmoc apply fork` の責務境界

- `cmoc apply fork` の責務は、指定された最大回数の範囲で調査・修正ループを実行し、その結果を人間が判断できる形でレポートすることである
- `cmoc apply fork` は、要修正点が残っていないことを保証しない
- `cmoc apply fork` は、全ての要修正点を漏れなく発見することは保証しない（あくまでベストエフォート的に振る舞う）
- ループが回数上限に達した場合も、コマンド実行としては正常系として扱う
- 回数上限到達後にさらに `cmoc apply fork` を再実行するか、`cmoc eval-oracles` や人手レビューを行うか、作業を打ち切るかは人間が判断する

## 調査対象 oracles ファイルの snapshot 原則

- `cmoc apply fork` 開始時点の `<cmoc-session-branch>` HEAD を `<oracle-snapshot-commit>` として固定し、その snapshot から `<cmoc-apply-branch>` を作成する。
- `cmoc apply fork` 開始後に `<cmoc-session-branch>` が進んでも、実行中の apply はその変更を取り込まない。
- `cmoc apply fork` の収束・未収束判定は `<oracle-snapshot-commit>` に対する判定である。

## `<cmoc-session-state-file>` 状態遷移

- 調査・修正ループ開始直前
    - `apply.state` を `running` に遷移させる
    - `apply` セクションに必要な情報 (e.g. `<apply-run-id>`, `<cmoc-apply-branch>`, `<cmoc-apply-worktree>`, `<oracle-snapshot-commit>`, ...) を保存する
- 調査・修正ループ完了直後
    - i.e. 全ての処理が正常に完了出来た場合
    - `apply.state` を `completed` に遷移させる
    - `apply` セクションに必要な情報 (e.g. `apply_head_before_merge`, ...) を保存する
- 途中でエラーが発生して処理を中止した場合
    - `apply.state` を `error` に遷移させる

## git worktree と編集操作

- `<cmoc-apply-worktree>` 上の `oracles/` は編集禁止である。
- Codex CLI による実装修正が `<apply-worktree>/oracles` を変更した場合はエラー終了する。
- 一方、apply 実行中にユーザーが `<cmoc-session-branch>` 側で `oracles/` を編集・commit しても、実行中の apply には取り込まれない。

## ループの反復回数の決め方

- 調査・修正ループ
    - サブコマンドの引数 `--repeat-investigate-and-fix` で調査・修正ループの反復回数を受け取る
    - デフォルト値は 5 とする
- 要修正点リスト改善ループ
    - サブコマンドの引数 `--repeat-improove-fixing-list` で要修正点リスト改善ループの反復回数を受け取る
    - デフォルト値は 3 とする

## 調査対象ファイルリストアップの仕様

### 対象となる git スナップショット

`cmoc apply fork` の評価対象は開始時点の `<oracle-snapshot-commit>` に固定される。
つまり、例えば、 `cmoc apply fork` の実行開始後にユーザーによって oracles ファイルの編集が `<cmoc-session-branch>` へ commit された場合、その編集内容は既に実行開始した `cmoc apply fork` の調査対象には含まれない。

### 部分適用モード・全体適用モード

`cmoc apply fork` は以下の２つのモードを持つ

- `--full` が付いている場合は全体適用モード
- `--full` が付いていない場合は部分適用モード

全体適用モードでは、変更有無による絞り込みを行わない。
部分適用モードでは調査対象を以下に絞る

- `<session-start-commit>..<oracle-snapshot-commit>` で変更された oracles ファイル
- `<session-start-commit>..<oracle-snapshot-commit>` で変更された実装ファイル

## 要修正点リストアップの仕様

- Codex CLI の呼び出し 1 回でで 1 つのファイルを起点とした要修正点リストアップ作業を Codex CLI に依頼する
- この「起点とした」とは
    - `codex exec` に渡すプロンプトで、調査するべきファイルを指定することを指す
    - ただし、この指定は「だけ」の意味ではない
    - i.e. 指定したファイルは以外のファイルも、調査のために必要ならば読むべきである
- このファイル起点の依頼は、事前に列挙したファイルリスト上のファイル全てに対して個別に行う
- つまり、調査対象となる oracles ファイルが N 件と実装ファイルが M 件存在するのであれば `codex exec` を N + M 回呼び出すということ
- 要修正点リストは Structured Output で受け取る

## 「要修正点」の定義

- oracles ファイルと実装との明確な不整合
    - 「oracles ファイル上で記述されている仕様」と「実装」とが明確に不整合している点を指す
    - oracles は仕様断片であるから、明記されていない仕様の隙間は AI の裁量であり、原則として不整合とはみなさない
    - しかしながら、仕様文言から推測可能な意図と実装とが著しく乖離する場合は要修正点とみなす
- 実装上の明確な問題点
    - 実装だけから見た成果物の品質としての問題を指す
    - バグのような致命的な問題だけを対象とする
    - 「こうした方が良い」のようなクオリティアップ的な話は対象としない
    - 当然ながら、修正後の実装は oracles ファイル上で記述されている仕様を満たしている必要がある

## 要修正点リスト改善の仕様

- ファイルごとに個別に列挙された要修正点リストを１つに連結する
- 連結した要修正点リストの改善作業を Codex CLI に依頼する
- 改善作業完了後、要修正点リストは以下の要件を満たしている事を目指す（ベストエフォートで良い）
    - 要修正点の内容の品質に明確な問題が存在しないこと
    - 要修正点同士に内容的な重複がないこと
    - 要修正点同士が相互に矛盾していないこと
    - 要修正点の内容が、 `<cmoc-apply-branch>` 上の過去の修正内容を考慮したものになっていること
    - 要修正点が False-Positive ではないこと
    - 要修正点を先頭から順番に対応した時に、それが作業順序として適切であること
    - 要修正点リスト改善の過程で発見した「漏れ」が要修正点リストに追加されていること
- 改善後の要修正点リストが空の場合のみ「検出された要修正点なし」と扱う
    - これは「この調査結果においては」という但し書きが付くが、要修正点の完全解消は `cmoc apply fork` の目的ではないので、これでよい
- 改善語の要修正点リストは Structured Output で受け取る

## 要修正点リストの Structured Output schema

```json
{
    "type": "object",
    "additionalProperties": false,
    "required": [
        "fixing_points"
    ],
    "properties": {
        "git_head_commit_hash": {
            "type": ["string", "null"],
            "description": "要修正点を発見した時点での git HEAD commit hash。後で機械的にフィルされるので AI による出力は null で良い。"
        },
        "fixing_points": {
            "type": "array",
            "description": "実装に対する要修正点のリスト。空配列の場合のみ要修正点なしとみなす。",
            "items": {
                "type": "object",
                "additionalProperties": false,
                "required": [
                    "title",
                    "evidences",
                    "oracle_requirement",
                    "observed_implementation",
                    "reason",
                    "suggested_fix"
                ],
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "要修正点の短い見出し。"
                    },
                    "evidences": {
                        "type": "array",
                        "description": "要修正点の根拠となる文言の位置情報。oracles・実装どちらかのファイルが必ず 1 つは根拠として存在するはずであるから空配列は想定しない。",
                        "items": {
                            "type": "object",
                            "additionalProperties": false,
                            "required": [
                                "path",
                                "line_start",
                                "line_end",
                                "summary"
                            ],
                            "properties": {
                                "path": {
                                    "type": "string",
                                    "description": "要修正点の根拠となるファイルの絶対パス。"
                                },
                                "line_start": {
                                    "type": ["integer", "null"],
                                    "description": "要修正点の根拠となる記述の開始行。行番号を特定できない場合は null。"
                                },
                                "line_end": {
                                    "type": ["integer", "null"],
                                    "description": "要修正点の根拠となる記述の終了行。行番号を特定できない場合は null。"
                                },
                                "summary": {
                                    "type": "string",
                                    "description": "該当箇所の短い要約。位置情報がズレた場合にそれを検知するための冗長情報。"
                                }
                            }
                        }
                    },
                    "oracle_requirement": {
                        "type": "string",
                        "description": "oracle が要求している仕様。実装のみから発見した要修正点であったとしても必ず関係する仕様を記載する。"
                    },
                    "observed_implementation": {
                        "type": "string",
                        "description": "調査時点の実装が実際にどうなっているか。"
                    },
                    "reason": {
                        "type": "string",
                        "description": "なぜ、明確に問題があり修正が必要であると言えるのか。推測や未確認事項は含めない。"
                    },
                    "suggested_fix": {
                        "type": "string",
                        "description": "問題を解決するために必要な実装修正の方針。"
                    }
                }
            }
        }
    }
}
```

## 要修正点対応作業の仕様

- リストアップされた要修正点に対する修正作業を Codex CLI に依頼する
- 要修正点１つにつき１回 Codex CLI を起動する
- 作業のためのヒントとして要修正点の情報をプロンプトに注入する
    - 「絶対に従わなければならない指示書」としては**扱わない**
    - 修正作業を行うエージェントは、この要修正点情報を無視しても良い
- Codex CLI に依頼する作業は要修正点として指摘されている問題の修正作業そのものを目的とする
    - 作業結果が、要修正点で述べている目的を達成したことの保証は求めない
    - ベストエフォート的に振る舞えばそれで良いものとする

## 回数上限でループを抜けた場合

- エラーとみはみなさず、作業結果の区分「未収束」として処理を続行する

## 作業レポートの仕様

- レポート執筆は Codex CLI に依頼する
- レポートの形式は markdown + YAML Front Matter とする
- YAML Front Matter に必ず含める項目
    - `<cmoc-session-branch>`
    - `<cmoc-apply-branch>`
    - apply worktree path
    - oracle snapshot commit
    - session head at apply start
    - session head at apply finish
- レポート本文に必ず含める項目
    - 作業結果
        - 収束 : 「検出された要修正点リストが空」によりループを終了した
        - 未収束 : 「回数上限に達した」によりループを終了した
        - エラー : 途中でエラーが起きてループを正常に終了出来なかった
    - 要修正点件数の推移
        - ループごとに何件の要修正点を見つけたかを書く
        - 「未収束」の場合は、まだ要修正点が残っている可能性を追記する
    - `<cmoc-apply-branch>` 上の全ての変更内容に対する要約
        - この `cmoc apply fork` で行った作業内容だけの要約に限定する
        - 変更内容の意味論に基づいたカテゴリ分けを行うこと
- レポート本体は `<repo-root>/.cmoc/reports/apply/fork/<time-stamp>.md` にファイルに保存する
- 作成したレポートのフルパスを標準出力に流す

## サブコマンドの終了コード

- 収束・未収束・エラーの３種類を区別可能であること
