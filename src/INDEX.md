# `commons`

## Summary

- `cmoc` の共通処理を集めた `src/commons` ディレクトリの目次です。
- `codex exec` 呼び出し、リポジトリ探索、共通エラー処理、サブコマンドログ、経過時間計測、タイムスタンプ生成、`INDEX.md` 保守の入口をまとめています。
- 各モジュールは個別サブコマンドから再利用される基盤処理で、実行制御と補助ユーティリティの責務分担を扱います。
- `__init__.py` を含む Python パッケージとしての共通領域を案内します。

## Read this when

- 共通モジュールのうち、どこに `codex exec` 呼び出し・repo 操作・ログ・タイミング・エラー処理があるか判断したいとき。
- `src/commons` のどのファイルを修正すべきか、責務の境界を確認したいとき。
- 実装やテストで、サブコマンド横断の共通基盤を参照したいとき。
- `INDEX.md` 自動保守や `<repo-root>` 解析など、複数モジュールにまたがる共通処理を追いたいとき。

## Do not read this when

- 個別サブコマンドの業務ロジックや CLI 引数だけを調べたいとき。
- `oracles` の正本仕様や利用者向け手順だけを確認したいとき。
- 開発規約、テスト規約、環境ルールだけを確認したいとき。
- `README.md`、`AGENTS.md`、`memo` の運用ルールだけを確認したいとき。

## hash

- e4742a1508cbab4d5e927c21a00799a4eca46911908360bf27eac07ce9cd4954

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

- `src/sub_commands` は、cmoc の各サブコマンド実装モジュールをまとめるルーティング用ディレクトリの目次です。
- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` の各本体実装への入口を案内します。
- `__init__.py` はサブコマンド実装パッケージであることを示す最小限の初期化ファイルです。
- 各モジュールは、それぞれのサブコマンドの処理順、事前条件、出力、終了条件、共通処理との接続点を担います。
- この目次は、個別実装を読む前に「どのファイルを参照すべきか」を切り分けるための案内です。

## Read this when

- `src/sub_commands` 配下のどのファイルがどのサブコマンドに対応するかを確認したいとき。
- `cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` の個別実装へ進む入口が必要なとき。
- サブコマンド実装パッケージ全体の境界や、各モジュールの役割分担を把握したいとき。
- 特定のサブコマンドの処理本体ではなく、まず参照先のファイルを絞り込みたいとき。

## Do not read this when

- 個別サブコマンドの引数、実行フロー、エラー処理などの詳細仕様だけを調べたいとき。
- `cmoc` 自体の開発ルール、設計規約、テスト規約、開発環境を調べたいとき。
- コマンド全体の共通仕様や `INDEX.md` 自動生成ルールだけを確認したいとき。
- `README.md`、`AGENTS.md`、`oracles`、`memo` の運用ルールだけを確認したいとき。

## hash

- e077b4c9e5f31047300c01e24cd4df8bae46a141ca82d53678adb49855f5481a
