import os
from typing import Optional, Union, Dict
import requests
from kagiapi.models import SearchResponse


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
        print(response.status_code, response.content, response.url)
        json_response = response.json()
        return SearchResponse(meta=json_response["meta"], data=json_response["data"])
