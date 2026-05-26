# `__init__.py`

## Summary

- `src/sub_commands/__init__.py` は `src.sub_commands` パッケージを宣言するだけの最小モジュールです。
- 公開 API、定数、実行ロジック、再エクスポートは持ちません。

## Read this when

- `src.sub_commands` が Python パッケージとして宣言されていることを確認したいとき。
- `src/sub_commands` ディレクトリ全体の入口を把握したいとき。
- パッケージレベルのルーティング文書を作成・更新したいとき。

## Do not read this when

- 個別のサブコマンド実装や実行フローを確認したいときは、`src/sub_commands/init.py` などの具体的なモジュールを読む。
- `cmoc init`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` などの挙動そのものを調べたいとき。
- `commons` 配下の共通処理やテスト仕様だけを確認したいとき。

## hash

- ea4df02b820eba1ca77dfb1b2227c81dbff61cd7c4c2bf4d26d891369b57fa77

# `apply.py`

## Summary

- `src/sub_commands/apply.py` は `cmoc apply` の本体で、作業ブランチ上の前提確認から `.cmoc` 保証、oracle 差分の commit、INDEX.md 維持、調査・修正ループ、report 出力までをまとめています。
- 不整合調査用の Structured Output schema、要修正点の改善・整理、oracle / 実装ファイルごとの調査対象選定、修正適用と commit の流れを含みます。
- report 生成、prompt 生成、出力検証、編集禁止領域チェックなど、`cmoc apply` 周辺の補助処理もこのモジュールに集約されています。

## Read this when

- `cmoc apply` の起動条件、処理順、終了コード、report 出力を確認したいとき。
- oracle / 実装ファイルの調査対象選定、部分適用と全体適用の切り替え、要修正点リストの整理ロジックを追いたいとき。
- apply run における `.cmoc` の追跡対象外保証、oracle 差分の commit、INDEX.md の維持、編集禁止領域チェックを実装・修正したいとき。
- Structured Output schema、調査用 prompt、要修正点の検証、apply report の内容検査を変更したいとき。

## Do not read this when

- `cmoc init`、`cmoc session fork`、`cmoc session join`、`cmoc merge` など、`cmoc apply` 以外のサブコマンド仕様だけを確認したいとき。
- `cmoc apply` の中でも、調査・修正ループや report 生成ではなく、branch や session の運用仕様だけを見たいとき。
- `INDEX.md` の一般的な生成ルールや、`oracles` 配下の仕様断片そのものだけを読みたいとき。
- `cmoc apply` の実装ではなく、ユーザー向けの使い方全体をざっくり把握したいだけのとき。

## hash

- 41a8ccb21ff6d59348628632f2a76126579127d7e3e982e299170c3a41fc6dcb

# `eval-oracles.py`

## Summary

- `cmoc eval-oracles` の実装本体で、`--full` とブランチ状態に応じた部分評価・全体評価の切り替え、oracle ファイル列挙、Codex CLI による評価実行、レポート保存までをまとめている。
- Structured Output schema の検証、評価用 prompt の組み立て、問題点集約、Markdown レポート生成の処理も含む。
- `.cmoc` の ignore 保証や INDEX.md メンテナンスなど、評価前後の周辺処理も扱う。

## Read this when

- `cmoc eval-oracles` の実装フローや `--full` の扱いを確認したいとき。
- 評価対象 oracle の選択、部分評価と全体評価の分岐、deleted oracle 検知の条件を確認したいとき。
- Codex CLI に渡す評価プロンプト、Structured Output schema、レポート生成の仕様を確認したいとき。
- `cmoc eval-oracles` の失敗時レポートや出力先 `.cmoc/reports/eval-oracles` の挙動を確認したいとき。

## Do not read this when

- `cmoc apply`、`cmoc init`、`cmoc session fork`、`cmoc session join` など、`cmoc eval-oracles` 以外のサブコマンド実装を調べたいとき。
- `oracles` 配下の個別仕様断片そのものを読みたいときは、この実装ファイルではなく対応する oracle 文書を読むべきとき。
- コマンドの設計ルール、評価基準、開発環境ルールだけを確認したいとき。
- 純粋なテスト実装や別モジュールの共通処理を追いたいとき。

## hash

- 8dbd4e4386d66f709cb2524ea2100c941f9589fc671a717f70adb1be1447879c

# `init.py`

## Summary

- `cmoc init` の本体処理を実装している。
- 直接呼び出し時は共通 runner に委譲し、`.cmoc` の ignore 保証と初期化差分の commit を 2 ステップで進める。
- 処理結果として `committed initialization changes` または `no initialization changes` を表示し、最後に処理時間を報告する。

## Read this when

- `cmoc init` の実際の処理順や、`repo_root` 未指定時の共通 runner 委譲を確認したいとき。
- `.cmoc` を git 追跡対象外にする保証処理と、初期化差分の commit 判定の実装を確認したいとき。
- 実行結果メッセージと timing report の出力条件を確認したいとき。

## Do not read this when

- `cmoc init` の仕様そのものではなく、他のサブコマンドの実装を確認したいとき。
- `.cmoc` の ignore 判定や tracked 解除の詳細ルールだけを仕様書側で確認したいとき。
- `cmoc session fork` / `cmoc session join` / `cmoc apply` / `cmoc eval-oracles` など、別コマンドの処理を見たいとき。

## hash

- 766eb4ef5567a176766be2bb55dbc8f955c55af92c1ddc3f64043c1be4bda4ee

# `merge.py`

## Summary

- `src/sub_commands/merge.py` は `cmoc merge` の実装本体で、cmoc 管理ブランチを現在の HEAD に `git merge --no-ff` する処理をまとめています。
- 対象ブランチが未指定の場合は未マージの cmoc 管理ブランチを 1 件に絞って自動選択し、cmoc 形式でない名前はエラーにします。
- merge 失敗時は Codex CLI に conflict marker の解消を依頼し、成功後は安全なら元ブランチを削除して処理時間も報告します。

## Read this when

- `cmoc merge` の実行条件、対象ブランチの決め方、標準出力・エラー出力の挙動を確認したいとき。
- `git merge --no-ff` と conflict 解消支援、merge commit 作成、ブランチ削除の流れを追いたいとき。
- `cmoc merge` のエラー処理や、merge 開始後に手動解消が必要な場合の案内文を確認したいとき。

## Do not read this when

- `cmoc init`、`cmoc apply`、`cmoc eval-oracles` など、他サブコマンドの仕様だけを確認したいとき。
- `src/commons` の共通基盤や `INDEX.md` 生成ロジックだけを確認したいとき。
- `cmoc session fork` や `cmoc session join` の session 管理仕様だけを確認したいとき。

## hash

- 6fbb49e7479bcd76e29c34c151ebdd39f0a88829283845f59955044aff90fb3d

# `session_fork.py`

## Summary

- `cmoc session fork` の本体処理を実装しており、現在の local branch を session home branch として session branch を作成し、session state を記録する。
- detached HEAD、remote-tracking branch、未コミット差分、`cmoc` 管理 branch、既存 active session などの事前条件チェックを行う。
- `.cmoc` の ignore 保証、session branch 作成の再試行、作成結果と home branch の標準出力表示を扱う。

## Read this when

- `cmoc session fork` の挙動やエラー条件を実装・修正・レビューしたいとき。
- 現在の branch から session branch を作る前提や、session state の保存処理を確認したいとき。
- branch 判定、`.cmoc` の扱い、session branch 名の生成方法を追いたいとき。

## Do not read this when

- `cmoc session join`、`cmoc session abandon`、`cmoc apply` など別サブコマンドの流れだけを確認したいとき。
- `cmoc` 全体の利用方法や branch model の概要だけを確認したいとき。
- 実装コードではなく、`session_fork` の正本仕様断片だけを確認したいとき。

## hash

- 2c5226845f7803912fa3146d9732d7c499b4080a9b6b2dec4519d6438c85686f
