#!/usr/bin/env python
# encoding: utf-8
# author: hzhiping
# datetime: 2022/11/12 16:45

def compare_operator():
    a = 16
    b = 4
    # 判断变量a和b是否相等
    if a == b:
        print("a等于b")
    else:
        print("a不等于b")
    # 判断变量a和b是否不相等
    if a != b:
        print("a不等于b")
    else:
        print("a等于b")
    # 判断变量a是否小于b
    if a < b:
        print("a小于b")
    else:
        print("a大于等于b")
    # 判断变量a是否大于b
    if a > b:
        print("a大于b")
    else:
        print("a小于等于b")
    # 修改变量a和b的值
    a = 15
    b = 32
    # 判断变量a是否小于等于b
    if a <= b:
        print("a小于等于b")
    else:
        print("a大于b")
    # 判断变量b是否大于等于a
    if b >= a:
        print("b大于等于a")
    else:
        print("b小于a")


if __name__ == '__main__':
    compare_operator()
