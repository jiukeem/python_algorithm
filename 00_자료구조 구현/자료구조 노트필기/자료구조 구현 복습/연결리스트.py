# 노드 구현
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

# 단일연결리스트 구현
class SinglyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.list_size = 1

    def access(self, idx):
        if idx >= self.list_size:
            return
        iter = self.head
        for _ in range(idx):
            iter = iter.next
        return iter

    def search(self, value):
        iter = self.head
        while iter:
            if iter.value == value:
                return iter
            else:
                iter = iter.next
        return None

    def insert(self, value, idx):
        node = Node(value)
        if idx >= self.list_size:
            return
        prev_node = self.access(idx-1)
        prev_node.next, node.next = node, prev_node.next
        self.list_size += 1

    def delete(self, idx):
        prev_node = self.access(idx-1)
        prev_node.next = prev_node.next.next
        self.list_size -= 1

    def insert_head(self, value):
        node = Node(value)
        self.head, node.next = node, self.head
        self.list_size += 1

    def insert_tail(self, value):
        node = Node(value)
        iter = self.head
        while iter.next:
            iter = iter.next
        iter.next = node
        self.list_size += 1

    def delete_head(self):
        if self.head and self.head.next:
            self.head = self.head.next
        self.list_size -= 1

    def delete_tail(self):
        tail_prev = self.access(self.list_size - 2)
        tail_prev.next = None
        self.list_size -= 1

    def __str__(self):
        to_print = '['
        iter = self.head
        while iter:
            to_print += str(iter)
            if iter.next:
                to_print += ", "
            iter = iter.next

        to_print += ']'
        return to_print

my_list = SinglyLinkedList(3)
print(my_list)
my_list.insert_tail(4)
my_list.insert(12, 1)
print(my_list)
my_list.insert_head(8)
node = my_list.search(3)
print(node, my_list)


