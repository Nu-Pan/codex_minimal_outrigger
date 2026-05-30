# `commons`

## Summary

- cmoc 全体で使う共通基盤モジュール群の集約先です。`codex.py`、`command_runner.py`、`repo.py`、`errors.py`、`subcommand_log.py`、`timing.py`、`timestamps.py`、`report_files.py`、`indexing.py` などが入っています。
- `codex exec` の起動、サブコマンド実行制御、リポジトリ探索、共通エラー整形、ログ記録、時間計測、レポート保存、`INDEX.md` メンテナンスを支えます。
- `__init__.py` はパッケージ宣言のみで、公開 API の本体は各モジュールに分かれています。

## Read this when

- cmoc 全体で使う共通処理の役割分担を確認したいとき。
- `codex exec` 呼び出し、サブコマンドの共通実行制御、Git リポジトリ操作、エラー整形、ログ、計時、レポート保存、`INDEX.md` メンテナンスの実装に入る前に入口を確認したいとき。
- `src.commons` が Python パッケージであることや、どのモジュールに何があるかを素早く把握したいとき。

## Do not read this when

- 個別サブコマンドの業務ロジックや `src/sub_commands` 側の振る舞いだけを確認したいとき。
- `oracles` の正本仕様や `INDEX.md` 生成ルールの詳細だけを確認したいとき。
- 共通処理のうち特定モジュールだけを追いたいときは、`codex.py`、`repo.py`、`errors.py` など該当ファイルへ直接進めば足ります。

## hash

- 826c3c469e7aeb8c5ebce53bc70a4464923068ec14f92014e6b964a2b15fbe9c
<!-- cmoc-index-kind: directory -->

# `main.py`

## Summary

- cmoc CLI のエントリーポイントで、Typer のルート `app` と `session` / `apply` / `review` の各サブアプリを組み立てるファイルです。
- `init`、`session`、`apply`、`review` の各コマンド登録に加えて、`eval-oracle` / `eval-oracles` の隠し別名や、`apply fork` の繰り返し回数・`scope`、`apply join` の `--force-resolve` などの既定値をまとめています。
- サブコマンド未指定時の `CmocError` 生成、補完プローブ時の分岐、Click/Typer 例外の共通整形、`python src/main.py` 直実行の起動経路を扱います。

## Read this when

- cmoc CLI の起動点と、`session` / `apply` / `review` のサブアプリ構成を確認したいとき。
- `init`、`session fork/join/abandon`、`apply fork/join/abandon`、`review oracles` の登録名、隠し別名、既定オプションを確認したいとき。
- サブコマンド未指定時の利用者向けエラー、補完プローブ時の分岐、Click/Typer 例外の共通整形を追いたいとき。
- `python src/main.py` で直接起動する経路と、そのときの例外処理を確認したいとき。

## Do not read this when

- `src/sub_commands/` 配下の各サブコマンド本体の実装だけを追いたいとき。
- `commons.errors` のエラー型や `format_error_report()` の整形ロジックだけを確認したいとき。
- `INDEX.md` の生成ルールや `oracles` 側のルーティング方針だけを確認したいとき。

## hash

- d03b4e0b3d0c12971884d8bc1e159f95c3f0efe50e8fca99dc96066066992456

# `sub_commands`

## Summary

- `src/sub_commands` は `cmoc` のサブコマンド実装をまとめるディレクトリの入口です。
- `__init__.py` はパッケージ宣言だけを担い、`init.py` と `eval_oracles.py` は個別サブコマンド本体を実装します。
- `apply/` と `session/` はそれぞれ独立したサブパッケージで、配下の詳細は各自の `INDEX.md` へ分岐します。

## Read this when

- `src/sub_commands` 配下の各サブコマンド実装の入口をまとめて把握したいとき。
- `init`、`eval_oracles.py`、`apply/`、`session/` のどの実装ファイルへ進むべきか整理したいとき。
- 個別ファイルではなく、サブコマンド群全体の役割分担と配置を俯瞰したいとき。

## Do not read this when

- `cmoc init`、`cmoc review oracles`、`cmoc apply`、`cmoc session` の個別仕様や処理順を確認したいときは、この目次ではなく対象モジュールを直接読むべきです。
- `apply` や `session` 配下の状態遷移、例外条件、終了条件などの詳細だけを確認したいときは、下位の `INDEX.md` を読むべきです。
- `sub_commands` ではなく `commons/` の共通処理や、CLI 入口全体の構成だけを確認したいときは、この目次を経由する必要はありません。

## hash

- f2acaceccd18c432c6ed08754b07336e46ce6cdedeb1214c2fbecaf88f720ef8
<!-- cmoc-index-kind: directory -->
