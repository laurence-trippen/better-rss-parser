from dataclasses import dataclass, field
from typing import Optional, Callable

DEFAULT_HEADERS = {
    'User-Agent': 'rss-parser',
    'Accept': 'application/rss+xml',
}

DEFAULT_MAX_REDIRECTS = 5
DEFAULT_TIMEOUT = 60_000


@dataclass
class ParserOptions:
    headers: dict[str, str] = {}


class Parser:
    def __init__(self, options: Optional[ParserOptions] = None):
        self.options = options or ParserOptions()
        self.etags = {}
        self.last_modified = {}

    def parse_string(xml: str, callback: Callable) -> None:
        pass

    def parse_url(feed_url: str, callback: Callable, redirect_count=0) -> None:
        pass
