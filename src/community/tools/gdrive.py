from typing import Any, Dict, List

import requests

from community.tools import BaseTool

#load the GDRIVE_AUTH environment variable from the .env file
import os
from dotenv import load_dotenv
load_dotenv()

GDRIVE_AUTH = os.getenv("GDRIVE_AUTH")
GDRIVE_URL = os.getenv("GDRIVE_URL")


"""
Plug in your Connector configuration here. For example:

Url: http://example_connector.com/search
Auth: Bearer token for the connector

More details: https://docs.cohere.com/docs/connectors
"""


class GDriveRetriever(BaseTool):

    def __init__(self, url: str, auth: str):
        # self.url = url
        # self.auth = auth
        self.url = GDRIVE_URL
        self.auth = GDRIVE_AUTH

    @classmethod
    def is_available(cls) -> bool:
        return True

    def call(self, parameters: dict, **kwargs: Any) -> List[Dict[str, Any]]:
        body = {"query": "summarize the document"}
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.auth}",
        }

        response = requests.post(self.url, json=body, headers=headers)

        return response.json()["results"][0]["text"]
