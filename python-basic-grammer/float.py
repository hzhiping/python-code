#!/usr/bin/env python
# encoding: utf-8
# author: hzhiping
# datetime: 2022/11/12 15:29

def float_test():
    a = 3.14
    b = 10.
    c = .001
    d = 1e100
    e = 3.14E-10
    f = 1e010
    g = 08.1
    print(a, b, c, d, e, f, g)
    # 将数值转换成浮点型
    h = float(150)
    print(h)


if __name__ == '__main__':
    float_test()
