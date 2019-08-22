'''
请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。

因为我们无法访问我们想要删除的节点之前的节点，我们始终不能修改该节点的 next 指针。
相反，我们必须将想要删除的节点的值替换为它后面节点中的值，然后删除它之后的节点。
'''



class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next