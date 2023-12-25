import sys

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
    api_balance: NotRequired[float]


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
    error: NotRequired[List[Dict[str, Any]]]


class SummarizationItem(TypedDict):
    output: str
    tokens: int


class SummarizationResponse(TypedDict):
    meta: Meta
    data: SummarizationItem
    error: NotRequired[List[Dict[str, Any]]]


class FastGPTReference(TypedDict):
    title: str
    snippet: str
    url: str


class FastGPTItem(TypedDict):
    output: str
    tokens: int
    references: List[FastGPTReference]


class FastGPTResponse(TypedDict):
    meta: Meta
    data: FastGPTItem
    error: NotRequired[List[Dict[str, Any]]]
