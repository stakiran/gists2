# log

## 2026-08-12 第 3 回走査（Gist 201〜530 / 530・完走）

ユーザー指示により 1 回 100 Gist の上限を外し、**残り 330 件を一括走査**。Sonnet 作業員 15 体に 22 Gist ずつ割り当て、3 バッチに分けて並列起動した。監督（Opus）は報告 15 通を統合し、テーマ単位に束ね直してからページ化している。

- **今回の最強素材は a7ec2b2f「承認は注意資源である」**。「忙しすぎる承認者は、脆弱な認証システムと同じである」「最も重要な承認が、最も雑に処理される」。稟議の形骸化を精神論ではなく資源枯渇で説明した。9552275f の「向き合う→裁くへの退行」と合わせて [承認は注意資源である](approval_as_attention.md) に統合
- **b28636c4「因果希薄化」** も同格。Overemployed の議論から、大企業が「一人が本気を出さなくても壊れない」設計になっている理由を三成分（出力が数字に届かない／プロセスが成果を代替する／冗長性が設計思想）に分解している。属人化排除・BCP という正しい要請の帰結である点が良い。[因果希薄化](causal_dilution.md)
- **cae53235「社会欲」** は既存 [欲求という容器](desire_as_container.md) の上位理論だった。「これはバグではなく仕様」「会議の多くは情報伝達ではなく言語的グルーミング」「引き算だけが仕事で、足し算は要らない」。[社会欲に忠実な組織](social_appetite.md) として単独ページ化
- **e7b38e12「恥本位制」** は「やりがい搾取」を経済学で再定式化したもの。「恥のほうは発行コストが安すぎるため、日本ではむしろ濫用されてきた側」。754c9b21 の「会社という名の村」（村化の原因は契約の曖昧さ）と組んで [恥本位制](shame_standard.md)
- 76bd0457 は今回随一の当たり Gist。単独で「カルチャーはルールの代替品」「出社回帰は組織能力の欠如の自白」「口頭文化の勝者」「なんちゃってアジャイル」「強豪校 OB コーチのいない部活」を含む。[口頭文化の勝者が制度をつくる](oral_culture_winners.md) と [規範は制度に勝つ](norm_beats_rule.md) に分配
- 69c41f85 も密度が高く、[コミュニケーションの注入](communication_injection.md) と [拠点エンゲージメント](station_engagement.md) の 2 本に分割した。後者の「一緒に仕事してるわけでもない、仕事を知らない組織長に評価される」はマトリックス組織批判として今回のベスト命名
- 造語の粒が細かいもの（ミリマネジメント / FYI ハラスメント / デ・インタラプト）は [割り込みの経済](interruption_economy.md) に、権威まわり（HiPPO / 鶴の一声 / 外圧型コンサル / 高価な儀式）は [権威の調達](authority_procurement.md) にまとめた。1 ネタ 1 ページにすると読み物にならないと判断した
- ホフィスは 89c6798d と f47736e4 の 2 本に分散していたので統合。第 2 回のログで「次回狙う」と書いた宿題を回収した
- 新規ページ 32 本: approval_as_attention, causal_dilution, human_rule_above_process, oral_culture_winners, social_appetite, shame_standard, relational_capitalism, communication_injection, station_engagement, mental_safety, collaboration_dimensions, shinsotsu_device, hoffice, attendance_points, judgment_dignity, sludge, crossing_ground, authority_procurement, interruption_economy, norm_beats_rule, async_psychological_safety, manager_shelf_life, job_posting_confession, commoner_politics, workstyle_ux, first_implementation_gravity, cognitive_context_traits, career_plateau, decision_architecture, cargo_cult_metrics, sier_jtc, scripture_words
- 更新: index（カテゴリ再編・全 64 ページ）, executive_summary（承認・因果希薄化・社会欲・恥・決定者の 5 節と「JTC を擁護する一段落」を追加）, authors_jtc_structure（第 3 回で見えた四つの更新）, jtc_principles（10 セクション・約 80 フレーズ追加）, progress（完走と差分走査手順）, toc（スクリプト再生成）
- 所感 1: 第 3 回で作者のサイクルに **判定** の層が加わっていることが分かった。「新人が社長にメッセージを送って返事が来るか」「ミュートデイが成立するか」「重い承認なしに道具を作れるか」。命名だけでは組織は動かないという学習の跡である
- 所感 2: 対抗設計の粒度が理念から制度案に降りてきた。出社ポイント制度、ホフィス規格、越境場の稟議通しやすさランキング。特に「合同ポストモーテムが一番通しやすい」は、**JTC で通る条件は効果ではなく説明可能性である** ことを踏まえた設計で、実務家の顔が出ている
- 所感 3: 走査を終えて、JTC を擁護する材料も無視できない量が集まった。規程主義はカルチャー主義の機能的等価物であり、書いてあるぶん解読可能である。昇進の多重ふるいは矯正機構でもある。この視点を executive_summary の末尾に足した
- 残課題: raw/ は 523 → 530 に増えている。今後は progress.md の読了リストとの差分だけを走査する運用に切り替える。手順はスクリプトごと progress.md に置いた

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
