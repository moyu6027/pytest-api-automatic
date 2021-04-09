# -*- coding: utf-8 -*-
# @Author  : sean
# @File    : Assert.py

from jsonpath import jsonpath
from core import Log


class Assertion:
    def __init__(self):
        self.log = Log.LogInfo()

    def assert_not_in(self, parm, list_param):
        try:
            assert parm not in list_param
            return True
        except Exception:
            self.log.error(f'AssertionError: param  {parm} in  list_param  {list_param}  ')
            raise

    def assert_in(self, parm, list_param):
        try:
            assert parm in list_param
            return True
        except Exception:
            self.log.error(f'AssertionError: param  {parm} not in  list_param  {list_param}  ')
            raise

    def assert_code(self, code, expect_code):
        try:
            assert code == expect_code
            return True
        except Exception:
            self.log.error('AssertionError: expect_code is %s, statusCode is %s ' % (expect_code, code))
            raise

    def assert_body(self, body, body_msg, expected_msg):
        """
        验证response body中任意属性的值
        :param body:
        :param body_msg:
        :param expected_msg:
        :param comment:
        :return:
        """
        try:
            msg = body[body_msg]

            assert msg == expected_msg
            return True
        except Exception as e:
            self.log.error(
                "Response body msg != expected_msg, expected_msg is %s, body_msg is %s" % (expected_msg, body_msg))
            raise

    def assert_time(self, time, expected_time):
        """
        验证response body响应时间小于预期最大响应时间,单位：毫秒
        :param body:
        :param expected_time:
        :return:
        """
        try:
            assert time < expected_time
            return True

        except:
            self.log.error("Response time > expected_time, expected_time is %s, time is %s" % (expected_time, time))
            raise

    def assert_kv(self, response_msg, expect_msg):
        """
        验证response response_msg中是否包含期望返回值key-value是否相等或key存在
        :param response_msg:
        :param expect_msg:
        :return:
        """

        try:
            if isinstance(expect_msg, dict):
                for key in expect_msg.keys():
                    assert key in response_msg
                    if isinstance(expect_msg[key], list):
                        for i in range(len(expect_msg[key])):
                            self.assert_kv(response_msg[key][i], expect_msg[key][i])
                    elif isinstance(expect_msg[key], dict):
                        self.assert_kv(response_msg[key], expect_msg[key])
                    elif expect_msg[key] != '':
                        assert expect_msg[key] == response_msg[key]
            else:
                assert response_msg == expect_msg

            return True
        except Exception:
            self.log.error("AssertionError:\n expect_key   is %s \n responseText is %s" % (expect_msg, response_msg))
            raise

    def assert_jsonpath(self, response_msg, json_path, expect_data, method):
        """

        :param response_msg: 返回信息
        :param json_path: json_path
        :param expect_data: 预期
        :param method: in, == 验证
        :return:
        """
        if method == 'in':
            json_path_val = jsonpath(response_msg, json_path)[0]
            try:
                assert expect_data in json_path_val
            except Exception:
                self.log.error("AssertionError:  %s not in  %s" % (expect_data, json_path_val))
                raise
        elif method == 'equal':
            json_path_val = jsonpath(response_msg, json_path)[0]
            try:
                assert expect_data == json_path_val
            except Exception:
                self.log.error("AssertionError:  %s not equal  %s" % (expect_data, json_path_val))
                raise
        elif method == 'Unequal':
            json_path_val = jsonpath(response_msg, json_path)[0]
            try:
                assert expect_data != json_path_val
            except Exception:
                self.log.error("AssertionError:  %s not equal  %s" % (expect_data, json_path_val))
                raise
        elif method == 'length':
            json_path_val = jsonpath(response_msg, json_path)[0]
            try:
                assert expect_data == len(json_path_val)
            except Exception:
                self.log.error("AssertionError:  %s length is not   %s" % (expect_data, json_path_val))
                raise
        elif method == "<=":
            try:
                assert expect_data <= response_msg
            except Exception:
                self.log.error("AssertionError:  %s length is not  <=  %s" % (expect_data, response_msg))
                raise
        elif method == "==":
            try:
                assert expect_data <= response_msg
            except Exception:
                self.log.error("AssertionError:  %s length is not    %s" % (expect_data, response_msg))
                raise
        else:
            raise
