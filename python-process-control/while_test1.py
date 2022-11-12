#!/usr/bin/env python
# encoding: utf-8
# author: hzhiping
# datetime: 2022/11/12 20:57


def while_test():
    a = 20
    summary = 0
    b = 1
    while b <= a:
        summary = summary + b
        b += 1
    print("1到%d之和为：%d" % (a, summary))


if __name__ == '__main__':
    while_test()
