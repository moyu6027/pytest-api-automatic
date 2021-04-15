# encoding: utf-8
import json

import allure
import pytest
from apiobjects.time_before import Time
from utils.test_data import get_data
from hypothesis import given, strategies as st

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
    @pytest.mark.parametrize('payload', get_data('testdata.csv'))
    def test_timestamp(self, payload, env_config):
        result = self.time_api.before_api(payload, env_config)
        self.time_api.Assert.assert_code(code=result['code'], expect_code=200)

    @allure.story('hypothesis test time-before')
    @given(timestamp=st.text(), target=st.text())
    def test_timestamp_hypothesis(self, timestamp, target, env_config):
        playload = dict()
        playload['timestamp'] = timestamp
        playload['target'] = target
        playload['expected'] = 'True'
        result = self.time_api.before_api(json.dumps(playload), env_config)
        self.time_api.Assert.assert_code(code=result['code'], expect_code=200)
