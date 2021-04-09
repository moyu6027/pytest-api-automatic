# encoding: utf-8
"""
全局钩子文件
"""
import codecs
import logging
import pytest
import allure
from ruamel import yaml
import os

'''
@author: sean
@file: conftest.py
@time: 2021/4/6
@desc:
'''


@pytest.fixture(scope="session", autouse=True)
def env_config(request):
    """
    读取yaml配置文件
    :param request:
    :return:
    """

    config_path = os.path.join(request.config.rootdir, "config", "env.yml")
    environment = request.config.getoption('environment')
    with codecs.open(config_path, "r", encoding='utf-8') as f:
        env_config = yaml.load(f, Loader=yaml.Loader)  # 读取配置文件
    return env_config[environment]


@pytest.fixture(scope="session", autouse=True)
def root_path(request):
    return request.config.rootdir


def pytest_addoption(parser):
    parser.addoption("--env",
                     action="store",
                     dest="environment",
                     default="test",
                     help="environment: test or prod or dev")
