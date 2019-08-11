# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head == None or k <= 0:
            return None
        p = head
        n = 1
        while p.next != None:
            p = p.next
            n = n + 1
        if k > n:
            return None
        for i in range(n - k):
            head = head.next
