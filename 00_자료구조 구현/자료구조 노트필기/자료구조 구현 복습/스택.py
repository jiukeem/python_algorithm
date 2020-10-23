# 파이썬의 리스트 이용(동적배열)
class Stack:
    def __init__(self):
        self.stack = []

    # 맨 뒤에 삽입 O(1)
    def append(self, data):
        self.stack.append(data)

    # 맨 뒤 요소에 접근 O(1)
    def last_data(self):
        return self.stack[-1]

    # 맨 뒤 요소 추출 O(1)
    def pop_last(self):
        return self.pop()

# 이중연결리스트로 구
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Stack_2:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # 맨 뒤에 삽입 O(1)
    def append(self, data):
        node = Node(data)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next, node.prev = node, self.tail

        self.size += 1

    # 맨 뒤 요소에 접근 O(1)
    def last_data(self):
        if self.tail:
            return self.tail.data
        else:
            return None

    # 맨 뒤 요소 추출 O(1)
    def pop_last(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            ans = self.tail.data
            self.head, self.tail = None, None
            self.size -= 1
            return ans
        else:
            prev_node = self.tail.prev
            prev_node.next = None
            ans = self.tail.data
            self.tail = prev_node
            self.size -= 1
            return ans

# 데크(이중연결리스트) 이용
from collections import deque
stack = deque()
stack.append()
stack.pop()
stack[-1]

# 큐를 이용. 파이썬에는 큐가 따로 없으니 데크를 사용하되, 큐의 기능만을 이용(맨끝추가, 맨앞접근, 맨앞추출)
# 스택과 큐를 서로를 이용해서 구현할 때는 실린더를 생각해주면 좀 더 쉽다.
class Stack:
    def __init__(self):
        self.queue = deque()

    def append(self, data):
        self.queue.append(data)
        for _ in range(len(self.queue) - 1):
            element = self.queue.popleft()
            self.queue.append(element)

    def last_data(self):
        return self.queue[0]

    def pop_last(self):
        return self.queue.popleft()


