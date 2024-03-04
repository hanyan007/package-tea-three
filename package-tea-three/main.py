#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : main.py
# @Author: hanyan_news
# @Desc  :

import itertools


case_lists = ['username', 'password']
value_lists = ['correct', 'incorrect', 'specific symbol', 'maximum length']


def gen_case(item=case_lists, value=value_lists):
    '''输出笛卡尔用例集合'''
    for i in itertools.product(item, value):
        print('输入'.join(i))

def test_print():
	print("hello world!")

if __name__ == '__main__':
    # test_print()
    gen_case(）