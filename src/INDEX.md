# `commons`

## Summary

- cmoc のサブコマンドで共通利用するユーティリティ群をまとめたディレクトリです。
- Codex CLI 呼び出し、サブコマンド実行ラッパー、共通エラー、git リポジトリ操作、INDEX.md 生成、ログ、タイムスタンプ、経過時間計測の実装が入っています。
- 各サブモジュールは個別機能ごとに分かれており、`__init__.py` はパッケージ宣言のみを担当します。

## Read this when

- 複数のサブコマンドから使う共通処理を追加・修正したいとき。
- Codex CLI の呼び出し方、Structured Output、INDEX.md 生成、ログ保存、タイミング表示、git リポジトリ操作の仕様を確認したいとき。
- エラー整形や共通例外の扱いを確認したいとき。
- 共有処理をどのモジュールへ置くべきか判断したいとき。

## Do not read this when

- 個別サブコマンドの業務ロジックや CLI 引数定義だけを確認したいとき。
- `src/sub_commands` の実装や `src/main.py` の引数解釈だけを追いたいとき。
- 特定の共通処理 1 つだけを詳しく知りたいときは、このディレクトリ全体ではなく該当モジュールを直接読むべきです。
- `README.md`、`AGENTS.md`、`oracles`、`memo` の運用だけを確認したいとき。

## hash

- 0c67c0b50ddd4bd9b5e315f94472a56a5e818be2763e4965ad3c7d874825016a

# `main.py`

## Summary

- `src/main.py` は `cmoc` CLI の Typer エントリーポイントで、`init`、`session`、`apply`、`eval-oracles` を登録するルーティング用ファイルです。
- `eval-oracles` は `src/sub_commands/eval-oracles.py` を動的に読み込み、`eval-oracle` という hidden な互換 alias も提供します。
- `main()` は `standalone_mode=False` で Typer / Click の例外を受け取り、共通エラーレポートへ変換して終了コードを決めます。
- `NoArgsIsHelpError` を含め、CLI 起動全体の入口と例外整形の責務をまとめて確認するためのファイルです。

## Read this when

- `cmoc` のトップレベルコマンド登録と、各実装への委譲関係を確認したいとき。
- `eval-oracles` の動的読み込みや `apply` の引数定義など、CLI 入口の挙動を見たいとき。
- Typer / Click の parse error、`NoArgsIsHelpError`、想定外例外の扱いを確認したいとき。
- `python src/main.py` で直接起動した場合の入口処理を確認したいとき。

## Do not read this when

- `src/sub_commands` 配下の各サブコマンド本体の業務ロジックだけを確認したいとき。
- `commons.errors` の共通エラー整形や終了コード処理の内部だけを追いたいとき。
- `cmoc` の利用手順や `oracles` 側の正本仕様そのものを確認したいとき。
- `src/commons` の共通基盤モジュールを横断的に確認したいとき。

## hash

- 5666099c1684ee39909d258100b79078f0af0e83050545d78a5ea76a3bd71526

# `sub_commands`

## Summary

- `src.sub_commands` パッケージ配下のサブコマンド実装をまとめた入口です。
- `apply.py`、`eval-oracles.py`、`init.py`、`merge.py`、`session_fork.py`、`__init__.py` への案内を含みます。
- このディレクトリから、各サブコマンドの本体実装やその役割を辿れるようにします。

## Read this when

- `src/sub_commands` 配下の各実装ファイルが何を担当しているかを素早く把握したいとき。
- `cmoc apply`、`cmoc eval-oracles`、`cmoc init`、`cmoc merge`、`cmoc session fork` のどの実装へ進むべきか整理したいとき。
- サブコマンド実装の入口をまとめて確認し、個別モジュールへたどる前の案内が欲しいとき。

## Do not read this when

- 個別サブコマンドの仕様だけを確認したいときは、この目次ではなく該当する `*.py` を直接読むべきです。
- `cmoc` 全体の共通仕様、`branch_model`、`INDEX.md` 生成ルール、`oracles` の扱いだけを確認したいときは、別の入口文書を読むべきです。
- 実装コードやテストコードだけで足りる作業では、このディレクトリの案内を読む必要はありません。

## hash

- 486f675b3a61fb2812cdfdb50e0e371b0e71cb95b5a57fbc4467251ad6efbfda
