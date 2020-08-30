class MyStack:

    def __init__(self):
        from collections import deque
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
            # 새로 추가하는 애 전까지 반복하면서 [0]을 맨뒤로 append한다.
            # 순서를 재정렬하는 것

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# 파이썬에는 큐가 따로 없으니 데크를 이용
# 하지만 큐의 기능, 즉 .append() .leftpop() [0]등으로만 구현해야함 (pop(), [-1]쓰면 반칙)

# 나는 push는 그냥 append로 구현하고 top을 어떻게 해야할까 고민했는데 그게 잘 안되더라
# [0]만 접근할 수 있었기 때문에 복사본을 만들어서 [0]을 계속 빼는방법 밖에 생각하지 못했음

# 책풀이는 반대로 push에 이것저것을 적용했다.
# 새로 push하는 요소를 [0]자리에 위치하게 하면 pop은 popleft로, top은 [0]로 간단히 해결할 수 있다.
