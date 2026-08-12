"""wiki/ の Markdown を HTML 化して docs/wiki/ に出力する。

使い方:
    pip install markdown
    python build_wiki.py

- wiki/(name)/*.md -> docs/wiki/(name)/*.html
- ページ内の相対 .md リンクは .html に書き換える
- docs/wiki/index.html は各 wiki へのリンクを並べる
"""

import html
import os
import re

from build import PAGE_TEMPLATE, convert, first_heading

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WIKI_DIR = os.path.join(BASE_DIR, "wiki")
OUT_DIR = os.path.join(BASE_DIR, "docs", "wiki")

MD_LINK_RE = re.compile(r"\]\((?!https?://)([^)#\s]+)\.md(#[^)]*)?\)")


def rewrite_md_links(md_text):
    return MD_LINK_RE.sub(r"](\1.html\2)", md_text)


def build_page(src, dst, nav):
    with open(src, encoding="utf-8") as f:
        md_text = f.read()
    title = first_heading(md_text) or os.path.splitext(os.path.basename(src))[0]
    page = PAGE_TEMPLATE.format(
        title=html.escape(title),
        nav=nav,
        body=convert(rewrite_md_links(md_text)),
    )
    with open(dst, "w", encoding="utf-8", newline="\n") as f:
        f.write(page)
    return title


def build_wiki(name):
    src_dir = os.path.join(WIKI_DIR, name)
    out_dir = os.path.join(OUT_DIR, name)
    os.makedirs(out_dir, exist_ok=True)
    count = 0
    title = name
    for fname in sorted(os.listdir(src_dir)):
        if not fname.endswith(".md"):
            continue
        stem = os.path.splitext(fname)[0]
        if stem == "index":
            nav = '<p><a href="../index.html">&laquo; wiki</a></p>'
        else:
            nav = '<p><a href="./index.html">&laquo; index</a></p>'
        page_title = build_page(
            os.path.join(src_dir, fname),
            os.path.join(out_dir, f"{stem}.html"),
            nav,
        )
        if stem == "index":
            title = page_title
        count += 1
    print(f"wiki/{name}: {count} pages")
    return title


def build_wiki_index(wikis):
    lines = []
    for name, title in wikis:
        lines.append(f'<li><a href="./{name}/index.html">{html.escape(title)}</a></li>')
    body = "<h1>wiki</h1>\n<ul>\n" + "\n".join(lines) + "\n</ul>"
    page = PAGE_TEMPLATE.format(
        title="wiki",
        nav='<p><a href="../index.html">&laquo; gists2</a></p>',
        body=body,
    )
    with open(os.path.join(OUT_DIR, "index.html"), "w", encoding="utf-8", newline="\n") as f:
        f.write(page)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    wikis = []
    for name in sorted(os.listdir(WIKI_DIR)):
        if os.path.isdir(os.path.join(WIKI_DIR, name)):
            wikis.append((name, build_wiki(name)))
    build_wiki_index(wikis)
    print(f"built {len(wikis)} wikis + wiki/index.html")


if __name__ == "__main__":
    main()
