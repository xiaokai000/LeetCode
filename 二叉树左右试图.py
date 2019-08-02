# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        que = [root]
        if root == None:
            return res
        while que:
            tempList = []
            for i in range(len(que)):
                node = que.pop(0)
                tempList.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(tempList)
        result = []
        for r in res:
            result.append(r[-1])
        return result

