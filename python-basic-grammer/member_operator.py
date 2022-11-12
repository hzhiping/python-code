#!/usr/bin/env python
# encoding: utf-8
# author: hzhiping
# datetime: 2022/11/12 16:48

def member_operator():
    a = '洗衣机'
    b = '风扇'
    goods = ['电视机', '空调', '洗衣机', '冰箱', '电脑']
    # 使用in成员运算符
    if a in goods:
        print("变量a在给定的列表goods中")
    else:
        print("变量a不在给定的列表goods中")
    # 使用not in成员运算符
    if b not in goods:
        print("变量b不在给定的列表goods中")
    else:
        print("变量b在给定的列表goods中")
    # 修改变量a的值
    a = '冷风扇'
    if a in goods:
        print("变量a在给定的列表goods中")
    else:
        print("变量a不在给定的列表goods中")


if __name__ == '__main__':
    member_operator()
