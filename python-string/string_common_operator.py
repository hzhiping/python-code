#!/usr/bin/env python
# encoding: utf-8
# author: hzhiping
# datetime: 2022/11/12 19:24


def string_common_operation():
    # 与列表的索引一样，字符串索引从0开始
    a = "Believe in yourself"
    print(a[0])
    b = "迟日江山丽，春风花草香。"
    print(b[1])
    # 字符串的索引值可以为负值。若索引值为负数，则表示由字符串的结尾向前数。
    a = "Believe in yourself"
    print(a[-1])
    b = "迟日江山丽，春风花草香。"
    print(b[-2])
    # 使用冒号（:）来分割指定范围的字符
    a = "Believe in yourself"
    print(a[0:6])
    b = "迟日江山丽，春风花草香。"
    print(b[1:4])
    # 如果省略开始索引值，分割字符串就由第一个字符到结尾索引值
    a = "Believe in yourself"
    print(a[:10])
    b = "迟日江山丽，春风花草香。"
    print(b[:10])
    # 如果省略结尾索引值，分割字符串就由开始索引对应的字符到最后一个字符
    a = "Believe in yourself"
    print(a[0:])
    b = "迟日江山丽，春风花草香。"
    print(b[1:])
    # 更新字符串
    a = "Believe in yourself"
    # 默认情况下，字符串被设置后就不可以直接修改，一旦直接修改字符串中的字符，就会弹出错误信息
    # a[1] = "w"
    # 如果一定要修改字符串，可以使用访问字符串值的方法进行更新操作
    a = "迟日江山丽，春春花草香。"
    a = a[:7] + "风" + a[8:]
    print(a)
    # 换行符使用
    a = "泥融飞燕子\n沙暖睡鸳鸯"
    print(a)
    # 双引号（\"）
    a = "对别人的意见要表示尊重。千万别说：\"你错了。\""
    print(a)
    # 各进制的ASCII码
    a = "\x48"
    print(a)
    a = "\103"
    print(a)
    # 加入反斜杠字符
    # 如果需要在字符串内加上反斜杠字符，就必须在字符串的引号前面加上"r"或"R"字符
    print(r"\d")
    print(R"\e,\f,\e")


if __name__ == "__main__":
    string_common_operation()
