# `commons`

## Summary

- `cmoc` の各サブコマンドから共通利用される基盤処理をまとめたディレクトリです。
- `codex exec` 呼び出し、共通エラー処理、Git リポジトリ操作、サブコマンドログ、経過時間計測、タイムスタンプ、レポート保存、`INDEX.md` 目次維持を扱います。
- サブコマンド実装の土台になる共通ユーティリティ群の入口です。

## Read this when

- `cmoc` 全体で共有する実行制御、Git 操作、ログ記録、経過時間計測の役割分担を把握したいとき。
- `codex exec` の起動基盤、共通エラー整形、タイムスタンプ生成、レポート保存、`INDEX.md` メンテナンスの共通処理を確認したいとき。
- サブコマンド本体を支える基盤モジュール群をまとめて見たいとき。

## Do not read this when

- 個別の共通処理だけを確認したいときは、この目次ではなく `codex.py`、`repo.py`、`errors.py` など該当ファイルを直接読むべきです。
- `src/sub_commands` 側の各コマンド実装や、`oracles` 配下の正本仕様だけを追いたいときは、このディレクトリではなく該当する入口を読むべきです。
- `INDEX.md` の自動生成・更新ルールだけを確認したいときは、この目次ではなく `indexing.py` を読むべきです。

## hash

- 9e06f8ebcc6d63b56a497898f8f73dbd2775317866eebca23eed7c44da085dec
<!-- cmoc-index-kind: directory -->

# `main.py`

## Summary

- cmoc CLI のエントリーポイントで、Typer のルート `app` と `session` / `apply` / `review` の各サブアプリを組み立てるファイルです。
- `init`、`session`、`apply`、`review` の各コマンド登録に加えて、`eval-oracle` / `eval-oracles` の隠し別名や、`apply fork` の繰り返し回数・`scope`、`apply join` の `--force-resolve` などの既定値をまとめています。
- サブコマンド未指定時の `CmocError` 生成、補完プローブ時の分岐、Click/Typer 例外の共通整形、`python src/main.py` 直実行の起動経路を扱います。

## Read this when

- cmoc CLI の起動点と、`session` / `apply` / `review` のサブアプリ構成を確認したいとき。
- `init`、`session fork/join/abandon`、`apply fork/join/abandon`、`review oracles` の登録名、エイリアス、既定オプションを確認したいとき。
- サブコマンド未指定時の利用者向けエラー、補完プローブの扱い、Click/Typer 例外の共通整形を追いたいとき。
- `python src/main.py` で直接起動する経路と、そのときの例外処理を確認したいとき。

## Do not read this when

- `src/sub_commands/` 配下の各サブコマンド本体の処理だけを確認したいとき。
- 共通エラー型や `format_error_report()` の整形仕様だけを確認したいとき。
- `INDEX.md` の生成ルールや `oracles` 側のルーティング方針だけを確認したいとき。

## hash

- 7eb6c6be9a4576cdc697c9a82f65de46450efcff9825b8fc064595ec07baf889
<!-- cmoc-index-kind: file -->

# `sub_commands`

## Summary

- `src/sub_commands` は `cmoc` のサブコマンド実装をまとめた入口ディレクトリです。
- `__init__.py`、`init.py`、`eval_oracles.py`、`apply/`、`session/` を通じて、各サブコマンド実装へ分岐していきます。
- この目次は、どの機能がどのファイルや配下ディレクトリにあるかを素早くたどるためのものです。

## Read this when

- `src/sub_commands` 配下にどの実装ファイルやパッケージがあるかを整理したいとき。
- `cmoc init`、`cmoc review oracles`、`cmoc apply` 系、`cmoc session` 系の入口をまとめて把握したいとき。
- このディレクトリの役割を、個別モジュールへ入る前の案内図として確認したいとき。

## Do not read this when

- `src/sub_commands` の中で、特定のサブコマンド実装だけを直接追いたいとき。
- `cmoc apply` や `cmoc session` の個別処理や状態遷移の詳細だけを確認したいとき。
- `cmoc` 全体の使い方や `oracles` の仕様断片だけを見たいとき。

## hash

- 58736f513cb72294f72b2929f048bbba6d96e438ddb0b666f1fae5dfe87e330c
<!-- cmoc-index-kind: directory -->
