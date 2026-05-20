# `__init__.py`

## Summary

- cmoc のサブコマンド実装パッケージであることを示すパッケージ初期化ファイル。
- 実行ロジックや公開 API の定義は含まず、パッケージ用途を docstring で説明するだけのファイル。

## Read this when

- src/sub_commands 配下が何のためのパッケージかを最小限確認したいとき。
- サブコマンド実装モジュール群のパッケージ境界や概要を確認したいとき。

## Do not read this when

- 個別サブコマンドの処理内容、引数、実行フローを調べたいとき。
- cmoc のコマンドルーティング、CLI エントリポイント、サブコマンド登録方法を調べたいとき。
- 実装上の詳細な仕様やテスト対象の振る舞いを確認したいとき。

## hash

- ea4df02b820eba1ca77dfb1b2227c81dbff61cd7c4c2bf4d26d891369b57fa77

# `apply.py`

## Summary

- `cmoc apply` サブコマンドの本体処理を実装するファイル。
- cmoc 作業ブランチ上でのみ apply を許可し、リポジトリ状態検証、`.cmoc` 無視設定、oracle 差分の commit、`INDEX.md` メンテナンスを行う。
- oracle ファイルごとに Codex CLI の read-only 実行で実装との不整合を Structured Output として調査し、不整合がある場合は workspace-write 実行で実装修正を依頼する。
- 不整合調査結果の JSON schema、schema 検証、調査用 prompt、実装修正用 prompt、commit message 生成用 prompt を定義する。
- 修正後は編集禁止領域である `oracles/` と `.agents/` の差分を拒否し、変更があれば Codex 生成の commit message で commit する。
- 指定 repeat 回数まで不整合調査と実装修正を反復し、収束時は 0、未収束時は専用終了コード 2 を返す。
- apply 結果レポートを `.cmoc/reports/apply/<timestamp>.md` に保存し、必須見出し、結果区分、不整合件数推移、未収束時文言、ブランチ変更内容要約を保存前に検証する。

## Read this when

- `cmoc apply` の全体フロー、ステップ表示、終了コード、repeat による反復処理を確認したいとき。
- apply 実行前に許可されるブランチ、未コミット差分、oracle 差分、`.gitignore` と `.cmoc` の扱いを調べたいとき。
- Codex CLI に oracle と実装の不整合調査を依頼する prompt、read-only 実行、Structured Output schema、JSON 検証の詳細を確認したいとき。
- Codex CLI に実装修正を依頼する prompt、workspace-write 実行、修正後 commit、commit message 生成の流れを調べたいとき。
- apply 中に `INDEX.md` がいつメンテナンスされるか、実装差分 commit 前に index 更新がどう扱われるか確認したいとき。
- apply が編集禁止領域の変更をどう検出し、どのパスを禁止扱いにするか調べたいとき。
- apply レポートの保存先、生成 prompt、必須内容、検証条件を確認したいとき。
- 不整合調査 Structured Output の `discrepancies` 各項目の必須キーや型検査を変更・テストしたいとき。

## Do not read this when

- `cmoc apply` 以外のサブコマンド、例えば init、branch、merge、eval-oracles の本体処理だけを調べたいとき。
- Codex CLI 呼び出しの共通実装、JSON パース、ログ保存、サンドボックス指定などの低レベル共通処理だけを確認したいとき。
- git コマンド実行、ブランチ判定、changed paths、oracle ファイル列挙、`.cmoc` ignore 保証など repo 共通 helper の内部実装だけを調べたいとき。
- `INDEX.md` 自動生成やメンテナンスの具体的な実装だけを確認したいとき。
- cmoc の CLI 引数パースやサブコマンド登録箇所だけを調べたいとき。
- cmoc の仕様断片そのものを確認したい場合で、実装コードではなく `oracles` 配下の正本仕様を読むべきとき。
- apply のテストケース、Fake Codex CLI、pytest fixture などテスト実装だけを確認したいとき。

## hash

- 0e6c6e61a595b1312c2e4277e44ddf6c4033cc6da11e2fde2592c5aa656c55f1

# `branch.py`

## Summary

- `cmoc branch` サブコマンドの本体処理を実装するファイル。
- 共通 runner 経由の repo root 解決、作業用ブランチ作成、`.cmoc` の git ignore 保証、作成元 commit の `.cmoc/branch` への記録を行う。
- ブランチ名は `cmoc_<timestamp>` 形式で生成し、衝突時は最大 10 回リトライする。
- 実行中の進捗表示は `branch (1/3)` から `branch (3/3)` までの段階表示と、各ブランチ作成試行の表示で構成される。
- 処理時間の計測と完了時レポートには `StepTimer` を使用する。

## Read this when

- `cmoc branch` の実装フローを確認したいとき。
- 作業用ブランチ名の生成規則や、timestamp 衝突時のリトライ挙動を調べたいとき。
- `cmoc branch` が base commit をどのタイミングで取得し、どこへ保存するか確認したいとき。
- `.cmoc` を git 追跡対象外にする処理が `cmoc branch` 内でいつ呼ばれるか調べたいとき。
- `cmoc branch` の stdout 進捗表示や `StepTimer` による計測箇所を確認したいとき。

## Do not read this when

- `cmoc init`、`cmoc apply`、`cmoc merge`、`cmoc eval-oracles` など他サブコマンドの本体処理を調べたいとき。
- repo root 探索、git 実行、`.cmoc` パス生成、timestamp 生成、時間計測などの共通ユーティリティ実装そのものを調べたいとき。
- `cmoc branch` の正本仕様やユーザー向け仕様だけを確認したいとき。
- 自動テストの構成、Fake Codex CLI、pytest 規約を調べたいとき。
- cmoc を用いて開発する `<repo-root>` 側の oracle や `INDEX.md` 生成仕様を調べたいとき。

## hash

- 3f0f49fc6b3453d7c26dea4e5cb47b8bd0b23b7378f6d77da6eeb182a334eee7

# `eval_oracles.py`

## Summary

- `cmoc eval-oracles` サブコマンドの本体処理を実装するファイル。
- `.cmoc` の ignore 保証、`INDEX.md` メンテナンス、評価対象 oracle の選択、Codex CLI による oracle 評価、Markdown レポート保存までの一連の実行フローを扱う。
- cmoc ブランチ上かどうか、`--full` 指定の有無、削除された oracle の有無から、差分評価と全体評価を切り替える。
- oracle 評価用プロンプトでは、実装やテストを参照せず、oracles ツリーと `INDEX.md` のルーティング情報に基づいて致命的な仕様問題を報告させる。
- 評価結果は `.cmoc/reports/eval-oracles/<timestamp>.md` に frontmatter 付き Markdown として保存される。

## Read this when

- `cmoc eval-oracles` の実行順序や stdout 進捗表示を確認したいとき。
- oracle 評価が部分評価になる条件と全体評価になる条件を調べたいとき。
- `--full`、cmoc ブランチ、base commit、削除 oracle の扱いが評価対象選択にどう影響するか確認したいとき。
- Codex CLI に渡す oracle 評価プロンプトの内容や、read-only 実行の指定を確認したいとき。
- eval-oracles の評価レポート保存先、ファイル名、frontmatter、oracle ごとの出力形式を調べたいとき。
- `maintain_indexes`、`ensure_cmoc_ignored`、oracle ファイル列挙、変更 oracle 検出、head commit 取得との接続点を確認したいとき。

## Do not read this when

- `cmoc eval-oracles` の CLI 引数定義や argparse への登録だけを調べたいとき。
- oracle ファイル列挙、cmoc ブランチ判定、base commit 読み取りなどの低レベル git/repo 操作の実装詳細だけを確認したいとき。
- `INDEX.md` 自動メンテナンス処理そのものの仕様や実装だけを調べたいとき。
- Codex CLI 呼び出し共通処理、ログ保存、リトライ、サンドボックス指定の共通実装だけを確認したいとき。
- タイムスタンプ生成や StepTimer の実装詳細だけを調べたいとき。
- 生成された eval-oracles レポートの内容を読みたいだけのとき。

## hash

- bfaa17519e59fa0a092983b1556fc578decfcb4312492879ecb884035d25fff1

# `init.py`

## Summary

- `cmoc init` サブコマンドの本体処理を定義する実装ファイル。
- `cmoc_init_impl` は、直接呼び出し時に共通 runner へ委譲し、repo root 解決と共通エラー整形を適用する。
- repo root が渡された実行では、`.cmoc` を git 追跡対象外にするための `.gitignore` ルール保証と tracked file 解除を行う。
- 初期化で発生した `.gitignore` や index の変更だけをコミットし、変更有無に応じた進捗メッセージを出力する。
- `StepTimer` を使って init 処理の各ステップ開始と完了時の経過時間レポートを管理する。

## Read this when

- `cmoc init` の実行本体がどの共通処理や repository helper を呼び出しているか確認したいとき。
- `.cmoc` を `.gitignore` に追加し、git 追跡対象外にする初期化処理の流れを調べたいとき。
- `cmoc init` が初期化変更をどの条件でコミットするか確認したいとき。
- `cmoc init` の stdout 進捗表示や `StepTimer` によるステップ計測の実装箇所を探しているとき。
- サブコマンド実装から `run_command` へ委譲する直接呼び出し時のパターンを確認したいとき。

## Do not read this when

- CLI 引数解析や `cmoc init` コマンドの登録箇所だけを調べたいとき。
- `.cmoc` ignore ルールの詳細な判定・書き込み・tracked file 解除ロジックそのものを調べたいとき。
- 初期化変更の git commit 対象や commit 実行の詳細ロジックを調べたいとき。
- `StepTimer` の実装や時間表示フォーマットそのものを確認したいとき。
- `cmoc branch`、`cmoc apply`、`cmoc merge` など、init 以外のサブコマンド本体を調べたいとき。

## hash

- fed23b7dbddef444bcd8f69f1bf09603a657028a6aaff10e70ae0ae3089fa822

# `merge.py`

## Summary

- `cmoc merge` サブコマンドの本体処理を実装するファイル。
- 作業ツリーの未コミット変更確認、`.cmoc` の git ignore 保証、merge 元 cmoc ブランチの解決、`git merge --no-ff` 実行、必要時の conflict 解消、merge 後の作業ブランチ削除までを扱う。
- merge 元ブランチが明示されていない場合は、未マージブランチから cmoc 命名規則に合う候補を 1 件だけ自動解決し、0 件または複数件なら利用者に明示指定を求める。
- merge conflict が発生した場合は unmerged path を取得し、Codex CLI に conflict marker 解消を依頼したうえで、残存 marker と unmerged path を検査してから `git add` と `git commit --no-edit` を実行する。
- conflict 解消用プロンプトでは `git add` と `git commit` の実行禁止、`oracles` と `.agents` の編集禁止、`memo` の読み書き禁止を明示する。
- git 管理対象ファイル全体から conflict marker を検出する補助処理、unmerged path 取得、source branch の安全削除、merge state が残る場合の手動解決案内を含む。

## Read this when

- `cmoc merge` の実装フローや各ステップの進捗表示を確認したいとき。
- merge 元 cmoc ブランチの自動解決条件、候補が 0 件または複数件の場合のエラー処理を調べたいとき。
- `git merge --no-ff` の実行方法、merge 失敗時に Codex CLI へ conflict 解消を依頼する流れを確認したいとき。
- merge conflict 解消後に conflict marker や unmerged path をどう検査し、どのタイミングで `git add` と `git commit --no-edit` を行うか調べたいとき。
- conflict 解消用 Codex プロンプトの内容、編集禁止パス、`skip_index_maintenance` の扱いを確認したいとき。
- merge 後に source branch を `git branch -d` で削除する条件や、削除失敗時の warning 表示を確認したいとき。
- merge state が残った可能性がある場合の手動解決メッセージや例外伝播の扱いを確認したいとき。

## Do not read this when

- `cmoc merge` の CLI 引数定義や argparse への登録箇所だけを調べたいとき。
- `run_git`、`run_command`、`run_codex_exec`、`StepTimer` など共通ユーティリティ自体の実装を調べたいとき。
- cmoc ブランチの命名規則そのものや `is_cmoc_branch` の詳細実装を確認したいとき。
- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles` など merge 以外のサブコマンド仕様を調べたいとき。
- INDEX.md の自動生成や Structured Output の共通仕様だけを調べたいとき。
- git merge や conflict 解消に関する一般的な Git の使い方だけを知りたいとき。

## hash

- 5b43334527c457c86e109e32bb6741a4a81e840be17191070ebbea74d7b0d017
