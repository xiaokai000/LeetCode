class Node:
    def __init__(self, data=None, next=None):
        self.val = data
        self.next = next


if __name__ == '__main__':
    l1 = Node(1, Node(4, Node(7)))
    l2 = Node(2, Node(5, Node(6)))

    res = Node()
    node = res
    while l1 and l2:
        if l1.val < l2.val:
            node.next, l1 = l1, l1.next
        else:
            node.next, l2 = l2, l2.next
        node = node.next
    if l1:
        node.next = l1
    else:
        node.next = l2

