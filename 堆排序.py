'''
输入两个链表，找出它们的第一个公共结点。
'''

class Node:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


def FindFirstCommonNode(pHead1, pHead2):
    # write code here
    p1 = pHead1
    p2 = pHead2
    while p1.val != p2.val:
        p1 = p1.next if p1!=None else pHead2
        p2 = p2.next if p2!=None else pHead1
    print(p1)
    return p1



if __name__ == '__main__':
    list_a = Node('a1', Node('a2', Node('c1', Node('c2', Node('c3')))))  # 构造不带头结点的链表：a1→a2→c1→c2→c3
    list_b = Node('b1', Node('b2', Node('b3', Node('c1', Node('c2', Node('c3'))))))  # 构造不带头结点的链表：b1→b2→b3→c1→c2→c3

    FindFirstCommonNode(list_a, list_b)