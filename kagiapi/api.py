import os
from typing import Optional, Union, Dict, Literal
import requests
from kagiapi.models import SearchResponse, SummarizationResponse, FastGPTResponse


class KagiClient:
    __version__ = "v0"
    BASE_URL = f"https://kagi.com/api/{__version__}"

    def __init__(self, api_key: Optional[str] = None) -> None:
        if api_key is None:
            api_key = os.environ.get("KAGI_API_KEY")

        if api_key is None:
            raise ValueError(
                "No API key provided. Please provide one or set the KAGI_API_KEY environment variable."
            )

        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bot {self.api_key}"})

    def search(self, query: str, limit: int = 10) -> SearchResponse:
        params: Dict[str, Union[int, str]] = {"q": query, "limit": limit}

        response = self.session.get(KagiClient.BASE_URL + "/search", params=params)
        response.raise_for_status()
        return response.json()

    def summarize(
        self,
        url: str = "",
        text: str = "",
        engine: Literal["cecil", "agnes", "daphne", "muriel"] = "cecil",
        summary_type: Literal["summary", "takeaway"] = "summary",
        target_language: Optional[str] = None,
        cache: Optional[bool] = None,
    ) -> SummarizationResponse:
        if url and text:
            raise ValueError(
                "Parameters url and text are exclusive. You must pass one or the other."
            )

        params: Dict[str, Union[int, str]] = {
            "engine": engine,
            "summary_type": summary_type,
        }
        if url:
            params["url"] = url
        elif text:
            params["text"] = text
        else:
            raise ValueError(
                "Parameters url and text are exclusive. You must pass one or the other."
            )

        if target_language:
            params["target_language"] = target_language

        if cache:
            params["cache"] = cache

        response = self.session.get(KagiClient.BASE_URL + "/summarize", params=params)
        response.raise_for_status()
        return response.json()

    def fastgpt(self, query: str, cache: bool = True) -> FastGPTResponse:
        data: Dict[str, Union[int, str]] = {"query": query}

        if cache:
            data["cache"] = cache

        response = self.session.post(KagiClient.BASE_URL + "/fastgpt", json=data)
        response.raise_for_status()
        return response.json()
