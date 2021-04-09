import os
import csv
from core.constant import Constant


def get_data():
    cls = []
    file_path = os.path.join(Constant.RESOURCE_DIR, "data", "testdata.csv")
    # 文件位置
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f, fieldnames=['timestamp', 'target', 'expected'])
        for item in reader:
            cls.append(item)

    print(cls[1:])
    return cls[1:]


if __name__ == '__main__':
    get_data()
