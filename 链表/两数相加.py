# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    s1 = ''
    s2 = ''
    while l1:
        v1 = l1.val
        s1 += str(v1)
        l1 = l1.next

    while l2:
        v2 = l2.val
        s2 += str(v2)
        l2 = l2.next

    s1 = s1[::-1]
    s2 = s2[::-1]

    num = int(s1) + int(s2)
    num_str = str(num)[::-1]

    node = ListNode(num_str[0])
    for i in range(1, len(num_str)):
        node.next = ListNode(num_str[i])
        node = node.next

    return node

addTwoNumbers()