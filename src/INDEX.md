# `commons`

## Summary

- `src/commons` は、cmoc 全体で共有する共通処理をまとめるディレクトリです。
- `codex exec` 呼び出しの共通ラッパー、共通エラー整形、`<repo-root>` 探索と git 操作、`INDEX.md` 自動メンテナンスを扱います。
- サブコマンド実行時のログ保存、経過時間計測、タイムスタンプ生成など、横断的に使う基盤処理を集約しています。
- 個別サブコマンドの本体ロジックではなく、複数機能から再利用される補助処理の置き場です。

## Read this when

- 複数のサブコマンドから使う共通処理の置き場所や責務分担を確認したいとき。
- `codex exec` の呼び出し方、Structured Output、リトライ、quota 待機の共通仕様を確認したいとき。
- `<repo-root>` の探索、`.cmoc` の追跡対象外保証、git 差分の扱い、共通コミット処理を確認したいとき。
- サブコマンドのログ保存、標準出力の tee、経過時間表示、タイムスタンプ生成の仕組みを確認したいとき。
- `INDEX.md` の列挙・生成・更新ロジックを追いたいとき。

## Do not read this when

- 個別サブコマンドの業務ロジックや引数仕様だけを調べたいときは、`src/sub_commands` 側を読むべきです。
- cmoc 自体のコーディング規約、設計規約、テスト規約、開発環境だけを調べたいとき。
- `README.md` や `AGENTS.md`、`oracles` の運用ルールだけを確認したいとき。
- 特定の共通機能だけを知りたいときに、`src/commons` 全体をまとめて読む必要がないとき。

## hash

- 651a39b3e1f77b5afb22c8bff17963f3483081cd1ce344517ba81f1acbf538a5

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

- `src/sub_commands` は、cmoc の各サブコマンド本体実装へのルーティング用ディレクトリの目次です。
- `__init__.py` と `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` の実装ファイルへの入口をまとめています。
- 各サブコマンドの処理順、前提条件、入力、出力、共通制御の詳細を探すときの最初の案内役になります。

## Read this when

- `src/sub_commands` 配下のどの実装ファイルを読むべきか判断したいとき。
- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` の本体実装の場所を知りたいとき。
- サブコマンド実装パッケージの境界や、各モジュールの役割をざっと確認したいとき。
- サブコマンド横断の実装フローや、個別処理のつながりを追いたいとき。

## Do not read this when

- `oracles` 側の正本仕様だけを調べたいとき。
- 開発者向けのコーディング規約、設計規約、テスト規約、開発環境だけを確認したいとき。
- CLI の実行時仕様ではなく、ルーティングや文書構成の変更可否だけを確認したいとき。
- サブコマンドの個別挙動が既に分かっていて、このディレクトリ全体の案内が不要なとき。

## hash

- b8b3b47ca40df5980d839372a58f6f93440115341be38652c386367a5dde633a
