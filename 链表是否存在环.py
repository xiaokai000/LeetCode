class LNode:
    def __init__(self, elem):
        self.elem = elem
        self.pnext = None


def exitLoop(LList):
    p1 = p2 = LList
    while p2 and p2.pnext:  # 当链表为空或者只有一个结点时，就不执行循环体里的程序，返回False
        p1 = p1.pnext
        p2 = p2.pnext.pnext
        if p1 == p2:
            return True
    return False


if __name__ == "__main__":
    LList = LNode(1)
    p1 = LNode(2)
    p2 = LNode(3)
    p3 = LNode(4)
    p4 = LNode(5)
    p5 = LNode(6)
    LList.pnext = p1
    p1.pnext = p2
    p2.pnext = p3
    p3.pnext = p4
    p4.pnext = p5
    p5.pnext = p2
    print(exitLoop(LList))
