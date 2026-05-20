# `commons`

## Summary

- `src/commons` は cmoc のサブコマンド横断で使う共通 Python モジュール群を収めるディレクトリです。
- Codex CLI 実行、Structured Output 検証、ログ保存、quota 待機・resume、JSON 応答パースなどの Codex 連携処理は `codex.py` に集約されています。
- Typer サブコマンド共通の repo root 解決、例外捕捉、終了コード変換は `command_runner.py` が担当します。
- 利用者向け復旧アクション付き例外 `CmocError` と共通エラーレポート整形は `errors.py` に定義されています。
- `INDEX.md` の自動配置・更新、目次対象列挙、除外規則、内容 hash による再利用判定、目次生成用 Codex 呼び出しは `indexing.py` が扱います。
- git リポジトリ探索、ブランチ・HEAD 取得、`.cmoc` ignore 保証、pathspec commit、oracle・実装ファイル列挙、変更・削除検出、git コマンド実行は `repo.py` にまとまっています。
- cmoc 仕様のタイムスタンプ生成は `timestamps.py`、サブコマンドのステップ別経過時間計測と表示は `timing.py` が提供します。
- `__init__.py` は `src.commons` を Python パッケージとして宣言するだけで、実行時ロジックや公開 API の集約は行っていません。

## Read this when

- cmoc の個別サブコマンド実装から使う共通処理がどのモジュールにあるか判断したいとき。
- Codex CLI 呼び出し、model・reasoning effort、sandbox、Structured Output、ログ保存、リトライ、quota resume の実装入口を探しているとき。
- サブコマンドの Typer 関数から本体 handler を呼び出す共通ラッパー、repo root への移動、例外から `typer.Exit` への変換を確認したいとき。
- `CmocError` の作り方、共通エラーレポートの見出し構成、次アクションや詳細・コールスタックの表示形式を調べたいとき。
- `INDEX.md` の生成対象、除外対象、既存ブロック再利用、hash 判定、Structured Output schema、Codex への目次生成依頼を実装・修正したいとき。
- git repository root 探索、現在ブランチ、HEAD、cmoc ブランチ判定、`.cmoc` の git 追跡対象外保証、未コミット差分検査を使う・直すとき。
- oracle ファイルや実装ファイルの列挙、変更済みファイルの抽出、削除検出、root `.gitignore` の適用範囲を確認したいとき。
- 初期化差分や INDEX メンテナンス差分など、指定 path だけを既存 staged 差分と混ぜずに commit する共通処理を理解したいとき。
- cmoc の `<time-stamp>` 形式や、サブコマンド完了時のステップ別タイミング表示を確認したいとき。

## Do not read this when

- 個別サブコマンドのユーザー向け仕様、引数、標準出力、ワークフローの詳細だけを調べたいとき。
- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` の本体処理そのものを追いたいとき。
- 設定ファイル `comconfig.json` や `CMOConfig` の読み書き・補完・公開プロパティだけを確認したいとき。
- cmoc の正本仕様断片を読むためのルーティングが目的で、実装コードの共通モジュール配置を調べる必要がないとき。
- テスト fixture、Fake Codex CLI、pytest 設定など、テストコード側の具体的な構成だけを探しているとき。
- Codex CLI や git の一般的な外部仕様だけを知りたいとき。
- `src.commons` が Python パッケージかどうかだけを確認したい場合を除き、空に近い `__init__.py` の実装詳細を読む必要があるとき。

## hash

- 0144237a77df11e66fd423d3c695956f948f7084e985b8cb66bcb7824314588b

# `main.py`

## Summary

- `src/main.py` は cmoc CLI のエントリーポイントで、Typer アプリ `cmoc` と主要サブコマンドを定義するファイルです。
- `init`、`branch`、`eval-oracles`、`apply`、`merge` の CLI コマンドを登録し、各コマンドの実処理を `sub_commands` 配下の実装関数へ委譲します。
- `eval-oracles` は `--full` / `-f`、`apply` は `--repeat` / `-r` と `--full` / `-f`、`merge` は任意の `cmoc_branch` 引数を受け取ります。
- `main()` は `app(prog_name="cmoc", standalone_mode=False)` で Typer を起動し、Click/Typer の終了や例外を cmoc 共通の終了処理へ変換します。
- Click のパースエラーや想定外例外は `commons.errors.format_error_report` で整形して表示し、可能な範囲で適切な終了コードを維持します。
- `python src/main.py` による直接実行時も `main()` を呼び出して CLI を起動します。

## Read this when

- cmoc CLI にどのサブコマンドが登録されているか確認したいとき。
- サブコマンドの CLI 引数やオプションが、どの実装関数へ渡されるか調べたいとき。
- `init`、`branch`、`eval-oracles`、`apply`、`merge` の入口関数を探しているとき。
- Typer / Click の例外、パースエラー、終了コードが cmoc でどのように扱われるか確認したいとき。
- `cmoc` コマンド起動時または `python src/main.py` 直接実行時の制御フローを追いたいとき。
- CLI コマンド名、オプション名、デフォルト値、引数の受け渡しに関する変更やテストを行うとき。

## Do not read this when

- 各サブコマンドの具体的な業務ロジックやファイル操作の詳細だけを調べたいとき。
- `cmoc init`、`cmoc branch`、`cmoc eval-oracles`、`cmoc apply`、`cmoc merge` の内部仕様を確認したい場合で、読むべき `sub_commands` 配下の実装ファイルが既に分かっているとき。
- 共通エラーレポートの整形内容そのものを調べたいとき。
- 設定ファイル、リポジトリ探索、Codex CLI 呼び出し、ログ保存、INDEX 生成などの横断ユーティリティ実装を直接調べたいとき。
- Typer や Click の一般的な使い方だけを知りたいとき。
- cmoc 自体ではなく、cmoc を使って開発する対象リポジトリ側の実装や仕様を調べたいとき。

## hash

- 9c6e6b4368e24e2ab9abc5e0f6d509566ee247ff725c25bf519730d332c47514

# `sub_commands`

## Summary

- `src/sub_commands` は cmoc の各サブコマンド本体を実装する Python パッケージです。
- `__init__.py` はサブコマンド実装パッケージであることを示す最小限の初期化ファイルです。
- `init.py` は `cmoc init` の本体で、`.cmoc` を git 追跡対象外にする初期化、`.gitignore` や git index 変更のコミット、2 段階の進捗表示と時間計測を扱います。
- `branch.py` は `cmoc branch` の本体で、`cmoc_<timestamp>` 形式の作業ブランチ作成、base commit の `.cmoc/branch` への記録、`.cmoc` ignore 保証、衝突時リトライ、3 段階の進捗表示を扱います。
- `eval_oracles.py` は `cmoc eval-oracles` の本体で、`.cmoc` ignore 保証、`INDEX.md` メンテナンス、部分評価または全体評価の対象 oracle 選択、Codex CLI による oracle 評価、必須見出し検証、`.cmoc/reports/eval-oracles` への Markdown レポート保存を扱います。
- `apply.py` は `cmoc apply` の本体で、cmoc 作業ブランチ検証、oracle 差分コミット、`INDEX.md` メンテナンス、Codex CLI による oracle と実装の不整合調査、Structured Output 検証、不整合への実装修正依頼、禁止パス検査、変更コミット、`.cmoc/reports/apply` へのレポート保存を扱います。
- `merge.py` は `cmoc merge` の本体で、作業ツリー検証、merge 元 cmoc ブランチ解決、`git merge --no-ff`、conflict 時の Codex CLI 解消依頼、conflict marker 検査、merge commit、source branch の安全な削除を扱います。
- 各ファイルは `commons.command_runner`、`commons.repo`、`commons.codex`、`commons.indexing`、`commons.timing` などの共通処理を組み合わせ、サブコマンドごとの制御フロー、進捗表示、Codex CLI プロンプト、レポート生成を担当します。

## Read this when

- cmoc の個別サブコマンド実装がどのファイルに分かれているか判断したいとき。
- `cmoc init`、`cmoc branch`、`cmoc eval-oracles`、`cmoc apply`、`cmoc merge` の実装本体や実行順序を調べたいとき。
- サブコマンドごとの stdout 進捗表示、`StepTimer` による計測、共通 runner への委譲箇所を確認したいとき。
- サブコマンドが `.cmoc` ignore 保証、base commit 記録、oracle 変更検出、INDEX.md メンテナンス、git commit、レポート保存をどのタイミングで呼ぶか調べたいとき。
- Codex CLI に渡す eval-oracles、apply、不整合調査、実装修正、commit message 生成、merge conflict 解消用プロンプトを確認したいとき。
- `cmoc apply` の Structured Output schema、不整合 payload 検証、部分適用と全体適用の切り替え、未収束時の終了コードやレポート検証を追いたいとき。
- `cmoc merge` の未マージ cmoc ブランチ自動解決、conflict marker 検出、手動解決が必要な場合の扱いを確認したいとき。
- サブコマンドの自動テストを書くために、直接呼び出し可能な `cmoc_*_impl` 関数や主要な補助関数の責務を把握したいとき。

## Do not read this when

- CLI エントリーポイントでサブコマンドがどう登録されるかだけを調べたいとき。
- repo root 探索、共通エラー整形、git 実行、Codex CLI 呼び出し、JSON パース、INDEX.md メンテナンス、タイマー、タイムスタンプなどの共通ユーティリティ実装だけを調べたいとき。
- cmoc の正本仕様断片を確認したいとき。仕様は `oracles` 配下の該当 `INDEX.md` から必要なファイルへ辿るべきです。
- cmoc 自体の開発規約、設計規約、テスト規約、開発環境ルールだけを確認したいとき。
- `tests` 配下のテスト fixture、Fake Codex CLI、pytest の具体的なテスト実装だけを調べたいとき。
- `README.md`、`AGENTS.md`、`oracles`、`memo` などのリポジトリ運用ルールや編集可否だけを確認したいとき。
- cmoc を使って開発する `<repo-root>` 側の oracle 内容や実装対象ファイルを調べたいとき。
- 特定の共通処理のバグを修正したいだけで、サブコマンド側の制御フローやプロンプトが関係しないとき。

## hash

- a0b9b10643e4c7ef1adb2fa9a1f7c488490cecab85e158ccfdf46f39d98c46ec
