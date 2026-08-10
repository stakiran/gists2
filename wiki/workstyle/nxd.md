# No XXXX Day (NXD)

会議をしない日、割り込みを受けない日、デプロイしない日。**「やらない」を制度にする** ための、作者の汎用フォーマットである。

## 定義

> **No XXXX Day（NXD）** とは XXXX をしない日を指す。

そして例外を一切認めない。

> 「しない」とは、その日は一回だろうが一秒だろうが一切しないことを意味する。例外はない。一瞬でも「してしまった」場合、その時点で NXD は失敗とみなす。

この厳格さが NXD の設計思想である。**「なるべく減らす」は減らない。** ゼロにしたときだけ、その日は別の性質の日になる。

適用範囲にも制約がある。

> NXD は個人ではなくチーム内で実行するものである。しかし組織内――たとえば 30 人からなる部門全員に適用するのは現実的ではない。なぜなら例外が発生して容易く失敗するからだ。一桁人数以下の、小さなチームでのみ通用するべきだろう。

## 周知の二パターン

作者は運用形態を最初から二つに分けている。

- **部分適用（宣言型）**: 全員ではないが n 人が NXD を表明しており、全員がそれを認識している
- **全体適用（義務型）**: チーム全員に NXD を課す

宣言型は足並みを揃えずに始められる代わりに、周囲が意識していないと結局同じように連絡が来る。義務型は徹底しやすい代わりに導入ハードルが高い。**小さく始めるなら宣言型、効かせたいなら義務型** という素直なトレードオフである。

## XXXX に何を入れるか

作者は AI 複数モデルに大量に列挙させ、目的別に整理している。実際に出てきたものを性質で束ねると、この造語の射程が見えてくる。

**集中を守る**: No Meeting Day / No Interrupt Day / No Ad-hoc Request Day / No Notification Day / No Context Switching Day / No Task Switching Day

**流入を止める**: No New Task Day / No New Ticket Day / No Reprioritization Day / No Backlog Grooming Day

**チャネルを絞る**: No Chat Day / No DM Day / No Email Day / No Camera Day

**リスクを凍結する**: No Deploy Day / No Production Change Day / No Big Merge Day / No Migration Day

**健康を守る**: No Overtime Day / No Lunch Meeting Day / No Back-to-Back Day / No Early Meeting Day

**空気を整える**: No Blame Day / No Negative Talk Day / No Feedback Day

**プロセスを緩める**: No Process Day / No Approval Day / No Policy Change Day

**逆張り**: No Solo Work Day（必ず誰かとペア／モブ）、No Coding Day（設計とドキュメントだけ）、No Undocumented Work Day（記録なしで完了扱いにしない）

最後の「逆張り」群が面白い。NXD は非同期主義者の道具に見えて、**同期を強制する方向にも同じ型が使える**。フォーマットとしての汎用性がある証拠である。

## 隣接する道具たち

NXD は「日」の単位で拘束を切る。作者は同じ発想を別の時間スケールでも実装している。

**時限切断（Auto Disconnect）** —— 指定時間経過後にイベント（特にミーティング）を強制切断する。

> 最大のハードルは実装であり、時限切断を採用したいなら時間指定と切断動作の両方はシームレスにしなくてはならない。ファシリテーターがユーザーにお願いするといった人力の運用は NG である。

作者は徹底しない導入を明確に拒否する。

> ここまで徹底できないのなら、時限切断を導入する意味はない。

そして例外を作らない理由も NXD と同じである。

> また時限切断に「例外的な延長」の概念はない。指定時間後に必ず切れるという世界観をシンプルに実現するため、時限切断は例外を持たない。

副産物として、こういう効果も挙げられている。

> あるいは、それでも構わずミーティングを続ける者がいた場合、それはそういう者（区切りや休憩を意識しない無能な人間）であることをあぶり出せたと言える。

**ミュートデイ** —— [ミリマネジメント](millimanagement.md) の判定基準。会議・進捗確認・即時応答を求めるメンションが一度もない勤務日を、**通常運用として** 設けられるか。NXD が「作る」ものなら、ミュートデイは「成立するか測る」ものである。

## この型が示していること

NXD の本質は、**やらないことを人の意志ではなく日付に紐づける** ところにある。「今日は集中したいので会議を断ります」は個人の交渉になるが、「今日は No Meeting Day です」は制度の参照になる。

[FYIハラスメント](fyi_harassment.md) が「立場の非対称性により受け手が拒否できない構造」を問題にしたなら、NXD は **拒否の根拠を個人から制度に移す** ことでその非対称性を回避する道具である。

関連: [ミリマネジメント](millimanagement.md) / [ソロワーク](solowork.md) / [働き方の8軸診断](collaboration_model_dimensions.md)

出典 Gist: [228e500e](https://gist.github.com/stakiran/228e500ed4c2d57826c373b99a65bc71) / [1248dcff](https://gist.github.com/stakiran/1248dcff33c8f84fab05bb5a3bd63390) / [0ad0060f](https://gist.github.com/stakiran/0ad0060fca36982f7a56a740d4d7f2af)
