# `conftest.py`

## Summary

- pytest 実行時に `<cmoc-root>/src` を Python の import path 先頭へ追加するテスト共通設定ファイルです。
- `tests` 配下のテストから cmoc 本体の `src` 配下モジュールを直接 import できるようにします。
- `Path(__file__).resolve().parents[1] / "src"` で `<cmoc-root>/src` を解決し、`sys.path.insert(0, ...)` で優先的に参照されるよう設定します。

## Read this when

- pytest で `src` 配下の cmoc 実装モジュールを import できる理由を確認したいとき。
- テスト実行時の Python import path 設定や `sys.path` の変更箇所を探しているとき。
- `tests` 配下の共通 pytest 設定が何をしているか把握したいとき。

## Do not read this when

- 個別テストケースの内容や期待値を調べたいとき。
- cmoc の CLI 挙動、サブコマンド仕様、ユーザー向け出力仕様を確認したいとき。
- pytest fixture、mock、Fake Codex CLI などの具体的なテスト補助機能を探しているとき。
- 本番コードの実装ロジックやアプリケーション設定の詳細を調べたいとき。

## hash

- 70811f2ee49ed59eeb60c3c17354146e78b9c21d8ab9bfbcb46007f9d6c8eb57

# `test_codex.py`

## Summary

- `commons.codex.run_codex_exec` の Codex CLI 呼び出しラッパーに対する pytest テストを定義するファイル。
- Structured Output の JSON parse 失敗、JSON Schema 検証失敗、JSON/text の意味的バリデーション失敗に対する 3 回リトライと `CmocError` 詳細出力を検証する。
- `--output-schema`、`--output-last-message`、`--json`、`--model`、`model_reasoning_effort="medium"` など、`codex exec` に渡す引数と schema ファイル化を検証する。
- stdout 進捗表示で prompt/output の先頭 80 文字を改行可視化前に切り出す挙動を検証する。
- Structured Output 利用時の `output_schema` 必須チェックと、oracle が禁止する `high` reasoning effort の起動前拒否を検証する。
- quota 枯渇時に疎通確認を行い、復旧後に `--resume` と session id 付きで同じ prompt を再実行する挙動、および resume 後の想定外エラーを検証する。
- 通常の Codex CLI 呼び出し直前に `commons.indexing.maintain_indexes` を実行することと、`skip_index_maintenance=True` で明示的にスキップできることを検証する。
- テスト内では一時ディレクトリに fake `codex` 実行ファイルを生成し、`PATH` 差し替え、`monkeypatch`、`capsys`、一時 repo、`.cmoc/logs/codex_exec` のログ確認を用いる。

## Read this when

- `run_codex_exec` のリトライ、Structured Output、schema 検証、意味的バリデーション、ログ保存の期待挙動を確認したいとき。
- Codex CLI へ渡す引数、`--output-schema` のファイル化、`--output-last-message` の扱い、reasoning effort 指定のテストを探しているとき。
- quota 枯渇時の待機、疎通確認、session id を使った `--resume` 再実行のテストを確認したいとき。
- `run_codex_exec` の stdout 進捗表示で prompt/output の短縮や改行エスケープがどう検証されているか知りたいとき。
- Codex CLI 呼び出し前の INDEX メンテナンス実行や `skip_index_maintenance` のテストを確認したいとき。
- fake `codex` コマンドを使ったテストパターン、`monkeypatch.setenv("PATH", ...)`、`.cmoc` ログ検証の実例を参照したいとき。

## Do not read this when

- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` など個別サブコマンドの CLI 挙動テストを探しているとき。
- INDEX 生成ロジックそのもの、oracle ファイル列挙、実装ファイル列挙、ハッシュ計算などの詳細テストを探しているとき。
- `commons.codex.run_codex_exec` の実装そのものを読みたいとき。
- cmoc のユーザー向け仕様や README レベルの利用手順だけを確認したいとき。
- Codex CLI を使わない純粋な git 操作、設定ファイル、エラー表示、パス探索などのテストを探しているとき。

## hash

- 6a1780f9ffd39d593358cb4cab15e946a06aadfd5b8eacaadd81648e2de8ed93

# `test_indexing.py`

## Summary

- `commons.indexing.maintain_indexes` による `INDEX.md` メンテナンス処理の pytest テストです。
- gitignore 対象の除外、空ディレクトリへの空 INDEX 作成、`build`/`tmp` の親目次掲載と配置除外、非 UTF-8 バイナリ除外、repo 直下以外の `memo` ディレクトリ処理を検証します。
- 既存 `INDEX.md` の必須セクション欠落時の再生成、Structured Output 不正時のリトライ、最新 INDEX では Codex CLI を呼ばないこと、自動コミット対象がメンテナンス差分に限られることを検証します。
- テスト用 git リポジトリ作成と git コマンド実行の補助関数を含みます。

## Read this when

- `maintain_indexes` の対象ファイル・対象ディレクトリ判定、除外規則、ハッシュによる再生成判定を確認したいとき。
- INDEX 生成で Codex CLI に渡す Structured Output schema、model、reasoning effort の期待値を確認したいとき。
- `build`、`tmp`、`memo`、`.gitignore`、非 UTF-8 バイナリ、空ディレクトリが INDEX メンテナンスでどう扱われるかを調べたいとき。
- INDEX が最新または壊れている場合の Codex CLI 呼び出し有無、再生成、リトライ挙動を検証したいとき。
- INDEX メンテナンス後の自動コミットがユーザー作業ファイルを巻き込まないことを確認したいとき。

## Do not read this when

- cmoc の INDEX 目次仕様そのものを正本仕様として確認したいとき。
- `maintain_indexes` の実装詳細を直接修正したいだけで、テスト期待値を確認する必要がないとき。
- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` など個別サブコマンドの挙動を調べたいとき。
- Codex CLI 実行共通処理や Structured Output リトライ処理の実装本体だけを読みたいとき。
- git リポジトリ操作一般、pytest 一般、またはテスト用 fixture の書き方だけを調べたいとき。

## hash

- 504580437f00209e97e48af790b47093fc22db05cdff8397315718693a437792

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

- `tests/test_subcommands.py` は、cmoc の主要サブコマンドと CLI ランチャーまわりの決定論的な制御ロジックを検証する pytest テストファイルです。
- `cmoc init` について、`.cmoc` の ignore 追加、tracked `.cmoc` ファイルの追跡解除、初期化 commit、既存 `.gitignore` 差分や事前 staged 差分を commit に混ぜないこと、unborn HEAD での初回 commit 作成を検証します。
- `cmoc branch` について、`cmoc_` で始まる作業ブランチ作成、base commit 記録ファイル作成、作成試行メッセージ表示を検証します。
- `cmoc eval-oracles` について、Fake Codex CLI を使った評価レポート保存、PEP 8 準拠の `eval_oracles.py` 配置、評価 prompt が実装参照を禁じること、prompt の順序を検証します。
- `cmoc apply` について、不整合なしの場合の完了レポート保存、`repeat` によるループ上限、未収束時の exit code、必須項目不足レポートの拒否、非 cmoc ブランチ拒否、oracle 外差分の拒否、`.cmoc` ignore 保証 commit と oracle commit の分離を検証します。
- apply の内部処理について、INDEX メンテナンス後に禁止領域差分が出た場合の commit 停止、不整合 JSON schema の必須項目不足や近似キーの拒否を検証します。
- `cmoc merge` について、明示 cmoc ブランチの merge と削除、自動解決失敗時の手動 merge state 案内抑止、conflict 解消 prompt で `oracles` 編集を常に禁じること、conflict marker 検査が git 管理対象全体を見ることを検証します。
- Typer エントリーポイントとランチャーについて、main の command 関数が各 impl へ直接委譲すること、`cmoc --help` の Usage 表示、サブコマンドエラーの非 0 終了、`bin/cmoc` が仮想環境 Python を必須にし、仮想環境欠如時に共通エラーレポートを stdout に出すことを検証します。
- 末尾には、テスト用 git repo を作る `_init_repo`、cmoc ブランチへ移動して base commit 記録を作る `_checkout_cmoc_branch`、git コマンドを実行する `_git` の補助関数があります。

## Read this when

- cmoc のサブコマンド実装を変更し、既存の決定論的制御ロジックに対するテスト範囲を把握したいとき。
- `cmoc init` の `.cmoc` ignore 保証、tracked `.cmoc` 追跡解除、初期化 commit、既存 staged 差分や `.gitignore` 差分の扱いをテストで確認したいとき。
- `cmoc branch` のブランチ名、base commit 記録、stdout 進捗表示の期待値を確認したいとき。
- `cmoc eval-oracles` の Codex 呼び出し fake、評価レポート保存、評価 prompt の禁止事項や構成順序、`eval_oracles.py` の配置規約を確認したいとき。
- `cmoc apply` の不整合調査 JSON、Structured Output schema、repeat 上限、収束・未収束レポート、exit code、レポート必須項目検証を調べたいとき。
- `cmoc apply` が非 cmoc ブランチ、oracle 外差分、INDEX メンテナンス後の禁止領域差分をどう拒否するか確認したいとき。
- `.cmoc` ignore 保証 commit と oracle commit を分離する apply の git index 操作や、事前 staged oracle 差分の扱いを調べたいとき。
- `cmoc merge` の merge 成功時ブランチ削除、conflict 自動解決失敗時の表示、conflict 解消 prompt、conflict marker 検査範囲を確認したいとき。
- Typer の `main.py` command 関数、`cmoc --help` の Usage、サブコマンドエラー時のプロセス終了コード、`bin/cmoc` の仮想環境 Python 必須チェックを変更するとき。
- このファイル内のテスト用 git repo 補助関数を再利用または変更したいとき。

## Do not read this when

- cmoc の正本仕様断片を確認したいだけで、テスト実装の期待値や fake の作り方を調べる必要がないとき。
- 特定サブコマンドのユーザー向け仕様だけを読みたいとき。このファイルではなく `oracles` 配下の該当仕様を入口にするべきです。
- INDEX 自動生成やルーティング文書の仕様そのものを確認したいとき。
- `commons` や `sub_commands` の本体実装の詳細な制御フローを読みたいとき。テストではなく `src` 配下の実装ファイルを読むべきです。
- pytest の一般的な使い方、git の一般的な使い方、Typer の一般的な使い方だけを調べたいとき。
- ネットワーク、外部 Codex CLI の実動作、実際の LLM 出力品質を確認したいとき。このファイルの多くは fake や monkeypatch による決定論的テストです。
- README、AGENTS.md、oracles、memo などのリポジトリ運用ルールや編集可否だけを確認したいとき。

## hash

- d3250a56b3a8b4cbe60a3301599c82aee50bfccd933344f9774ec25540b888ad

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
