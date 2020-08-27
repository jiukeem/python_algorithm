class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left_child = None
        self.right_child = None

def print_inorder(node):
    # 주어진 노드를 in-order로 출력
    # class 안의 print_sorted_tree 에 node 파라미터를 안 입력해도 되게 만들고 싶어서
    # 헬퍼 함수를 따로 구현
    if node is not None:
        print_inorder(node.left_child)
        print(node.data)
        print_inorder(node.right_child)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        # 데이터를 추가하면 맞는 자리로 이동시키는 함수
        new_node = Node(data)
        if self.root is None:
            # 빈 트리인 경우
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

    def search(self, data):
        # data를 갖는 노드를 찾아서 return
        iterator = self.root
        while iterator is not None:
            if iterator.data == data:
                return iterator
            if iterator.data < data:
                iterator = iterator.right_child
            else:
                iterator = iterator.left_child

        return None

    def find_min(self, node):
        # 해당노드를 뿌리로하는 부분 트리에서 가장 작은 값을 가지는 노드 return
        iterator = node
        while True:
            if iterator.left_child is None:
                return iterator
            else:
                iterator = iterator.left_child

        return iterator

    def delete(self, data):
        node_to_delete = self.search(data)
        parent_node = node_to_delete.parent

        # case1: 지우려는 노드가 leaf node 인 경우
        if node_to_delete.left_child is None and\
            node_to_delete.right_child is None:
            if self.root is node_to_delete:
                self.root = None
            elif parent_node.left_child is node_to_delete:
                parent_node.left_child = None
            else:
                parent_node.right_child = None

        # case2: 지우려는 노드가 한개의 자식노드만 가지고 있을 경우
        # 2-1: 오른쪽자식만 가지고 있는 경우
        elif node_to_delete.left_child is None:
            # 조건문을 이렇게만 써도 위의 if에서 둘 다 None인 경우는 걸러졌으므로
            # 오른쪽자식이 있고 왼쪽자식이 없는 경우 라는 조건이 된다.
            if self.root is node_to_delete:
                self.root = node_to_delete.right_child
                self.root.parent = None
            elif parent_node.left_child is node_to_delete:
                parent_node.left_child = node_to_delete.right_child
                node_to_delete.right_child.parent = parent_node
            else:
                parent_node.right_child = node_to_delete.right_child
                node_to_delete.right_child.parent = parent_node

        # 2-2: 왼쪽자식만 가지고 있는 경우
        elif node_to_delete.right_child is None:
            if self.root is node_to_delete:
                self.root = node_to_delete.left_child
                self.root.parent = None
            elif parent_node.left_child is node_to_delete:
                parent_node.left_child = node_to_delete.left_child
                node_to_delete.left_child.parent = parent_node
            else:
                parent_node.right_child = node_to_delete.left_child
                node_to_delete.left_child.parent = parent_node

        # case3: 지우려는 노드가 두 자식노드를 모두 가지고 있는 경우
        else:
            node_to_change = self.find_min(node_to_delete.right_child)
            # successor 찾기
            data = node_to_change.data
            self.delete(data)
            # node_to_change 는 case1 혹은 case2 에 항상 해당됨
            node_to_delete.data = data
            # 지우려는 노드의 데이터 변경

    def print_sorted_tree(self):
        # inorder 순회로 오름차순 출력
        print_inorder(self.root)


bst = BinarySearchTree()

# 데이터 삽입
bst.insert(7)
bst.insert(11)
bst.insert(9)
bst.insert(17)
bst.insert(8)
bst.insert(5)
bst.insert(19)
bst.insert(3)
bst.insert(2)
bst.insert(4)
bst.insert(14)

print(bst.find_min(bst.root).data)  # 전체 이진 탐색 트리에서 가장 작은 노드
print(bst.find_min(bst.root.right_child).data)
bst.print_sorted_tree()

bst.delete(2)
bst.delete(4)

bst.print_sorted_tree()

bst.delete(7)
bst.delete(11)

bst.print_sorted_tree()