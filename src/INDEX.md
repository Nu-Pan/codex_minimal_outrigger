# `commons`

## Summary

- `src/commons` の共通処理を集約するディレクトリの入口です。
- サブコマンド共通の実行制御、エラー整形、Codex CLI 呼び出し、Git リポジトリ操作、サブコマンドログ、タイムスタンプ、計測、`INDEX.md` メンテナンスを扱います。
- `__init__.py` はパッケージ宣言のみで、実装の中心は `codex.py`、`command_runner.py`、`errors.py`、`indexing.py`、`repo.py`、`subcommand_log.py`、`timestamps.py`、`timing.py` に分かれています。

## Read this when

- サブコマンド共通の実行制御、エラー整形、Codex CLI 呼び出し、リポジトリ操作、ログ、タイムスタンプ、計測の入口をまとめて把握したいとき。
- `codex.py`、`command_runner.py`、`errors.py`、`indexing.py`、`repo.py`、`subcommand_log.py`、`timestamps.py`、`timing.py` のどれを読むべきか整理したいとき。
- `INDEX.md` の生成・更新ルールや、共通ユーティリティ同士の役割分担を確認したいとき。
- `src/commons` 配下の共通処理を、どのファイルに何があるかという観点で把握したいとき。

## Do not read this when

- 個別サブコマンドの業務ロジックや CLI 引数定義だけを確認したいときは、このディレクトリではなく `src/sub_commands/` 側を読むべきです。
- `oracles` の正本仕様やユーザー向け手順だけを確認したいときは、このディレクトリではなく `oracles/` 側を読むべきです。
- `src/commons` のうち特定の 1 モジュールだけを深掘りしたいときは、該当する `*.py` を直接読むべきです。
- `README.md`、`AGENTS.md`、`memo` の扱いだけを確認したいときは、このディレクトリの案内を読む必要はありません。

## hash

- 3420e9cd69d52dd18c215cb13f9769b7ba221d81291e94db31c73f644ca92e6c

# `main.py`

## Summary

- `cmoc` CLI のエントリーポイントで、Typer アプリ本体と `session` / `apply` のサブアプリを組み立てています。
- `init`、`session`、`apply`、`eval-oracles` の各コマンドを定義し、実処理は `src/sub_commands/` 側の実装へ委譲しています。
- Typer / Click の例外処理をまとめて受け、`NoArgsIsHelpError` を含むエラーを `format_error_report()` で整形して終了コード付きで終了します。

## Read this when

- `cmoc` のエントリーポイント、Typer アプリの構成、サブコマンド登録を修正・レビューしたいとき。
- `init`、`session fork/join/abandon`、`apply fork/join/abandon`、`eval-oracles` とその引数定義を確認したいとき。
- サブコマンドなし起動時の `NoArgsIsHelpError` の扱い、`--help` 相当の挙動、終了コードの伝播を確認したいとき。
- Typer / Click の例外を `CmocError` と共通エラーレポートへ変換する起動経路を確認したいとき。
- `python src/main.py` で直接起動する経路の振る舞いを確認したいとき。

## Do not read this when

- 各サブコマンド本体の処理内容だけを確認したいときは、このファイルではなく `src/sub_commands/` 配下の実装を見るべきです。
- 共通エラー型やエラーレポートの整形だけを確認したいときは、このファイルではなく `src/commons/errors.py` を見るべきです。
- CLI の設計ルールや配置方針だけを確認したいときは、このファイルではなく `oracles/dev_rules/design_rules.md` を見るべきです。
- サブコマンドごとの仕様断片だけを確認したいときは、このファイルではなく `oracles/app_specs/sub_commands/` 配下の文書を見るべきです。

## hash

- fd4b3fe58ddc1bb32e637e83cc5ddca509458ade3b15a69c1c5d5bc677ba138b

# `sub_commands`

## Summary

- `src/sub_commands` は `cmoc` のサブコマンド実装群の入口です。
- `__init__.py` はパッケージ宣言のみを担い、`apply` と `session` はそれぞれ専用のサブディレクトリに分かれています。
- `eval_oracles.py` は `cmoc eval-oracles` の本体、`init.py` は `cmoc init` の本体です。
- この目次から、`apply/INDEX.md` と `session/INDEX.md` へ進んで、それぞれの詳細実装へたどれます。

## Read this when

- `src/sub_commands` 配下のサブコマンド実装全体を、どのファイルに何があるかという観点で把握したいとき。
- `apply`、`session`、`eval-oracles`、`init` の実装入口をまとめて整理したいとき。
- 各サブコマンドの個別モジュールへ進む前に、役割分担と配置方針を確認したいとき。
- `src/sub_commands` 以下の入口案内として、どの INDEX や実装ファイルへ進むべきかを判断したいとき。

## Do not read this when

- 個別の `cmoc apply` 実装だけを確認したいときは、この目次ではなく `apply/INDEX.md` を直接読むべきです。
- 個別の `cmoc session` 実装だけを確認したいときは、この目次ではなく `session/INDEX.md` を直接読むべきです。
- `cmoc eval-oracles` や `cmoc init` の処理内容だけを確認したいときは、この目次ではなく `eval_oracles.py` や `init.py` を直接読むべきです。
- `src/sub_commands` が Python パッケージとして宣言されているかだけを確認したいときは、`__init__.py` だけで足ります。

## hash

- 9a0d7d5af087c5fc768acb3eb8b4da92f8ed61023ed700b0b122876c877e170c
