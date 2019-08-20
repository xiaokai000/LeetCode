#-*- coding:utf-8 -*-
class Node:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


def FindKthToTail(head, k):
    # write code here
    if head == None or k <= 0:
        return None
    p1 = head
    p2 = head
    for i in range(k-1):
        if p1.next == None:
            return None
        p1 = p1.next
    while p1.next != None:
        p1 = p1.next
        p2 = p2.next
    return p2


head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9)))))))))

print(FindKthToTail(head, 4).val)