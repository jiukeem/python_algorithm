class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def len(self):
        length = 0
        iterator = self.head
        while iterator is not None:
            length += 1
            iterator = iterator.next
        return length

    def append(self, data):
    # 추가 연산(중간에 삽입이 아닌 마지막에 append)
        new_node = Node(data)

        if self.head is None:
        # 연결리스트가 비어있는 경우
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert_after(self, previous_node, data):
    # 삽입 연산
        new_node = Node(data)
        if previous_node is self.tail:
        # append 가 되는 경우
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            new_node.next, new_node.prev = previous_node.next, previous_node
            previous_node.next = new_node
            new_node.next.prev = new_node

    def prepend(self, data):
    # 연결리스트의 맨 앞에 추가하고 싶은 경우(insert_after로는 못하는 예외 경우)
        new_node = Node(data)
        if self.head is None:
        # 연결리스트가 비어있는 경우
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, node_to_delete):
        data = node_to_delete.data

        if self.len() == 1:
        # 연결리스트에 지우려는 노드 딱 하나만 들어있는 경우
            self.head = None
            self.tail = None
        elif node_to_delete is self.tail:
        # 마지막 노드를 삭제하는 경우
            self.tail = node_to_delete.prev
            self.tail.next = None
        elif node_to_delete is self.head:
        # 맨 앞의 노드를 삭제하는 경우
            self.head = node_to_delete.next
            self.head.prev = None
        else:
            prev = node_to_delete.prev
            next = node_to_delete.next
            prev.next = next
            next.prev = prev

        return data

    def find_node_at(self, index):
    # 접근 연산
        mid = self.len() / 2
        if index < mid:
        # 인덱스가 중간보다 앞쪽에 위치하는 경우
            iterator = self.head
            for _ in range(index):
                iterator = iterator.next
        else:
        # 인덱스가 중간보다 뒤쪽에 위치하는 경우
            iterator = self.tail
            for _ in range(self.len() - index - 1):
                iterator = iterator.prev

        return iterator

    def find_node_with_data(self, data):
    # 탐색 연산
        iterator = self.head
        iterator_2 = self.tail
        # head와 tail에서 동시에 선형탐색을 시작할 것임

        while iterator and iterator_2:
            if iterator.data == data:
                return iterator
            if iterator_2.data == data:
                return iterator_2

            iterator = iterator.next
            iterator_2 = iterator_2.prev

        return None
        # data가 연결리스트에 없는 경우 None 을 반환환


    def __str__(self):
        str = '|'
        iterator = self.head
        while iterator is not None:
            str += f' {iterator.data} |'
            iterator = iterator.next

        return str


my_list = DoublyLinkedList()

my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)
print(my_list)

my_list.prepend(10)
print(my_list)

# 두 노드 사이에 있는 노드 삭제
node_at_index_2 = my_list.find_node_at(2)
my_list.delete(node_at_index_2)
print(my_list)

# 가장 앞 노드 삭제
head_node = my_list.head
print(my_list.delete(head_node))
print(my_list)

# 가장 뒤 노드 삭제
tail_node = my_list.tail
my_list.delete(tail_node)
print(my_list)

