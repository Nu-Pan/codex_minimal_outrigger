# `branch_model.md`

## Summary

- cmoc の branch model を定義する仕様断片です。
- session の起点 branch、session 用 branch、apply 用 branch の役割分担と命名規則をまとめています。
- `cmoc apply` の snapshot 原則と、`<cmoc-session-state-file>` のスキーマも扱います。

## Read this when

- `<local-branch>`、`<cmoc-session-branch>`、`<cmoc-apply-branch>` の関係と命名規則を確認したいとき
- session の起点となる `<cmoc-session-home-branch>` の決め方や、active session の扱いを実装・修正したいとき
- `cmoc apply` の snapshot 固定ルールや、開始後に session が進んだ場合の扱いを確認したいとき
- `<cmoc-session-state-file>` の役割や、session/apply の状態遷移に使う保存情報を確認したいとき

## Do not read this when

- `cmoc session fork`、`cmoc session join`、`cmoc apply` など個別サブコマンドの詳細な手順だけを確認したいとき
- `cmoc init` や開発環境、コーディング規約、テスト規約など、branch model 以外の仕様を確認したいとき
- `<cmoc-session-state-file>` の保存形式よりも、状態遷移やコマンド出力の詳細を別仕様で確認したいとき

## hash

- 0430e1f694da4e1c5fe29d9c8189e1cb514324b94ec03593eed53dfa252a4585

# `codex_call.md`

## Summary

- `cmoc` から `codex exec` を呼び出すための共通規約をまとめた文書です。
- stdin でプロンプト本文を渡す方法、プロンプトの構成要件、アクセス制限の書き方、モデル指定と出力方法、失敗時の扱いまでを扱います。

## Read this when

- `codex exec` の起動方法や、stdin 経由でのプロンプト送信ルールを実装・修正・レビューしたいとき
- prompt の構成、argv に載せてよい情報の制約、`--output-schema` / `--output-last-message` を含む出力規約を確認したいとき
- sandbox の read-only / workspace-write の選択基準、Model / Reasoning Effort の指定方針、quota 不足時の待機・再開手順を確認したいとき

## Do not read this when

- `cmoc session` / `cmoc apply` / `cmoc eval-oracles` など、個別サブコマンド固有の処理ロジックだけを確認したいとき
- `codex exec` 以外の実行手段や、一般的なシェル呼び出し方針を知りたいとき
- `INDEX.md` 生成規約や、他の仕様ファイルのルーティングだけを確認したいとき

## hash

- bd838ad821fa22f2c811f51ef3663e5235af9a23c9e1f3ca2da0fd043c3bcf08

# `console_and_file_log.md`

## Summary

- サブコマンド呼び出しごとのコンソール・ファイル両方への tee 出力、ログ保存先、追跡可能性の要件を定めている。
- ステップ開始通知、Codex CLI 呼び出し通知、経過時間、戻り値、途中経過と作業完了レポートの見分け方を扱う。
- 標準出力に流す時間表示フォーマットを定義している。

## Read this when

- サブコマンド実行時の標準出力とログファイルの出し分け、または tee の実装を確認したいとき。
- `.cmoc/logs/sub_commands/<time-stamp>.log` への保存や、過去の実行を辿れるログ構造を設計・修正したいとき。
- ステップ開始通知や Codex CLI 呼び出し通知、経過時間表示、完了報告の表示形式を実装・調整したいとき。
- 時間表示を `<hour>h <minute>m <sec>.<msec>s` 形式に揃える必要があるとき。

## Do not read this when

- 特定のサブコマンドの引数、状態遷移、業務ロジックだけを確認したいとき。
- branch model、session/apply の手順、エラー処理など、出力規則以外の仕様を調べたいとき。
- README や AGENTS などのリポジトリ運用ルールだけを確認したいとき。

## hash

- 87802561acbe4b063a58543c94ec190bcbebf3ff78dd8ee015a51e071ab05a1b

# `error_handling.md`

## Summary

- cmoc 全体に適用される一般的なエラーハンドリング規則をまとめた参照先。特別な仕様がない限り、処理を中断し、エラーレポートを stdout に出し、エラー終了ステータスコードを返す。特別な記載がある場合はその指示を優先する。

## Read this when

- 処理を中断してエラーとして扱うべきかを判断したい場合
- エラーレポートとして stdout に何を出すかを確認したい場合
- エラー終了時のステータスコードや、特別な記載がある仕様との優先関係を確認したい場合

## Do not read this when

- 各サブコマンドや個別機能の仕様に、独自のエラー処理が明記されている場合
- 通常の成功系フローや出力仕様だけを確認したい場合
- エラーハンドリング以外の設計規則や実装ルールを調べたい場合

## hash

- bfaceea1701755cbe1f24db75ea9044ad4d4ed7dc98edef844bc94e39c3bbdf8

# `indexing.md`

## Summary

- `cmoc` が `<repo-root>` 配下に `INDEX.md` を自動配置・自動更新するための仕様をまとめた文書。
- 配置対象ディレクトリと、目次作成対象から除外するファイル・ディレクトリの判定ルールを定義している。
- `INDEX.md` の各目次項目に必要な見出し構成、説明の書き方、参照ハッシュの扱いを定めている。
- 目次情報の生成方法として、Structured Output の JSON スキーマと `codex exec` の使い方を指定している。
- `INDEX.md` メンテナンスの実行タイミング、処理順序、既存差分の扱い、自動コミット条件を定義している。

## Read this when

- `<repo-root>` 配下の `INDEX.md` をどこに置くか決めるとき。
- `INDEX.md` に載せるべきファイル・ディレクトリの選別ルールを確認するとき。
- `INDEX.md` の各項目に書く Summary / Read this when / Do not read this when / hash の形式を実装・更新するとき。
- `INDEX.md` の生成や再生成、差分更新、自動コミットの流れを実装するとき。
- Codex CLI を呼ぶ前に実行するべき `INDEX.md` メンテナンスの条件を確認するとき。

## Do not read this when

- `INDEX.md` の配置・更新・検証に関係しない機能を実装するとき。
- `INDEX.md` の目次生成ルールではなく、他の `oracles` の仕様だけを確認すれば足りるとき。
- リポジトリの一般的なアプリ機能や業務ロジックを扱っていて、`INDEX.md` のメンテナンス処理を触らないとき。

## hash

- 5690765b2f0740b860e81c8096b3adb5ab80983eafbffce20b09338a1b33f920

# `misc_specs.md`

## Summary

- `cmoc` 全体に共通する雑多な基礎仕様をまとめたファイルです。
- 実装ファイルの列挙ルール、`<repo-root>` 探索とカレントディレクトリ変更、`<repo-root>/.cmoc` の扱いを定義します。
- タイムスタンプ形式と、`<cmoc-managed-branch>` 上で何を指すかの定義も含みます。

## Read this when

- `<repo-root>` 配下の実装ファイルを機械的に列挙するルールを確認したいとき
- `<repo-root>` の探索方法や、`<repo-root>/oracles`・`.gitignore`・`.git`・`INDEX.md` の扱いを確認したいとき
- `<repo-root>` を git 管理リポジトリとしてどう仮定するか、また `cmoc` 実行時のカレントディレクトリの扱いを確認したいとき
- `<repo-root>/.cmoc` の追跡対象外ルールや、タイムスタンプ形式、`<cmoc-managed-branch>` の定義を確認したいとき

## Do not read this when

- `cmoc` の具体的なサブコマンドの手順や入出力仕様を探しているとき
- `apply` / `eval-oracles` / `session-fork` など個別機能の詳細仕様を探しているとき
- リポジトリ固有の実装方針やドメイン知識を確認したいとき

## hash

- 396555d1a18571100a3731b268271af191e67faa57b86ac4f1e9e107be9e1f1b

# `oracles.md`

## Summary

- `oracles ファイル` の定義、役割、自動処理上の扱いをまとめた入口です。
- `<repo-root>/oracles` 配下の非 `INDEX.md` ファイルが対象であり、AI は提案できても編集は人間が行う前提を示します。
- Codex CLI が読み書きしてよい範囲と、workspace-write 後に差分がないことを機械的に検査する規則を確認できます。

## Read this when

- `oracles ファイル` の定義を確認したいとき
- `oracles ファイル` を人間が所有し、AI が編集しない前提を確認したいとき
- `oracles` 配下のファイルに対する読み書き可否や自動処理規則を確認したいとき

## Do not read this when

- `INDEX.md` の作成手順やメンテナンス規則だけを確認したいとき
- `cmoc` のサブコマンド仕様や実装方針を確認したいとき
- `oracles` 配下の個別仕様ファイルそのものを編集したいとき

## hash

- 846f75a87ba5831d36df56aa4f44028b2b6c01f4fd11932d0dac73376382191b

# `sub_commands`

## Summary

- `apply_abandon.md` は、未 join の apply run を破棄する `cmoc apply abandon` の仕様入口である。
- `apply_fork.md` は、Codex CLI による調査・修正ループを開始する `cmoc apply` の仕様入口である。
- `apply_join.md` は、`cmoc` が積み上げた成果物を `cmoc-session-branch` に統合する `cmoc apply join` の仕様入口である。
- `eval_oracles.md` は、現在の `<repo-root>/oracles` スナップショットを仕様だけで評価する `cmoc eval-oracles` の仕様入口である。
- `init.md` は、`<repo-root>` を cmoc 作業可能状態に初期化する `cmoc init` の仕様入口である。
- `session_abandon.md` は、`cmoc-session-branch` を本流へ merge せず破棄する `cmoc session abandon` の仕様入口である。
- `session_fork.md` は、現在の local branch から `cmoc/session/...` を作る `cmoc session fork` の仕様入口である。
- `session_join.md` は、`cmoc-session-branch` を home branch に merge する `cmoc session join` の仕様入口である。
- レガシーな `cmoc branch` と `cmoc merge` は、それぞれ `session_fork.md` と `session_join.md` で扱う。

## Read this when

- `cmoc apply abandon` / `cmoc apply fork` / `cmoc apply join` のいずれかの実装・修正・レビューを行うとき。
- `cmoc eval-oracles` の評価範囲、結果レポート、Structured Output を確認したいとき。
- `cmoc init` の初期化手順や `.cmoc` の追跡対象外保証を確認したいとき。
- `cmoc session fork` / `cmoc session join` / `cmoc session abandon` の session ライフサイクルを確認したいとき。
- 個別のサブコマンド仕様を選別したいときに、どの文書へ進むべきか判断したいとき。

## Do not read this when

- この配下のどれか 1 つのサブコマンドに絞っていて、他のサブコマンド仕様まで読む必要がないとき。
- サブコマンド個別の実装ではなく、`cmoc` の共通設計や上位方針だけを確認したいとき。
- `oracles` や `dev_rules` の別系統の仕様だけを追いたいとき。
- 実装ファイルやテストファイルだけを確認すれば十分なとき。

## hash

- e2dca6d4820b09467166231971955f241b2ee96178d4e76db785b4009c201740

# `usage.md`

## Summary

- `cmoc` のユーザー向け使用方法をまとめた入口で、実行前提と典型的な運用フローを説明している。
- `PATH` 設定による起動方法、初回の `cmoc init`、`session fork`・`eval-oracles`・`apply`・`session join` の流れを扱う。
- 実装詳細ではなく、`cmoc` をどう使うかを把握するための案内文書である。

## Read this when

- `cmoc` を人間がどのように呼び出して使うか、全体の利用手順を確認したいとき
- 初回に一度だけ必要な `cmoc init` の前提を確認したいとき
- `session fork` から `eval-oracles`、`apply`、`session join` までの想定ワークフローを把握したいとき
- `<cmoc-root>/bin` を `PATH` に追加して `cmoc` コマンドとして実行する前提を確認したいとき

## Do not read this when

- `cmoc` の個別サブコマンド（`init`、`session fork`、`eval-oracles`、`apply`、`session join` など）の詳細仕様だけを確認したいとき
- エラー処理、終了コード、レポート形式などの共通規約だけを確認したいとき
- ブランチモデルや `oracles` の更新規約など、使用方法ではなく内部仕様を確認したいとき

## hash

- 1acb8c34c04e0211c05442f2a1753897cdb9c7ce8c5849112fdaff932bcc4dba
