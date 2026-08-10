# -*- coding: utf-8 -*-
"""wiki/workstyle/toc.md を決定的に生成するスクリプト。

このディレクトリの *.md（toc.md 自身を除く）をファイル名順に並べ、
各ファイルの最初の見出し行をタイトルとして 1 行 1 リンクで出力する。
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
EXCLUDE = {"toc.md"}


def first_heading(path):
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.startswith("# "):
                return line[2:].strip()
    return os.path.basename(path)


def main():
    lines = ["# toc", ""]
    for name in sorted(os.listdir(HERE)):
        if not name.endswith(".md") or name in EXCLUDE:
            continue
        title = first_heading(os.path.join(HERE, name))
        lines.append("- [{}]({})".format(title, name))
    with open(os.path.join(HERE, "toc.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
