#!/usr/bin/env python
# encoding: utf-8
# author: hzhiping
# datetime: 2020/12/4 16:58


def string_method():
    # capitalize()方法将字符串的第一个字符转化为大写，其他字符转化为小写
    str = "i can fly"
    tt = str.capitalize() + "：我能飞"
    print(tt)
    # 如果字符串的首字符不是字母，那么该字符串中的第一个字符不会转换为大写，而转换为小写
    str = "123 I can because I think I can"
    print(str.capitalize())
    str = "@ I can because I think I can"
    print(str.capitalize())
    # count()方法用于统计字符串里某个字符出现的次数，可选参数为在字符串搜索的开始与结束位置
    str = "The best preparation for tomorrow is doing your best today"
    s = 'b'
    print("字符b出现的次数为：", str.count(s))
    s = 'best'
    print("best出现的次数为：", str.count(s, 0, 6))
    print("best出现的次数为：", str.count(s, 0, 40))
    print("best出现的次数为：", str.count(s, 0, 80))
    # find()方法检测字符串中是否包含子字符串。如果包含子字符串，就返回开始的索引值；否则就返回-1
    str1 = "青海长云暗雪山，孤城遥望玉门关。"
    str2 = "玉门"
    print(str1.find(str2))
    print(str1.find(str2, 10))
    print(str1.find(str2, 13, 15))
    # index()方法检测字符串中是否包含子字符串。如果包含子字符串，就返回开始的索引值，否则就会报一个异常
    str1 = "青海长云暗雪山，孤城遥望玉门关。"
    str2 = "玉门"
    print(str1.index(str2))
    print(str1.index(str2, 10))
    # print(str1.index(str2, 13, 15))
    # isalnum()方法检测字符串是否由字母和数字组成
    str1 = "whateverisworthdoingisworthdoingwell"  # 字符串没有空格print(str1.isalnum())
    print(str1.isalnum())
    str1 = "Whatever is worth doing is worth doing well"  # 这里添加了空格print (str1.isalnum())
    print(str1.isalnum())
    # join()方法用于将序列中的元素以指定的字符连接生成一个新的字符串
    s1 = ""
    s2 = "*"
    s3 = "#"
    # 字符串序列
    e1 = ("黄", "沙", "百", "战", "穿", "金", "甲")
    e2 = ("不", "破", "楼", "兰", "终", "不", "还")
    print(s1.join(e1))
    print(s2.join(e2))
    print(s3.join(e2))
    # isalpha()方法检测字符串是否只由字母或汉字组成
    s1 = "Believe相信"
    print(s1.isalpha())
    s1 = "大漠风尘日色昏，红旗半卷出辕门。"
    print(s1.isalpha())
    # isdigit()方法检测字符串是否只由数字组成
    s1 = "123456789"
    print(s1.isdigit())
    s1 = "Believe123456789"
    print(s1.isdigit())
    # low ()方法将字符串中的所有大写字符转化为小写字符
    s1 = "HAPPINESS"
    print('使用low()方法后的效果：', s1.lower())
    s2 = "Happiness"
    print('使用low()方法后的效果：', s2.lower())
    # 在一个字符串中查找某个子字符串并忽略大小写
    s1 = "HAPPINESS"
    s2 = "Ss"
    print(s1.find(s2))  # 都不转化为小写，找不到匹配的字符串
    print(s1.lower().find(s2))  # 被查找字符串转化为小写，找不到匹配的字符串
    print(s1.lower().find(s2.lower()))  # 全部转化为小写，找到匹配的字符串
    # max()方法返回字符串中的最大值
    s1 = "abcdefgh"
    print(max(s1))
    s2 = "abcdefghABCDEFGH"
    print(max(s2))
    # min()方法返回字符串中的最小值
    s1 = "abcdefgh"
    print(min(s1))
    s2 = "abcdefghABCDEFGH"
    print(min(s2))
    # replace()方法用于把字符串中的旧字符串替换为新字符串
    s1 = "最近采购货物为冰箱"
    print(s1.replace("冰箱", "洗衣机"))
    s1 = "一片两片三四片五片六片七八片九片十片片片飞飞入芦花皆不见"
    print(s1.replace("片", "页", 1))
    print(s1.replace("片", "页", 2))
    print(s1.replace("片", "页", 10))
    print(s1.replace("片", "页"))
    # swapcase()方法用于对字符串的大小写字母进行转换，即将字符串中小写字母转换为大写、大写字母转为小写
    s1 = "Happiness is a way station between too much and too little"
    print('原始的字符串：', s1)
    print('转换后的字符串：', s1.swapcase())
    # title()方法返回“标题化”的字符串，即所有单词都以大写开始，其余字母均为小写
    s1 = "Happiness is a way station between too much and too little"
    print('原始的字符串：', s1)
    print('转换后的字符串：', s1.title())


if __name__ == "__main__":
    string_method()
