# `commons`

## Summary

- `src/commons` は、cmoc 全体で共有する基盤処理をまとめるディレクトリです。
- `codex.py` は `codex exec` の共通ラッパー、`command_runner.py` はサブコマンドの共通実行制御、`errors.py` は共通例外とエラーレポートを扱います。
- `repo.py` は `<repo-root>` 探索と git 操作、`indexing.py` は `<repo-root>` 配下の `INDEX.md` 保守、`subcommand_log.py` は tee ログを担当します。
- `timestamps.py` は `<time-stamp>` 生成、`timing.py` はステップ別経過時間表示を担当します。
- `__init__.py` は `src.commons` パッケージの入口だけを定義します。

## Read this when

- 共通処理のうち、どのモジュールを読むべきか切り分けたいとき。
- `codex exec` の共通引数、Structured Output、JSON 検証、リトライ、ログ保存を確認したいとき。
- 共通エラーハンドリング、`<repo-root>` 探索、git 操作、`INDEX.md` 保守、サブコマンドログ、タイムスタンプ、経過時間表示を確認したいとき。
- CLI サブコマンドの共通実行制御や終了コードの扱いを確認したいとき。
- `src/commons` 全体の役割をパッケージ境界として把握したいとき。

## Do not read this when

- 個別サブコマンドの業務ロジックや CLI 引数定義だけを追いたいとき。
- `src/commons` の中でも特定モジュールの実装詳細だけを見たいときで、ディレクトリ全体の案内が不要なとき。
- `src` 全体の設計規約やテスト規約、`oracles` の正本仕様だけを調べたいとき。
- `README.md`、`AGENTS.md`、`memo` などの運用ルールだけを確認したいとき。

## hash

- d0d623ae83f44c8819e7ec6392c664646773f99c6ba8678c7df980475496e706

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

- `cmoc` の各サブコマンド本体実装をまとめた `src/sub_commands` ディレクトリの目次です。
- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` の個別実装ファイルへの入口を案内します。
- この配下では、各サブコマンドの処理本体と、そのパッケージ境界を素早く把握することを目的にしています。

## Read this when

- どのサブコマンド実装ファイルを読むべきか判断したいとき。
- `src/sub_commands` 配下の全体像や、個別サブコマンドへのルーティングを確認したいとき。
- 各サブコマンドの責務分担や、実装ファイルの所在を一覧で把握したいとき。

## Do not read this when

- `commons` 側の共通ユーティリティや基盤実装だけを調べたいとき。
- `oracles` 配下の正本仕様そのものを確認したいとき。
- 開発ルール、コーディング規約、テスト規約などの開発者向け指針だけを調べたいとき。
- CLI エントリーポイントでのサブコマンド登録方法だけを確認したいとき。

## hash

- bb7268ab4ee180b6f51135e7d6848844b8253b7cfd3b4b49a477670b5642d265
