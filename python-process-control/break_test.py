#!/usr/bin/env python
# encoding: utf-8
# author: hzhiping
# datetime: 2022/11/12 21:02


def break_test():
    a = "盈盈一水间，脉脉不得语"
    for b in a:
        if b == "不":
            print("当前的文字是：", b)
            break
        else:
            print("没有发现对应的文字")


if __name__ == '__main__':
    break_test()
