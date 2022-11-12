#!/usr/bin/env python
# encoding: utf-8
# author: hzhiping
# datetime: 2022/11/12 16:50

def priority():
    a = 10
    b = 6
    c = 4
    d = 2
    e = (a + b) * c / d  # (16 * 4) / 2
    print("(a + b) * c / d 运算结果为：", e)
    e = ((a + b) * c) / d  # (16 * 4 ) / 2
    print("((a + b) * c) / d 运算结果为：", e)
    e = (a + b) * (c / d)  # (16) * (4 / 2)
    print("(a + b) * (c / d) 运算结果为：", e)
    e = a + (b * c) / d  # 10 + (24 / 2)
    print("a + (b * c) / d 运算结果为：", e)


if __name__ == '__main__':
    priority()
