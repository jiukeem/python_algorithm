class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)

class DoublyLinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.list_size = 1

    def search_with_idx(self, idx):
        if self.list_size <= idx:
            return None
        iter = self.head
        for _ in range(idx):
            iter = iter.next
        return iter

    def search_with_value(self, value):
        iter = self.head
        while iter:
            if iter.value == value:
                return iter
            iter = iter.next
        return None

    def insert(self, value, idx):
        # 중간에 추가하는 연산
        if self.list_size <= idx:
            return None
        new_node = Node(value)
        prev_node = self.search_with_idx(idx-1)
        next_node = self.search_with_idx(idx)
        prev_node.next, next_node.prev = new_node, new_node
        new_node.next, new_node.prev = new_node, prev_node
        self.list_size += 1

    def prepend(self, value):
        # 맨 앞에 추가하는 연산
        new_node = Node(value)
        new_node.next, self.head.prev = self.head, new_node
        self.head = new_node
        self.list_size += 1

    def append(self, value):
        # 맨 뒤에 추가하는 연산
        new_node = Node(value)
        new_node.prev, self.tail.next = self.tail, new_node
        self.tail = new_node
        self.list_size += 1

    def delete_with_idx(self, idx):
        # 중간을 삭제
        if self.list_size <= idx:
            return None
        node_to_del = self.search_with_idx(idx)
        if not node_to_del:
            return None
        prev_node, next_node = node_to_del.prev, node_to_del.next
        prev_node.next, next_node.prev = next_node, prev_node
        self.list_size -= 1

    def delete_first(self):
        # head 삭제
        if not self.head:
            return None
        self.head = self.head.next
        self.head.prev = None
        self.list_size -= 1

    def delete_last(self):
        # tail 삭제
        if not self.tail:
            return None
        self.tail = self.tail.prev
        self.tail.next = None
        self.list_size -= 1

    def delete_with_value(self, value):
        node_to_del = self.search_with_value(value)
        if not node_to_del:
            return None
        prev_node, next_node = node_to_del.prev, node_to_del.next
        prev_node.next, next_node.prev = next_node, prev_node
        self.list_size -= 1

    def __str__(self):
        to_print = "["
        iter = self.head
        while iter:
            to_print += str(iter)
            if iter.next:
                to_print += ", "
            iter = iter.next
        to_print += "]"
        return to_print

my_dlist = DoublyLinkedList(7)
my_dlist.prepend(31)
my_dlist.append(1)
my_dlist.append(4)
my_dlist.append(9)
print(my_dlist)
node = my_dlist.search_with_idx(3)
print(node)
print(my_dlist.tail)
my_dlist.delete_last()
print(my_dlist)
my_dlist.delete_with_idx(1)
my_dlist.delete_with_idx(9)
print(my_dlist)
my_dlist.delete_first()
print(my_dlist)

# 연결리스트 복습 끝!

