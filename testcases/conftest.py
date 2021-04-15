import pytest
import logging
import os
import yaml
import json


@pytest.fixture(scope='package', autouse=True)
def testsuite_setup_teardown():
    logging.info('------------------------------------- Start to run test case ---------------------------------\n')
    yield
    logging.info('------------------------------------- End to run test case------------------------------------')


def pytest_generate_tests(metafunc):
    ids = []
    markers = metafunc.definition.own_markers
    for marker in markers:
        if marker.name == 'datafile':  # 读取数据
            test_data_path = os.path.join(metafunc.config.rootdir, "resource", "data", marker.args[0])  # 拼接测试数据路径
            # test_data_section = marker.args[1]
            with open(test_data_path) as f:
                ext = os.path.splitext(test_data_path)[-1]
                if ext in ['.yaml', '.yml']:
                    test_data = yaml.safe_load(f)
                elif ext == '.json':
                    test_data = json.load(f)
                else:
                    raise TypeError('datafile must be yaml，root must be testcases')
    if "parameters" in metafunc.fixturenames:  # 用外部数据进行参数化
        # for data in test_data['tests']:  # 用test_data中的case作为测试用例名称
        #     ids.append(data['case'])
        # 用test_data这个列表对parameters进行参数化。
        test_data_section = metafunc.function.__name__
        metafunc.parametrize("parameters", test_data[test_data_section], scope="function")
