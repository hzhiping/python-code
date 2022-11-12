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


if __name__ == '__main__':
    list_recurrence()
