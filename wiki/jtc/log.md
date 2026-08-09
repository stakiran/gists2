# log

## 2026-08-09 第 2 回走査（Gist 101〜200 / 523）

Sonnet 作業員 5 体に 20 Gist ずつ割り当てて並列走査。監督（Opus）が報告を受け、主要ソース 5 件は原文を自分で読み直して引用を検証してからページ化した。

- **最大の収穫は 63b19162「AI 資料をドヤって共有するおっさん」**。単なる愚痴に見えて、フリーライド感／恥の回路／流暢性の錯覚／フォーマットに動機が漏れる／綺麗さの通貨価値の暴落という五つの独立した装置が入っていた。既存 JTC 語彙のどれにも接続しないのに、発生の土壌は完全に JTC 的という新種。[AI 資料ドヤおじさん](ai_doya_ojisan.md) として単独ページ化
- 39ee18c0『V 字回復の経営』読解メモが第 1 回の [骨抜きの正規プロセス](gutted_reform.md) の裏面（攻撃側の教本）だったので、[改革の政治工学](reform_political_engineering.md) と [誰も嘘をつかずに全員が被害者になる](nobody_lies_everyone_suffers.md) の 2 本に分割
- 4c13a48d が第 1 回の [既婚の単一性](marriage_monoculture.md) の理論版だった。三軸モデル（Memory/Attention/Sensor）で説明し直し、さらに「マネジメントが割り込み耐性を要求するのは本質か様式か」という自己批判まで展開している。[認知アーキテクチャによる選抜](cognitive_selection.md) として別ページを立て、旧ページから続報リンクを張った
- 4ca5fe8e は本 Wiki 初の実証系ネタ。3 社 x 3 サイトの投稿数を突き合わせて「口コミが同時に途絶える」異常を検出している。[口コミブラックアウト](review_blackout.md) と命名
- 52319f04 は [コンセモニー](consemony.md) 命名以前の設計図だった。合意形成主義・儀式主義の両方の ❌ 側が「権限委譲して」で始まっており、5659409879 の予実管理の議論（[予実管理という統治の代用品](budget_variance_ritual.md)）と同じ診断に着地する。会議で埋めるか数字で埋めるかの違いにすぎない、と読めるようになった
- 新規ページ 13 本: ai_doya_ojisan, reuseism, reform_political_engineering, nobody_lies_everyone_suffers, budget_variance_ritual, review_blackout, silent_quitting, glue_ojisan, cognitive_selection, manager_onsite_bundle, open_office_pressure, desire_as_container, revenue_per_head_layers, independent_parallel（14 本）
- 更新: index（カテゴリ分けに再編）, executive_summary（数字・辞め方・AI の 3 節を追加）, authors_jtc_structure（第 2 回で足された生々しさ 3 点）, jtc_principles（20 フレーズ追加）, consemony / marriage_monoculture / quiet_quitting（続報と相互リンク）
- 所感: 第 1 回の作者は「概念設計者」だったが、第 2 回では **当事者としての作者** が出てきた。AI ドヤおじさんの実写描写、ASD 合理的配慮の法的武装（「前例がない」への先回り）、そして「SE の仕事はナレッジワークではない、ゴールが決まっていて手段を模索しているにすぎない」という自己認識。この 3 点は観察 → 命名 → 設計のサイクルの外側にある層で、次回以降も追いたい
- 次回走査（201 番目 645b667e 〜）では、第 1 回で保留した collaboration-modules 系のフルページと、ホフィス構想の完成版を狙う

## 2026-08-08 第 1 回走査（Gist 1〜100 / 523）

初回起動。wiki/jtc/ を新規構築した。

- 監督（Opus 相当）+ Sonnet 作業員 5 体の体制で、raw/ のアルファベット順先頭 100 Gist を読了
- 収穫: JTC ネタの密度が最も高かったのは 0ad0060f（作者の概念カタログ「モジュール」索引）。コンセモニー、Paper-Trail Fear、PWEP、流用主義などの造語群を発掘
- 単独ネタとして最強だったのは 330df365 + 1279ff93 の「既婚の単一性」仮説。管理職の同質性を婚姻という軸で切る、既存 JTC 語彙にない新規ネタ
- 作成ページ: index, toc, log, progress, executive_summary, authors_jtc_structure, jtc_principles + 現象ページ 10 本（consemony, paper_trail_fear, pwep_yellow_signal, scripty, marriage_monoculture, katamari_work, gutted_reform, meeting_as_responsibility_diffusion, shadow_ai, white_harassment, quiet_quitting, rto_as_quiet_firing の 12 本）
- toc.md は決定的スクリプト build_toc.py で生成する方式にした
- 所感: 作者は稟議・ハンコ型の古典 JTC ネタをほぼ書かない。「同期・対面・関係性」の複合体を敵と定め、観察→命名→対抗設計のサイクルを回す概念設計者だった。次回走査（101 番目〜）では collaboration-modules 系のフルページや経営小説考察の続編に注目したい
