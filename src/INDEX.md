# `commons`

## Summary

- `src/commons` は、cmoc 全体で共有する共通処理をまとめたモジュール群です。
- `__init__.py` は `src.commons` パッケージの境界を示す最小ファイルです。
- `codex.py` は `codex exec` 呼び出し、Structured Output、JSON 検証、リトライ、quota 待機を扱います。
- `command_runner.py` と `errors.py` は、サブコマンド実行の共通制御とエラーレポート整形を担います。
- `indexing.py`、`repo.py`、`subcommand_log.py`、`timestamps.py`、`timing.py` は、`INDEX.md` 管理、repo 探索、ログ保存、タイムスタンプ生成、経過時間計測を支えます。

## Read this when

- サブコマンドから使う共通ロジックの置き場所と役割を把握したいとき。
- `codex exec` の共通ラッパー、出力スキーマ、JSON 解析、リトライ方針を確認したいとき。
- `<repo-root>` の探索、現在ブランチ、`HEAD`、差分収集、`.cmoc` の追跡外保証を確認したいとき。
- 共通エラーハンドリング、標準出力とファイルへのログ保存、経過時間表示、タイムスタンプ生成を確認したいとき。
- `INDEX.md` の自動生成・更新や、サブコマンド共通の実行制御を確認したいとき。

## Do not read this when

- 個別サブコマンドの引数や業務ロジックだけを知りたいとき。
- `oracles` 配下の正本仕様やサブコマンド別の利用手順だけを確認したいとき。
- cmoc 自体の開発規約、設計規約、テスト規約、環境ルールだけを調べたいとき。
- `README.md`、`AGENTS.md`、`memo` の運用ルールだけを確認したいとき。
- このディレクトリの共通処理ではなく、別モジュールやテストコードの詳細実装を追いたいとき。

## hash

- 51f65a6990af5db52f722b640018f422c19e6405f1e85894896b0adc4d8f4141

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

- `src/sub_commands` は、cmoc の各サブコマンド本体実装を集めたルーティング用ディレクトリです。
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

- 72cedd67d728075b0bdaf20765e58c0d354b15d0bbd4581a47e5105b14086676
