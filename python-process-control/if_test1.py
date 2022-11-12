#!/usr/bin/env python
# encoding: utf-8
# author: hzhiping
# datetime: 2022/11/12 20:42

def if_test():
    a = int(input("请输入第1个数："))
    b = int(input("请输入第2个数："))
    print("")
    if a <= b:
        print("它们的差值：", b - a)
    elif a > b:
        print("它们的差值：", a - b)


if __name__ == '__main__':
    if_test()
