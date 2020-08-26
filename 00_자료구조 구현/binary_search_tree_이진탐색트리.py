class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left_child = None
        self.right_child = None

def print_inorder(node):
    # 주어진 노드를 in-order로 출력
    if node is not None:
        print_inorder(node.left_child)
        print(node.data)
        print_inorder(node.right_child)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return

        node_to_compare = self.root
        while node_to_compare is not None:
            if node_to_compare.data < data:
                if node_to_compare.right_child is None:
                    new_node.parent = node_to_compare
                    node_to_compare.right_child = new_node
                    return
                else:
                    node_to_compare = node_to_compare.right_child

            if node_to_compare.data > data:
                if node_to_compare.left_child is None:
                    new_node.parent = node_to_compare
                    node_to_compare.left_child = new_node
                    return
                else:
                    node_to_compare = node_to_compare.left_child


    def print_sorted_tree(self):
        # inorder 순회로 오름차순 출력
        print_inorder(self.root)
