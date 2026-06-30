import json
from pathlib import Path
from typing import List, Optional

class BookmarkStore:
    def __init__(self, path: Optional[str] = None):
        self.path = Path(path or "~/.quickmark/bookmarks.json").expanduser()
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._load()

    def _load(self):
        if self.path.exists():
            with open(self.path) as f:
                self.bookmarks = json.load(f)
        else:
            self.bookmarks = []

    def _save(self):
        with open(self.path, 'w') as f:
            json.dump(self.bookmarks, f, indent=2)

    def add(self, url: str, title: str = '', tags: List[str] = None):
        bookmark = {
            'url': url,
            'title': title or url,
            'tags': tags or [],
        }
        self.bookmarks.append(bookmark)
        self._save()

    def search(self, query: str) -> List[dict]:
        query = query.lower()
        return [b for b in self.bookmarks 
                if query in b['url'].lower() or query in b['title'].lower()]

    def list(self, tag: str = None) -> List[dict]:
        if tag:
            return [b for b in self.bookmarks if tag in b['tags']]
        return self.bookmarks
