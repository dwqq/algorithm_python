#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------
# @Author: dwqq
# @Date  : 2020/12/4 18:15 
# @File  : traversal_BTree.py
# @IDE   : PyCharm
# -------------------------------


class TreeNode(object):
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BTree(object):
    def __init__(self):
        self.res = []

    def pre_order_traversal(self, root):
        """
        前序遍历
        :param root: treeNode
        :return: list
        """
        if root:
            self.res.append(root.data)
            self.pre_order_traversal(root.left)
            self.pre_order_traversal(root.right)
        return self.res

    def in_order_traversal(self, root):
        """中序遍历"""
        if root:
            self.in_order_traversal(root.left)
            self.res.append(root.data)
            self.in_order_traversal(root.right)
        return self.res

    def post_order_traversal(self, root):
        """后序遍历"""
        if root:
            self.post_order_traversal(root.left)
            self.post_order_traversal(root.right)
            self.res.append(root.data)
        return self.res

    def bfs(self, root):
        """广度优先遍历，层次遍历"""
        queue = [root]
        while queue:
            cur = queue.pop(0)
            self.res.append(cur.data)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return self.res


if __name__ == '__main__':
    node_list = [1, 'null', 2, 3]
    t2 = TreeNode(2)
    t2.left = TreeNode(3)
    t = TreeNode(1)
    t.right = t2

    print(BTree().pre_order_traversal(t))
    print(BTree().in_order_traversal(t))
    print(BTree().post_order_traversal(t))

    print(BTree().bfs(t))
