#!/usr/bin/env python
# encoding: utf-8
# author: hzhiping
# datetime: 2022/11/12 16:46


def logical_operator():
    a = 10
    b = 20
    # 布尔‘与’运算
    if a and b:
        print("变量a和b都为true")
    else:
        print("变量a和b有一个不为true")
    # 布尔‘或’运算
    if a or b:
        print("变量a和b都为true，或其中一个变量为true")
    else:
        print("变量a和b都不为true")
    # 修改变量a的值
    a = 0
    if a and b:
        print("变量a和b都为true")
    else:
        print("变量a和b有一个不为true")
    if a or b:
        print("变量a和b都为true，或其中一个变量为true")
    else:
        print("变量a和b都不为true")
    # 布尔‘非’运算
    if not (a and b):
        print("变量a和b都为false，或其中一个变量为false")
    else:
        print("变量a和b都为true")


if __name__ == '__main__':
    logical_operator()
