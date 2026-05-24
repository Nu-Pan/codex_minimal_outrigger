# `commons`

## Summary

- `cmoc` の共通処理を集約する `src/commons` パッケージの目次です。
- Codex CLI 呼び出し、サブコマンド実行制御、共通エラー整形、リポジトリ探索、サブコマンドログ、タイムスタンプ、経過時間計測、`INDEX.md` 自動更新を扱います。
- 各サブコマンド本体を薄く保ち、再利用する基盤機能への入口をまとめています。

## Read this when

- 共通モジュールの役割分担や、どの処理をどのファイルで追うべきか確認したいとき。
- `codex exec` の呼び出し、Structured Output、ログ保存、リトライ、quota 待機の流れを確認したいとき。
- git リポジトリのルート探索、`.cmoc` の追跡除外、サブコマンドの共通実行制御、共通エラー表示、タイムスタンプ生成、経過時間表示を調べたいとき。
- `INDEX.md` の生成や更新の共通ロジックを確認したいとき。

## Do not read this when

- 個別サブコマンドの業務ロジックや CLI 引数だけを調べたいとき。
- `oracles` 側の正本仕様やサブコマンド個別仕様を先に読むべきとき。
- このディレクトリに含まれないテストコードや実装コードの詳細を探しているとき。
- `README.md`、`AGENTS.md`、`memo` の運用ルールだけを確認したいとき。

## hash

- d8367196d28c4a5b2ef805414b138f066719f1b2f2d863ab0dc7cf1b1b0f539f

# `main.py`

## Summary

- `src/main.py` は `cmoc` CLI の Typer エントリーポイントをまとめるルーティング用ファイルです。
- `init`、`branch`、`eval-oracles`、`apply`、`merge` の各サブコマンド登録と、対応する `src/sub_commands` 実装への委譲関係を案内します。
- Typer / Click の parse error、`NoArgsIsHelpError`、想定外例外を共通エラーレポートへ変換して終了コードを決める入口です。
- `python src/main.py` で直接起動される経路も含めて、CLI 起動全体の入口を整理します。

## Read this when

- `cmoc` のトップレベルコマンド一覧や、各サブコマンドの登録箇所を確認したいとき。
- 各コマンドがどの `src/sub_commands` の実装関数へ渡されるかを調べたいとき。
- `apply` の引数定義や既定値、`eval-oracles` の `--full` や互換 alias を含む CLI 挙動を確認したいとき。
- Typer / Click の parse error や想定外例外が、どのようにエラーレポートと終了コードへ変換されるか確認したいとき。
- `app` オブジェクトや `main()` の起動条件、`python src/main.py` での直接実行時挙動を調べたいとき。

## Do not read this when

- 各サブコマンドの業務ロジックや `src/sub_commands` 配下の本体実装を追いたいとき。
- 共通エラーレポートの本文生成や `commons.errors` の内部を詳しく確認したいとき。
- `src/commons` の共通基盤や `INDEX.md` 自動生成など、CLI 入口以外の横断仕様を調べたいとき。
- `cmoc` の利用手順全体や、`oracles` 側の正本仕様そのものを知りたいとき。

## hash

- 364d4061be59dadf7450ca3f98e034994463ff03257cae90b47575d6d9941568

# `sub_commands`

## Summary

- `src/sub_commands` は、cmoc の各サブコマンド実装をまとめるルーティング用ディレクトリです。
- この配下には `__init__.py`、`apply.py`、`branch.py`、`eval-oracles.py`、`init.py`、`merge.py` があり、それぞれ `cmoc apply`、`cmoc branch`、`cmoc eval-oracles`、`cmoc init`、`cmoc merge` の本体実装への入口になります。
- サブコマンドごとの業務ロジック、処理順、引数、終了条件を追うときの最初の案内所として機能します。

## Read this when

- `src/sub_commands` 配下で、どのファイルがどのサブコマンドを担当しているかを確認したいとき。
- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` の実装本体へ移動したいとき。
- サブコマンド実装パッケージの境界や、各モジュールの役割をざっと把握したいとき。

## Do not read this when

- 個別サブコマンドの具体的な処理手順、引数、エラーハンドリングだけを確認したいとき。
- `cmoc` 自体の開発ルール、コーディング規約、テスト規約、開発環境を調べたいとき。
- `README.md`、`AGENTS.md`、`oracles`、`memo` の運用ルールや編集可否だけを確認したいとき。

## hash

- 05d25427815a6fea0d0959f24c25d773aa20c97904f5a59d4054409695f755cb
