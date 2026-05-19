# `conftest.py`

## Summary

- pytest execution helper that prepends the repository's src directory to sys.path so tests can import cmoc source modules without installation.
- Defines SRC as the repository root's src path relative to tests/conftest.py and inserts it at the front of Python's import search path.

## Read this when

- Investigating how tests import modules from <cmoc-root>/src.
- Debugging pytest import errors, module resolution order, or test environment setup.
- Changing the test suite's Python path/bootstrap behavior.

## Do not read this when

- Looking for individual test cases or assertions for cmoc behavior.
- Investigating application runtime import behavior outside pytest.
- Changing cmoc implementation code under <cmoc-root>/src.

## hash

- 32bfe11389fb732e9ac0cc6ecb2e14bf9722d848696fc618e360ef72c19633e7

# `test_codex.py`

## Summary

- `commons.codex.run_codex_exec` の振る舞いを検証する pytest テストファイル。
- Structured Output 利用時の JSON parse 失敗、JSON Schema 検証失敗、意味的バリデーション失敗に対する 3 回リトライとエラー詳細出力を検証する。
- `--output-schema` に渡す schema ファイル生成、codex exec 引数、ログへの試行情報・schema パス記録を検証する。
- Structured Output 指定時に `output_schema` が必須であることを検証する。
- 通常の Codex CLI 呼び出し直前に `commons.indexing.maintain_indexes` が実行されることと、`skip_index_maintenance=True` で明示的にスキップできることを検証する。
- テスト用の fake `codex` 実行ファイルを一時ディレクトリに作成し、`PATH` 差し替え、`tmp_path`、`monkeypatch`、`pytest.raises` を使って外部 Codex CLI 呼び出しを隔離している。

## Read this when

- `run_codex_exec` のリトライ、Structured Output、schema ファイル渡し、ログ出力に関する期待挙動を確認したいとき。
- Codex CLI 呼び出しラッパーのエラー詳細に `Last JSON error`、`Last stdout`、`Log` などが含まれるかを調べたいとき。
- `expect_json=True` と `output_schema`、`json_validator` の組み合わせに関するテストを追加・修正するとき。
- Codex CLI 呼び出し前の `INDEX.md` メンテナンス実行や `skip_index_maintenance` の仕様をテスト側から確認したいとき。
- fake `codex` コマンドを使った CLI ラッパーの単体テストパターンを参照したいとき。

## Do not read this when

- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc merge` など個別サブコマンドの CLI 仕様や統合テストを調べたいとき。
- `INDEX.md` 生成ロジックそのものの実装詳細や、目次メンテナンス対象ファイルの走査規則を調べたいとき。
- Codex CLI ラッパーではなく、git 操作、oracle 評価、ブランチ作成、マージ処理の実装を確認したいとき。
- 実際の Codex CLI の一般的な使い方や外部サービスとしての挙動を知りたいとき。
- cmoc のユーザー向け README やリポジトリ運用ルールだけを確認したいとき。

## hash

- 8e795a51180bf7dbecb39c8f35e9ac8facbd3fdae5515ad4c52b175f32f8a071

# `test_indexing.py`

## Summary

- `commons.indexing.maintain_indexes` による `INDEX.md` 自動メンテナンス処理を検証する pytest テストファイルです。
- git 管理下の一時リポジトリを作成し、目次エントリ生成、gitignore 対象の除外、空ディレクトリへの空 INDEX 作成、build/tmp の扱い、ネストした memo ディレクトリの扱いを確認します。
- 既存 INDEX エントリの必須セクション欠落時の再生成、Structured Output schema 不一致時のリトライ、最新 INDEX では Codex CLI を呼ばないこと、自動コミット時にメンテナンス対象パスだけをコミットすることを検証します。
- テスト用 git リポジトリ作成と git コマンド実行の補助関数 `_init_repo` と `_git` を含みます。

## Read this when

- `maintain_indexes` の期待挙動や回帰テストの対象範囲を確認したいとき。
- `INDEX.md` 生成時に gitignore、空ディレクトリ、build/tmp、memo ディレクトリがどう扱われるべきかを調べたいとき。
- INDEX エントリの hash が最新でも必須セクションが欠ける場合の再生成条件を確認したいとき。
- INDEX 生成用 Codex CLI の Structured Output schema、リトライ、未呼び出し条件をテストで確認したいとき。
- `commit_changes=True` による自動コミットがユーザー作業ファイルを巻き込まないことを確認したいとき。

## Do not read this when

- cmoc の CLI サブコマンド仕様やユーザー向けワークフローを調べたいだけのとき。
- `commons.indexing` の実装詳細を直接修正したいが、まず実装コードを読むべきとき。
- INDEX 以外の機能、たとえば branch、apply、merge、eval-oracles のテストを探しているとき。
- pytest や git 操作の一般的な使い方だけを知りたいとき。

## hash

- 7e58154a1a5e5987a5f2c7550e41f0147143513e45f5953660963380f90faf04

# `test_repo.py`

## Summary

- `tests/test_repo.py` は、`commons.repo` の git リポジトリ共通処理を検証する pytest テストファイルです。
- `find_repo_root` による親ディレクトリ探索、`ensure_cmoc_ignored` による `.cmoc` ignore 追記・冪等性・tracked `.cmoc` ファイルの index 除外を扱います。
- `list_oracle_files` の oracle ファイル列挙について、`INDEX.md` 除外、root `.gitignore` の尊重、tracked かつ ignored なファイルの除外、slash pattern、`**` semantics、oracles 配下 `.gitignore` の非使用、root 起点 basename pattern の扱いを検証します。
- `changed_oracle_files` の部分評価対象抽出について、cmoc ブランチ base commit からの committed 差分、未コミット変更、未追跡ディレクトリ配下の新規 oracle、gitignore 除外、slash pattern の階層 semantics を検証します。
- `has_deleted_oracle_files` による base..HEAD、working tree、staging area の oracle 削除検出と、削除時の全体評価切替条件を検証します。
- `assert_only_oracles_uncommitted` が `cmoc apply` の事前条件として oracles 外の未コミット差分を拒否することを検証します。
- `is_cmoc_branch` の cmoc ブランチ命名規則判定と、`branch_base_commit_path` の `.cmoc/branch` 配下記録先生成を検証します。
- テスト補助として、一時 git リポジトリを初期化する `_init_repo` と、指定 repo 上で git コマンドを実行する `_git` を定義しています。

## Read this when

- `commons.repo` の実装を変更し、リポジトリ root 探索、`.cmoc` ignore 保証、oracle ファイル列挙、oracle 差分抽出、oracle 削除検出の期待挙動を確認したいとき。
- root `.gitignore` の pattern 解釈を `list_oracle_files` や `changed_oracle_files` に反映する実装を修正するとき。
- `INDEX.md` や gitignored ファイルを oracle 列挙・部分評価対象から除外する条件を確認したいとき。
- `cmoc eval-oracles` の部分評価・全体評価切替に関係する、変更 oracle 抽出や oracle 削除検出のテスト観点を確認したいとき。
- `cmoc apply` の事前条件として、未コミット差分が oracles 配下だけかどうかを判定する仕様を確認したいとき。
- cmoc ブランチ名の形式や branch base commit 記録ファイルのパス生成を変更・確認したいとき。
- pytest 上で一時 git リポジトリを作って `commons.repo` の git 連携処理をテストする方法を参考にしたいとき。

## Do not read this when

- cmoc の CLI コマンド引数、stdout 表示、Codex CLI 呼び出し、Structured Output などのユーザー向け実行時仕様だけを調べたいとき。
- `commons.repo` 以外の実装、たとえばサブコマンド本体、Codex 実行ラッパー、ログ保存、プロンプト生成のテストを探しているとき。
- oracle 正本仕様そのものの内容や、`oracles` 配下のルーティング情報を確認したいだけのとき。
- README、AGENTS、memo、oracles などの編集可否やリポジトリ運用ルールだけを確認したいとき。
- gitignore pattern の一般仕様だけを調べており、cmoc の oracle ファイル列挙・差分抽出での適用挙動が不要なとき。

## hash

- 436bb2308067b9d20eb7220f14d6174748f1586a508f639c1ace9c38a6758c3c

# `test_subcommands.py`

## Summary

- `tests/test_subcommands.py` は、cmoc の主要サブコマンド本体と周辺ヘルパーの決定論的な制御ロジックを検証する pytest テストファイルです。
- `cmoc init` について、`.cmoc` を `.gitignore` に追加して commit すること、既に追跡されている `.cmoc` ファイルを追跡解除して commit すること、既存の `.gitignore` 差分を許容することを検証します。
- `cmoc branch` について、`cmoc_` で始まる作業ブランチを作成し、`.cmoc/branch/<branch>.txt` に base commit を記録することを検証します。
- `cmoc eval-oracles --full` について、INDEX メンテナンスと Codex CLI 呼び出しを fake に差し替えた上で評価レポートを `.cmoc/reports/eval-oracles` に保存すること、実装本体が import 可能な `eval_oracles.py` に置かれること、評価 prompt が実装・テスト・設定ファイル参照を禁止することを検証します。
- `cmoc apply` について、cmoc ブランチ上での不整合調査 JSON、Structured Output schema の利用、repeat 回数による実装ループ上限、レポート保存、終了コード、非 cmoc ブランチ拒否、oracle 外のユーザー差分拒否、`.cmoc` ignore 保証 commit と oracle commit の順序を検証します。
- `cmoc apply` 関連ヘルパーについて、INDEX メンテナンス後に禁止領域差分が発生した場合 `_commit_all_changes` が commit 前に停止すること、不整合 JSON payload が必須項目不足や近似キーを拒否することを検証します。
- `cmoc merge` について、明示された cmoc ブランチを clean tree で merge して安全なら削除すること、自動解決開始前の失敗では merge state 手動解決案内を表示しないこと、conflict 解消 prompt が常に oracles 編集を禁止すること、conflict marker 検査が渡された対象ファイル一覧を見ることを検証します。
- `main` の Typer 対応関数について、共通 runner ではなく各サブコマンド impl へ直接委譲すること、`python -m main --help` の Usage が `cmoc` コマンド名を表示することを検証します。
- テスト用 helper として、一時 git repository を初期化して初期 commit を作る `_init_repo` と、指定 repository で git コマンドを実行する `_git` を定義しています。

## Read this when

- cmoc のサブコマンド実装を変更し、既存テストがどの制御ロジックや git 操作を保護しているか把握したいとき。
- `cmoc init` の `.cmoc` ignore 保証、tracked `.cmoc` の追跡解除、`.gitignore` commit 挙動を確認したいとき。
- `cmoc branch` のブランチ命名や base commit 記録ファイルの期待値を確認したいとき。
- `cmoc eval-oracles` のレポート保存、prompt 制約、実装モジュール名に関するテストを探しているとき。
- `cmoc apply` の事前条件、repeat ループ、不整合 JSON schema、レポート保存、終了コード、commit 順序、禁止領域差分チェックを確認したいとき。
- `cmoc merge` の成功時ブランチ削除、自動解決失敗時の表示、conflict prompt、conflict marker 検出のテストを確認したいとき。
- Typer の CLI 関数が各 impl に直接委譲しているか、`cmoc --help` のコマンド名表示が守られているかを調べたいとき。
- 一時 git repository を使うテスト helper の書き方や、既存テストでの monkeypatch、capsys、subprocess の使い方を参考にしたいとき。

## Do not read this when

- サブコマンドの正本仕様そのものを確認したいとき。このファイルは仕様書ではなく、実装に対する自動テストです。
- cmoc の実装コードを直接修正したいだけで、既存テストの保護範囲や期待値を確認する必要がないとき。
- Codex CLI 呼び出し、prompt 構成、Structured Output、ログ保存などの横断仕様を体系的に調べたいとき。まず oracles 配下の該当仕様を読んでください。
- Python コーディング規約、設計規約、テスト規約、開発環境ルールを確認したいとき。このファイルではなく開発ルールのルーティング情報を参照してください。
- `cmoc` を用いて別の `<repo-root>` を開発する利用手順だけを知りたいとき。
- README、AGENTS、oracles、memo などの編集可否やリポジトリ運用ルールだけを確認したいとき。

## hash

- 4b6aaed4c68f03775e9036f8808b4152b85c780886eda6901c63306586a57b21

# `test_timestamps.py`

## Summary

- `commons.timestamps.make_timestamp` と `commons.timing.format_duration` の出力形式を検証するテストファイルです。
- cmoc timestamp が `YYYY-MM-DD_HH-MM_SS_mmm` 形式で、日時要素とミリ秒がゼロ埋めされることを確認します。
- 経過時間表示が stdout 用の固定幅 ` h  m  s` 形式になり、秒の小数第 1 位が切り捨てで表示されることを確認します。

## Read this when

- タイムスタンプ文字列の仕様や `make_timestamp` の期待フォーマットを確認したいとき。
- サブコマンド完了時などに表示する経過時間文字列のフォーマットを確認したいとき。
- `commons.timestamps` または `commons.timing` の出力仕様を変更し、その既存テスト影響を把握したいとき。

## Do not read this when

- タイムスタンプや経過時間表示と関係のない CLI サブコマンド仕様を調べているとき。
- 日時生成処理そのものの実装詳細だけを読みたいとき。
- Codex CLI 呼び出し、ログ保存、oracle 評価などの高レベルな実行仕様を確認したいとき。

## hash

- 05d4e42195653c5b491aa1c7a212a92f0c106b6988f231389a2ab14348ca30dc
