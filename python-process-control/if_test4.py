#!/usr/bin/env python
# encoding: utf-8
# author: hzhiping
# datetime: 2022/11/12 20:56


def if_test():
    a = int(input("请输入三角形的第一条边:"))
    b = int(input("请输入三角形的第二条边:"))
    c = int(input("请输入三角形的第三条边:"))
    print("")
    if a == b and a == c:
        print("等边三角形")
    elif a == b or a == c or b == c:
        print("等腰三角形")
    elif a == b or a == c or b == c:
        print("等腰三角形")
    elif a * a + b * b == c * c or a * a + c * c == b * b or c * c + b * b == a * a:
        print("直角三角形")
    else:
        print("一般三角形")


if __name__ == '__main__':
    if_test()
