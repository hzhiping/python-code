#!/usr/bin/env python
# encoding: utf-8
# author: hzhiping
# datetime: 2022/11/12 18:10


def tuple_operator():
    # 如果创建的元组对象只有一个元素，就必须在元素之后加上逗号（,）
    # 创建只有一个元素的元组
    a = (100,)
    print(a)
    a = (100)
    print(a)
    # 在元组中，不可以修改元组对象内的元素值
    a = (100, 200, 300, 400)
    # 以下修改元组元素操作是非法的
    # a[1] = 100
    print(a)
    # 虽然元组内的元素值不能修改，但是可以删除，从而达到更新元组对象的效果
    a = (100, 200, 300, 400)
    a = a[0], a[2], a[3]
    print(a)
    # 元组对象支持使用索引值的方式来返回元素值
    a = (100, 200, 300, 400)
    print(a[0])
    print(a[1])
    print(a[2])
    print(a[3])
    # 组合元组
    a = (100, 200)
    b = ("河汉清且浅", "相去复几许")
    c = a + b
    print(c)
    # 删除整个元组
    d = (100, 200, 300, 400)
    print(d)
    del d
    # print(d)


if __name__ == '__main__':
    tuple_operator()
