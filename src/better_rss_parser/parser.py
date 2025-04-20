from dataclasses import dataclass, field
from typing import Optional, Dict
from xml.etree import ElementTree

DEFAULT_HEADERS = {
    'User-Agent': 'rss-parser',
    'Accept': 'application/rss+xml',
}

DEFAULT_MAX_REDIRECTS = 5
DEFAULT_TIMEOUT = 60_000


@dataclass
class ParserOptions:
    headers: Dict[str, str] = field(default_factory=dict)
    customFields: dict = field(default_factory=lambda: {
        'item': [],
        'feed': [],
    })
    requestOptions: dict = field(default_factory=dict)
    maxRedirects: int = DEFAULT_MAX_REDIRECTS
    timeout: int = DEFAULT_TIMEOUT


class Parser:
    def __init__(self, options: Optional[ParserOptions] = None):
        self.options = options or ParserOptions()
        self.etags = {}
        self.last_modified = {}

        print(self.options)

    def parse_string(self, xml: str) -> None:
        print(xml)

        root = ElementTree.fromstring(xml)
        print(root.tag)

        if root.tag == "feed":
            self.build_atom_feed(root)
        elif root.tag == "rss":
            pass

    def parse_url(self, feed_url: str, redirect_count=0) -> None:
        pass

    def build_atom_feed(self, root) -> None:
        print("build atom feed")
