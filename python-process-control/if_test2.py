#!/usr/bin/env python
# encoding: utf-8
# author: hzhiping
# datetime: 2022/11/12 20:43

def if_test():
    sc = int(input("请输入考试分数:"))
    print("")
    if sc < 60:
        print("成绩不及格")
    elif 60 <= sc <= 70:
        print("成绩及格")
    elif 70 < sc <= 80:
        print("成绩良好")
    elif 80 < sc:
        print("成绩优秀")
    input("按Enter键退出")


if __name__ == '__main__':
    if_test()
