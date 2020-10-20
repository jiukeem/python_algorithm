class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return "(" + str(self.key) + ": " + self.value + ")"

# chaining 에 쓸 아주 간단한 연결리스트
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def search_with_key(self, key):
        iter = self.head
        while iter:
            if iter.key == key:
                return iter
            iter = iter.next
        return None

    def append(self, key, value):
        new_node = Node(key, value)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail=  new_node
        else:
            self.tail.next, new_node.prev = new_node, self.tail
            self.tail = new_node

    def delete(self, key):
        node = self.search_with_key(key)
        if node == self.head:
            next = node.next
            next.prev = None
            self.head = next
        elif node == self.tail:
            prev = node.prev
            prev.next = None
            self.tail = prev
        else:
            prev, next = node.prev, node.next
            prev.next, next.prev = next, prev

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


class HashTableChaining:
    def __init__(self, size):
        self.size = size
        self.table = [LinkedList() for _ in range(self.size)]

    def hash(self, key):
        return key % self.size

    def search_with_key(self, key):
        list = self.table[self.hash(key)]
        return list.search_with_key(key)

    def delete(self, key):
        list = self.table[self.hash(key)]
        list.delete(key)

    def insert(self, key, value):
        list = self.table[self.hash(key)]
        existing_node = list.search_with_key(key)
        if existing_node:
            existing_node.value = value
        else:
            list.append(key, value)

    def __str__(self):
        to_print = "["
        for list in self.table:
            to_print += str(list)
        to_print += "]"
        return to_print


ht = HashTableChaining(10)
print(ht)
ht.insert(107, "지우")
print(ht)
ht.insert(1505, "지희")
ht.insert(705, "광호")
print(ht)
print(ht.search_with_key(805))
print(ht.search_with_key(705))