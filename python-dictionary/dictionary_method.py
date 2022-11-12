#!/usr/bin/env python
# encoding: utf-8
# author: hzhiping
# datetime: 2022/11/12 18:19

def dictionary_method():
    # len(dict)：计算字典元素个数，即键值的总数
    a = {"名称": "冰箱", "产地": "北京", "价格": "6500"}
    print(len(a))
    # str(dict)：将字典的元素转化为可打印的字符串形式
    a = {"名称": "冰箱", "产地": "北京", "价格": "6500"}
    print(str(a))
    # type(variable)：返回输入的变量类型，如果变量是字典，就返回字典类型
    a = {"名称": "冰箱", "产地": "北京", "价格": "6500"}
    print(type(a))
    # 字典对象有许多内置方法，在Python解释器内输入dir({})，就可以显示这些内置方法的名称
    print(dir({}))
    # clear()：清除字典中的所有元素
    a = {"名称": "冰箱", "产地": "北京", "价格": "6500"}
    a.clear()
    print(a)
    # copy()：复制字典
    a = {"名称": "冰箱", "产地": "北京", "价格": "6500"}
    b = a.copy()
    print(b)
    # get(k[, d])：k是字典的索引值，d是索引值的默认值。如果k存在，就返回其值，否则返回d
    a = {"名称": "冰箱", "产地": "北京", "价格": "6500"}
    print(a.get("名称"))
    print(a.get("品牌", "不存在"))
    # items()：使用字典中的元素创建一个由元组对象组成的列表
    a = {"名称": "冰箱", "产地": "北京", "价格": "6500"}
    print(a.items())
    # keys()：使用字典中的键值创建一个列表对象
    a = {"名称": "冰箱", "产地": "北京", "价格": "6500"}
    print(a.keys())
    # popitem()：删除字典中的最后一个元素
    a = {"名称": "冰箱", "产地": "北京", "价格": "6500"}
    a.popitem()
    print(a)
    # setdefault(k [, d])：k是字典的键值，d是键值的默认值。如果k存在，就返回其值；否则返回d，并将新的元素添加到字典中
    a = {"名称": "冰箱", "产地": "北京", "价格": "6500"}
    a.setdefault("名称")
    print(a.setdefault("名称"))
    print(a)
    a.setdefault("品牌", "海尔")
    print(a)
    # update(E)：E是字典对象，由字典对象E来更新此字典
    a = {"名称": "冰箱", "产地": "北京", "价格": "6500"}
    a.update({"品牌": "海尔"})
    print(a)
    # values()：使用字典中键值的数值创建一个列表对象
    a = {"名称": "冰箱", "产地": "北京", "价格": "6500"}
    print(a.values())


if __name__ == '__main__':
    dictionary_method()
