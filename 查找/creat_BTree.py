#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------
# @Author: dwqq
# @Date  : 2020/12/4 16:11 
# @File  : creat_BTree.py
# @IDE   : PyCharm
# -------------------------------


class TreeNode(object):
    """
    树节点
    """
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BTree(object):
    def __init__(self, root=None):
        self.root = root

    def is_empty(self):
        return self.root is None

    def create(self, input_list):
        tree = [0]
        node_list = [0] + input_list
        num = 1
        for item in node_list:
            temp = TreeNode(item)
            tree.append(temp)
        for item in tree:
            if item.data == 'null':
                continue
            if 2*num <= len(node_list) and tree[2*num].data != 'null':
                item.left = tree[2*num]
            if 2*num+1 <= len(node_list) and tree[2*num+1].data != 'null':
                item.right = tree[2*num+1]
            num += 1

