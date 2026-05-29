# `commons`

## Summary

- `src/commons` は cmoc 全体で使う共通処理の集まりです。
- 実行ラッパー、エラー処理、リポジトリ操作、サブコマンドログ、時間計測、タイムスタンプ、`INDEX.md` 生成をまとめています。
- 個別サブコマンドより先に読む横断的な基盤モジュール群の入口です。

## Read this when

- `cmoc` の共通実行制御、リポジトリルート解決、エラー整形、ログ記録、時間計測をまとめて把握したいとき。
- session / apply のブランチや state、`<repo-root>/.cmoc` 配下の共通管理処理を確認したいとき。
- `codex exec` 呼び出し、Structured Output 検証、`INDEX.md` 生成・維持などの横断的な共通処理を追いたいとき。
- タイムスタンプ生成やサブコマンド終了レポートなど、CLI 共通の補助機能を確認したいとき。

## Do not read this when

- 個別サブコマンドの業務ロジック、引数定義、状態遷移だけを確認したいとき。
- `src/commons` のうち特定の 1 モジュールだけを深掘りしたいときは、この目次ではなく該当ファイルを直接読むべきです。
- テスト実装や CLI 全体の画面設計だけを確認したいとき。

## hash

- 9350995962ac8eb21e2d657f9d2de613890b23c068035946e6e799b4669a15db

# `main.py`

## Summary

- `cmoc` CLI のエントリーポイントで、Typer アプリ本体と `session` / `apply` / `review` のサブアプリを組み立てています。
- `init`、`session fork/join/abandon`、`apply fork/join/abandon`、`review oracles` の各コマンドを定義し、実処理は `src/sub_commands/` 側へ委譲しています。
- Typer / Click の例外を共通エラーレポートへ変換し、`NoArgsIsHelpError` を含む起動時エラーを終了コード付きで処理します。

## Read this when

- `cmoc` のエントリーポイント、Typer アプリの構成、サブコマンド登録を修正・レビューしたいとき
- `init`、`session fork/join/abandon`、`apply fork/join/abandon`、`review oracles` とその引数定義を確認したいとき
- サブコマンドなし起動時の `NoArgsIsHelpError` の扱い、`--help` 相当の挙動、終了コードの伝播を確認したいとき
- Typer / Click の例外を `CmocError` と共通エラーレポートへ変換する起動経路を確認したいとき
- `python src/main.py` で直接起動する経路の振る舞いを確認したいとき

## Do not read this when

- 各サブコマンド本体の処理内容だけを確認したいとき
- 共通エラー型やエラーレポートの整形だけを確認したいとき
- CLI の設計ルールや配置方針だけを確認したいとき
- サブコマンドごとの仕様断片だけを確認したいとき

## hash

- 0c76935e2e4d5e562d321e1b65e17c49e36e89415a7d311c6f037b13785a396f

# `sub_commands`

## Summary

- `src/sub_commands` は `cmoc` のサブコマンド実装をまとめるディレクトリで、`__init__.py` に加えて `apply`、`session`、`eval_oracles.py`、`init.py` が置かれています。
- `apply` は `cmoc apply` 系の実装入口で、`fork`、`join`、`abandon` に分かれています。
- `session` は `cmoc session` 系の実装入口で、`fork`、`join`、`abandon` に分かれています。
- `eval_oracles.py` は `cmoc review oracles` の本体実装、`init.py` は `cmoc init` の本体実装を担います。

## Read this when

- `cmoc` のサブコマンド実装全体の入口を把握したいとき。
- `apply`、`session`、`review oracles`、`init` のどの実装モジュールへ進むべきかを切り分けたいとき。
- `src/sub_commands` 配下のパッケージ構成と、各サブコマンド実装ファイルの役割を整理したいとき。

## Do not read this when

- `cmoc apply` や `cmoc session` のうち、個別のサブコマンド1つだけの詳細仕様、状態遷移、前提条件を確認したいとき。
- `cmoc review oracles` の評価手順や `cmoc init` の初期化手順など、特定コマンドの本体仕様だけを直接追いたいとき。
- `src/sub_commands` ではなく、`oracles` 配下の仕様断片や共通仕様（branch model、error handling、indexing など）を確認したいとき。

## hash

- 27be8e7019cc371c9ae33cfe7345dc23535a8c0e4948a26f145cfb97c4a6a8e5
