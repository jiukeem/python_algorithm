# 해시테이블에서 충돌이 일어날 경우를 위한 chaining 용 링크드리스트 구현

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def find_node_with_key(self, key):
        iterator = self.head

        while iterator is not None:
            if iterator.key == key:
                return iterator
            iterator = iterator.next

        return None

    def append(self, key, value):
        new_node = Node(key, value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def delete(self, node_to_delete):
        if self.head is self.tail:
            self.head = None
            self.tail = None

        elif self.tail is node_to_delete:
            self.tail = self.tail.prev
            self.tail.next = None

        elif self.head is node_to_delete:
            self.head = self.head.next
            self.head.prev = None

        else:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev

    def __str__(self):
        str = ''
        iterator = self.head

        while iterator is not None:
            str += f'{iterator.key}: {iterator.value}\n'
            iterator = iterator.next

        return str

my_list = LinkedList()
my_list.append('지우', '0521')
my_list.append('지희', '0117')
my_list.append('광호', '0207')
print(my_list)