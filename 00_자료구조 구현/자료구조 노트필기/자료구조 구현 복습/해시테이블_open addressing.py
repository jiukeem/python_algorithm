class HashTableOA:
    def __init__(self, size):
        self._size = size
        self._table = [() for _ in range(self._size)]
        self.idx = None

    def hash(self, key):
        return key % self._size

    def search_with_key(self, key):
        idx = self.hash(key)
        while self._table[idx] != () and idx < self._size:
            if self._table[idx][0] == key:
                self.idx = idx
                return self._table[idx]
            idx  = (idx + 1) % self._size
        self.idx = idx
        return None

    def insert(self, key, value):
        element = (key, value)
        _ = self.search_with_key(key)
        self._table[self.idx] = element
        self.idx = None
        return

    def delete(self, key):
        existing = self.search_with_key(key)
        if existing:
            self._table[self.idx] = 'deleted'
        self.idx = None
        return

    def __str__(self):
        to_print = "["
        for element in self._table:
            if element == ():
                to_print += "()"
            elif element == 'deleted':
                to_print += "(" + element + ")"
            else:
                to_print += "(" + str(element[0]) +": " + str(element[1]) + ")"
        return to_print

ht = HashTableOA(5)
ht.insert(2, 7)
ht.insert(79, 1)
print(ht)
ht.insert(47, 9)
print(ht)
ht.insert(72, 10)
print(ht)
ht.delete(47)
print(ht)
print(ht.search_with_key(72))
# 너무 재밌당 내가 만들었는데도 신기해 호호