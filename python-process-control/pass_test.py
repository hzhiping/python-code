#!/usr/bin/env python
# encoding: utf-8
# author: hzhiping
# datetime: 2022/11/12 21:03


def pass_test():
    for a in "江南可采莲，莲叶何田田，鱼戏莲叶间":
        if a == "鱼":
            pass
            print("执行pass语句")
        print("当前的文字：", a)
    print("搜素完毕！")


if __name__ == '__main__':
    pass_test()
