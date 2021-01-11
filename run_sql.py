"""
Python codes for mysql database
"""

import pymysql

from typing import List
from configuration import *


def get_sql():
    f = open("sql_files/1.sql", "r", encoding="utf-8")
    raw_sql = f.read().split(";")
    for i in range(len(raw_sql)):
        raw_sql[i] = raw_sql[i].replace('\n', ' ')
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
    # sql = ';'.join(sql_list)

    for sql in sql_list:
        try:
            cursor.execute(sql)
            db.commit()
        except Exception as err:
            db.rollback()
            print(err)
    db.close()


def main():
    print(run_sql())


if __name__ == '__main__':
    main()
