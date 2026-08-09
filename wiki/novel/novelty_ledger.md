# novel 判定台帳

522 Gist から抽出した約 130 件の候補を、監督（Opus）と顧問（Fable）が三層に選別した記録。**落選したものも既存名を対応づけて残す。** それ自体が[概念の5要件](concept_five_requirements.md)の「系譜に接続されている」の実演になるからである。

## 判定基準

「既存概念の別名」とは、(a) 学術・実務で確立した名前が既にあり、(b) 候補概念がその適用範囲を超える主張を含まない、の**両方**を満たすもの。片方だけなら B 層（合成・転写）に置く。

## A 層 —— 真に名前のない空白（7 件）

| 概念 | Gist | 判定理由 |
|---|---|---|
| [初期実装の重力](initial_implementation_gravity.md) | af215b94 | **筆頭**。AI の in-context learning と人間の心理的コストが同一実装物に二重に働く機構の特定、および「最も考えられていない表層が最も忠実に複製される」というねじれ。AI 協働時代固有で未命名。反証可能 |
| [検証の償却](verification_amortization.md) | c61208ef | 実践は PAL / tool synthesis に合流するが、**「検証コストの会計」として経営語彙化した名前が存在しない**。エンジニアリング慣行と経営概念の間の空白に正確に着地 |
| [尋問可能な成果物](interrogable_artifact.md) | feb494bc | 部品（assurance case、AQL、RAG の引用義務、口頭試問）は既存。**AI 生成物レビュープロトコルとしての合成**が空白。成立条件と失敗モードまで設計済み |
| [同族の測定器問題](same_family_instrument.md) | d2a35d64 | judge と生成器の誤差相関自体は self-preference bias として既知。**製造業 MSA という検証済みの規律を輸入した点**が novel。ビジネス書読者層にはほぼ確実に空白 |
| [Mechanical Style](mechanical_style.md) | 17006811 | オースティンの performative / constative のほぼ直訳的転写。ただし**「AI 出力無修正可という文書クラスを制度として定義する」**ポリシー概念は各社が今必要としていて名前がない |
| 既婚の単一性 | 1279ff93 / 330df365 | DEI 言説で婚姻状態が同質性軸として命名された例を知らない。marriage premium の選抜仮説とも整合。**真の空白だが政治的に最も燃えやすい**（下記注記） |
| 出社ポイント制度 | 6e9b6dc0 | cap-and-trade の RTO への移植。機構設計として未命名・未実施。novel だが**実証ゼロ**なので提案として扱うべき |

### 既婚の単一性についての注記

意思決定層の既婚者率の高さを、性別・国籍と並ぶ未命名の同質性軸として立てる仮説。因果の向きの整理が鋭い。

> 「結婚して性質が変わる」のではなく、**元々その指向性を持つ者が結婚を選ぶ**。ゆえに DINKs・子なし・別居婚でも単一性は保たれる。

空白としては本物だが、実装可能性は低い。「既婚者を減らせ」という施策には転化できず、意思決定層の多様性監査の切り口としてのみ機能する。作者自身も相関と因果の切り分けの困難を留保している。なお同種の論点は [wiki/jtc](../jtc/marriage_monoculture.md) が JTC の角度から扱っている。

## B 層 —— 既存の合成・転写だが、命名・体系化に固有の価値（6 件）

| 概念 | Gist | 先行 | 残る価値 |
|---|---|---|---|
| [NDD/DD](ndd_dd.md) | c1a0c97b | progressive hardening、JIT/PGO、知識蒸留 | **DD 比率を説明可能性の指標にする**測定提案 |
| 非同期心理的安全性 APS | e91a2ec9 | Edmondson × danah boyd（networked publics の 4 特性と 4 リスクがほぼ一対一） | boyd を引いた上での職場適用は正当な空白。[注意の転嫁](attention_transfer.md)参照 |
| [権限者の余裕](authority_slack.md) | a7ec2b2f | DeMarco『ゆとりの法則』の organizational slack | **内部統制への特化適用**。COSO 系に「統制実施者の余裕」項目はない |
| [圧縮の傲慢](compression_arrogance.md) | 9552275f | トヨタの現地現物、Bezos のナラティブメモ | **「圧縮が必要悪だった前提が崩れた」という時代診断**。前提失効の宣言 |
| [概念の5要件](concept_five_requirements.md) | d764e06e | conceptual engineering（Cappelen, Chalmers） | 「分野はある、道具がない」型の空白。実務用ルーブリック |
| 境界盲 Boundary Blindness | 4cf9ca01 / ee934efe | Robert Levy の **hypocognition**（経験に対応する概念を欠く状態） | hypocognition 自体が無名なので命名価値は残る |

## C 層 —— 既存概念の別名（落選）

容赦なく落とす。ただし系譜情報として残す。

| 候補 | 既存名 |
|---|---|
| FYI ハラスメント | "This meeting could have been an email"、attention theft、Newport の hyperactive hive mind |
| スロップハラスメント | **workslop**（HBR 2025）。しかも同じ Gist 内で AI が既存の俗語として説明している。作者の造語ではなく独立再発明 |
| エクスプロラトリ | **open allocation**（Valve Handbook）。「public 共有だけ義務」の一点のみ差分 |
| カルチャー＝ルールの代替品 | **Ouchi の clan control**（1979-80）が完全に先行 |
| 越境場 | Nonaka の「場」＋ Wenger の CoP ＋ Star の boundary object ＋ Turner の communitas |
| 個別的配慮 | 障害学の social model ＋ person-centered planning |
| 余裕性／スリースラック | Graham の Maker's Schedule、Viva Insights の focus time |
| ミュートデイ | No-Meeting Days（研究蓄積あり）。二値診断への転用のみ差分 |
| MAMA（Meeting as an AMA） | manager office hours ＋ 社内 AMA |
| ホフィス | office hoteling / 商業不動産の hotelization |
| クローズドな匿名 | Suler の online disinhibition effect ＋ stranger-on-a-train 現象 |
| SDR | PMO 標準実務の decision log |
| LIY（List It Yourself） | 「魚の釣り方を教えろ」＋メタ認知訓練。諺レベル |
| Toolonomy／職人性 | からくり改善、end-user development、citizen development。「技能でなく許可構造」の切り分けのみ良い |
| IOOO | VARK（学習スタイル論、**効果研究では概ね棄却済み**）＋ ニューロダイバーシティ配慮。SOGI 転写は修辞として巧いが中身が弱い |
| 判断尊厳 / scripty | autonomy、moral injury、Bourdieu の doxa |
| 社会欲の私事化 | workism 批判（Thompson）＋ Netflix「家族ではなくチーム」 |
| 認知的コンテキスト特性 CCT | 作業記憶・切替コスト・チャンキングの再包装。DiSC 的な疑似アセスメント化リスク |
| ペアコミュニケーション | silent meetings（Amazon/Square）＋ペアプロ一般化。L2 > L1 指標のみ独自 |
| [空白発見型ネーミング](blank_naming.md) | **category design**（Play Bigger, 2016）＋言語学の lexical gap。ただし自己診断装置としては別の価値がある（B 層相当として単独ページ化） |
| Human Context 3 層 | SECI・KM の 30 年が「空白」主張を弱める。3 層整理自体は簡潔で悪くない |
| Spike Driven Development | XP の spike の再結合。番号参照コミュニケーションは modest |
| コンセモニー / 流用主義 / PWEP 等 | JTC 現象語彙群。[wiki/jtc](../jtc/index.md) が扱済み。本 Wiki の射程外 |

## 判定の副産物：novelty と革新性は逆相関する

顧問が指摘した不都合な事実。

**革新性**（権限を持つ者がいきなりフル投入して効く確度と効果）が高いのは、先行慣行や実証に裏打ちされたものである。それは定義上 novel でない。逆に真に novel なものは、誰も試していないから確度が低い。

| | novelty 高 | novelty 低 |
|---|---|---|
| **革新性 高** | 検証の償却、尋問可能な成果物、Mechanical Style、同族の測定器問題 | ミュートデイ、権限者の余裕 |
| **革新性 低** | 既婚の単一性、出社ポイント制度 | IOOO、CCT、LIY |

**左上のセルが本 Wiki の成果物である。** 両立している 4 件は、いずれも[検証経済](verification_economy.md)の系に属する。これは偶然ではなく、検証経済が「まだ誰も名付けていないが、既に全員が困っている」領域だからである。

## 革新性ランキング（明日投入して効く順）

1. **[検証の償却](verification_amortization.md) ＋ [NDD/DD](ndd_dd.md)（統合）** —— CTO 号令「反復性のある AI 委任は、成果物でなく変換器を納品させよ」。失敗してもスクリプト資産が残るので下方リスクが小さい
2. **[Mechanical Style](mechanical_style.md)** —— 既に起きている行動を合法化するだけなので抵抗が最小。偽装コストと疑心コストを即日削減
3. **[尋問可能な成果物](interrogable_artifact.md)** —— レビュー規程の改定一本。効果測定は答弁不能率
4. **[同族の測定器問題](same_family_instrument.md)** —— 「効く」というより**既に出血している傷を塞ぐ**類
5. **[権限者の余裕](authority_slack.md)** —— CFO 号令。監査法人相手に説明が立つ
6. **[圧縮の傲慢](compression_arrogance.md)** —— 5 とセットで投入すると一貫した経営姿勢になる
7. （次点）ミュートデイ —— novel ではないが確度は最高クラス。投入コストほぼゼロ

**選外の明示**: 出社ポイント制度は効果期待は大きいが、ゲーミング・公平性紛争・労務リスクで確度が低く「いきなりフル投入」条件を満たさない。IOOO・既婚の単一性など識別系は効果の即効性がない。

## 判定の限界

- 監督・顧問ともに 2026 年前半までの学習知識に依存する。**先行研究の見落としがありうる**
- 特に workslop、category design、boyd の 4 特性、Ouchi、からくり改善への対応づけは、原典の一次確認を経ていない
- スロップハラスメントについては、原典 Gist（3877911c）を監督が直読し、AI が既存俗語として説明していることを確認済み

関連: [検証経済](verification_economy.md) / [エグゼクティブサマリー](executive_summary.md) / [tickets](tickets.md)
