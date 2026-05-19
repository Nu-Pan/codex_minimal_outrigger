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

- `src/sub_commands` は、cmoc の各 CLI サブコマンド本体を実装するパッケージです。
- `init.py`、`branch.py`、`apply.py`、`eval_oracles.py`、`merge.py` に、各サブコマンドの実行フロー、進捗表示、共通 helper 呼び出し、Codex CLI 呼び出し、レポート保存や git 操作の制御が分かれて配置されています。
- `__init__.py` はサブコマンド実装パッケージであることを示すだけの初期化ファイルで、実行ロジックは含みません。
- `cmoc init` は `.cmoc` を git 追跡対象外にする初期化処理と、その変更の commit を扱います。
- `cmoc branch` は cmoc 作業用ブランチの作成、base commit の記録、`.cmoc` ignore 保証を扱います。
- `cmoc apply` は oracle と実装の不整合調査、Codex CLI による実装修正依頼、禁止パス検査、変更 commit、apply レポート生成を扱う大きな実装です。
- `cmoc eval-oracles` は oracle 断片の部分評価または全体評価を Codex CLI に依頼し、評価結果を Markdown レポートとして保存します。
- `cmoc merge` は cmoc ブランチの merge、未マージ cmoc ブランチの自動解決、conflict 発生時の Codex CLI 解消依頼、merge commit、source branch 削除を扱います。

## Read this when

- cmoc の個別サブコマンド本体がどのファイルに実装されているか確認したいとき。
- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` の実行順序、進捗表示、終了時処理を調べたいとき。
- 各サブコマンドが `commons` 配下の repo helper、command runner、Codex CLI wrapper、index maintenance、timer などをどこで呼び出すか確認したいとき。
- サブコマンドごとの git 操作、`.cmoc` ignore 保証、branch/base commit 管理、oracle 差分処理、レポート生成の接続点を探しているとき。
- Codex CLI に渡す apply 不整合調査、実装修正、commit message 生成、oracle 評価、merge conflict 解消の prompt を確認したいとき。
- サブコマンドの実装を修正する前に、対象ファイルを `init.py`、`branch.py`、`apply.py`、`eval_oracles.py`、`merge.py` のどれに絞るべきか判断したいとき。

## Do not read this when

- CLI 引数解析、サブコマンド登録、エントリーポイント全体の構造だけを調べたいとき。
- repo root 探索、git コマンド実行、Codex CLI 実行、Structured Output parsing、INDEX.md メンテナンス、timestamp、StepTimer などの共通 helper 自体の詳細実装だけを調べたいとき。
- cmoc の正本仕様断片やユーザー向け仕様を読みたいだけで、Python 実装の配置を確認する必要がないとき。
- 自動テスト、Fake Codex CLI、pytest 規約、テストケースの配置を調べたいとき。
- README、AGENTS、oracles、memo などの編集可否やリポジトリ運用ルールだけを確認したいとき。
- cmoc を用いて開発する `<repo-root>` 側の oracle 内容、生成済みレポート、または自動生成された `INDEX.md` の内容だけを読みたいとき。

## hash

- 980e41cbca3d5840393a9c040e267cb26f60fc290bc242b3c18e47c8d0b7ab0f
