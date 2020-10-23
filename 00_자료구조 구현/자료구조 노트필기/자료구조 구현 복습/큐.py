# 데크(이중연결리스트) 이용
from collections import deque
queue = deque()
queue.append()
queue[0]
queue.popleft()

# 스택으로 구현 - 파이썬에는 스택이 따로 없으니 리스트를 사용(데크 사용해도 무방)
# 큐는 한쪽에서 들어오고 반대쪽에서 나가기 때문에 큐 한개만으로 스택을 구현할 수 있지만
# 스택은 들어간쪽으로 나오니 스택 한개로는 안쪽에 접근할 수가 없다(한쪽이 막힌 실린더처럼) 그래서 스택을 이용한 큐 구현시에는 스택이 2개 필요함
# 공 옮길 때처럼 완전히 뒤집어서 다른 실린더에 집어넣으면 순서관계가 뒤바뀌게 됨

class Queue:
    def __init__(self):
        self.i_stack = []
        self.o_stack = []

    def append(self, data):
        self.i_stack.append(data)

    def first_data(self):
        if not self.o_stack:
            while self.i_stack:
                self.o_stack.append(self.i_stack.pop())

        return self.o_stack[-1]

    def pop_first(self):
        self.first_data()
        return self.o_stack.pop()
