#!/usr/bin/env python
# encoding: utf-8
# author: hzhiping
# datetime: 2022/11/12 17:11

def list_feature():
    # 定义列表
    a = ['泠泠七弦上，', '静听松风寒。', '古调虽自爱，', '今人多不弹。']
    print(a)
    # 列表对象中的元素可以是不同的类型
    b = [12, "何当共剪西窗烛", 1.66, 5 + 3j]
    print(b)
    # 列表对象中的元素可以是另一个列表
    c = [12, "何当共剪西窗烛", 1.66, ["一夕轻雷落万丝", "霁光浮瓦碧参差", 3.66]]
    # 读取列表
    print(c[3])
    # 读取列表对象中嵌套的另一个列表
    print(c[3][1])
    # 判断一个元素是否存在于列表中
    print(1 in [1, 2, 3])


if __name__ == '__main__':
    list_feature()
