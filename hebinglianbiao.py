class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


if __name__ == '__main__':
    link1 = Node(1, Node(4, Node(7)))
    link2 = Node(2, Node(5, Node(6)))


    res = head = Node(0)
    while link1 and link2:
        if link1.data < link2.data:
            head.next = link1
            link1 = link1.next

        elif link1.data >= link2.data:
            head.next = link2
            link2 = link2.next

        head = head.next
    head.next = link1 or link2

    print(res.next.data)

