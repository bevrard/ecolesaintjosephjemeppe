#!/usr/bin/env python3
"""Check every generated page, local target, anchor, image and PDF."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json
import re

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.refs, self.ids, self.errors = [], set(), []
        self.h1 = self.main = self.cards = 0
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            if attrs['id'] in self.ids:
                self.errors.append(f'duplicate id: {attrs["id"]}')
            self.ids.add(attrs['id'])
        self.h1 += tag == 'h1'
        self.main += tag == 'main'
        self.cards += 'news-card' in attrs.get('class', '').split()
        if tag == 'img' and 'alt' not in attrs:
            self.errors.append('image without alt')
        for attr in ('src', 'href'):
            if attr in attrs:
                if not attrs[attr]:
                    self.errors.append(f'empty {attr}')
                self.refs.append(attrs[attr])


def main():
    pages = {p: Page(p.read_text()) for p in ROOT.rglob('*.html') if '.git' not in p.parts}
    failures, count = [], 0
    for path, page in pages.items():
        for error in page.errors:
            failures.append(f'{path.relative_to(ROOT)}: {error}')
        if page.h1 != 1 or page.main != 1:
            failures.append(f'{path.relative_to(ROOT)}: expected one h1 and one main')
        for ref in page.refs:
            url = urlsplit(ref)
            if url.scheme or url.netloc:
                continue
            count += 1
            dest = (ROOT / unquote(url.path).lstrip('/') if url.path.startswith('/') else path.parent / unquote(url.path)).resolve() if url.path else path
            if dest.is_dir():
                dest /= 'index.html'
            if not dest.is_file():
                failures.append(f'{path.relative_to(ROOT)}: missing {ref}')
            elif url.fragment and dest in pages and unquote(url.fragment) not in pages[dest].ids:
                failures.append(f'{path.relative_to(ROOT)}: missing anchor {ref}')
    for path in ROOT.glob('resources/css/school.css'):
        for ref in re.findall(r'url\([\'\"]?([^\)\'\"]+)', path.read_text()):
            if not (path.parent / ref).is_file():
                failures.append(f'missing CSS asset: {ref}')
    life = json.loads((ROOT / 'data/vie-ecole.json').read_text())
    docs = json.loads((ROOT / 'data/documents.json').read_text())
    assert len(life) == 3 and pages[ROOT/'vie-ecole/index.html'].cards == 3
    assert pages[ROOT/'index.html'].cards == 3
    assert len(docs) == 12
    for doc in docs:
        if not (ROOT/doc['file']).read_bytes().startswith(b'%PDF-'):
            failures.append(f'invalid PDF: {doc["file"]}')
    for path, parsed in pages.items():
        source = path.read_text()
        assert not any(token in source for token in ['fbcdn.net', 'vrt_esjjemeppe', 'Voir la publication', '<time', 'facebook.com/reel', 'facebook.com/permalink'])
        assert not re.search(r'(?<![\w/])20(?:17|20|21|23|24|25|26)(?![\w/])', re.sub(r'<[^>]+>', '', source)), path
        for ref in parsed.refs:
            if 'facebook.com' in ref:
                assert ref == 'https://www.facebook.com/profile.php?id=61579439886113', ref
    if failures:
        raise SystemExit('\n'.join(failures))
    print(f'OK: {len(pages)} pages, {count} local references, 3 evergreen topics, 12 PDFs, no visible dates or post links.')


if __name__ == '__main__':
    main()
