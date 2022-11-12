#!/usr/bin/env python
# encoding: utf-8
# author: hzhiping
# datetime: 2022/11/12 21:02


def continue_test():
    aa = 0
    while aa < 100:
        aa = aa + 10
        if aa == 80:
            continue
        print(aa, "小于或等于100")


if __name__ == '__main__':
    continue_test()
