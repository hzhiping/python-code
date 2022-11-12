#!/usr/bin/env python
# encoding: utf-8
# author: hzhiping
# datetime: 2022/11/12 20:55


def if_test():
    num = int(input("输入一个数字:"))
    if num % 2 == 0:
        if num % 3 == 0:
            print("你输入的数字可以整除2和3")
        else:
            print("你输入的数字可以整除2，但不能整除3")
    else:
        if num % 3 == 0:
            print("你输入的数字可以整除3，但不能整除2")
        else:
            print("你输入的数字不能整除2和3")


if __name__ == '__main__':
    if_test()
