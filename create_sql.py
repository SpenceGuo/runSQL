import random

from typing import List

names = [
    'Spence', 'James', 'McEnany',
    'Rick', 'Valentine', 'Tiffany'
    'Rowling', 'Robert', 'Matthew',
    'Donald', 'Nick', 'Jonas', 'Adam',
    'Kayleigh', 'Stephen', 'Carolla'
]

classes = [
    'class-1', 'class-2', 'class-3', 'class-4', 'class-5'
]

sexes = ['male', 'female']


def creat_sql(n: int):
    global names, classes, sexes

    f = open("sql_files/test.sql", "a", encoding="utf-8")
    for i in range(n):
        name = random.choice(names)
        sex = random.choice(sexes)
        classroom = random.choice(classes)
        age = str(random.randint(20, 25))
        sql = f"\nINSERT INTO students(name,age,sex,class) VALUES('{name}','{age}','{sex}','{classroom}');"
        f.write(sql)
    f.close()


if __name__ == '__main__':
    creat_sql(49990)
    print("Finished!")
