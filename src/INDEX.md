# `commons`

## Summary

- `cmoc` の各サブコマンドから共通利用される基盤処理をまとめたディレクトリです。
- 実行ラッパー、Codex 呼び出し、Git リポジトリ操作、共通エラー、サブコマンドログ、時間計測、タイムスタンプ生成、レポート保存、`INDEX.md` 目次維持が含まれます。
- サブコマンド実装の土台と、目次文書の自動維持を支える共通モジュール群の入口です。

## Read this when

- `src/commons` 配下にどの共通処理があり、どのファイルを読むべきか一覧で把握したいとき。
- `cmoc` 全体で使う実行制御、Git 操作、エラー処理、ログ、時間計測、タイムスタンプ、レポート保存、`INDEX.md` 維持の役割分担を確認したいとき。
- 共通基盤モジュール群の入口として、実装やテストに入る前に読むべき場所を整理したいとき。

## Do not read this when

- 個別の `cmoc` サブコマンドの引数や状態遷移、業務ロジックだけを確認したいとき。
- `oracles` 配下の正本仕様や運用手順だけを確認したいとき。
- `src/commons` のうち特定の 1 モジュールだけを深掘りしたいときは、この目次ではなく該当ファイルを直接読むべきです。

## hash

- 7057e12a09671338c722f95eea812af8f2869867bfe9103e9115872e3155160a
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

- `src/sub_commands` は `cmoc` のサブコマンド実装をまとめる入口です。
- この配下には `__init__.py`、`init.py`、`eval_oracles.py`、`apply/`、`session/` があり、それぞれが個別機能の実装入口になります。
- ここは各コマンドの詳細仕様ではなく、実装ファイルへのルーティングを素早く行うための目次です。

## Read this when

- `src/sub_commands` 配下にどの実装ファイルやパッケージがあるかを整理したいとき。
- `cmoc init`、`cmoc review oracles`、`cmoc apply`、`cmoc session` の実装入口を一覧で把握したいとき。
- 個別モジュールへ進む前に、サブコマンド実装全体の配置と役割分担を確認したいとき。

## Do not read this when

- 個別の `init`、`review oracles`、`apply`、`session` の実行手順や状態遷移だけを追いたいとき。
- 各サブコマンドの引数、終了条件、エラー処理の詳細仕様を知りたいとき。
- `src/sub_commands` のパッケージ宣言だけを確認したいときは、`__init__.py` を直接読むべきです。

## hash

- 9a1040f121d7680f6697f809d9fe808efc42af2c38de2f04e2359d08b3d50eac
<!-- cmoc-index-kind: directory -->
