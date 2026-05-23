# `commons`

## Summary

- `src/commons` は、cmoc 全体で共有する基盤処理を集めたディレクトリの目次です。
- `codex exec` 呼び出し、共通エラー処理、repo / git 操作、`INDEX.md` 自動生成、サブコマンドログ、タイムスタンプ、経過時間計測などの横断機能への入口を案内します。
- 各モジュールは、`command_runner.py`、`codex.py`、`errors.py`、`indexing.py`、`repo.py`、`subcommand_log.py`、`timestamps.py`、`timing.py` に分かれています。

## Read this when

- cmoc の共通処理のうち、どのモジュールを読むべきか判断したいとき。
- `codex exec` の呼び出し規約、Structured Output、リトライ、ログ保存の共通仕様を確認したいとき。
- 共通エラーハンドリング、`<repo-root>` 探索、git 操作、`INDEX.md` 生成、サブコマンドのログ出力や時間計測の仕様を確認したいとき。

## Do not read this when

- 個別サブコマンドの業務ロジックや CLI 引数定義だけを調べたいとき。
- `src` や `tests` 全体の設計方針、コーディング規約、開発環境ルールだけを調べたいとき。
- `README.md`、`AGENTS.md`、`oracles`、`memo` などのリポジトリ運用ルールだけを確認したいとき。

## hash

- a88ef58908f9bbe5c5564d5eb1186d43057e110dcd13ed69eb5ad71beb4f5a16

# `main.py`

## Summary

- `cmoc` CLI の Typer エントリーポイントを定義するファイルです。
- `init`、`branch`、`eval-oracles`、`apply`、`merge` を `app` に登録し、それぞれ対応する `src/sub_commands` 実装へ処理を委譲します。
- `main()` で Typer / Click の起動を包み、parse error や想定外例外を共通エラーレポート形式に整えて終了コードを決めます。
- `python src/main.py` で直接実行された場合の起動経路も、このファイルでまとめています。

## Read this when

- `cmoc` のトップレベルコマンド一覧と、各サブコマンドの登録箇所を確認したいとき。
- 各コマンドがどの `src/sub_commands` 実装関数へ渡されるかを調べたいとき。
- `apply` の `--repeat` や `--full`、`eval-oracles` の `--full` などの Typer 引数定義や既定値を確認したいとき。
- Typer / Click の parse error、`NoArgsIsHelpError`、想定外例外がどのように終了コード付きのエラーレポートへ変換されるか確認したいとき。
- `app` オブジェクトや `main()` の起動条件、`python src/main.py` での直接実行時挙動を調べたいとき。

## Do not read this when

- 各サブコマンドの業務ロジックや `src/sub_commands` 配下の本体実装を追いたいとき。
- 共通エラーレポートの本文生成や `commons.errors` の内部を詳しく確認したいとき。
- `INDEX.md` 自動生成、repo 探索、ログ保存などの共通基盤の仕様を調べたいとき。
- `cmoc` の利用手順全体や各サブコマンドの正本仕様を知りたいとき。

## hash

- d8532edf006b5e6a2d51210f24708a8edb537cc004a848ebe834777bdb456caa

# `sub_commands`

## Summary

- `src/sub_commands` は cmoc のサブコマンド実装をまとめるルーティング用ディレクトリの目次です。
- `apply.py`、`branch.py`、`eval_oracles.py`、`init.py`、`merge.py` と、パッケージ境界を示す `__init__.py` への入口を案内します。
- 各サブコマンドの本体実装の所在を整理し、個別モジュールへ進む前の導線を一箇所に集約します。
- このディレクトリはユーザー向けの実行時仕様ではなく、実装ファイル同士の関係を把握するための案内です。

## Read this when

- cmoc のサブコマンド実装がどのファイルに分かれているか確認したいとき。
- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` の本体実装へ進む入口が必要なとき。
- サブコマンド実装パッケージの境界や、それぞれのモジュールの役割をざっと把握したいとき。
- 実装コードを読む前に、どのファイルを優先して読むべきか整理したいとき。

## Do not read this when

- cmoc 全体の開発ルール、コーディング規約、テスト規約、開発環境だけを調べたいとき。
- 共通ユーティリティや `commons` 配下、CLI エントリーポイントの仕様だけを知りたいとき。
- このディレクトリ全体ではなく、特定のサブコマンド 1 つの詳細仕様だけを確認したいとき。
- `README.md`、`AGENTS.md`、`oracles`、`memo` の運用ルールだけを確認したいとき。

## hash

- db80909cffbdec78386c92676dc233a298cf76286ee596d35a0b6826d6dcac01
