import httpx
import pytest
from apiobjects.base_api import BaseApi
from utils.test_data import get_data


class Time(BaseApi):

    def before_api(self, playload, env_config):
        url = env_config['host']['url']
        r = httpx.get(url, params=playload)
        self.Logger.info(str(r.content))
        return r
