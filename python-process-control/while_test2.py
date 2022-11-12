#!/usr/bin/env python
# encoding: utf-8
# author: hzhiping
# datetime: 2022/11/12 20:57


def while_test():
    aa = "商品"
    while aa == "商品":  # 表达式永远为True
        name = str(input("请输入需要采购商品的名称: "))
        print("你输入的商品名称是:", name)
    print("商品采购完毕! ")


if __name__ == '__main__':
    while_test()
