# encoding: utf-8
import allure
import pytest
import requests
import httpx
import os
import pandas as pd
from utils.test_data import get_data

'''
@author: sean
@file: test_postman_api.py
@time: 2021/4/7 20:54
@desc: 测试postman API
'''


@allure.feature('postman')
@allure.story('postman-api')
@pytest.mark.parametrize('playload', get_data())
def test_timestamp(playload, env_config):
    """
    用例描述：测试不同的timestamp和target
    """
    # 从yml配置文件获取url

    url = env_config['host']['url']
    r = httpx.get(url, params=playload)
    with allure.step("GET请求接口"):
        allure.attach(name="请求接口", body=str(env_config['host']['url']))
        allure.attach(name="请求参数", body=str(playload))
        allure.attach(name="返回状态码", body=str(r.status_code))
        allure.attach(name="返回内容", body=r.content)
    result = r.json()
    assert str(result['before']) == playload['expected']
