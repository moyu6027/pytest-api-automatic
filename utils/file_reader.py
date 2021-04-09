import demjson
from ruamel import yaml


def read_json(json_absolute_path):
    """
    读取json文件
    :param json_absolute_path: 参数为需要读取的json文件的绝对路径
    :return:
    """

    with open(json_absolute_path, "r", encoding="utf-8") as f:
        data_list = demjson.decode(f.read(), encoding="utf-8")
    return data_list
    # 返回一个数据列表


def read_yaml(yaml_absolute_path):
    """
    读取yaml文件
    :param yaml_absolute_path: 参数为需要读取的yaml文件的绝对路径
    :return:
    """

    with open(yaml_absolute_path, "r", encoding="utf-8") as f:
        data_list = yaml.load(f, Loader=yaml.Loader)
    return data_list
    # 返回一个数据列表
