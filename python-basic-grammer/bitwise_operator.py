#!/usr/bin/env python
# encoding: utf-8
# author: hzhiping
# datetime: 2022/11/12 16:48

def bitwise_operator():
    a = 12  # 12=0000 1100
    b = 6  # 6=0000 0110
    c = 0
    # 按位与运算
    c = a & b  # 4=0000 0100
    print("c的值为：", c)
    # 按位或运算
    c = a | b  # 14=0000 1110
    # print("c的值为:"，c)
    # 按位异或运算
    c = a ^ b  # 10=0000 1010
    print("c的值为：", c)
    # 按位取反运算
    c = ~a  # -13=1000 1101
    print("c的值为：", c)
    # 左移动运算
    c = a << 2  # 48=0011 0000
    print("c的值为：", c)
    # 右移动运算
    c = a >> 2  # 3=0000 0011
    print("c的值为：", c)


if __name__ == '__main__':
    bitwise_operator()
