#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------
# @Author: dwqq
# @Date  : 2021/2/1 9:52 
# @File  : 有效的括号.py
# @IDE   : PyCharm
# -------------------------------


def isValid(s):
    """
    判断括号是否有效合法
    :param s: 各种括号组成的字符串
    :return:
    """
    if len(s) % 2 != 0:
        return False

    s_dict = {')': '(',
              ']': '[',
              '}': '{'}
    stack = []
    for each_s in s:
        if each_s in s_dict:
            if stack[-1] != s_dict[each_s] or not stack:
                return False
            stack.pop()
        else:
            stack.append(each_s)
    
    return not stack


if __name__ == '__main__':
    print(isValid('(){}[]'))
    print(isValid('({[]})'))
    print(isValid('([)'))