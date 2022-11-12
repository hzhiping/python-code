#!/usr/bin/env python
# encoding: utf-8
# author: hzhiping
# datetime: 2020/12/4 16:43


def string_format():
    # 字符串格式化使用字符串操作符百分号（%）来实现
    a = "目前市场上%s的价格为每公斤%d元。"
    b = ('苹果', 20)
    c = a % b
    print(c)
    # 若格式化浮点数，则可以提供所需要的精度
    a = "今天的苹果的售价为每公斤%.2f元。"
    b = 20.16
    c = a % b
    print(c)
    # 不指定精度
    a = "今天的苹果的售价为每公斤%f元。"
    b = 20.16
    c = a % b
    print(c)
    # 如果要在格式化字符串中包含百分号，就必须使用%%
    a = "今年苹果的销售额比去年提升了：%.2f%%"
    b = 20.16
    c = a % b
    print(c)
    # 还有一种方式也可以实现上述结果
    a = "今年苹果的销售额比去年提升了：%.2f"
    b = 20.16
    c = a % b
    print(c + "%")


if __name__ == "__main__":
    string_format()
