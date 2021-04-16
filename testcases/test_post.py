# encoding: utf-8
import json

import allure
import pytest

from apiobjects.post import Post
from utils.test_data import get_data
from hypothesis import given, strategies as st
from core import Log
'''
@author: sean
@file: test_post.py
@time: 2021/4/15 20:54
@desc: 测试postman API
'''


@allure.epic('postman')
@allure.feature('postman-api')
class TestPost:
    post_api = Post()

    @allure.story('post_param')
    # @pytest.mark.parametrize('payload', get_data('post_param.csv'))
    @pytest.mark.datafile('api_test_data.yml')
    def test_post_param(self, parameters, env_config):
        foo1, foo2, expect_code = parameters
        json_data = {
            "foo1": foo1,
            "foo2": foo2,
        }
        header = {
            "Content-Type": "application/json"
        }
        result = self.post_api.post_param(json_data, env_config)
        self.post_api.Assert.assert_code(code=result['code'], expect_code=expect_code)
