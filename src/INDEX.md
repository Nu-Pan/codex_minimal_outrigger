# `commons`

## Summary

- `src/commons` は、cmoc 全体で共通利用する実行制御、`codex exec` 呼び出し、git 操作、エラー表示、ログ、時間計測、時刻生成をまとめた基盤ディレクトリです。
- `codex.py` は `codex exec` の共通起動処理を担当し、Structured Output、JSON 検証、再試行、quota 待機、詳細ログ保存を扱います。
- `command_runner.py`、`errors.py`、`repo.py`、`subcommand_log.py`、`timing.py`、`timestamps.py` は、サブコマンド実行に必要な横断処理をそれぞれ分担します。
- `indexing.py` は `<repo-root>` 配下の `INDEX.md` を列挙・再生成・更新し、必要に応じて自動コミットするための共通モジュールです。
- `__init__.py` は `src.commons` パッケージの存在を示す最小構成のモジュールです。

## Read this when

- `src/commons` 配下のどの共通モジュールを読むべきか判断したいとき。
- `cmoc` のサブコマンド入口、`repo_root` 解決、共通エラー処理、終了コード処理を確認したいとき。
- `codex exec` の呼び出し方、Structured Output の schema、JSON 検証、再試行、quota 待機の挙動を確認したいとき。
- `git` の root 探索、`HEAD` やブランチ取得、`.cmoc` の追跡除外、部分 commit、変更ファイル列挙の仕組みを確認したいとき。
- 標準出力とログファイルの tee、経過時間表示、タイムスタンプ生成、`INDEX.md` 自動生成の流れを確認したいとき。

## Do not read this when

- 個別サブコマンドの業務ロジックや引数定義だけを調べたいとき。
- `oracles` 配下の正本仕様や、ユーザー向け CLI 仕様そのものを探したいとき。
- `README.md`、`AGENTS.md`、`memo` の運用ルールや編集可否だけを確認したいとき。
- `src/commons` 以外の実装やテストの配置を知りたいとき。
- `INDEX.md` の生成・更新ルールではなく、特定機能の実装詳細だけを追いたいとき。

## hash

- de3c670fcc7dbbbed5ab0f79608637c6e3b3ba203376d458f391f12af7779e92

# `main.py`

## Summary

- `cmoc` CLI の Typer エントリーポイントとサブコマンド登録をまとめる目次です。
- `init`、`branch`、`eval-oracles`、`apply`、`merge` の各コマンド定義と、対応する `src/sub_commands` 実装への委譲関係を案内します。
- Typer / Click の parse error、`NoArgsIsHelpError`、想定外例外を共通エラーレポートへ変換して終了コードを決める処理への入口です。
- `python src/main.py` で直接起動される経路も含めて、CLI 起動全体の入口を整理します。

## Read this when

- `cmoc` のトップレベルコマンド一覧や、各サブコマンドの登録箇所を確認したいとき。
- 各コマンドがどの `src/sub_commands` の実装関数へ渡されるかを調べたいとき。
- `apply` の `--repeat`、`--repeat-inveatigate-and-fix`、`--full` などの引数定義や既定値を確認したいとき。
- `eval-oracles` の `--full` や `eval-oracle` の互換 alias を含む CLI 挙動を確認したいとき。
- Typer / Click の parse error や想定外例外が、どのようにエラーレポートと終了コードへ変換されるか確認したいとき。
- `app` オブジェクトや `main()` の起動条件、`python src/main.py` での直接実行時挙動を調べたいとき。

## Do not read this when

- 各サブコマンドの業務ロジックや `src/sub_commands` 配下の本体実装を追いたいとき。
- 共通エラーレポートの本文生成や `commons.errors` の内部を詳しく確認したいとき。
- `src/commons` の共通基盤仕様や `INDEX.md` 自動生成など、CLI 入口以外の横断仕様を調べたいとき。
- `cmoc` の利用手順全体や、`oracles` 側の正本仕様そのものを知りたいとき。

## hash

- cb380259debbaae71cb88e4b9959201e67bf14dedef7073dec0c842bc4ad9a8b

# `sub_commands`

## Summary

- `src/sub_commands` は、cmoc の各サブコマンド本体を置く実装パッケージです。
- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` の実装入口と、その周辺の補助関数をまとめています。
- 各サブコマンドごとの処理フロー、引数の扱い、出力、共通処理との境界を案内する目次です。

## Read this when

- `src/sub_commands` がどの責務を担うか確認したいとき。
- 各サブコマンドの実装ファイルや補助関数の位置を知りたいとき。
- サブコマンドごとの処理順、前提条件、出力、エラー処理の概略を把握したいとき。
- 共通処理が `commons` 側なのか、サブコマンド側なのか切り分けたいとき。

## Do not read this when

- cmoc 全体の開発ルール、コーディング規約、テスト規約だけを調べたいとき。
- CLI のエントリーポイントやサブコマンド登録方法だけを確認したいとき。
- `src/commons` の共通基盤だけを調べたいとき。
- `oracles` 側の正本仕様そのものや、個別仕様断片だけを確認したいとき。
- `src/sub_commands` の実装ではなく、ユーザー向けの実行時仕様だけを知りたいとき。

## hash

- 70d4cfa828993a1a5d7fd7baa3c5a205e8c520efd297d583822b9f1bfeeccef8
