#!/usr/bin/env python
# encoding: utf-8
# author: hzhiping
# datetime: 2022/11/12 15:35

def complex_test():
    a = 1.5 + 0.5j
    b = 1J
    c = 2 + 1e100j
    d = 3.14e-10j
    print(a, b, c, d)
    # 可以使用real和imag分别取出复数的实数和虚数部分
    print(a.real)
    print(a.imag)
    # 可以使用complex将实数和虚数装换成复数
    print(complex(1.5, 2))


if __name__ == '__main__':
    complex_test()
