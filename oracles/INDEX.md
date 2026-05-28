
## hash

- c9f87cbde042bcc4d69ed56a068f214a0dc1fda96510a6403b13bd366a5dd111

# `considered_alternatives`

## Summary

- `cmoc` で採用しなかった設計案や、その不採用理由をまとめたディレクトリの入口です。
- 修正点リスト後の作業計画立案、AI-generated kaizen の自動注入、作業計画レビューの不採用理由を扱います。
- `oracles` と実装の役割分担を考えるときに、代替案の判断材料をたどるための目次です。

## Read this when

- `cmoc apply` 系で、修正点リスト完成後に作業計画を立てる案を採用しなかった理由を確認したいとき。
- AI-generated kaizen を次回の実行コンテキストへ自動的に持ち越さない方針と、その理由を整理したいとき。
- `tgbt plan` や `/plan` のような作業計画レビューを採用しなかった背景や、人間が `oracles` を編集して AI が追従する方針を把握したいとき。

## Do not read this when

- `cmoc apply` 系の実装手順やコマンド仕様そのものを確認したいときは、この配下ではなく該当する正本仕様を直接読むべきです。
- `INDEX.md` の生成ルールや `oracles` 全体のルーティング方針だけを確認したいときは、このディレクトリを読む必要はありません。
- この配下のうち特定の代替案だけを見たいときは、`apply_behavior.md`、`memory_alternative.md`、`working_plan_review.md` を直接参照すべきです。

## hash

- f2a1dd4e497749ef098f24010c2ea174bc89d7c7203024192c524c53e3bb0490
