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

- `tests/test_repo.py` は、`commons.repo` が提供する git リポジトリ共通処理の pytest テストです。
- `find_repo_root` による親ディレクトリ探索、`ensure_cmoc_ignored` による `.cmoc` ignore 追記の冪等性と tracked `.cmoc` ファイルの index 除外を検証します。
- `list_oracle_files` が `oracles/INDEX.md` と root `.gitignore` 対象を除外し、tracked だが ignore pattern に一致する oracle、slash 付き pattern、`**` pattern、oracles 配下 `.gitignore` の非参照、root 起点 basename pattern を正しく扱うことを検証します。
- `changed_oracle_files` が cmoc ブランチ base commit からの履歴上の oracle 変更と未コミット変更を列挙し、revert 済み履歴変更、未追跡ディレクトリ内の新規 oracle、gitignore 対象除外、slash pattern の階層 semantics を扱うことを検証します。
- `has_deleted_oracle_files` が base..HEAD、削除後再追加の履歴、working tree、staging area の oracle 削除を検出し、`INDEX.md` 削除と root `.gitignore` 対象ファイル削除を無視することを検証します。
- `assert_only_oracles_uncommitted` が `cmoc apply` 前提として oracles 外の未コミット変更を拒否することを検証します。
- `is_cmoc_branch` の cmoc ブランチ命名規則判定と、`branch_base_commit_path` の `.cmoc/branch` 配下パス生成を検証します。
- テスト補助として、一時 git repo を初期化して初期 commit を作る `_init_repo` と、指定 repo で git コマンドを実行する `_git` を定義しています。

## Read this when

- `commons.repo` の git リポジトリ共通処理に関するテストの全体像を把握したいとき。
- repo root 探索、`.cmoc` の gitignore 保証、tracked `.cmoc` ファイルの untrack 処理を変更・確認するとき。
- oracle ファイル列挙における `oracles/INDEX.md` 除外、root `.gitignore` の pattern 解釈、tracked ignored file、slash pattern、`**` semantics、oracles 配下 `.gitignore` 非参照の期待値を確認したいとき。
- oracle 差分抽出で base commit からの履歴変更、未コミット変更、未追跡ファイル、revert 済み変更、gitignore 対象除外を扱う仕様を確認したいとき。
- oracle 削除検出による部分評価から全体評価への切替条件を確認したいとき。
- `cmoc apply` の事前条件として oracles 外差分を拒否する挙動を確認したいとき。
- cmoc ブランチ名の正規表現相当の判定や、branch base commit 記録ファイルの保存先を確認したいとき。

## Do not read this when

- CLI サブコマンドのユーザー向け出力、プロンプト構成、Codex CLI 呼び出し、ログ保存などの実行時仕様だけを調べたいとき。
- `commons.repo` の実装そのものを読みたいとき。
- oracle 正本仕様断片の内容やルーティング文書の記述方針だけを調べたいとき。
- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` の個別仕様を直接確認したいとき。
- gitignore pattern の一般仕様だけを調べており、cmoc の oracle 列挙・差分抽出テストの期待値が不要なとき。
- ファイル編集可否、リポジトリ運用ルール、AGENTS.md の制約だけを確認したいとき。

## hash

- e72ecce669d5465f7ed7dd914612dddbc5c96b17ae27727444496f3251f2a9db

# `test_subcommands.py`

## Summary

- `tests/test_subcommands.py` は、cmoc の主要サブコマンド実装と周辺ヘルパーの決定論的な制御ロジックを検証する pytest ファイルです。
- `cmoc init` について、`.cmoc` ignore ルールの追加、既存 tracked `.cmoc` ファイルの追跡解除、既存 `.gitignore` 差分を初期化 commit に混ぜないことを確認します。
- `cmoc branch` について、`cmoc_` で始まる作業ブランチ作成、base commit 記録、作成試行の進捗表示を検証します。
- `cmoc eval-oracles` について、Fake Codex CLI を使った評価レポート保存、PEP 8 名の実装ファイル配置、評価 prompt が実装・テスト参照を禁じることを検証します。
- `cmoc apply` について、不整合なし時の完了レポート、`repeat` によるループ上限、未収束時の終了コード、必須項目不足レポートの拒否、非 cmoc ブランチ拒否、oracle 外差分拒否、`.cmoc` ignore 保証と oracle commit の順序を検証します。
- apply 関連ヘルパーについて、INDEX メンテナンス後に禁止領域差分が出た場合の commit 中止、不整合 JSON schema の必須項目不足や近似キーの拒否を検証します。
- `cmoc merge` について、明示 cmoc ブランチの merge と削除、自動解決失敗時の案内文、conflict 解消 prompt の oracle 編集禁止、conflict marker 検査対象の固定化を検証します。
- CLI 表層について、Typer 関数が対応する impl だけへ委譲すること、`cmoc --help` の Usage 表示、`bin/cmoc` ランチャーが venv Python を必須にすることを検証します。
- 末尾に、テスト用 git リポジトリを作る `_init_repo` と、指定 repo 内で git コマンドを実行する `_git` の補助関数があります。

## Read this when

- cmoc の主要サブコマンドに対する回帰テストの全体像を把握したいとき。
- `cmoc init` の `.gitignore` 更新、`.cmoc` 追跡解除、初期化 commit の扱いを確認したいとき。
- `cmoc branch` のブランチ命名、base commit 記録、stdout 進捗表示に関するテストを探しているとき。
- `cmoc eval-oracles` のレポート保存、実装ファイル名、評価 prompt 制約を変更・確認したいとき。
- `cmoc apply` の収束・未収束判定、repeat 上限、Codex JSON schema、レポート必須項目、commit 順序、禁止差分検出を確認したいとき。
- `cmoc merge` の merge 成功時処理、branch 削除、conflict 自動解決失敗時の表示、conflict prompt、marker 検査を変更・確認したいとき。
- Typer エントリーポイント、`python -m main --help` のコマンド名表示、`bin/cmoc` ランチャーの Python 選択仕様に関するテストを探しているとき。
- tmp_path 上に git リポジトリを作るテスト補助関数や、テスト内 git 実行ヘルパーの使い方を確認したいとき。

## Do not read this when

- cmoc の実装仕様そのものを正本として確認したいとき。正本仕様は `oracles` 配下の該当仕様を読むべきです。
- サブコマンド実装コードの詳細を読みたいとき。`src/sub_commands` 配下の対象モジュールを読むべきです。
- pytest 全体の共通設定、fixture、Fake Codex CLI の仕組みだけを調べたいとき。
- INDEX 生成やルーティング文書の実装詳細だけを調べたいとき。
- README、AGENTS、oracles、memo などのリポジトリ運用ルールや編集可否だけを確認したいとき。
- 外部利用者向けの cmoc 操作手順や導入説明だけを知りたいとき。

## hash

- af9622b044ac9b00ba66c87a60501b63adcc9f3aeed02d0dd4ee9e8fadb866f8

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
