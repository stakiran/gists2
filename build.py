"""raw/ の gist file を HTML 化して docs/ に出力する。

使い方:
    pip install markdown
    python build.py

- raw/(GistID).md -> docs/(GistID).html
- docs/index.html は最新 gist が上にくる形で 1 行 1 gist へのリンクを並べる
- 並び順・タイトルは raw/index.json(gists.py が生成)を使う
"""

import html
import json
import os

import markdown

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_DIR = os.path.join(BASE_DIR, "raw")
DOCS_DIR = os.path.join(BASE_DIR, "docs")

PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
body {{
  max-width: 800px;
  margin: 0 auto;
  padding: 1em;
  font-family: sans-serif;
  line-height: 1.7;
}}
pre {{
  background: #f6f8fa;
  padding: 1em;
  overflow-x: auto;
}}
code {{
  background: #f6f8fa;
  padding: 0.1em 0.3em;
}}
pre code {{
  padding: 0;
}}
img {{
  max-width: 100%;
}}
blockquote {{
  color: #57606a;
  border-left: 4px solid #d0d7de;
  margin-left: 0;
  padding-left: 1em;
}}
table {{
  border-collapse: collapse;
}}
th, td {{
  border: 1px solid #d0d7de;
  padding: 0.3em 0.6em;
}}
</style>
</head>
<body>
{nav}
{body}
</body>
</html>
"""


def load_index():
    path = os.path.join(RAW_DIR, "index.json")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def convert(md_text):
    return markdown.markdown(
        md_text,
        extensions=["fenced_code", "tables", "nl2br"],
    )


def first_heading(md_text):
    for line in md_text.splitlines():
        line = line.strip()
        if line.startswith("#"):
            return line.lstrip("#").strip()
    return ""


def entry_title(entry):
    return entry["description"] or entry.get("heading") or entry["id"]


def build_gist_page(entry):
    gist_id = entry["id"]
    src = os.path.join(RAW_DIR, f"{gist_id}.md")
    if not os.path.isfile(src):
        return False
    with open(src, encoding="utf-8") as f:
        md_text = f.read()
    entry["heading"] = first_heading(md_text)
    page = PAGE_TEMPLATE.format(
        title=html.escape(entry_title(entry)),
        nav='<p><a href="./index.html">&laquo; index</a></p>',
        body=convert(md_text),
    )
    with open(os.path.join(DOCS_DIR, f"{gist_id}.html"), "w", encoding="utf-8", newline="\n") as f:
        f.write(page)
    return True


def build_index_page(entries):
    lines = []
    for e in entries:
        date = e["created_at"][:10]
        title = html.escape(entry_title(e))
        lines.append(f'<li>{date} <a href="./{e["id"]}.html">{title}</a></li>')
    body = "<h1>gists2</h1>\n<ul>\n" + "\n".join(lines) + "\n</ul>"
    page = PAGE_TEMPLATE.format(title="gists2", nav="", body=body)
    with open(os.path.join(DOCS_DIR, "index.html"), "w", encoding="utf-8", newline="\n") as f:
        f.write(page)


def main():
    os.makedirs(DOCS_DIR, exist_ok=True)
    entries = load_index()
    entries.sort(key=lambda e: e["created_at"], reverse=True)

    built = [e for e in entries if build_gist_page(e)]
    skipped = len(entries) - len(built)
    if skipped:
        print(f"skipped (no md file): {skipped}")

    build_index_page(built)
    print(f"built {len(built)} pages + index.html")


if __name__ == "__main__":
    main()
