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

- `commons.codex.run_codex_exec` の Codex CLI 呼び出しラッパーを検証する pytest ファイル。
- Structured Output の JSON parse 失敗、JSON Schema 不一致、JSON/text の意味的 validation failure を 3 回までリトライし、失敗時に `CmocError` の詳細へ最終エラー、ログ、stdout などを含める挙動をテストする。
- `--output-schema`、`--output-last-message`、`--json`、`--model`、`model_reasoning_effort="medium"` など、`codex exec` に渡す引数と schema ファイル化を確認する。
- stdout 進捗表示では prompt/output を元文字列の先頭 80 文字で切ってから改行を可視化することを検証する。
- Structured Output 呼び出しで `output_schema` 未指定を拒否すること、oracle で禁止された `high`/`xhigh` reasoning effort を起動前に拒否することを確認する。
- quota 枯渇時に疎通確認を行い、復旧後に `--resume` と元 prompt で再実行する挙動、および resume 後の想定外エラーを即時 `CmocError` にする挙動をテストする。
- 通常の Codex CLI 呼び出し直前に `commons.indexing.maintain_indexes` を実行すること、`skip_index_maintenance=True` で明示的にスキップできることを確認する。
- テスト内では一時ディレクトリに fake `codex` 実行ファイルを作り、`PATH`、`time.sleep`、INDEX メンテナンス関数を monkeypatch して外部 Codex CLI に依存しない形で検証する。

## Read this when

- `run_codex_exec` のリトライ回数、ログ出力、Structured Output 検証、semantic validator の扱いを変更・確認したいとき。
- Codex CLI へ渡す引数、`--output-schema` の schema ファイル、`--output-last-message` の扱い、reasoning effort の既定値や禁止値を確認したいとき。
- quota 枯渇検知、疎通確認、`--resume` による再実行、resume 失敗時のエラー処理を実装・修正するとき。
- `run_codex_exec` の stdout 進捗表示で prompt/output の切り詰めや改行エスケープ仕様を確認したいとき。
- Codex 呼び出し前の `INDEX.md` メンテナンス実行タイミング、または `skip_index_maintenance` の用途と期待動作を確認したいとき。
- fake Codex CLI を使った `run_codex_exec` のテスト追加方法や、`tmp_path`・`monkeypatch`・`capsys` を使う既存パターンを参照したいとき。

## Do not read this when

- `run_codex_exec` の実装そのものを読みたいとき。このファイルはテストであり、実装は `src` 配下の `commons.codex` 側を確認する。
- Codex CLI ラッパー以外のサブコマンド、設定ファイル、oracle 評価、merge/apply/init/branch の仕様やテストを探しているとき。
- 実際の Codex CLI の一般仕様や外部サービスとしての挙動を調べたいとき。このファイルは fake `codex` による cmoc 内部契約の検証に限られる。
- INDEX 生成ロジックそのものの詳細を調べたいとき。このファイルでは `run_codex_exec` 直前にメンテナンスが呼ばれるか、またはスキップできるかだけを扱う。
- リポジトリ全体のテスト方針、pytest 規約、開発環境ルールだけを確認したいとき。

## hash

- 0425b8ac4c0a4ace1f8c10e2cd9683c98da115990738bea08798e531392fe426

# `test_indexing.py`

## Summary

- `commons.indexing.maintain_indexes` による `INDEX.md` 自動メンテナンス処理を検証する pytest テストファイル。
- 直下エントリ生成、`.gitignore` 対象除外、空ディレクトリへの空 `INDEX.md` 作成、`build`・`tmp` の親目次掲載と配下 `INDEX.md` 非作成を確認する。
- NUL を含まない非 UTF-8 バイナリの目次除外、ルート直下ではない `memo` ディレクトリへの `INDEX.md` 配置、壊れた既存エントリの再生成を検証する。
- Structured Output schema 不一致時の Codex CLI リトライ、最新 `INDEX.md` では Codex CLI を呼ばないこと、自動コミット時に `INDEX.md` などメンテナンス差分だけをコミットすることを確認する。
- テスト用 git リポジトリ作成ヘルパー `_init_repo` と、テストリポジトリ内で git コマンドを実行する `_git` ヘルパーを含む。

## Read this when

- `maintain_indexes` の挙動を変更し、既存の `INDEX.md` 生成・更新テストが何を保証しているか確認したいとき。
- `INDEX.md` の目次対象、配置対象、除外対象、空ディレクトリ処理、`build`・`tmp`・`memo` の扱いに関するテストを探しているとき。
- Structured Output schema、Codex CLI の fake 化、schema 不一致時のリトライ、最新インデックス時の Codex CLI 呼び出し抑制を確認したいとき。
- `maintain_indexes(..., commit_changes=True)` がユーザー作業ファイルを巻き込まず、メンテナンス対象パスだけをコミットするテストを確認したいとき。
- 一時ディレクトリ上に git リポジトリを作って `maintain_indexes` を検証するテストパターンを参考にしたいとき。

## Do not read this when

- cmoc の CLI サブコマンド仕様やユーザー向けワークフローを調べたいだけのとき。
- `INDEX.md` メンテナンス処理の実装本体を読みたいとき。実装は `commons.indexing` 側を確認する。
- Codex CLI 呼び出し、Structured Output、ログ保存、リトライなどの正本仕様断片を調べたいとき。仕様は `oracles` 配下の該当ファイルを確認する。
- pytest 全体の設定、テスト環境、Fake Codex CLI の一般規約を調べたいだけのとき。
- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` など個別サブコマンドのテストを探しているとき。

## hash

- d26d557b64944b6635a24ba6ef7122c8cb0b1f9991b499da8ddabe870ffbb938

# `test_repo.py`

## Summary

- `tests/test_repo.py` は、`commons.repo` にある git リポジトリ共通処理の自動テストです。
- `find_repo_root`、`.cmoc` の ignore 保証、`.cmoc` 配下 tracked ファイルの index 除外、cmoc ブランチ名判定、branch base commit 記録パスを検証します。
- oracle ファイル列挙について、`INDEX.md` の除外、root `.gitignore` のみを使う除外判定、slash 付き pattern、`**` pattern、tracked かつ gitignore 対象の扱いを検証します。
- 実装ファイル列挙について、`oracles`、`.git`、`INDEX.md`、gitignore 対象を除外し、実装対象だけを返すことを検証します。
- cmoc ブランチの base commit からの変更検出について、committed 変更、未コミット変更、未追跡ディレクトリ内の新規 oracle、履歴上で戻された変更、rename 後 path、gitignore 対象除外を検証します。
- oracle 削除検出について、committed 削除、途中 commit での削除後再追加、working tree 削除、staged 削除を全体評価切替条件として扱うことを検証します。
- oracle 削除検出の除外条件として、rename、`INDEX.md` の削除、root `.gitignore` 対象ファイルの削除を削除扱いしないことを検証します。
- 実装ファイル変更・削除検出について、oracle や `INDEX.md` を除いた実装対象の変更抽出と、実装ファイル削除の検出を検証します。
- `assert_only_oracles_uncommitted` が `cmoc apply` の事前条件として oracles 外の未コミット差分を拒否することを検証します。
- テスト用 git リポジトリを作成する `_init_repo` と、指定リポジトリで git コマンドを実行する `_git` の補助関数を含みます。

## Read this when

- `commons.repo` の git リポジトリ探索、cmoc 用 `.gitignore` 更新、`.cmoc` 配下ファイルの追跡解除に関するテストを確認したいとき。
- oracle ファイル列挙や変更検出で、`INDEX.md`、root `.gitignore`、slash pattern、double-star pattern、tracked ignored file をどう扱うべきか確認したいとき。
- `changed_oracle_files`、`has_deleted_oracle_files`、`changed_implementation_files`、`has_deleted_implementation_files` の期待挙動をテストから把握したいとき。
- cmoc ブランチの base commit を基準に、committed 変更、未コミット変更、未追跡ファイル、rename、削除、再追加履歴をどう検出するか確認したいとき。
- `cmoc apply` 実行前に oracles 外の未コミット差分を拒否する条件を確認したいとき。
- cmoc ブランチ名の正規表現的な判定条件や、branch base commit 記録ファイルの配置を確認したいとき。
- git を使う pytest の fixture 的な補助関数や、一時リポジトリ作成パターンを参考にしたいとき。

## Do not read this when

- CLI サブコマンドのユーザー向け仕様や stdout 表示、Codex CLI 呼び出し、Structured Output、ログ保存などの実行時仕様を調べたいとき。
- `commons.repo` 以外の実装モジュール、サブコマンド本体、設定ファイル処理、エラーレポート処理のテストを探しているとき。
- oracle 正本仕様そのものの記述内容や、仕様ファイル間のルーティングを調べたいとき。
- `README.md`、`AGENTS.md`、`oracles`、`memo` の編集可否など、リポジトリ運用ルールだけを確認したいとき。
- cmoc を使って別リポジトリを開発する `<repo-root>` 側の作業手順を知りたいとき。
- gitignore pattern の一般仕様だけを調べており、cmoc の oracle・実装ファイル列挙における期待挙動が不要なとき。

## hash

- cfb776e4fd4975b4cf44e30dbf3f26ce83f82cd6aa53526305112fd45422cd03

# `test_subcommands.py`

## Summary

- `tests/test_subcommands.py` は、cmoc のサブコマンド実装と CLI エントリーポイント周辺の決定論的な制御ロジックを検証する pytest ファイルです。
- `cmoc init`、`branch`、`eval-oracles`、`apply`、`merge` の実装関数を直接呼び、git リポジトリ上の副作用、コミット内容、レポート保存、エラー条件、プロンプト文面を確認します。
- `main` モジュールと `bin/cmoc` ランチャーについて、Typer 関数の委譲構造、`cmoc --help` の Usage、サブコマンドエラー時の終了コード、仮想環境 Python 必須化と stdout エラーレポートも検証します。
- テスト用ヘルパーとして、一時 git リポジトリを作る `_init_repo`、固定名の cmoc ブランチへ切り替える `_checkout_cmoc_branch`、git コマンドを実行する `_git` を定義しています。

## Read this when

- cmoc の主要サブコマンド実装を変更し、既存テストがどの振る舞いを固定しているか確認したいとき。
- `.cmoc` の git 追跡対象外保証、初期化コミット、cmoc ブランチ作成、base commit 記録、oracle 評価レポート、apply 反復処理、merge 後のブランチ削除などをテスト上で追いたいとき。
- `sub_commands.apply` の不整合 JSON schema、レポート必須項目、repeat オプション、cmoc ブランチ外拒否、oracle 外差分拒否、INDEX メンテナンス後の禁止パス再検査に関する期待値を調べたいとき。
- `sub_commands.eval_oracles` や `sub_commands.merge` が生成する Codex 向けプロンプトで、参照禁止範囲、報告順序、oracles 編集禁止などの文言がどう守られているか確認したいとき。
- `main.py` や `bin/cmoc` を変更し、CLI 表示名、エラー出力先、終了コード、仮想環境 Python の扱いに関する回帰テストを確認したいとき。

## Do not read this when

- cmoc の正本仕様断片を調べたいとき。まず `<cmoc-root>/oracles/INDEX.md` から必要な仕様ファイルへ辿ってください。
- サブコマンドの実装詳細そのものを読みたいだけのとき。対象は `src/sub_commands` 配下や `src/main.py` です。
- ユーザー向けの使い方、インストール手順、全体ワークフローを確認したいとき。テストではなく README や該当する oracle を参照してください。
- pytest の共通設定、依存関係、テスト実行環境全般を調べたいとき。このファイルは個別のサブコマンド回帰テストが中心です。
- `memo` 配下の情報が必要な作業をしているとき。このリポジトリでは `<cmoc-root>/memo` は AI の閲覧・編集禁止対象です。

## hash

- 7356e10e1c4a4e3db155ddbc6715fad0ed7bb1e194eca10990cbb6b38818fe8d

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
