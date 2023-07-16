from typing import Dict

import requests
import logging

logger = logging.getLogger('django')


class DataManager:
    def __init__(self):
        self.data = None
        self.api_url = None

    def prepare_data(self) -> str:
        """
        Clean data from external API
        """
        advice = self.data.get('slip').get('advice')
        if advice:
            return advice

        return 'Something wrong! Pls try ti create report again.'

    def make_request(self) -> Dict[str, str]:
        """
        Send get request to external API method
        """
        self.api_url = url = 'https://api.adviceslip.com/advice'
        self.data = requests.get(url).json()
        logger.info(f'Get the following result from external API: {self.data}')
        return self.data

    def get_data(self) -> str:
        """
        Get data from external API
        """
        self.make_request()
        data = self.prepare_data()
        return data

