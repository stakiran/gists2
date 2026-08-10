"""stakiran の全 Gist を raw/(GistID).md として保存する。

使い方:
    python gists.py           # 差分取得(前回から更新のない gist はスキップ)
    python gists.py --force   # 全件取得

- GitHub API で gist 一覧を取得(per_page=100 で最大ページネーション)
- 前回の raw/index.json と updated_at を比較し、未変更かつファイルが
  存在する gist はダウンロードをスキップする
- 各 gist の中身は raw_url から取得して raw/(GistID).md に保存
- 複数ファイルを含む gist は区切りコメントを挟んで連結
- メタデータ(id, description, created_at, updated_at)を raw/index.json に保存
- 環境変数 GITHUB_TOKEN があれば API リクエストに使う(レート制限緩和)
"""

import json
import os
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

GIST_USER = "stakiran"
RAW_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "raw")
PER_PAGE = 100
MAX_WORKERS = 8


def build_request(url):
    headers = {"User-Agent": "gists2-fetcher"}
    token = os.environ.get("GITHUB_TOKEN")
    if token and url.startswith("https://api.github.com/"):
        headers["Authorization"] = f"Bearer {token}"
    return urllib.request.Request(url, headers=headers)


def fetch(url):
    with urllib.request.urlopen(build_request(url), timeout=30) as res:
        return res.read()


def list_all_gists():
    gists = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{GIST_USER}/gists?per_page={PER_PAGE}&page={page}"
        batch = json.loads(fetch(url).decode("utf-8"))
        if not batch:
            break
        gists.extend(batch)
        print(f"page {page}: {len(batch)} gists")
        page += 1
    return gists


def build_content(gist):
    parts = []
    files = sorted(gist["files"].values(), key=lambda f: f["filename"])
    multiple = len(files) > 1
    for f in files:
        raw = fetch(f["raw_url"]).decode("utf-8", errors="replace")
        if multiple:
            parts.append(f"<!-- gist file: {f['filename']} -->\n\n{raw}")
        else:
            parts.append(raw)
    return "\n\n".join(parts)


def save_gist(gist):
    gist_id = gist["id"]
    path = os.path.join(RAW_DIR, f"{gist_id}.md")
    content = build_content(gist)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    return gist_id


def load_prev_index():
    path = os.path.join(RAW_DIR, "index.json")
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as f:
        return {e["id"]: e["updated_at"] for e in json.load(f)}


def save_index(gists):
    entries = [
        {
            "id": g["id"],
            "description": g["description"] or "",
            "created_at": g["created_at"],
            "updated_at": g["updated_at"],
        }
        for g in gists
    ]
    entries.sort(key=lambda e: e["created_at"], reverse=True)
    path = os.path.join(RAW_DIR, "index.json")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(entries, f, ensure_ascii=False, indent=1)


def is_fetched(gist, prev):
    path = os.path.join(RAW_DIR, f"{gist['id']}.md")
    return prev.get(gist["id"]) == gist["updated_at"] and os.path.exists(path)


def main():
    force = "--force" in sys.argv
    os.makedirs(RAW_DIR, exist_ok=True)
    gists = list_all_gists()
    prev = {} if force else load_prev_index()
    targets = [g for g in gists if not is_fetched(g, prev)]
    print(f"total: {len(gists)} gists (fetch: {len(targets)}, skip: {len(gists) - len(targets)})")

    failed = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(save_gist, g): g["id"] for g in targets}
        done = 0
        for future in as_completed(futures):
            gist_id = futures[future]
            try:
                future.result()
            except Exception as e:
                failed.append((gist_id, e))
                print(f"NG {gist_id}: {e}")
            done += 1
            if done % 20 == 0 or done == len(targets):
                print(f"saved {done}/{len(targets)}")

    # 保存に失敗した gist は前回の updated_at のまま index に残し、次回リトライさせる
    failed_ids = {gist_id for gist_id, _ in failed}
    for g in gists:
        if g["id"] in failed_ids and g["id"] in prev:
            g["updated_at"] = prev[g["id"]]
    save_index(gists)

    if failed:
        print(f"failed: {len(failed)}")
        sys.exit(1)
    print("done")


if __name__ == "__main__":
    main()
