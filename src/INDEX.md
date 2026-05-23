# `commons`

## Summary

- `src/commons` は、cmoc の複数サブコマンドから共通利用する基盤モジュール群をまとめたディレクトリです。
- `codex exec` 呼び出しの共通ラッパー、git リポジトリ操作、共通エラー整形、サブコマンドログ、経過時間計測、タイムスタンプ生成、`INDEX.md` 保守処理を収めています。
- `__init__.py` はパッケージ宣言のみで、実行ロジックや公開 API は持ちません。
- 個別サブコマンドの業務ロジックではなく、実装全体で再利用する横断的な処理の入口です。

## Read this when

- 複数のサブコマンドで共通に使う処理を探したいとき。
- `codex exec` の起動方法、Structured Output、リトライ、quota 待機、JSON 検証の実装を確認したいとき。
- `<repo-root>` の探索、git ブランチや `HEAD` 取得、`.cmoc` の追跡対象外保証、差分収集や commit 補助を調べたいとき。
- 共通エラーハンドリング、標準出力とファイルへのログ保存、ステップ単位の経過時間表示、タイムスタンプ形式を確認したいとき。
- `INDEX.md` の自動生成・更新に関わる共通処理を確認したいとき。

## Do not read this when

- 特定サブコマンドの入出力仕様や業務フローだけを知りたいとき。
- CLI のエントリーポイントや引数定義だけを調べたいとき。
- テスト実装や Fake Codex CLI の使い方だけを確認したいとき。
- `README.md`、`AGENTS.md`、`oracles` などの運用ルールだけを確認したいとき。

## hash

- 73a74cd42486d438c22fc5b94642204454e75f74dd1328941bacdf259f95f6c8

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

- `src/sub_commands` は、cmoc の各サブコマンド本体実装へのルーティング用ディレクトリです。
- `__init__.py` はパッケージ宣言のみを担い、サブコマンド実装群の入口をまとめます。
- `apply.py`、`branch.py`、`eval_oracles.py`、`init.py`、`merge.py` が、それぞれ `cmoc apply`、`cmoc branch`、`cmoc eval-oracles`、`cmoc init`、`cmoc merge` の本体処理を担います。
- 各モジュールは、サブコマンド固有の引数、前提条件、実行順、報告出力、終了コード制御をまとめています。
- このディレクトリは、サブコマンドの個別実装を探すときの最初の案内役です。

## Read this when

- どの実装ファイルがどのサブコマンドに対応するか確認したいとき。
- 特定のサブコマンドの処理順や前提条件、入出力の流れを追いたいとき。
- サブコマンド実装パッケージの境界や役割をざっと把握したいとき。
- CLI の入口ではなく、本体実装の場所を探したいとき。

## Do not read this when

- `oracles` 側の正本仕様だけを調べたいとき。
- `src/commons` の共通基盤仕様だけを調べたいとき。
- 開発規約、コーディング規約、テスト規約、開発環境だけを確認したいとき。
- CLI の引数登録や `main.py` のルーティングだけを確認したいとき。

## hash

- b10e0cdc7d76ad12fa26b0471de85cbc301b1ad4864a361795e08cb369911274
