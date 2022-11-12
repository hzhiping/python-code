#!/usr/bin/env python
# encoding: utf-8
# author: hzhiping
# datetime: 2022/11/12 20:59


def while_test():
    a = 1
    while a < 20:
        print(a, "小于20")
        a = a + 1
    else:
        print(a, "大于或等于20")


if __name__ == '__main__':
    while_test()
