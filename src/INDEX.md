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

- `cmoc` CLI の Typer エントリーポイントで、`init`、`session`、`apply`、`eval-oracles` のトップレベルルーティングを定義する。
- `session fork/join/abandon` と `apply fork/join/abandon` の CLI 入口を登録し、各サブコマンド実装への委譲と未実装エラーの扱いをまとめている。
- `eval-oracles` は `src/sub_commands/eval-oracles.py` を動的読み込みし、互換の `eval-oracle` hidden alias も含めている。
- `main()` は Typer / Click の例外を `cmoc` 形式のエラーレポートへ変換し、`python src/main.py` の直接起動経路も担う。

## Read this when

- `cmoc` のトップレベルコマンド登録と、各サブコマンドへの委譲関係を確認したいとき。
- `eval-oracles` の動的読み込みや、`eval-oracle` 互換 alias の扱いを確認したいとき。
- `NoArgsIsHelpError` を含む Typer / Click の parse error を、共通エラーレポートへどう変換するか追いたいとき。
- `python src/main.py` で直接実行した場合の起動経路を確認したいとき。

## Do not read this when

- `src/sub_commands` 配下の各サブコマンド本体の業務ロジックだけを確認したいとき。
- `commons.errors` の内部実装や、エラーレポートの詳細だけを確認したいとき。
- `cmoc` の利用手順や `oracles` 側の正本仕様だけを確認したいとき。
- `apply` や `session` の個別処理の詳細だけが必要で、CLI 入口のルーティングは不要なとき。

## hash

- c0c9448fe30b21eb69912998ca85c96e3d1be5abb61fcea1bc781a6273785bbc

# `sub_commands`

## Summary

- src/sub_commands は cmoc のサブコマンド実装をまとめるディレクトリで、パッケージ宣言用の __init__.py と、各コマンド本体の apply.py、apply_join.py、eval-oracles.py、init.py、session_abandon.py、session_fork.py、session_join.py を案内します。
- この INDEX.md は、どのファイルに各サブコマンドの実装があるかをたどるための入口です。
- ここからは実装の詳細には踏み込まず、目的に応じて各モジュールへ直接進むための案内を担います。

## Read this when

- src/sub_commands 配下の各サブコマンド実装を、どのファイルに置くか判断したいとき。
- cmoc apply、cmoc apply join、cmoc eval-oracles、cmoc init、cmoc session fork、cmoc session join、cmoc session abandon の入口を整理したいとき。
- src/sub_commands のルーティング文書を作成・更新したいとき。

## Do not read this when

- cmoc apply や cmoc session fork など、個別サブコマンドの具体的な実装だけを確認したいときは、各モジュールを直接読むべきです。
- src/sub_commands 全体の入口や、この配下にあるファイル一覧だけを把握したいときは、ここではなくこのディレクトリの INDEX.md を参照すべきです。
- 共通機能や設計ルールだけを確認したいときは、src/commons や oracles/dev_rules 側の文書を読むべきです。
- src/sub_commands/__init__.py だけが目的なら、パッケージ宣言の確認にとどめれば十分です。

## hash

- c9fe76b41956ef82983be35fa028c9cfbba885f3a7b81b458ecaa39fcdacf88b
