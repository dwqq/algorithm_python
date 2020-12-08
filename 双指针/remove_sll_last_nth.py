#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------
# @Author: dwqq
# @Date  : 2020/12/7 15:40 
# @File  : remove_sll_last_nth.py
# @IDE   : PyCharm
# -------------------------------


class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkList(object):
    def __init__(self):
        self._head = None

    def length(self):
        """单链表长度"""
        count = 0
        cur = self._head
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def append(self, item):
        """单链表尾部添加元素"""
        node = Node(item)
        if self._head is None:
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def remove_last_nth(self, n):
        """删除倒数第n个元素"""
        len_sll = self.length()
        index_n = len_sll - n
        cur = self._head
        pre = None
        if n <= 0 or n > len_sll:
            print('元素超出链表范围')
            return False
        elif index_n == 0:
            self._head = cur.next
        else:
            for _ in range(index_n):
                pre = cur
                cur = cur.next
            pre.next = cur.next

    def items(self):
        """遍历链表"""
        cur = self._head
        res = []
        while cur is not None:
            res.append(cur.item)
            cur = cur.next
        return res


if __name__ == '__main__':
    sll = SingleLinkList()
    for i in range(6):
        sll.append(i)
    print(sll.items())
    sll.remove_last_nth(4)
    print(sll.items())