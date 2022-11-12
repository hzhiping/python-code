#!/usr/bin/env python
# encoding: utf-8
# author: hzhiping
# datetime: 2020/12/4 17:52


# 测试多样赋值语句
def define_variable():
    # 在Python中，变量没有类型，所说的“类型”是指内存中对象的类型
    aa = "刘笑笑"
    bb = False
    cc = "临别亦听得到你讲再见，在有生的瞬间能遇到你"
    # 下面的赋值方式是非法的
    # b = (a = a - 100)
    # if (b = 100)
    # 序列解包
    # 由于赋值运算符的结合性是由右至左，因此在Python语言中，可以一次性给多个变量同时赋值
    x, y, z = 1, 2, '春花秋月何时了'  # 一次性给多个变量同时赋值
    print(x)
    print(y)
    print(z)
    print(x, y, z)
    # 交换赋值
    x, y, z = 1, 2, '春花秋月何时了'  # 一次性给多个变量同时赋值
    x, y = y, x  # x和y的值交换
    print(x, y, z)  # 输出交换后的值
    # 解包序列中的元素数量必须与放置在赋值符号左边的数量完全一致，否则会在赋值时引发异常
    a = 1, 2, '春花秋月何时了'  # 一次性给多个变量同时赋值
    a
    x, y, z = a
    print(x, y, z)
    a = 1, 2, '春花秋月何时了'  # 一次性给多个变量同时赋值
    a
    # x, y = a  # 赋值时少了一个元素
    # x, y, z, h = a  # 赋值时多了一个元素
    # 链式赋值
    a = b = c = "繁华事散逐香尘，流水无情草自春。"  # 为变量连续赋值
    print(a, b, c)
    a = "繁华事散逐香尘，流水无情草自春。"  # 为变量连续赋值
    b = a
    c = a
    print(a, b, c)
    # 其他赋值方式
    a = 100
    a += 20  # 复合赋值运算符
    print(a)
    # 其他赋值方式
    a = 100
    b = 200
    c = a * 2 + b
    d = a + b + c
    print(d)
    # 其他赋值方式
    a = 100  # 初始化变量a
    print(a)
    b = c = 700 / 200
    # 为变量连续赋值
    print(b, c)
    a, b = 100, 150
    c = a * 3 + b
    d = a + b + c  # 赋值号右边也可以是表达式
    print(d)
    a = 100
    a += 40  # 复合赋值运算符
    print(a)
    # 同一变量名在不同阶段可以存储不同类型的数据
    a = 3
    print(a)
    a = '迢迢牵牛星，皎皎河汉女。'
    print(a)
    a = 10.88
    print(a)
    # 其他赋值方式
    a = 100
    a += 20
    print(a)
    # 等号右边是表达式
    a = 100
    b = 200
    c = a * 2 + b
    d = a + b + c
    print(d)
    # 赋值的综合案例
    a = 100  # 初始化变量a
    print(a)
    b = c = 700 / 200  # 为变量连续赋值
    print(b, c)
    a, b = 100, 150
    c = a * 3 + b
    d = a + b + c  # 赋值号右边也可以是表达式
    print(d)
    a = 100
    a += 40  # 复合赋值运算符
    print(a)


if __name__ == "__main__":
    define_variable()
