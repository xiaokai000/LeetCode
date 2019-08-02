class Node(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def mirror_recursively(node):
    if node is None or (node.left is None and node.right is None):
        return
    node.left, node.right = node.right, node.left

    if node.left:
        mirror_recursively(node.left)

    if node.right:
        mirror_recursively(node.right)

root = Node(1, Node(2, Node(4), Node(5)), Node(3))
mirror_recursively(root)
print(root.right.left.value)