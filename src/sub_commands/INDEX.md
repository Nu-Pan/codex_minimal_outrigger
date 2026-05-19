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
- cmoc 作業ブランチ上でのみ実行できることを検査し、oracle 外の未コミット差分を拒否し、`.cmoc` の ignore 保証や oracle 変更の commit、`INDEX.md` メンテナンスを行う。
- oracle ファイルごとに Codex CLI の read-only 実行で実装との不整合を Structured Output として調査し、不整合があれば workspace-write 実行で修正を依頼する反復ループを持つ。
- 実装修正後は `oracles/` と `.agents/` の禁止領域が変更されていないことを検査し、INDEX 更新後に Codex CLI で commit message を生成して全差分を commit する。
- apply の収束・未収束、ループごとの不整合件数、ブランチ上の変更内容を `.cmoc/reports/apply/<timestamp>.md` にレポートとして保存し、未収束時は終了コード 2 を返す。
- 不整合調査用 JSON schema、調査・修正・レポート・commit message 生成用プロンプト、Structured Output の厳密なバリデーション補助関数を含む。

## Read this when

- `cmoc apply` の処理順序、ステップ表示、終了コード、レポート生成の流れを確認したいとき。
- apply 実行前のブランチ検査、作業ツリー検査、`.cmoc` ignore 保証、oracle 変更 commit の扱いを調べたいとき。
- oracle と実装の不整合を Codex CLI に調査させる Structured Output schema や、その検証ロジックを確認したいとき。
- 不整合解消を Codex CLI に依頼する prompt、read-only と workspace-write の使い分け、反復回数 `repeat` の扱いを調べたいとき。
- Codex CLI による実装修正後、`oracles/` や `.agents/` の禁止変更をどう検出して中断するか確認したいとき。
- apply が生成する commit message、commit 対象、INDEX 更新タイミング、作業レポート保存先を調べたいとき。

## Do not read this when

- `cmoc init`、`cmoc branch`、`cmoc merge`、`cmoc eval-oracles` の個別実装だけを調べたいとき。
- Codex CLI 呼び出しの低レベル実装、JSON パース、共通コマンド実行、git ラッパー、INDEX メンテナンスの内部詳細だけを知りたいとき。
- oracle 仕様ファイルそのものの内容や、`oracles/INDEX.md` のルーティング情報を確認したいとき。
- cmoc の CLI 引数定義やサブコマンド登録箇所だけを調べたいとき。
- テストコードの構成、Fake Codex CLI、pytest 上の期待値だけを確認したいとき。
- `cmoc apply` を使う側のリポジトリで発生した具体的な不整合内容を調査したいだけのとき。

## hash

- fb84093b01667d6890786ce109f296288f18142ff8b3ebaddf0926c491b0f585

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

# `eval-oracles.py`

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

# `eval_oracles.py`

## Summary

- Python の import 名として使える `eval_oracles` モジュールから、ハイフンを含む実体ファイル `eval-oracles.py` を読み込むための互換ローダーです。
- `Path(__file__).with_name("eval-oracles.py")` で同じディレクトリの本体ファイルを特定し、その内容を UTF-8 で読み込んで `compile` と `exec` により現在のモジュール名前空間へ展開します。
- `cmoc eval-oracles` の実行ロジック自体はこのファイルには直接書かれておらず、実体は `src/sub_commands/eval-oracles.py` にあります。

## Read this when

- `src.sub_commands.eval_oracles` という通常の Python import 名で `eval-oracles.py` の内容を参照できる仕組みを確認したいとき。
- ハイフンを含むファイル名 `eval-oracles.py` と、アンダースコア名の互換モジュール `eval_oracles.py` の関係を調べたいとき。
- テストや他モジュールから `eval-oracles` 本体を import する経路がどこで用意されているか確認したいとき。

## Do not read this when

- `cmoc eval-oracles` の処理順序、部分評価条件、Codex CLI 評価プロンプト、レポート生成処理を調べたいとき。その場合は `src/sub_commands/eval-oracles.py` を読むべきです。
- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc merge` など、他サブコマンドの実装を調べたいとき。
- Codex CLI 呼び出し、INDEX.md メンテナンス、repo 操作、StepTimer、timestamp 生成などの共通処理の内部実装を確認したいとき。
- oracle 正本仕様の内容や `cmoc eval-oracles` のユーザー向け仕様を確認したいだけで、Python import 互換ローダーの仕組みが不要なとき。

## hash

- f379ba6eee9ecf739a17cc501c7a4ec3f99a0358158c5c065aa8a98b9e15cff0

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

- `cmoc merge` の本体処理を実装するモジュール。
- 未コミット変更の有無や `.cmoc` ignore 状態を検証し、明示指定された cmoc ブランチ、または未マージ cmoc ブランチ候補から自動解決した 1 件を現在の HEAD へ `git merge --no-ff` する。
- merge conflict が発生した場合、unmerged path を取得して Codex CLI に conflict marker 解消を依頼し、marker 残存確認、対象ファイルの `git add`、unmerged path 再確認、`git commit --no-edit` までを行う。
- merge 完了後は `git branch -d` による source branch 削除を試み、失敗時は warning に留める。
- merge 開始後に例外が発生した場合は、merge state をロールバックせず手動解決が必要であることを stderr に表示する。
- 進捗表示と `StepTimer` による `validate repository state`、`resolve source branch`、`run git merge`、`delete source branch if safe` のステップ計測を行う。

## Read this when

- `cmoc merge` コマンドの実行フロー、前提条件検証、進捗表示、時間計測の実装を確認したいとき。
- 未マージ cmoc ブランチを自動選択する条件や、候補が 0 件または複数件だった場合のエラー処理を調べたいとき。
- `git merge --no-ff` の失敗時に Codex CLI へ conflict 解消を依頼する処理を確認したいとき。
- conflict marker の検出、unmerged path の取得、解決後の `git add` と merge commit 作成の責務を調べたいとき。
- merge 後に source branch を安全な場合だけ削除する処理や、削除失敗時の warning 表示を確認したいとき。
- merge 開始後の例外時に、ロールバックせず手動解決を促す挙動を確認したいとき。

## Do not read this when

- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles` など、merge 以外のサブコマンド本体を調べたいとき。
- CLI 引数パースやサブコマンド登録など、`cmoc merge` を呼び出す外側のエントリーポイントを確認したいとき。
- `run_git`、`assert_no_uncommitted_changes`、`ensure_cmoc_ignored`、`run_command`、`run_codex_exec`、`StepTimer` などの共通 helper 自体の詳細実装を調べたいとき。
- cmoc の正本仕様、ユーザー向け仕様、開発ルール、テスト規約を確認したいとき。
- merge conflict の一般的な Git 操作方法だけを知りたいとき。

## hash

- a9075e3e12b541b2c55ed64ef0aea73ca3b7289325ead8e3a7372c061989ee5b
