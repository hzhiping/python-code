#!/usr/bin/env python
# encoding: utf-8
# author: hzhiping
# datetime: 2020/12/4 16:25


def string_operator():
    # 加号（+）运算符可以将两个字符串连接起来
    a = "梨花风起正清明，" + "游子寻春半出城。"
    print(a)
    # 乘号（*）运算符可以将一个字符串的内容复制数次
    a = "万株杨柳属流莺" * 4
    print(a)
    # 使用大于（>）、等于（==）和小于（<）逻辑运算符比较两个字符串的大小
    a = "hello"
    b = "world"
    print(a > b)
    print(a == b)
    print(a < b)
    # 使用in或not in运算符测试某个字符是否存在于字符串内
    a = "h"
    b = "hello"
    print(a in b)
    print(a not in b)


def example():
    a = "客从远方来，"
    b = "遗我一端绮。"
    print("a + b输出结果:", a + b)
    print("a * 2输出结果:", a * 2)
    print("a[1]输出结果:", a[1])
    print("a[1:4]输出结果:", a[1:4])  # 使用in关键词
    if "远方" in a:
        print("远方在变量a中")
    else:
        print("远方不在变量a中")  # 使用not in关键词
    if "外客" not in b:
        print("外客不在变量b中")
    else:
        print("外客在变量b中")


if __name__ == "__main__":
    string_operator()
    example()
