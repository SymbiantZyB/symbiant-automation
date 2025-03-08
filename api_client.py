"""
API Client Module
------------------
Handles API interactions, including GET, POST, PUT, and DELETE requests.

Author: SymbiantZyB
"""

import requests

class APIClient:
    """
    A generic API client to interact with web APIs.
    """

    def __init__(self, base_url: str, api_key: str = None):
        """
        Initializes the API client.

        Args:
            base_url (str): The base URL of the API.
            api_key (str, optional): API key for authentication.
        """
        self.base_url = base_url
        self.api_key = api_key
        self.headers = {"Authorization": f"Bearer {api_key}"} if api_key else {}

    def get(self, endpoint: str, params: dict = None):
        """Sends a GET request."""
        response = requests.get(f"{self.base_url}/{endpoint}", headers=self.headers, params=params)
        return response.json()

    def post(self, endpoint: str, data: dict):
        """Sends a POST request."""
        response = requests.post(f"{self.base_url}/{endpoint}", json=data, headers=self.headers)
        return response.json()

# Example Usage
if __name__ == "__main__":
    client = APIClient("https://example.com/api", "your_api_key_here")
    print(client.get("status"))
