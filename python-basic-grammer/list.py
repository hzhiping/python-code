#!/usr/bin/env python
# encoding: utf-8
# author: hzhiping
# datetime: 2022/11/12 16:21

def list_test():
    # 定义列表类型的数据结构
    s = [10, 20, 30, 40]
    print(s)
    # 访问列表中的元素
    print(s[0])
    print(s[1])
    # 索引值超出范围，抛出异常
    # print(s[4])
    # 特殊语法，访问列表的最后一个值
    print(s[-1])
    # 特殊语法，访问列表的倒数第二个值
    print(s[-2])


if __name__ == '__main__':
    list_test()
