# `commons`

## Summary

- `src/commons` は、cmoc の複数サブコマンドから使われる共通処理を集約する Python パッケージです。
- Codex CLI 呼び出し、Structured Output 検証、`INDEX.md` 自動メンテナンス、共通エラー表示、Typer サブコマンド実行ラッパー、git リポジトリ状態検査、oracle ファイル列挙、タイムスタンプ生成、ステップ時間計測を扱います。
- `codex.py` は `codex exec` の実行、ログ保存、サンドボックス指定、JSON リトライと schema 検証の入口です。
- `indexing.py` は `INDEX.md` の配置対象列挙、除外規則、内容ハッシュ判定、Codex CLI による目次情報生成、既存目次ブロック再利用、自動コミットを担います。
- `repo.py` は `<repo-root>` 探索、cwd 固定、git コマンド実行、`.cmoc` ignore 保証、未コミット差分検査、oracle ファイル列挙、cmoc ブランチの base commit 記録読み取りを担います。
- `errors.py`、`command_runner.py`、`timestamps.py`、`timing.py` は、それぞれ共通エラー型と表示、CLI 実行制御、`<time-stamp>` 生成、ステップ別経過時間表示を提供します。

## Read this when

- cmoc の個別サブコマンドから再利用される共通ユーティリティの配置先や責務を把握したいとき。
- `codex exec` 呼び出し、Structured Output、JSON schema 検証、Codex 実行ログ、stdout 進捗表示、リトライ処理を確認・修正したいとき。
- `INDEX.md` の自動生成・更新、目次対象の除外規則、既存ブロックの再利用、内容ハッシュによる更新判定、目次生成 prompt を調べたいとき。
- サブコマンド実行時の `<repo-root>` 探索、カレントディレクトリ移動、Typer の終了コード変換、共通エラーレポート表示の流れを確認したいとき。
- `.cmoc` を git 追跡対象外にする処理、未コミット差分の検査、対象 path の clean 検査、初期化差分や INDEX メンテナンス差分の commit 補助を調べたいとき。
- oracle ファイル列挙、変更 oracle ファイル抽出、oracle 削除判定、root `.gitignore` の評価、cmoc ブランチ base commit ファイルの扱いを確認したいとき。
- ログ名やブランチ名などに使うタイムスタンプ形式、またはサブコマンドのステップ別・総経過時間表示を確認したいとき。
- 共通処理のテストを書くために、例外型、関数入口、副作用、git や Codex CLI への依存箇所を把握したいとき。

## Do not read this when

- 特定サブコマンドの CLI オプション、利用者向け説明、業務ロジックだけを調べたいとき。
- cmoc の正本仕様断片そのものを読む必要があり、実装コードではなく `oracles` 配下の仕様ファイルへのルーティングが必要なとき。
- README、AGENTS、memo、oracles の編集可否など、リポジトリ運用ルールだけを確認したいとき。
- cmoc を用いて開発する `<repo-root>` 側のアプリケーションコードや仕様を調べており、cmoc 自体の共通実装が不要なとき。
- pytest fixture、Fake Codex CLI、テストデータなど、テストコード側の実装詳細だけを調べたいとき。
- Codex CLI や git の一般的な使い方だけを知りたく、cmoc 固有のラッパーや制約を確認する必要がないとき。
- `__pycache__` などの生成物やバイナリキャッシュの内容を確認したいとき。

## hash

- 9ce21f978370248b2a06676cc19525708a656cdcd3a323c6b2abc1b04d62bde6

# `main.py`

## Summary

- cmoc CLI の Typer エントリーポイントを定義するファイル。
- `cmoc` アプリケーション本体を生成し、`init`、`branch`、`eval-oracles`、`apply`、`merge` の各サブコマンドを登録している。
- 各 CLI callback は引数やオプションを受け取り、実処理を `sub_commands` 配下の対応する実装関数へ委譲する。
- `main()` は `app(prog_name="cmoc", standalone_mode=False)` で Typer を起動し、Typer/Click 由来の終了や parse error、想定外例外を共通エラーレポート形式へ変換して終了コードを制御する。
- `python src/main.py` で直接実行された場合にも `main()` を呼び出す。

## Read this when

- cmoc CLI にどのサブコマンドが登録されているか確認したいとき。
- `init`、`branch`、`eval-oracles`、`apply`、`merge` の CLI 引数・オプションから本体実装への委譲関係を調べたいとき。
- `--full` や `--repeat`、`merge` の任意ブランチ引数など、トップレベル CLI の受け口を確認したいとき。
- Typer/Click の parse error や想定外例外が、cmoc の共通エラーレポートと終了コードへどう変換されるか調べたいとき。
- `cmoc` コマンドの起動経路、または `python src/main.py` による直接実行経路を確認したいとき。

## Do not read this when

- 各サブコマンドの具体的な処理内容や仕様準拠ロジックを調べたいとき。対応する `sub_commands` 配下の実装を読むべき。
- 共通エラーレポートの整形内容そのものを変更・確認したいとき。`commons.errors` を読むべき。
- Codex CLI 呼び出し、ログ保存、リトライ、oracle 評価などの詳細挙動を調べたいとき。
- cmoc のテスト実装、Fake Codex CLI、テスト用 fixture の構造を調べたいとき。
- リポジトリ初期化後の `<repo-root>` 側ファイル配置や `.cmoc` 配下の詳細を調べたいとき。

## hash

- c264f36683bb0871f97ca3b702e30b151da6231cdaac4c26e2e94d261367ddf0

# `sub_commands`

## Summary

- `src/sub_commands` は、cmoc の各サブコマンド本体を実装する Python パッケージです。
- `init.py`、`branch.py`、`apply.py`、`eval_oracles.py`、`merge.py` に、`cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` の実行フローが分かれて配置されています。
- 各モジュールは、共通 runner による `<repo-root>` 解決、`StepTimer` による進捗・時間計測、`commons.repo` や `commons.codex` などの共通処理呼び出しを組み合わせて、サブコマンド固有の手順を実装します。
- `init.py` は `.cmoc` を git 追跡対象外にする初期化処理と、その変更のコミット処理を扱います。
- `branch.py` は cmoc 作業ブランチの作成、base commit の記録、`.cmoc` ignore 保証を扱います。
- `apply.py` は oracle と実装の不整合調査、Codex CLI への実装修正依頼、禁止領域変更検査、実装差分 commit、apply レポート保存を扱います。
- `eval_oracles.py` は oracle 評価対象の選択、Codex CLI による仕様断片評価、評価レポート保存を扱います。
- `merge.py` は cmoc ブランチの解決、`git merge --no-ff`、conflict 発生時の Codex CLI 解消依頼、marker 検査、merge commit、作業ブランチ削除を扱います。
- `__init__.py` はサブコマンド実装パッケージであることを示すだけの軽量な初期化ファイルです。

## Read this when

- cmoc の各サブコマンド本体がどのファイルに実装されているか把握したいとき。
- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` の処理順序、進捗表示、終了条件を実装コードから確認したいとき。
- サブコマンド実装が `commons` 配下の共通 repo helper、Codex CLI 呼び出し、index メンテナンス、時間計測とどう接続しているか調べたいとき。
- `.cmoc` ignore 保証、cmoc ブランチ作成、base commit 記録、oracle 差分 commit、merge 元ブランチ解決など、サブコマンド単位の orchestration を確認したいとき。
- Codex CLI に渡す apply 不整合調査 prompt、実装修正 prompt、eval-oracles 評価 prompt、merge conflict 解消 prompt の組み立て箇所を探しているとき。
- apply や eval-oracles が `INDEX.md` メンテナンスをどのタイミングで実行するか確認したいとき。
- apply、eval-oracles、merge のレポート保存先や保存形式、検証処理との接続点を調べたいとき。
- サブコマンドのテストを追加・修正するために、対象となる実装関数や外部依存呼び出しを確認したいとき。

## Do not read this when

- argparse による CLI 引数定義、サブコマンド登録、エントリーポイントだけを調べたいとき。
- git 実行、repo root 探索、cmoc ブランチ判定、oracle ファイル列挙、`.cmoc` ignore 保証などの共通 helper 内部実装だけを確認したいとき。
- Codex CLI 呼び出し、JSON パース、Structured Output、ログ保存、サンドボックス指定、リトライなどの共通処理だけを調べたいとき。
- `INDEX.md` 自動生成・メンテナンス処理そのものの実装や仕様だけを確認したいとき。
- cmoc の正本仕様断片を確認したい場合で、実装コードではなく `oracles` 配下を読むべきとき。
- cmoc 自体の Python コーディング規約、テスト規約、開発環境など、開発者向けルールだけを調べたいとき。
- pytest fixture、Fake Codex CLI、テストデータなど、テスト実装の詳細だけを確認したいとき。
- 生成済みの `.cmoc/reports` 配下のレポート内容を読みたいだけのとき。

## hash

- 8cd808a410e2c52b360714bf48c5fe832c0631e5a7c9889fa29ac8d9fbe137ff
