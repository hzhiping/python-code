#!/usr/bin/env python
# encoding: utf-8
# author: hzhiping
# datetime: 2022/11/12 17:58


def list_recurrence():
    # 递推式构造列表
    a = "ab"
    b = [100, 200, 300, 400]
    c = [(x, y) for x in a for y in b]
    print(c)
    # 毕达哥拉斯三元组
    d = [(x, y, z) for x in range(1, 30) for y in range(x, 30) for z in range(y, 30) if x ** 2 + y ** 2 == z ** 2]
    print(d)


if __name__ == '__main__':
    list_recurrence()
