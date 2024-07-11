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

    # def __init__(self, url: str, auth: str):
    def __init__(self):
        # self.url = url
        # self.auth = auth
        self.url = GDRIVE_URL
        self.auth = GDRIVE_AUTH



    @classmethod
    def is_available(cls) -> bool:
        return True

    def call(self, parameters: dict, **kwargs: Any) -> List[Dict[str, Any]]:
        print("abc")
        # print(GDRIVE_AUTH)
        # print(GDRIVE_URL)
        # print(self.auth)
        # print(self.url)
        # print(parameters)

        body = parameters
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.auth}",
        }

        try:
            response = requests.post(self.url, json=body, headers=headers)
            response.raise_for_status()  # This will raise an HTTPError for bad responses
            print(f"Response Status Code: {response.status_code}")
            # print(f"Response Headers: {response.headers}")
            # print(f"Response Content: {response.content}")
            # return response.json()["results"][0]["text"]
            # return response.json()["results"]
            # response_content = response.content
            print ("xyz")
            # print(response_content)
            # return response_content["results"]
            # Convert response content to JSON
            response_json = response.json()
            # print(f"Response JSON: {response_json}")

            # Access the first result's text field
            result_text = response_json["results"][0]["text"]
            print(f"Result Text: {result_text}")

            # return result_text
            return response_json["results"]

        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
        except requests.exceptions.JSONDecodeError as err:
            print(f"JSON decode error occurred: {err}")
            print(f"Response Content: {response.content}")
        except Exception as err:
            print(f"Other error occurred: {err}")


        # return response.json()["results"][0]["text"]

