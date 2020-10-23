class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None

def traverse_inorder(node):
    if node is not None:
        traverse_inorder(node.left_child)
        print(node.data)
        traverse_inorder(node.right_child)
