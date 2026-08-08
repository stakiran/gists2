# gists2

## ディレクトリ構造
- raw/
    - Gists https://gist.github.com/stakiran から取得した Gist を `(GistID).md` で保存する。これを gist file と呼ぶことにする
    - 取得時の pagenation は最大で良い。短時間で取得したいからである
- docs/
    - raw の gist file を HTML 化したものを格納する
    - GitHub Pages で公開する
    - ビルド高速化のため Jekyll は使わず、軽量な markdown to html 変換で済ます。またビルドは GitHub Actions 側で行うことし、html ファイルはバージョン管理しない
- wiki/
    - AI エージェントが raw/ を読み、自身の役割や設定に応じて LLM Wiki をつくるためのディレクトリ
    - 例: JTC(japanese traditional company) 芸人エージェントが、JTC に関するネタを掘り下げた LLM Wiki を wiki/jtc/ 内につくる
    - 1-agent 1-wiki をつくり、Markdown（Obsidianではない） で書く。Front Matter も不要
    - Cosense（旧 Scrapbox）にも精通しており、Cosense の文化に則ったページのつくりかたも駆使する
    - 辞典や辞書をつくりたいのではない。読み物としての面白さ、読みやすさ、覚えやすくて理解しやすい名前やフレーズを使う。備忘録や日記といった生きた営みも歓迎される。造語は構わないが、必ず定義を盛り込む
    - ファイル名はアンダースコア区切りの英語小文字にする
    - 以下のページは必ずつくる:
        - index.md: トップページ
        - toc.md: 目次ページ。全ページへのリンクを網羅している。1行1リンク。決定的なスクリプトを実行するだけで完結させること。
        - log.md: 作業するたびに何をしたかタイムスタンプつきで日記を書くこと。1記事1見出し。Prependで書く
