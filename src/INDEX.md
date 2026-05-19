# `commons`

## Summary

- `src/commons` は、cmoc のサブコマンド実装から共通利用される Python ユーティリティ群をまとめたパッケージです。
- Codex CLI 呼び出し、Structured Output 検証、`INDEX.md` 自動メンテナンス、共通エラー整形、Typer サブコマンド実行ラッパー、git リポジトリ操作、タイムスタンプ生成、ステップ時間計測を扱います。
- `codex.py` は `codex exec` の引数構築、サンドボックス指定、ログ保存、JSON リトライ、schema 検証を担当します。
- `indexing.py` は `INDEX.md` の配置対象列挙、除外規則、ハッシュ判定、既存目次再利用、Codex CLI による目次生成、自動コミットを担当します。
- `repo.py` は `<repo-root>` 探索、cwd 固定、git コマンド実行、`.cmoc` の ignore 保証、未コミット差分検査、oracle ファイル列挙、cmoc ブランチ関連情報を担当します。
- `command_runner.py`、`errors.py`、`timestamps.py`、`timing.py` は、それぞれサブコマンド共通の実行制御、エラーレポート、`<time-stamp>` 生成、経過時間表示を担当します。

## Read this when

- cmoc の複数サブコマンドから共有される処理の実装場所を探したいとき。
- CLI エントリーポイントからサブコマンド本体へ渡る前後の共通処理、repo root 解決、例外表示、終了コード変換を確認したいとき。
- Codex CLI 呼び出し、Structured Output schema、JSON 応答検証、リトライ、`.cmoc/logs/codex_exec` へのログ保存を実装または調査したいとき。
- `INDEX.md` の自動生成・更新、配置対象や除外対象、内容ハッシュ、既存ブロック再利用、目次生成プロンプトを確認したいとき。
- `.cmoc` を git 追跡対象外に保つ処理、`.gitignore` 更新、tracked `.cmoc` の解除、関連差分だけを commit する処理を調べたいとき。
- git の現在ブランチ、HEAD commit、未コミット差分、oracles 配下の変更ファイルや削除ファイルの判定を共通処理として使いたいとき。
- cmoc の `<time-stamp>` 形式や、サブコマンドのステップ別経過時間表示の実装を確認したいとき。

## Do not read this when

- 個別サブコマンドのユーザー向け仕様、オプション、処理順序だけを確認したいとき。
- cmoc のアプリケーション仕様や開発ルールの正本断片を探しており、実装コードではなく `oracles` 配下の仕様を読むべきとき。
- Typer アプリ本体のコマンド登録や各サブコマンド固有ロジックを調べたいとき。
- oracle 評価の判定内容、適用処理、merge 処理など、共通補助ではない業務ロジックの詳細を探しているとき。
- テストコード、pytest fixture、Fake Codex CLI など、テスト側の実装だけを確認したいとき。
- Python 標準ライブラリや git、Codex CLI、JSON Schema の一般的な使い方だけを知りたいとき。

## hash

- bb1dab836e77c45fcc3680bd19441413b960b61a72fc5abe5579ab9d33295617

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

- `src/sub_commands` は cmoc の各サブコマンド本体を実装する Python パッケージです。
- `init.py`、`branch.py`、`apply.py`、`eval-oracles.py`、`merge.py` に、それぞれ `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` の実行フローが分かれて配置されています。
- 各サブコマンドは共通 runner、repo helper、Codex CLI 呼び出し、INDEX メンテナンス、StepTimer などの共通モジュールを呼び出し、サブコマンド固有の前提条件検査、進捗表示、レポート生成、commit や merge などの操作をまとめています。
- `eval_oracles.py` は通常の Python import 名から、ハイフンを含む本体ファイル `eval-oracles.py` を読み込むための互換ローダーです。
- `__init__.py` はサブコマンド実装パッケージであることを示すだけで、実行ロジックは持ちません。
- `__pycache__` 配下は Python の実行時キャッシュであり、仕様調査や実装確認の通常対象ではありません。

## Read this when

- cmoc の個別サブコマンド本体がどのファイルに実装されているか確認したいとき。
- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` の処理順序、前提条件検査、stdout 進捗表示、終了時処理を調べたいとき。
- サブコマンドが `.cmoc` ignore 保証、INDEX.md メンテナンス、oracle 変更の扱い、Codex CLI 呼び出し、レポート保存、git commit や git merge とどう接続しているか確認したいとき。
- `cmoc apply` の不整合調査、Structured Output schema、Codex CLI による実装修正依頼、禁止パス検査、commit message 生成、未収束時の終了コードを調べたいとき。
- `cmoc eval-oracles` の部分評価と全体評価の切り替え条件、oracle 評価プロンプト、評価レポート生成を確認したいとき。
- `cmoc merge` の未マージ cmoc ブランチ解決、conflict marker 解消依頼、merge commit 作成、source branch 削除の流れを調べたいとき。
- `eval-oracles.py` と `eval_oracles.py` の関係や、テスト・他モジュールから eval-oracles 本体を import する仕組みを確認したいとき。

## Do not read this when

- CLI 引数解析、サブコマンド登録、エントリーポイント全体の構造だけを調べたいとき。
- repo root 探索、git 実行ラッパー、`.cmoc` パス生成、oracle ファイル列挙、共通エラー整形、StepTimer、timestamp 生成など、共通 helper 自体の詳細実装だけを確認したいとき。
- Codex CLI 呼び出しの低レベル実装、JSON パース、ログ保存、リトライ、サンドボックス指定などの共通処理だけを調べたいとき。
- INDEX.md 自動メンテナンス処理そのものの内部実装や仕様だけを確認したいとき。
- cmoc の正本仕様断片、ユーザー向けワークフロー、開発ルール、テスト規約など、実装ファイル以外のルールを調べたいとき。
- 生成済みレポート、`.cmoc` 作業データ、Python の `__pycache__` キャッシュ内容を確認したいだけのとき。

## hash

- eb84bf680bcd8ae6066fb26a896f7afc0e063aabda9de293c064d012687b2cbe
