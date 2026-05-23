# `commons`

## Summary

- src/commons は、cmoc 全体で使う共通処理を集めたモジュール群です。
- git リポジトリのルート探索、ブランチ判定、差分検査、`.cmoc` の追跡外保証などの repo 共通処理を扱います。
- `codex exec` 呼び出しのラッパー、Structured Output、リトライ、quota 待機などの実行制御を扱います。
- サブコマンド共通のエラー整形、標準出力とファイルへの tee ログ、経過時間計測、タイムスタンプ生成を扱います。
- `INDEX.md` の自動メンテナンスと、生成済み目次の再利用・更新判定の基盤を含みます。

## Read this when

- サブコマンドから使う共通ロジックの配置や役割を把握したいとき。
- `<repo-root>` の探索、現在ブランチ、`HEAD`、未コミット差分、`cmoc` 作業用ブランチ判定を確認したいとき。
- `codex exec` の呼び出し方、JSON 返却、Structured Output、リトライ、quota 待機の仕様を確認したいとき。
- 共通エラーレポート、ログ保存、`tee` 出力、経過時間表示、タイムスタンプ生成の実装を確認したいとき。
- `INDEX.md` の自動生成・更新や、`memo` や `.gitignore` 対象の除外規則を確認したいとき。

## Do not read this when

- 個別サブコマンドの引数や業務ロジックだけを知りたいとき。
- `oracles` 配下の正本仕様やサブコマンド別の利用手順だけを確認したいとき。
- 開発規約、テスト規約、環境ルールなど、cmoc 自体の開発方針だけを調べたいとき。
- `README.md`、`AGENTS.md`、`memo` の運用ルールだけを確認したいとき。
- このディレクトリ配下の共通処理ではなく、別モジュールやテストコードの詳細実装を追いたいとき。

## hash

- 3a856f1815c6cbe0e24c97ec3881ef263fddc06c1651c4bc67b23911c95694f8

# `main.py`

## Summary

- `cmoc` CLI の Typer エントリーポイントを定義するファイルです。
- `init`、`branch`、`eval-oracles`、`apply`、`merge` を `app` に登録し、それぞれ対応する `sub_commands` 実装へ処理を委譲します。
- `main()` で Typer / Click の起動を包み、parse error や想定外例外を共通エラーレポート形式に整えて終了コードを決めます。
- `python src/main.py` で直接実行された場合の起動経路も、このファイルでまとめています。

## Read this when

- `cmoc` のトップレベルコマンド一覧と、各サブコマンドの登録箇所を確認したいとき。
- 各コマンドがどの `sub_commands` 実装関数へ渡されるかを調べたいとき。
- `apply` の `--repeat` や `--full`、`eval-oracles` の `--full` などの Typer 引数定義や既定値を確認したいとき。
- Typer / Click の parse error、`NoArgsIsHelpError`、想定外例外がどのように終了コード付きのエラーレポートへ変換されるか確認したいとき。
- `app` オブジェクトや `main()` の起動条件、`python src/main.py` での直接実行時挙動を調べたいとき。

## Do not read this when

- 各サブコマンドの業務ロジックや `src/sub_commands` 配下の本体実装を追いたいとき。
- 共通エラーレポートの本文生成や `commons.errors` の内部を詳しく確認したいとき。
- `INDEX.md` 自動生成、repo 探索、ログ保存などの共通基盤の仕様を調べたいとき。
- `cmoc` の利用手順全体や各サブコマンドの正本仕様を知りたいとき。

## hash

- 0332175dfe26d12c8c9399d5f7bf9d97c1aaf35044ca0eb67fbe696644a3d041

# `sub_commands`

## Summary

- `src/sub_commands` は、cmoc のサブコマンド本体実装をまとめるルーティング用ディレクトリです。
- `__init__.py` はパッケージ境界を示す最小ファイルで、実行ロジックは持ちません。
- `init.py`、`branch.py`、`apply.py`、`eval_oracles.py`、`merge.py` に、それぞれ `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` の本体実装があります。
- この目次は、個別サブコマンドの実装入口を素早く見つけるための案内です。

## Read this when

- 特定のサブコマンド実装が `src` のどのファイルにあるか確認したいとき。
- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` の実装位置を一覧したいとき。
- サブコマンド実装パッケージの境界や、各モジュールの役割を把握したいとき。
- 実装コードを読む前に、どのファイルから追い始めるべきか判断したいとき。

## Do not read this when

- 個別サブコマンドの引数、詳細な実行手順、終了条件だけを知りたいときは、対応するモジュールを直接読むほうがよいとき。
- cmoc 全体の設計規約、テスト規約、開発環境ルールだけを調べたいとき。
- CLI の共通ルーティングや共通ヘルパーの仕様だけを確認したいとき。
- `README.md`、`AGENTS.md`、`oracles` の運用ルールだけを確認したいとき。

## hash

- 9bd9981514310ee4f09cde6270f9e101160e3bdb563b72176fc5dcea710a319c
