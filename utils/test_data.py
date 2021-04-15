import os
import csv
import pytest
from core.constant import Constant


def get_data(csv_data_file):
    """
    解析配置文件,type: 'yml' or 'csv'
    """
    try:
        cls = []
        file_path = os.path.join(Constant.RESOURCE_DIR, "data", csv_data_file)
        # 文件位置
        with open(file_path, newline='') as f:
            reader = csv.DictReader(f)
            for item in reader:
                cls.append(item)

        print(cls)
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        return cls


if __name__ == '__main__':
    get_data('post_param.csv')
