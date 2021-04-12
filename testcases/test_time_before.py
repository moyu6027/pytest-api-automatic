# encoding: utf-8
import allure
import pytest
import requests
import httpx
import os
import pandas as pd
from core.Assert import Assertion
from apiobjects.time_before import Time
from utils.test_data import get_data

'''
@author: sean
@file: test_time_before.py
@time: 2021/4/7 20:54
@desc: 测试postman API
'''


@allure.epic('postman')
@allure.feature('postman-api')
class TestTime:
    time_api = Time()

    @allure.story('time_before')
    @pytest.mark.parametrize('playload', get_data())
    def test_timestamp(self, playload, env_config):
        result = self.time_api.before_api(playload, env_config)
        self.time_api.Assert.assert_code(code=result['code'], expect_code=200)