import httpx
import pytest
from apiobjects.base_api import BaseApi
from utils.test_data import get_data


class Time(BaseApi):

    def before_api(self, playload, env_config):
        url = env_config['host']['url']
        return self.rest_client.requests(host=url, url='/time/before', method='GET', params=playload)
