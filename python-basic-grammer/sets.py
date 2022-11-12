#!/usr/bin/env python
# encoding: utf-8
# author: hzhiping
# datetime: 2022/11/12 16:21
def sets_test():
    # 定义集合类型的数据结构
    fruit = {'香蕉', '苹果', '山竹'}
    print(fruit)
    # 将删除重复的元素
    goods = {'冰箱', '浴巾', '冰箱', '空调', '风扇'}
    print(goods)
    # 定义一个空的集合
    book = set()
    print(book)


if __name__ == '__main__':
    sets_test()
