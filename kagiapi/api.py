import os
import requests

class KagiClient:
    BASE_URL = "https://kagi.com/api/v0/search"

    def __init__(self, api_key=None):
        if api_key is None:
            api_key = os.environ.get("KAGI_API_KEY")

        if api_key is None:
            raise ValueError("No API key provided. Please provide one or set the KAGI_API_KEY environment variable.")

        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bot {self.api_key}"})

    def search(self, query, limit=None):
        params = {"q": query}

        if limit is not None:
            params["limit"] = limit

        response = self.session.get(KagiClient.BASE_URL, params=params)
        response.raise_for_status()

        return response.json()["data"]
