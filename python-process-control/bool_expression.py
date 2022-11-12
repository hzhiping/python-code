#!/usr/bin/env python
# encoding: utf-8
# author: hzhiping
# datetime: 2022/11/12 20:37


def bool_expression():
    # 案例
    print(True)
    print(False)
    print(True == 1)
    print(False == 0)
    print(False + True + 100)
    # 使用bool()函数可以将其他值转换为布尔类型
    print(bool(100))
    print(bool("采薇采薇，薇亦作止。"))
    print(bool(""))
    print(bool([100]))
    print(bool([]))
    print(bool())


if __name__ == '__main__':
    bool_expression()
