import sys

# You may also pick one without version check, of course
if sys.version_info < (3, 11):
    from typing_extensions import NotRequired
else:
    from typing import NotRequired
from typing import List, Dict, Any, TypedDict
from datetime import datetime


class Meta(TypedDict):
    id: str
    node: str
    ms: int


class Image(TypedDict):
    url: str
    height: int
    width: int


class SearchItem(TypedDict):
    t: int
    rank: NotRequired[int]
    url: NotRequired[str]
    title: NotRequired[str]
    snippet: NotRequired[str]
    published: NotRequired[datetime]
    thumbnail: NotRequired[Image]
    list: NotRequired[List[str]]


class SearchResponse(TypedDict):
    meta: Meta
    data: List[SearchItem]
