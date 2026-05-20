# `commons`

## Summary

- `src/commons` は、cmoc の各サブコマンドから共有される基盤処理を集約する Python パッケージです。
- Codex CLI 呼び出し、Structured Output 検証、ログ保存、`INDEX.md` 自動メンテナンス、共通エラー整形、Typer 実行ラッパーを扱います。
- git リポジトリルート探索、cwd 固定、`.cmoc` の git 追跡対象外保証、未コミット差分検査、oracle ファイル列挙、共通 git 実行処理を提供します。
- cmoc 仕様のタイムスタンプ生成と、サブコマンドのステップ別・総経過時間レポート用タイマーを含みます。
- `__init__.py` はパッケージ宣言のみで、実装の中心は `codex.py`、`command_runner.py`、`errors.py`、`indexing.py`、`repo.py`、`timestamps.py`、`timing.py` に分かれています。

## Read this when

- cmoc の複数サブコマンドで共有する処理の実装場所を探したいとき。
- `codex exec` の呼び出し方法、サンドボックス指定、Structured Output schema、JSON リトライ、ログ保存、進捗表示を確認したいとき。
- `INDEX.md` の配置対象、除外規則、目次生成プロンプト、既存エントリ再利用、内容ハッシュ比較、自動コミット処理を調べたいとき。
- cmoc の共通エラー型、エラーレポート形式、例外から `typer.Exit` への変換、終了コードの扱いを確認したいとき。
- `<repo-root>` の探索、カレントディレクトリ変更、git コマンド実行、`.cmoc` ignore 保証、未コミット差分チェックを実装または修正するとき。
- oracle ファイルの列挙、変更済み oracle ファイルの検出、削除済み oracle ファイルの判定、root `.gitignore` による除外処理を確認したいとき。
- cmoc ブランチ名の形式判定、HEAD commit 取得、cmoc branch の base commit 記録ファイルの扱いを調べたいとき。
- ログ名やブランチ名などに使う `<time-stamp>` 生成形式、またはサブコマンドのステップ時間計測と表示形式を確認したいとき。

## Do not read this when

- 個別サブコマンドのユーザー向け仕様、引数、処理順序、プロンプト内容だけを調べたいとき。
- cmoc の正本仕様断片を読みたいだけで、実装コードの共通処理を確認する必要がないとき。
- テストコード、pytest 設定、Fake Codex CLI など、テスト実装の詳細だけを探しているとき。
- README、AGENTS、oracles、memo の編集可否やリポジトリ運用ルールだけを確認したいとき。
- cmoc を用いて開発される別リポジトリ側のアプリケーションコードや業務ロジックを調べたいとき。
- 生成済みの `INDEX.md` の内容だけを読みたい場合で、生成・保守ロジックや共通基盤の実装が不要なとき。
- Python 標準ライブラリ、Typer、git、Codex CLI、JSON Schema の一般的な使い方だけを知りたいとき。

## hash

- 5dba14c56d902200fbc419b983c288de7efff896e654fec5ae4afd1262f44e1f

# `main.py`

## Summary

- `src/main.py` は cmoc CLI の Typer エントリーポイントです。
- `cmoc init`、`cmoc branch`、`cmoc eval-oracles`、`cmoc apply`、`cmoc merge` の各サブコマンドを登録し、実処理を `sub_commands` 配下の実装関数へ委譲します。
- ハイフンを含む `sub_commands/eval-oracles.py` は通常 import ではなく `importlib.util` で読み込み、`cmoc_eval_oracles_impl` を取得します。
- `main()` は `app(prog_name="cmoc", standalone_mode=False)` で Typer を起動し、Click/Typer の終了や例外を cmoc 共通エラーレポート形式へ変換します。
- `python src/main.py` で直接実行された場合も `main()` を呼び出して CLI を起動します。

## Read this when

- cmoc CLI のトップレベル構成、サブコマンド登録、Typer アプリ定義を確認したいとき。
- `init`、`branch`、`eval-oracles`、`apply`、`merge` の CLI callback がどの実装関数へ委譲されるか調べたいとき。
- `eval-oracles.py` のようなハイフン付きファイル名のサブコマンド実装を、どのように動的ロードしているか確認したいとき。
- CLI parse error、ClickException、想定外例外がどのように共通エラーレポートへ整形され、終了コードへ変換されるか調べたいとき。
- `cmoc` コマンド実行時または `python src/main.py` 直接実行時の起動経路を確認したいとき。

## Do not read this when

- 各サブコマンドの具体的な業務ロジック、git 操作、Codex CLI 呼び出し、ファイル生成処理の詳細を調べたいとき。
- `commons.errors.format_error_report` のエラーレポート内容や整形ルールそのものを確認したいとき。
- cmoc の正本仕様、開発規約、テスト規約を調べたいとき。
- `src/sub_commands` 配下の個別実装ファイルや `commons` 配下の共通処理の内部構造だけを調べたいとき。
- README、AGENTS、oracles、memo などのリポジトリ運用ルールや編集可否だけを確認したいとき。

## hash

- 0f134142481216bb3b754486a7b245b44d4e24ebe5602cb9712613d61c22faa2

# `sub_commands`

## Summary

- `src/sub_commands` は cmoc の各サブコマンド本体実装を置くパッケージです。
- `__init__.py` はサブコマンド実装パッケージであることを示すだけの初期化ファイルです。
- `init.py` は `cmoc init` の実装で、`.cmoc` を git 追跡対象外にする保証、初期化差分のコミット、2段階の進捗表示と時間レポートを扱います。
- `branch.py` は `cmoc branch` の実装で、`cmoc_<timestamp>` 形式の作業ブランチ作成、衝突時リトライ、`.cmoc` ignore 保証、作成元 commit の `.cmoc/branch` 記録を扱います。
- `eval-oracles.py` は `cmoc eval-oracles` の実装で、`.cmoc` ignore 保証、`INDEX.md` メンテナンス、部分評価または全体評価の対象 oracle 選択、Codex CLI による oracle 評価、Markdown レポート保存を扱います。
- `apply.py` は `cmoc apply` の実装で、cmoc ブランチ制約、oracle 外差分の拒否、`INDEX.md` メンテナンス、oracle と実装の不整合調査、Codex CLI による実装修正、禁止パス検査、コミット、apply レポート生成を扱います。
- `merge.py` は `cmoc merge` の実装で、未コミット差分確認、merge 元 cmoc ブランチ解決、`git merge --no-ff`、conflict 時の Codex CLI 解消依頼、marker 残存検査、merge commit、source branch の安全な削除を扱います。
- 各サブコマンドは主に `commons.command_runner`、`commons.repo`、`commons.codex`、`commons.indexing`、`commons.timing`、`commons.timestamps` などの共通処理を組み合わせ、ユーザー向け進捗表示と実行フローを制御します。

## Read this when

- cmoc の個別サブコマンド本体がどのファイルに実装されているか判断したいとき。
- `cmoc init`、`cmoc branch`、`cmoc eval-oracles`、`cmoc apply`、`cmoc merge` の実行フローや責務を確認したいとき。
- サブコマンドごとの stdout 進捗表示、StepTimer による時間計測、レポート生成、コミット処理の呼び出し箇所を追いたいとき。
- サブコマンドが共通ユーティリティとどう接続しているか、特に repo root 解決、git 操作、`.cmoc` ignore 保証、Codex CLI 呼び出し、`INDEX.md` メンテナンスとの連携点を調べたいとき。
- oracle 評価、oracle と実装の不整合追従、merge conflict 解消など、Codex CLI をサブコマンドから呼び出す具体的なプロンプトや実行条件を確認したいとき。
- サブコマンド実装に対するテストを書くために、直接呼び出し可能な `cmoc_*_impl` 関数や補助関数の責務を把握したいとき。

## Do not read this when

- CLI エントリーポイントや argparse へのサブコマンド登録方法だけを調べたいとき。
- repo root 探索、git コマンドラッパー、Codex CLI 共通実行、Structured Output パース、`INDEX.md` 自動生成、タイマー、タイムスタンプなど、共通処理の内部実装だけを調べたいとき。
- cmoc の正本仕様断片やユーザー向け仕様だけを確認したいとき。
- cmoc 自体の開発規約、テスト規約、環境構築、README、AGENTS の編集可否など、リポジトリ運用ルールだけを確認したいとき。
- `tests` 配下の pytest 実装や Fake Codex CLI の詳細を調べたいとき。
- `__pycache__` 配下の Python バイトコードや生成物を調べようとしているとき。

## hash

- 692d5340418aefa4fec7b535cd3caac986a1ad47771e66c0365654280790dccb
