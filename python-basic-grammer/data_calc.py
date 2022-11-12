#!/usr/bin/env python
# encoding: utf-8
# author: hzhiping
# datetime: 2022/11/12 16:05

def data_calc():
    print(50 + 40)
    print(50 - 40)
    print(3 * 5)
    print(3 / 5)
    print(3 // 5)
    print(15 % 2)
    print(2 ** 6)
    # 用户可以将数值使用在函数内
    print(round(12.32, 1))
    print(round(12.35, 1))
    print(round(12.36, 1))
    # 00010000->01000000
    print(16 << 2)
    # 00010000->00000100
    print(16 >> 2)
    # 0x1B->1*(16^1) + 11*(16^0)
    print(0x1B)
    print(0x12fd2)
    '''
    30/2  15  0
    15/2  7   1
    7/2   3   1
    3/2   1   1
    1/2   0   1
    011110->不足在左边补0
        ↓
    00011110
    0x1B
        ↓
    00011011
        ↓
    00011110
    00011011
    两者相与，1&1=1，1&0=0
        ↓
    00011010->转换成十进制为26
    '''
    print(30 & 0x1B)
    '''
    010
    101
    111->转换成十进制为7
    '''
    print(2 | 5)
    '''
    在python中^表示异或：当两对应的二进位相异时，结果为1
    011
    101
     ↓
    110->转换成十进制为6
    '''
    print(3 ^ 5)
    '''
    在python中~表示按位取反，对数据的每个二进制位取反，即把1变为0，把0变为1。
    '''
    print(~2)


if __name__ == '__main__':
    data_calc()
