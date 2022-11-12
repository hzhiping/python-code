#!/usr/bin/env python
# encoding: utf-8
# author: hzhiping
# datetime: 2022/11/12 16:45

def assigning_operator():
    a = 24
    b = 8
    c = 6
    # 简单的赋值运算
    c = a + b
    print("c的值为:", c)
    # 加法赋值运算
    c += a
    print("c的值为:", c)
    # 乘法赋值运算
    c *= a
    print("c的值为:", c)
    # 除法赋值运算
    c /= a
    print("c的值为:", c)
    # 取模赋值运算
    c = 12
    c %= a
    print("c的值为:", c)
    # 幂赋值运算
    a = 3
    c **= a
    print("c的值为:", c)
    # 取整除赋值运算
    c //= a
    print("c的值为:", c)


if __name__ == '__main__':
    assigning_operator()
