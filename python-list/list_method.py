#!/usr/bin/env python
# encoding: utf-8
# author: hzhiping
# datetime: 2022/11/12 17:56

def list_method():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # len()函数返回列表的长度
    print(len(a))
    # max()函数返回列表元素中的最大值
    print(max(a))
    # a = [100, 200, 300, 400, 'qq']
    # print(max(a))
    # min()函数返回列表元素中的最小值
    print(min(a))
    # dir([])显示这些内置的列表方法
    print(dir([]))
    # append()方法在列表对象的结尾，加上新对象object
    b = [100, 200, 300, 400]
    b.append(500)
    print(b)
    b.append([600, 700])
    print(b)
    # clear()函数用于清空列表
    b = [100, 200, 300, 400]
    b.clear()
    print(b)
    # copy()函数用于复制列表
    a = ['香蕉', '柚子', 1.25, 3]
    b = a.copy()
    print(b)
    # count(value)方法针对列表对象中的相同元素值value计算其数目
    a = [100, 133, 166, 188, 166, 266]
    print(a.count(166))
    # extend(list)方法将参数list列表对象中的元素加到此列表中
    a = [100, 200, 300, 400]
    a.extend([500, 600, 700, 800])
    print(a)
    # index(value)方法将列表对象中元素值为value的索引值返回
    a = [100, 200, 300, 400, 500, 600, 700, 800]
    print(a.index(800))
    # insert(index, object)方法将在列表对象中索引值为index的元素之前插入新元素object
    a = [100, 200, 300, 400, 500, 600, 700, 800]
    a.insert(1, "新元素")
    print(a)
    # pop([index])方法将列表对象中索引值为index的元素删除。如果没有指定index的值，就将最后一个元素删除
    a = [100, 200, 300, [400, 500, 600]]
    a.pop(1)
    print(a)
    a.pop()
    print(a)
    # remove(value)方法将列表对象中元素值为value的删除
    a = [100, 200, 300, 400]
    a.remove(300)
    print(a)
    # reverse()方法将列表对象中的元素颠倒排列
    a = [100, 200, 300, 400]
    a.reverse()
    print(a)
    # sort()方法将列表对象中的元素依照大小顺序排列
    a = [100, 600, 800, 400, 500, 200, 300, 700]
    a.sort()
    print(a)


if __name__ == '__main__':
    list_method()
