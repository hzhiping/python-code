#!/usr/bin/env python
# encoding: utf-8
# author: hzhiping
# datetime: 2022/11/12 21:00


def for_test():
    fruit = ["苹果", "葡萄", "橘子", "香蕉", "西瓜", "芒果"]
    for f in fruit:
        if f == "西瓜":
            print("水果中包含西瓜")
            break
        print(f)
    else:
        print("没有发现需要的水果！")
    print("水果搜索完毕！")


if __name__ == '__main__':
    for_test()
