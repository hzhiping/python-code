#!/usr/bin/env python
# encoding: utf-8
# author: hzhiping
# datetime: 2022/11/12 16:49

def identity_operator():
    a = '风扇'
    b = '冷风扇'
    # 使用is身份运算符
    if a is b:
        print("a和b有相同的标识")
    else:
        print("a和b没有相同的标识")
    # 使用not in身份运算符
    if a is not b:
        print("a和b没有相同的标识")
    else:
        print("a和b有相同的标识")
    # 修改变量a的值
    a = '冷风扇'
    if a is b:
        print("修改后的a和b有相同的标识")
    else:
        print("修改后的a和b仍然没有相同的标识")


if __name__ == '__main__':
    identity_operator()
