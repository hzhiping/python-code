#!/usr/bin/env python
# encoding: utf-8
# author: hzhiping
# datetime: 2022/11/12 18:10


def tuple_method():
    # len()函数
    a = (100, 200, 300, 400, 500, 600, 700, 800, 900)
    print(len(a))
    # max()函数返回元组或列表元素中的最大值
    a = (100, 200, 300, 400, 500, 600, 700, 800, 900)
    print(max(a))
    b = ['a', 'c', 'd', 'e', 'f', 'g', 'h', 'o', 'p']
    print(max(b))
    # min()函数返回元组或列表元素中的最小值
    a = (100, 200, 300, 400, 500, 600, 700, 800, 900)
    print(min(a))
    b = ['a', 'c', 'd', 'e', 'f', 'g', 'h', 'o', 'p']
    print(min(b))
    # sum()函数
    a = (100, 200, 300, 400, 500, 600, 700, 800, 900)
    print(sum(a))
    print(type(a))
    print(dir(()))


if __name__ == '__main__':
    tuple_method()
