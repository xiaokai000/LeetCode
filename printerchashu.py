'''
从上往下打印出二叉树的每个节点，同层节点从左至右打印。

'''


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right



root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, TreeNode(1), TreeNode(7)))


nodes = [root]

def asd(root):
    if not root:
        return

    if root.left:
        nodes.append(root.left)

    if root.right:
        nodes.append(root.right)

    asd(root.left)
    asd(root.right)

asd(root)
print([node.val for node in nodes])