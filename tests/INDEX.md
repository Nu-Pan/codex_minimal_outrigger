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

- `commons.codex.run_codex_exec` の Codex CLI 呼び出しラッパーに関する pytest テストをまとめたファイルです。
- Structured Output の JSON parse 失敗、JSON Schema 不一致、意味的バリデーション失敗に対する 3 回リトライとエラー詳細を検証します。
- `--output-schema` に渡すスキーマファイル生成、ログへの試行情報・スキーマパス・標準出力情報の記録、stdout 進捗表示の 80 文字切り詰めと改行可視化を検証します。
- 通常の Codex CLI 呼び出し直前に `commons.indexing.maintain_indexes` が実行されることと、`skip_index_maintenance=True` で INDEX メンテナンスをスキップできることを検証します。
- テスト内では一時ディレクトリに fake `codex` 実行ファイルを作成し、`PATH` を差し替えて `run_codex_exec` の外部コマンド連携を制御します。

## Read this when

- `run_codex_exec` の Structured Output 対応、JSON 再試行、スキーマ検証、意味的バリデーション、エラー詳細のテストを確認したいとき。
- Codex CLI 呼び出し時に `--output-schema` がどのように渡され、`.cmoc/logs/codex_exec` のログへ何が残るべきかを確認したいとき。
- stdout 進捗表示で prompt と stdout の先頭 80 文字を扱う仕様のテスト例を探しているとき。
- Codex 呼び出し前の `INDEX.md` 自動メンテナンス実行や、INDEX 生成・merge conflict 解消向けのスキップ指定を確認したいとき。
- fake `codex` コマンド、`monkeypatch`、一時 git repo を使った `commons.codex` 周辺のテストパターンを参考にしたいとき。

## Do not read this when

- `run_codex_exec` の実装そのものを読みたいとき。
- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc merge` など個別サブコマンドの CLI 挙動テストを探しているとき。
- INDEX 生成ロジック自体の詳細実装や、`commons.indexing` の単体テストを確認したいとき。
- Codex CLI ではなく git 操作、oracle 評価、ファイルマージ処理などのテストを探しているとき。
- README、AGENTS、oracles、memo などのリポジトリ運用ルールや編集可否だけを確認したいとき。

## hash

- ff401a6a7b166b183f603554871dc502f0b7a0c4ccfa196b2404298ee0d8e030

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

- `tests/test_repo.py` は、`commons.repo` にある git リポジトリ共通処理の pytest テストをまとめたファイルです。
- `find_repo_root`、`ensure_cmoc_ignored`、`list_oracle_files`、`changed_oracle_files`、`has_deleted_oracle_files`、`assert_only_oracles_uncommitted`、`is_cmoc_branch`、`branch_base_commit_path` の挙動を検証します。
- 一時ディレクトリに実 git リポジトリを作成し、commit、stage、working tree、untracked file、deleted file、`.gitignore` pattern を使って、cmoc が扱う `<repo-root>` と `oracles` 配下ファイルの判定を確認します。
- oracle ファイル列挙では `INDEX.md` 除外、root `.gitignore` のみの参照、tracked かどうかに依存しない gitignore 除外、slash 付き pattern、`**` pattern、root 起点 basename pattern の扱いをテストします。
- 変更 oracle 抽出では、cmoc branch base commit から HEAD までの履歴変更と未コミット変更の和集合、履歴上の変更が HEAD で元に戻ったケース、未追跡ディレクトリ配下の新規 oracle、gitignore 対象除外をテストします。
- oracle 削除検出では、base から HEAD までの削除、削除後に再追加された履歴、working tree の削除、staging area の削除を全体評価切替条件として検出することを確認します。
- 補助関数として、テスト用 git repo を初期化する `_init_repo` と、指定 repo で git コマンドを実行する `_git` を定義しています。

## Read this when

- `commons.repo` の git リポジトリ探索、`.cmoc` ignore 設定、oracle ファイル列挙、変更 oracle 抽出、削除 oracle 検出を修正するとき。
- root `.gitignore` の pattern semantics、slash 付き pattern、`**`、root 起点 pattern、tracked かつ ignored な oracle ファイルの扱いに関するテストを確認したいとき。
- `cmoc eval-oracles` の部分評価対象や、oracle 削除時に全体評価へ切り替える条件に関する実装影響を確認したいとき。
- `cmoc apply` の事前条件として、未コミット差分が `oracles` 配下だけかを判定する処理のテストを確認したいとき。
- cmoc 作業ブランチ名の判定規則や、`.cmoc/branch` 配下の base commit 記録パス生成を確認したいとき。
- pytest で一時 git repo を作成して commit、stage、untracked、delete、gitignore の状態を再現するテストパターンを参照したいとき。

## Do not read this when

- cmoc の CLI サブコマンド全体の仕様やユーザー向けワークフローだけを調べたいとき。
- `commons.repo` 以外の実装、たとえば Codex CLI 呼び出し、Structured Output、ログ保存、プロンプト生成などのテストを探しているとき。
- oracle 正本仕様そのものの内容や、`oracles` 配下のルーティング情報を確認したいとき。
- README、AGENTS、memo、oracles の編集可否など、リポジトリ運用ルールだけを確認したいとき。
- gitignore pattern の詳細や oracle 差分判定ではなく、一般的な pytest の書き方だけを知りたいとき。

## hash

- 5e798d3d90ef8491c792ae09b5542bb39e52038e70c2cf7c45dba7bf57b745fb

# `test_subcommands.py`

## Summary

- `tests/test_subcommands.py` は、cmoc の主要サブコマンド本体と関連ヘルパーの決定論的な制御ロジックを検証する pytest テストファイルです。
- `cmoc init` について、`.cmoc` ignore ルールの追加、tracked `.cmoc` ファイルの追跡解除、既存 `.gitignore` 差分を初期化 commit に混ぜないことを検証します。
- `cmoc branch` について、`cmoc_` で始まる作業ブランチ作成、base commit 記録、stdout の試行表示を検証します。
- `cmoc eval-oracles --full` について、INDEX メンテナンスと Codex 実行を fake 化し、評価レポート保存、モード記録、サブコマンド本体ファイル配置、評価 prompt の実装参照禁止文言を検証します。
- `cmoc apply` について、cmoc ブランチ制約、不整合なし時の収束レポート、repeat 回数によるループ上限、oracle 外差分の拒否、`.cmoc` ignore 保証 commit と oracle commit の順序、INDEX メンテナンス後の禁止領域差分検出を検証します。
- `cmoc apply` の不整合調査 JSON について、Structured Output schema の使用、必須項目不足、近似キーの拒否など、payload 検証の失敗条件を扱います。
- `cmoc merge` について、明示 cmoc ブランチの merge と削除、自動解決失敗時の案内抑制、conflict 解消 prompt での `oracles` 編集禁止、固定された conflict 対象ファイルの marker 検査を検証します。
- Typer 側の `main` 関数群について、共通 runner を使わず各 impl へ直接委譲することと、`python -m main --help` が `cmoc` コマンド名の Usage を表示することを検証します。
- テスト内ヘルパーとして、一時 git repository を初期化する `_init_repo` と、指定 repo で git コマンドを実行する `_git` を定義しています。

## Read this when

- サブコマンド実装の変更後に、既存テストがどの挙動を固定しているか確認したいとき。
- `cmoc init` の `.gitignore` 更新、`.cmoc` 追跡解除、commit 対象の切り分けに関するテストを探しているとき。
- `cmoc branch` のブランチ命名、base commit 記録、進捗表示の期待値を確認したいとき。
- `cmoc eval-oracles` のレポート保存、Codex 実行の fake 化、評価 prompt、サブコマンドファイル配置に関するテストを確認したいとき。
- `cmoc apply` のブランチ制約、dirty tree 判定、oracle 差分 commit、`.cmoc` ignore 保証、repeat ループ、レポート生成の期待挙動を調べたいとき。
- 不整合調査 JSON の schema や `_validate_discrepancy_payload` の拒否条件をテストから把握したいとき。
- `cmoc merge` の merge 成功時のブランチ削除、失敗時メッセージ、conflict prompt、conflict marker 検査に関するテストを探しているとき。
- Typer エントリーポイントが impl に直接委譲する構造や、CLI help のコマンド名表示を確認したいとき。
- 一時 git repo を使うサブコマンドテストの書き方や、既存の `_init_repo`・`_git` ヘルパーの利用方法を知りたいとき。

## Do not read this when

- サブコマンドの正本仕様を確認したいだけのとき。このファイルではなく `oracles` 配下の該当仕様を読むべきです。
- cmoc の実装コードそのものを修正したいときの入口を探しているだけなら、`src/sub_commands` や `src/main.py` を先に読むべきです。
- INDEX.md の生成仕様、Structured Output 形式、目次メンテナンス仕様だけを確認したいとき。
- pytest 全体の設定、依存関係、実行環境、テスト規約を調べたいだけのとき。
- Codex CLI の呼び出し方法、ログ保存、サンドボックス指定などの共通実行時仕様を調べたいとき。
- README、AGENTS、oracles、memo などのリポジトリ運用ルールや編集禁止ルールだけを確認したいとき。
- サブコマンドのユーザー向け利用手順や全体ワークフローを把握したいだけのとき。

## hash

- e4f3165f6e174c01f0d33276a2ecc0019b3030ee619f265b3688b2967336ec83

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
