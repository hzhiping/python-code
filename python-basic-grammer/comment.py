#!/usr/bin/env python
# encoding: utf-8
# author: hzhiping
# datetime: 2022/11/12 13:05

def comment():
    # 单行注释使用“#”
    print("hello world")
    '''
    这是一个单引号的多行注释
    这是一个单引号的多行注释
    这是一个单引号的多行注释
    '''
    print("hello china")
    """
    这是一个双引号的多行注释
    这是一个双引号的多行注释
    这是一个双引号的多行注释
    """
    print("hello python")


if __name__ == '__main__':
    comment()
