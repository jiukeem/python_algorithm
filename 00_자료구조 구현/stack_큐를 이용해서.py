# leetcode의 225번 문제
# 파이썬에는 큐가 따로 없으니 데크를 이용하며 큐의 기능만을 이용한다.

from collections import deque

class Stack:
    def __init__(self):
        self.queue = deque()

    def push(self, x):
    # x를 맨 뒤에 추가
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
            # 새로 넣는 애를 제외하고 나머지를 앞에서 꺼내서 뒤로 추가.
            # 요소들 순서를 재정렬하는 것

    def pop(self):
    # 가장 마지막으로 들어온 요소를 삭제하고 해당 요소를 return
        return self.queue.popleft()

    def top(self):
    # 가장 마지막으로 들어온 요소 return
        return self.queue[0]

    def empty(self):
    # 스택이 비었는지 여부
        return not self.queue