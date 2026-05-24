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

- `cmoc apply` の本体処理を実装している。`cmoc` 作業ブランチ上での前提確認、`.cmoc` の追跡対象外保証、oracle 差分の commit、INDEX.md のメンテナンス、調査・修正ループ、最終 merge とレポート出力までを扱う。
- 不整合調査用の Structured Output schema、要修正点リストの整理、実装ファイル / oracle ファイルごとの調査対象選定、要修正点の適用と commit も含む。
- 各種 prompt 生成・出力検証・apply report 生成など、`cmoc apply` の周辺補助処理がまとまっている。

## Read this when

- `cmoc apply` の起動条件、処理順、終了コード、レポート仕様を確認したいとき。
- 調査対象となる oracle / 実装ファイルの列挙、partial/full の切り替え、要修正点リストの改善ロジックを追いたいとき。
- apply run の commit 生成、編集禁止領域チェック、merge 前後の扱いを実装・修正したいとき。
- Structured Output の schema や prompt を変更したいとき。

## Do not read this when

- `cmoc init`、`cmoc session fork`、`cmoc session join`、`cmoc eval-oracles` など別サブコマンドの仕様だけを調べたいとき。
- セッション metadata や branch 運用の詳細だけを確認したいとき。
- `INDEX.md` の一般的な配置ルールや、`oracles` 配下の仕様断片そのものを読みたいとき。
- `cmoc apply` の実装ではなく、ユーザー向けの使用方法全体をざっくり把握したいだけのとき。

## hash

- 6d65e2c2e5b7cd48ca74a600fd0146689c05a736ed11782b554362c2bc342935

# `branch.py`

## Summary

- `src/sub_commands/branch.py` は `cmoc branch` の本体処理で、`cmoc session fork` 相当の作業用ブランチ作成と作成元 `HEAD` commit の記録を担う。
- 直接呼び出し時は共通 runner に処理を委譲し、リポジトリ root 解決とエラー整形を共有する。
- ブランチ名は `cmoc_<timestamp>` 形式で最大 10 回まで再試行し、衝突時は短い sleep を挟んで再生成する。
- 作成後に `.cmoc` の追跡外保証を行い、`.cmoc/branch/<branch>.txt` に base commit を保存して進捗を表示する。

## Read this when

- `cmoc branch` / `cmoc session fork` がどの commit からブランチを切るか確認したいとき。
- `cmoc_<timestamp>` 形式のブランチ名生成と衝突時の再試行条件を確認したいとき。
- `.cmoc` を追跡外に保つ処理や、base commit の保存先 `.cmoc/branch/<branch>.txt` を確認したいとき。
- 直接呼び出し時の `run_command` 委譲や `StepTimer` による進捗表示を確認したいとき。

## Do not read this when

- `cmoc init`、`cmoc eval-oracles`、`cmoc apply`、`cmoc merge` の仕様を知りたいとき。
- `commons.repo` の `ensure_cmoc_ignored`、`head_commit`、`branch_base_commit_path` の共通実装だけを追いたいとき。
- `src/main.py` のコマンド登録や CLI 起動フローだけを確認したいとき。
- `oracles` 側の正本仕様や他サブコマンドの目次を調べたいとき。

## hash

- 93c54f033993e66c3f411c74ac27489e478bb2fec68df1798aafba6d5ebc7235

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

- `src/sub_commands/merge.py` は `cmoc merge` の実装本体で、未マージの cmoc ブランチを現在の HEAD に `git merge --no-ff` する処理をまとめている。
- 明示指定がない場合は未マージの cmoc ブランチを 1 件に絞って選び、対象が cmoc 形式でない場合はエラーにする。
- merge 失敗時は Codex CLI に conflict marker の解消を依頼し、成功後は安全なら元ブランチを削除し、処理時間も報告する。

## Read this when

- `cmoc merge` の実行条件、対象ブランチの決め方、標準出力・エラー出力の挙動を確認したいとき。
- `git merge --no-ff` と conflict 解消支援、merge commit 作成、ブランチ削除の流れを追いたいとき。
- `cmoc merge` のエラー処理や、merge 開始後に手動解消が必要な場合の案内文を確認したいとき。

## Do not read this when

- `cmoc init`、`cmoc apply`、`cmoc eval-oracles` など他サブコマンドの仕様を調べたいとき。
- `src/commons` の共通基盤や `INDEX.md` 生成ロジックだけを確認したいとき。
- `cmoc session fork` や `cmoc session join` の session 管理仕様を知りたいだけのとき。

## hash

- 29c7f8ce32b28daad894635f7ad5f0c2b28fe3bfd111fd3ba0e49e438fd61961
