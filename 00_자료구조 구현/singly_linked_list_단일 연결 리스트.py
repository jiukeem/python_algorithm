class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):                       # 마지막에 새로운 노드 추가
        new_node = Node(data)
        if self.head is None:                     # 연결리스트가 비어있는 경우
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):                      # 리스트의 가장 앞에 추가
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_after(self, previous_node, data):  # 삽입 연산 메소드
        new_node = Node(data)
        if self.tail is previous_node:            # 맨 마지막에 삽입하는 경우 즉, append일 때
            self.append(data)
        else:
            new_node.next = previous_node.next
            previous_node.next = new_node

    def delete_after(self, previous_node):        # 삭제 연산 메소드
        data = previous_node.next.data
        if previous_node.next is self.tail:
            previous_node.next = None
            self.tail = previous_node
        else:
            previous_node.next = previous_node.next.next

        return data                               # 삭제하는 노드의 데이터를 return하는게 관습이라고 함

    def find_node_at(self, index):                # 접근 연산 메소드
        iterator = self.head
        for _ in range(index):
            iterator = iterator.next
        return iterator

    def find_node_with_data(self, data):          # 탐색 연산 메소드
        iterator = self.head
        while iterator is not None:
            if iterator.data == data:
                return iterator
            iterator = iterator.next
        return None

    def __str__(self):
        to_print = '|'
        iterator = self.head

        while iterator is not None:
            to_print += f' {iterator.data} |'
            iterator = iterator.next
        return to_print

my_list = LinkedList()
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)
print(my_list)

node_2 = my_list.find_node_at(2)
my_list.insert_after(node_2, 6)
print(my_list)

head_node = my_list.head
my_list.insert_after(head_node, 14)
print(my_list)

my_list.delete_after(node_2)
print(my_list)

second_to_last_node = my_list.find_node_at(3)
print(my_list.delete_after(second_to_last_node))
print(my_list)