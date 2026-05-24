# `commons`

## Summary

- `src/commons` 配下の共通基盤モジュールをまとめるルーティング用ディレクトリの目次です。
- `codex exec` 呼び出し、共通エラー処理、`INDEX.md` 自動メンテナンス、`<repo-root>` 探索と git 操作、サブコマンド共通ログ、タイムスタンプ、経過時間表示の入口を案内します。
- `__init__.py` を含む各共通モジュールへの入口を集約し、サブコマンド実装から再利用する横断機能の所在を整理します。

## Read this when

- `src/commons` のどのモジュールを読むべきか判断したいとき。
- `codex exec` の共通ラッパー、Structured Output、ログ保存、再試行、quota 待機の仕様を確認したいとき。
- 共通エラー整形、終了コード、`typer.Exit` の扱いを確認したいとき。
- `<repo-root>` の探索、`.cmoc` の追跡除外、変更差分の収集、ブランチ基準 commit の扱いを確認したいとき。
- `INDEX.md` の自動生成・再利用・更新ルールや、目次対象の判定を確認したいとき。
- サブコマンドの標準出力とファイルログの tee、ログ保存先、経過時間表示、タイムスタンプ形式を確認したいとき。

## Do not read this when

- 個別サブコマンドの引数、入出力、操作手順だけを確認したいとき。
- `oracles` 配下の正本仕様やサブコマンド固有仕様だけを確認したいとき。
- `tests` 配下のテスト構成や個別テストケースの内容だけを確認したいとき。
- `README.md`、`AGENTS.md`、`memo` の編集可否や運用ルールだけを確認したいとき。
- このディレクトリ全体ではなく、特定の `src/commons` モジュールの実装詳細だけを既に把握しているとき。

## hash

- 3173b6633e2dcd59f4f7eaf64c01f43fa98bef9dcccccb231ec2b6ba7cbdeb00

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
