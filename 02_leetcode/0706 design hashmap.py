# 내 풀이 - 파이썬의 리스트자료형 사용
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bucket = []


    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        for element in self.bucket:
            if key == element[0]:
                element[1] = value
                return
        self.bucket.append([key, value])


    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        for element in self.bucket:
            if key == element[0]:
                return element[1]
        return -1


    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        for i in range(len(self.bucket)):
            if key == self.bucket[i][0]:
                del self.bucket[i]
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# 잘 돌아가기는 하는데 runtime이 너무 길다. 아슬아슬하게 타임아웃이 아닌 수준.
# 매번 for문으로 돌리니 그런건데 어떻게 더 효율적으로 탐색할 수 있을까?
# 현재 put: O(n), get: O(n), remove: O(n)


# 책 풀이
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bucket = []


    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        for element in self.bucket:
            if key == element[0]:
                element[1] = value
                return
        self.bucket.append([key, value])


    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        for element in self.bucket:
            if key == element[0]:
                return element[1]
        return -1


    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        for i in range(len(self.bucket)):
            if key == self.bucket[i][0]:
                del self.bucket[i]
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)