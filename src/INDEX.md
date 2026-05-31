# `commons`

## Summary

- cmoc の共通基盤モジュール群をまとめたディレクトリです。
- `codex.py`、`command_runner.py`、`errors.py`、`indexing.py`、`repo.py`、`subcommand_log.py`、`timing.py`、`timestamps.py`、`report_files.py` など、CLI 全体で再利用する処理が入っています。
- 個別サブコマンドの実装ではなく、実行制御・エラー処理・リポジトリ操作・ログ・計測・INDEX メンテナンスの入口として読む場所です。

## Read this when

- `codex exec` の呼び出し、Structured Output 検証、`INDEX.md` メンテナンスの実装を確認したいとき。
- エラーレポート、repo 探索、branch や worktree の扱い、session/apply 状態管理を確認したいとき。
- サブコマンドログ、経過時間計測、タイムスタンプ生成、レポート保存などの共通処理を確認したいとき。

## Do not read this when

- 個別サブコマンドの引数や状態遷移、業務ロジックだけを確認したいとき。
- `oracles` 配下の正本仕様そのものや、`INDEX.md` の生成ルールだけを確認したいとき。
- 共通基盤ではなく、特定の機能実装やテストコードだけを追いたいとき。

## hash

- c0742348ff00971232aaf4b95e4452b7b6c07b76dc2144484ca30739adacafa1

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

- 34ab9fdae7d4622e261437958669dd52ce211f233a2300c1c7c831efc256c365

# `sub_commands`

## Summary

- `src/sub_commands` は cmoc の個別サブコマンド実装を置く入口で、現時点ではパッケージ宣言の `__init__.py` と `cmoc init` 本体の `init.py` だけが入っています。
- `__init__.py` は `src.sub_commands` をパッケージ化するだけの最小モジュールで、`init.py` は `cmoc init` の初期化処理を担当します。

## Read this when

- `src/sub_commands` 配下で、どのモジュールが何を担当しているかを素早く切り分けたいとき。
- `cmoc init` の実装・修正・テスト・レビューに進む前に、入口モジュールを確認したいとき。
- `src.sub_commands` を import できる理由や、`cmoc init` の本体処理がどこにあるかを探したいとき。

## Do not read this when

- `cmoc apply`、`cmoc session`、`cmoc review oracles` など、他のサブコマンドの仕様や実装だけを確認したいとき。
- `init.py` の処理内容そのものを追いたいときは、この目次ではなく `init.py` を直接読むべきです。
- `src/commons` の共通基盤、`tests` の回帰テスト、`oracles` 側の正本仕様だけを確認したいとき。

## hash

- 95132c3905cb7ffd8362fedcc39877f035a2d7c34e2fd397a4b98d92daa02612
