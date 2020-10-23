class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        node = Node(data)
        if not self.root:
            self.root = node
            return
        else:
            iter = self.root
            while iter:
                if iter.data < data:
                    if iter.right_child:
                        iter = iter.right_child
                    else:
                        iter.right_child = node
                        node.parent = iter
                        return

                elif iter.data > data:
                    if iter.left_child:
                        iter = iter.left_child
                    else:
                        iter.left_child = node
                        node.parent = iter
                        return

    def search(self, data):
        iter = self.root
        while iter:
            if iter.data == data:
                return iter
            elif iter.data < data:
                iter = iter.right_child
            else:
                iter = iter.left_child

        return None

    def delete(self, data):
        node_to_del = self.search(data)
        if not node_to_del:
            return

        parent = node_to_del.parent
        # case1. leaf node일 경우
        if not node_to_del.right_child and not node_to_del.left_child:
            if data < parent.data:
                parent.left_child = None
            else:
                parent.right_child = None

        # case2-1. left child만 가질경우
        elif not node_to_del.right_child:
            child = node_to_del.left_child
            if data < parent.data:
                parent.left_child, child.parent = child, parent
            else:
                parent.right_child, child.parent = child, parent

        # case2-2. right child만 가질 경우
        elif not node_to_del.left_child:
            child = node_to_del.right_child
            if data < parent.data:
                parent.left_child, child.parent = child, parent
            else:
                parent.right_child, child.parent = child, parent

        # case3. 양쪽 자식 노드를 둘 다 가지고 있는 경우
        else:
            iter = node_to_del.right_child
            while iter.left_child:
                iter = iter.left_child
            data = iter.data
            self.delete(iter.data)
            node_to_del.data = data

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left_child)
            print(node.data)
            self.inorder_traversal(node.right_child)









