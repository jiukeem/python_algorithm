# leetcode의 232번 문제
# 파이썬에는 스택이 따로 없으니 리스트를 이용하며 스택의 기능만을 이용한다.

class Queue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
    # x를 맨 뒤에 추가
        self.input.append(x)

    def pop(self):
    # 가장 먼저 들어온 요소를 삭제하고 해당 요소를 return
        self.peek()
        return self.output.pop()

    def peek(self):
    # 가장 먼저 들어온 요소 return
        if self.output is None:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self):
    # queue가 비었는지 여부
        return not self.output and not self.input

# 큐를 이용한 스택구현과 다르게 얘는 스택이 두개 필요하다.
# 큐는 앞에서 빼서 뒤에 추가하는게 가능하기 때문에 in-place로 요소를 재정렬할 수 있지만
# 스택은 맨뒤에서 빼서 맨 뒤에 추가하는 것 밖에 못하기 때문에 긴 실린더에 들어있는 공들처럼
# 두 개를 사용해야 재정렬이 가능함