import requests
from requests.exceptions import HTTPError, Timeout, RequestException
import logging

class APIClient:
    """
    A generic API client to interact with web APIs.
    """

    def __init__(self, base_url: str, api_key: str = None, timeout: int = 10):
        """
        Initializes the API client.

        Args:
            base_url (str): The base URL of the API.
            api_key (str, optional): API key for authentication.
            timeout (int, optional): Timeout for the requests in seconds.
        """
        self.base_url = base_url
        self.api_key = api_key
        self.timeout = timeout
        self.headers = {"Authorization": f"Bearer {api_key}"} if api_key else {}
        self.session = requests.Session()
        self.session.headers.update(self.headers)

        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def get(self, endpoint: str, params: dict = None, headers: dict = None) -> dict:
        """
        Sends a GET request.

        Args:
            endpoint (str): The API endpoint.
            params (dict, optional): Query parameters.
            headers (dict, optional): Custom headers.

        Returns:
            dict: JSON response from the API.
        """
        try:
            response = self.session.get(
                f"{self.base_url}/{endpoint}",
                params=params,
                headers=headers,
                timeout=self.timeout
            )
            response.raise_for_status()
            self.logger.info(f"GET {endpoint} - Status Code: {response.status_code}")
            return response.json()
        except (HTTPError, Timeout, RequestException) as e:
            self.logger.error(f"GET {endpoint} - Error: {e}")
            return {}

    def post(self, endpoint: str, data: dict, headers: dict = None) -> dict:
        """
        Sends a POST request.

        Args:
            endpoint (str): The API endpoint.
            data (dict): JSON payload.
            headers (dict, optional): Custom headers.

        Returns:
            dict: JSON response from the API.
        """
        try:
            response = self.session.post(
                f"{self.base_url}/{endpoint}",
                json=data,
                headers=headers,
                timeout=self.timeout
            )
            response.raise_for_status()
            self.logger.info(f"POST {endpoint} - Status Code: {response.status_code}")
            return response.json()
        except (HTTPError, Timeout, RequestException) as e:
            self.logger.error(f"POST {endpoint} - Error: {e}")
            return {}

# Example Usage
if __name__ == "__main__":
    client = APIClient("https://example.com/api", "your_api_key_here")
    print(client.get("status"))
