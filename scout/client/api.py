import asyncio
import json
import os

import httpx
from dotenv import load_dotenv
from utilities.logging import logger


load_dotenv()


class TorScoutApiClient:

    def __init__(
            self,
            key=os.environ.get('API_KEY'),
            url=os.environ.get('API_URL'),
    ):
        self.key = key
        self.url = url
        self.logger = logger
        self.POST_RESPONSE_ENDPOINT = f'{self.url}/api/process-response/'
        self.POST_SUMMARY_ENDPOINT = f'{self.url}/api/process-summary/'
        self.HOME_ENDPOINT = f'{self.url}/api/'

    async def get(self, url: str):
        """
        Sends get request to specified URL.
        - :arg url: Requested URL.
        """
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(url)
                if response:
                    return response.json()
        except Exception as e:
            self.logger.error(f'(API CLient Get) Some other exception: {e}')
            pass

    async def post(self, url: str, data: dict):
        """
        Sends post request to specified URL.
        - :arg url: Requested URL.
        - :arg data: Dictionary with prepared data.
        """
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(url, json=json.dumps(data))
                if response:
                    return response
        except Exception as e:
            self.logger.error(f'(API CLient Post) Some other exception: {e}')
            pass

    def ping_home(self):
        """"""
        try:
            with httpx.Client() as client:
                response = client.get(self.HOME_ENDPOINT, timeout=5)
                return response
        except Exception:
            pass

    async def get_home(self):
        """
        Requests endpoint: api/.
        """
        try:
            tasks = [asyncio.create_task(
                self.get(self.HOME_ENDPOINT)
            )]
            responses = await asyncio.gather(*tasks)
            if responses:
                return responses[0]
        except Exception as e:
            self.logger.error(f'(API CLient get_home) Some other exception: {e}')
            pass

    async def post_response_data(self, data: dict):
        """
        Sends response data to: api/process-response/
        """
        try:
            tasks = [asyncio.create_task(
                self.post(self.POST_RESPONSE_ENDPOINT, data=data)
            )]
            responses = await asyncio.gather(*tasks)
            if responses:
                return responses[0]
        except Exception as e:
            self.logger.error(f'(API CLient post_response_data) Some other exception: {e}')
            pass

    async def post_summary_data(self, data: dict):
        """
        Sends summary crawling data to: api/summary/
        """
        try:
            tasks = [asyncio.create_task(
                self.post(self.POST_SUMMARY_ENDPOINT, data=data)
            )]
            responses = await asyncio.gather(*tasks)
            if responses:
                return responses[0]
        except Exception as e:
            self.logger.error(f'(API CLient post_summary_data) Some other exception: {e}')
            pass