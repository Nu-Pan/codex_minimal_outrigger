# `commons`

## Summary

- `src/commons` は cmoc のサブコマンド横断で使う共通処理を集約する Python パッケージです。
- Codex CLI 呼び出し、Structured Output 検証、ログ保存、リトライ、quota 待機・resume、JSON 応答パースは `codex.py` が扱います。
- Typer サブコマンドの共通実行ラッパー、`<repo-root>` 解決、共通エラー表示への変換は `command_runner.py` が扱います。
- 利用者向け復旧アクション付き例外 `CmocError` と、`ERROR` レポート整形は `errors.py` が扱います。
- `INDEX.md` の配置対象列挙、除外規則、内容 hash に基づく再利用・更新、Codex CLI への目次生成依頼、自動コミット連携は `indexing.py` が扱います。
- git リポジトリ検出、ブランチ・HEAD 取得、`.cmoc` ignore 保証、未コミット差分検査、oracle・実装ファイル列挙、指定 pathspec commit などの git 共通処理は `repo.py` が扱います。
- cmoc 仕様のタイムスタンプ生成は `timestamps.py`、サブコマンドのステップ別経過時間計測と表示は `timing.py` が扱います。
- `__init__.py` は `src.commons` パッケージ宣言のみで、実行時ロジックや公開 API 集約は持ちません。

## Read this when

- cmoc の複数サブコマンドから共有される実行制御、エラー処理、git 操作、Codex CLI 呼び出し、INDEX 保守、時刻・計測処理の入口を探したいとき。
- Typer の各サブコマンド関数を薄く保つために、共通ラッパーや `<repo-root>` 解決がどこで行われているか確認したいとき。
- Codex CLI 連携の共通仕様として、`codex exec` の引数、sandbox、model、reasoning effort、Structured Output、ログ保存、検証リトライ、quota 枯渇時の再開処理を調べたいとき。
- cmoc 全体の例外型、エラーレポート形式、終了コード変換、利用者向け次アクションの扱いを実装または修正したいとき。
- `INDEX.md` の自動生成・更新、目次対象の除外規則、hash による再生成判定、既存ブロック再利用、`.cmoc` ignore 保証や自動コミットとの連携を確認したいとき。
- git リポジトリ root 探索、cmoc ブランチ判定、未コミット差分チェック、`.cmoc` の追跡対象外化、oracle ファイルや実装ファイルの列挙、削除ファイル検出、指定パスだけの commit 処理を調べたいとき。
- ログ名・ブランチ名・ディレクトリ名などで使う `<time-stamp>` 形式や、サブコマンド完了時の step timing 表示を確認したいとき。
- 個別サブコマンドの実装中に、既存の共通ユーティリティを使うべきか、新しい共通処理を追加すべきか判断したいとき。

## Do not read this when

- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` など、個別サブコマンド固有の業務ロジックや CLI オプションだけを調べたいとき。
- cmoc の正本仕様断片そのものを確認したいとき。この場合は `oracles` 配下の該当 `INDEX.md` から必要な仕様ファイルへ進むべきです。
- 設定ファイル `comconfig.json` や `CMOConfig` の読み書き・補完・公開プロパティだけを調べたいとき。
- README、AGENTS、oracles、memo などのリポジトリ運用ルールや編集可否だけを確認したいとき。
- テストコード、Fake Codex CLI、pytest fixture、テスト用データの配置だけを調べたいとき。
- Codex CLI や git の一般的な使い方だけを知りたいとき。cmoc 固有の共通実装に関心がない場合は読む必要はありません。
- `INDEX.md` の生成結果としての目次本文だけを読みたいとき。自動メンテナンス処理や hash 判定の実装に関心がないなら `indexing.py` ではなく対象ディレクトリの `INDEX.md` を読むべきです。
- 単一ファイル内の局所的な実装詳細が既に分かっており、共通モジュール全体のルーティング情報が不要なとき。

## hash

- 877ad4da645990535e7fd4fadaacae166b5436e738b7ac0cdd7fc523112ea6ae

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

- `src/sub_commands` は cmoc の個別サブコマンド本体実装を配置するパッケージです。
- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` の実行フロー、進捗表示、共通 runner への委譲、repo helper や Codex CLI 連携の呼び出し箇所を扱います。
- `init.py` は `.cmoc` を git 追跡対象外にする初期化処理と、その変更の commit 処理を実装します。
- `branch.py` は `cmoc_<timestamp>` 形式の作業用ブランチ作成、base commit 記録、`.cmoc` ignore 保証を実装します。
- `apply.py` は cmoc 作業ブランチ上で oracle 変更を commit し、`INDEX.md` をメンテナンスし、oracle と実装の不整合調査、Codex CLI による実装修正、禁止パス検査、変更 commit、apply レポート生成を行います。
- `eval_oracles.py` は oracle ファイルの部分評価または全体評価を選択し、Codex CLI による仕様評価結果を `.cmoc/reports/eval-oracles` に Markdown レポートとして保存します。
- `merge.py` は cmoc ブランチの merge、未マージ cmoc ブランチの自動解決、conflict 発生時の Codex CLI 解消依頼、marker 検査、merge commit、作業ブランチ削除を扱います。
- `__init__.py` はサブコマンド実装パッケージであることを示すだけで、実行ロジックや公開 API は定義しません。

## Read this when

- cmoc の個別サブコマンド本体がどのファイルに実装されているか判断したいとき。
- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` の実装フローやステップ表示を確認したいとき。
- サブコマンドが共通 runner、repo helper、timing、timestamp、indexing、Codex CLI ラッパーをどの順序で呼び出すか調べたいとき。
- `.cmoc` ignore 保証、初期化 commit、作業用ブランチ作成、base commit 記録など、cmoc 作業準備系サブコマンドの実装を確認したいとき。
- oracle 変更を実装へ反映する `cmoc apply` の調査対象選択、Structured Output schema、prompt、validator、不整合整理、実装修正、禁止パス検査、レポート生成を調べたいとき。
- oracle 仕様評価を行う `cmoc eval-oracles` の部分評価・全体評価の判定、評価 prompt、必須見出し検証、レポート保存形式を確認したいとき。
- cmoc ブランチを merge する処理、conflict 解消を Codex CLI に依頼する条件、conflict marker 検査、merge commit、作業ブランチ削除の挙動を調べたいとき。
- サブコマンド実装のテストを書くために、直接呼び出し可能な `cmoc_*_impl` 関数や内部 helper の責務を確認したいとき。

## Do not read this when

- argparse でサブコマンドがどのように登録されるか、CLI エントリーポイントだけを調べたいとき。
- repo root 探索、共通エラー整形、git 実行、変更ファイル列挙、`.cmoc` パス生成などの共通 helper の内部実装だけを確認したいとき。
- Codex CLI 呼び出しの低レベル実装、ログ保存、リトライ、sandbox 指定、Structured Output の共通処理だけを調べたいとき。
- `INDEX.md` メンテナンス処理そのものの対象ディレクトリ、除外規則、ハッシュ判定、目次生成 prompt の詳細だけを調べたいとき。
- cmoc の正本仕様断片やユーザー向け仕様を確認したいだけで、Python 実装コードを読む必要がないとき。
- Python コーディング規約、テスト規約、開発環境、依存管理など、cmoc 開発者向けルールだけを調べたいとき。
- `.cmoc/reports` 配下に保存された過去の apply レポートや eval-oracles レポートの内容を読みたいだけのとき。
- cmoc を使って開発する `<repo-root>` 側の oracle、実装、テスト、生成済み `INDEX.md` の内容を調べたいとき。

## hash

- 6eb2dc5308abcd4c7e92b5a71c106c67adcc3721b5de73ead0b90a73e3a3f4cb
