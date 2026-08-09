# progress

novel concept 探索エージェント（監督）の走査進捗管理ページ。

## 走査体制

- **監督**: Opus。作業員の統括、novel 判定、Wiki 執筆
- **作業員**: Sonnet。割り当てられた Gist を精読し、novel concept 候補を返却する
- **顧問**: Fable。判断困難時に相談する。残数は [tickets.md](tickets.md) が唯一の真実

## 走査方式

- 対象: `raw/*.md` 全 **522** ファイル（`index.json` を除く）
- ファイル名アルファベット順に 18 バッチへ等分（1 バッチ 29 前後）
- 作業員 1 体 = 1 バッチ。第1波 batch 00-08、第2波 batch 09-17

## 状態

- **走査済み: 522 / 522（100%）** — 2026-08-09 完了
- 抽出候補: 約 130 件
- 判定済み: A 層 7 / B 層 6 / C 層 20 数件（[判定台帳](novelty_ledger.md)）
- 現在フェーズ: **第1回走査完了。Wiki 初版公開済み**

## バッチ割り当てと結果

| batch | 範囲（先頭 Gist ID） | 状態 |
|---|---|---|
| 00 | 00436190… | 完了 |
| 01 | 1248dcff… | 完了 |
| 02 | 1d96331e… | 完了 |
| 03 | 2c81c98d… | 完了 |
| 04 | 3ebedd65… | 完了 |
| 05 | 4bdb8e60… | 完了 |
| 06 | 58733f97… | 完了 |
| 07 | 65c1dd78… | 完了 |
| 08 | 7217fde1… | 完了 |
| 09 | 7f0c8f9b… | 完了 |
| 10 | 8cf19259… | 完了 |
| 11 | 9af66093… | 完了 |
| 12 | a903349f… | 完了 |
| 13 | b7227b43… | 完了 |
| 14 | c97c5a83… | 完了 |
| 15 | d7967937… | 完了 |
| 16 | e3d75973… | 完了 |
| 17 | f1d65621… | 完了 |

走査対象の全 ID リストは `.filelist.txt` に保存してある。

## 未処理・積み残し

第1回では扱いきれなかったもの。次回の起点にする。

### 一次確認が必要な先行研究の対応づけ

顧問の判定のうち、外部事実に依存し監督が裏取りしていないもの。

- workslop（HBR 2025）とスロップハラスメントの先行関係 — **原典 Gist 3877911c は直読済み。AI が既存俗語として説明していることを確認。外部一次資料は未確認**
- category design（Play Bigger, 2016）と空白発見型ネーミング
- danah boyd の networked publics 4 特性と APS の 4 リスク
- Ouchi の clan control（1979-80）とカルチャー＝ルールの代替品
- Robert Levy の hypocognition と境界盲

### 単独ページ未作成の A 層

- 出社ポイント制度（6e9b6dc0）— 実装可能性が低く後回し
- 既婚の単一性（1279ff93 / 330df365）— [wiki/jtc](../jtc/marriage_monoculture.md) と重複するため判定台帳の記載に留めた

### 判定に至っていない候補群

作業員が拾ったが、監督が三層選別にかけていないもの。

- デデンス（dedense）、VUCARD、Four-jects（Preject / Transject / Coject）
- Modular Notion 系（マンダラ、ヘックス、スプレディケーション）
- HOAST、kairon、DiD/AiD、CMC 原理、四余、annoylogue、こえしろ
- Engineering Guardian、社内仕事マーケットプレイス、AI 代理コミュニケーション
- Liquidware、Conceptware / Contextware、シフト・エンジニアリング

これらは第1回では[検証経済](verification_economy.md)への収束を優先したため保留した。第2回で別 world として扱うか、C 層落選として系譜づけるかを判断する。
