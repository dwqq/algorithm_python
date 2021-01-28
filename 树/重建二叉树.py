#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------
# @Author: dwqq
# @Date  : 2021/1/28 14:52 
# @File  : 重建二叉树.py
# @IDE   : PyCharm
# -------------------------------


class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def reConstructBinaryTree(pre, tin):
    """
    根据前序遍历序列和中序遍历序列重建二叉树
    :param pre:
    :param tin:
    :return:
    """
    if not pre:
        return None
    root_val = pre[0]
    root = TreeNode(root_val)
    for i in range(len(tin)):
        if tin[i] == root_val:
            break
    root.left = reConstructBinaryTree(pre[1:1+i], tin[:i])
    root.right = reConstructBinaryTree(pre[1+i:], tin[1+i:])
    return root


def preorder(root):
    if root:
        preorder(root.left)
        print(root.data)
        preorder(root.right)


if __name__ == '__main__':
    test = reConstructBinaryTree([3, 9, 2, 1, 7], [9, 3, 1, 2, 7])
    preorder(test)
