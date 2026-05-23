# `commons`

## Summary

- `src/commons` は、cmoc 全体で再利用する共通処理をまとめるディレクトリです。
- `codex exec` 呼び出し、リポジトリ探索、共通エラー整形、サブコマンド共通実行制御、ログ記録、経過時間計測、タイムスタンプ生成、`INDEX.md` 生成・更新の基盤を提供します。
- 個別サブコマンドの実装ではなく、各コマンドから横断利用される基盤モジュールを集約しています。

## Read this when

- cmoc の共通処理を実装・修正したいとき。
- `codex exec` の共通ラッパー、Structured Output、ログ保存、リトライ、quota 復帰の流れを確認したいとき。
- git リポジトリ探索、`<repo-root>` 解決、ブランチ判定、`.cmoc` の ignore 保証、差分検査、commit 制御を確認したいとき。
- サブコマンド共通のエラー表示、tee ログ、経過時間表示、タイムスタンプ生成を確認したいとき。
- `<repo-root>` 配下の `INDEX.md` 自動生成・更新ロジックを確認したいとき。

## Do not read this when

- 個別サブコマンドの業務ロジックや CLI 引数定義を調べたいとき。
- `oracles` 配下の正本仕様やディレクトリのルーティングだけを確認したいとき。
- `README.md`、`AGENTS.md`、`memo` などの運用ルールだけを確認したいとき。
- テスト実装やモックの詳細だけを調べたいとき。

## hash

- 59226fc86f2aa8f1073b983e1192dace60dbdfa80b0552a38ca4a92da1a026ec

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

- `src/sub_commands` は cmoc のサブコマンド本体実装を集約するディレクトリです。
- この配下には `__init__.py` と、`cmoc init`、`cmoc branch`、`cmoc apply`、`cmoc eval-oracles`、`cmoc merge` に対応する実装モジュールがあります。
- 各モジュールは対応サブコマンドの実行フロー、前提条件、Codex CLI 呼び出し、進捗表示、レポート出力などの入口になります。

## Read this when

- `src/sub_commands` 配下で、どのファイルがどのサブコマンドに対応するか確認したいとき。
- サブコマンド本体の実装ファイルを探して、個別仕様やコードを読み進めたいとき。
- `cmoc` のルーティング先をたどる前に、このディレクトリ全体の構成を把握したいとき。

## Do not read this when

- `cmoc` の実行時仕様や個別サブコマンドの詳細挙動そのものを知りたいとき。
- `oracles` 側の正本仕様断片や、共通の `INDEX.md` ルーティング規則を読みたいとき。
- cmoc 自体の開発ルール、テスト規約、開発環境だけを確認したいとき。

## hash

- ee6e0bd62a58536c1a86a9d2c9e74272b26af055831638d5d1319cd02d4e7704
