"""
Python codes for mysql database
"""

import pymysql

from typing import List
from configuration import *


def get_sql():
    f = open("sql_files/test.sql", "r", encoding="utf-8")
    # 使用 ';' 切割字符串，这会使得得到的的字符串数组最后一个元素为空
    raw_sql = f.read().split(";")
    for i in range(len(raw_sql)):
        raw_sql[i] = raw_sql[i].replace('\n', ' ')
    f.close()
    return raw_sql


def run_sql():
    db = pymysql.connect(
        host=host,
        port=port,
        user=username,
        password=password,
        database=database_name
    )
    cursor = db.cursor()

    sql_list = get_sql()
    try:
        for sql in sql_list[:-1]:
            cursor.execute(sql)
        db.commit()
    except Exception as err:
        db.rollback()
        print(err)
    db.close()


def main():
    run_sql()
    print("Finished!")


if __name__ == '__main__':
    main()
