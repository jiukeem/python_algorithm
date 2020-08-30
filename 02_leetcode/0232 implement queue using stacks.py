# 내 풀이
class MyQueue:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        reloc_stack = []
        for _ in range(len(self.stack)):
            reloc_stack.append(self.stack.pop())
            # 스택에서 스택으로 옮기면서 순서를 반대로 뒤집어준다.
        front = reloc_stack.pop()

        for _ in range(len(reloc_stack)):
            self.stack.append(reloc_stack.pop())
            # 원하는 요소를 뺐으니 다시 뒤집어준다.

        return front

    def peek(self) -> int:
        reloc_stack = []
        for _ in range(len(self.stack)):
            reloc_stack.append(self.stack.pop())
        front = reloc_stack[-1]

        for _ in range(len(reloc_stack)):
            self.stack.append(reloc_stack.pop())

        return front

    def empty(self) -> bool:
        return not self.stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# 파이썬에는 스택 자료형이 없으니 리스트를 사용하자
# 사용할 수 있는 기능은 pop(), [-1], append() 정도

# 0225 문제와 짝꿍이다
# push 함수에서 제일 먼저 들어온 요소가 제일 뒤에 있을 수 있게 재정렬해주면 된다
# 라고 생각했는데 코드를 짜보니 그렇지가 않다.
# 큐를 쓸 때는 앞에서 빼서 뒤에 붙여주는게 가능했는데 스택은 빼고 더하고를 다 뒤에서만 할 수 있으므로
# 225번 문제처럼 풀 수 없다.
# 이 문제는 오히려 처음 내 방식, 즉 push는 그냥 append 해주고 pop에서 처리를 해주는 식으로 풀어야한다.

# 맞긴 했는데 pop과 peek에서 새 스택으로 옮겼다가 다시 원상복구해주는게 좀 비효율적인 것 같고
# 한줄 빼고는 같은 코드를 두번 쓰는 것도 낭비다.



# 책 풀이
class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return self.input == [] and self.output == []
# 와 너무 똑똑하다. myqueue에 추가한 데이터들을 input과 output에 흩어져 있는 형태겠지만
# 이 문제에서 원하는게 큐 전체를 print하는 것도 아니고,
# 4개의 기능들만 수행할 수 있으면 안에서 어떤 상태로 저장하고 있든 상관이 없다.
# 나는 항상 self.stack에 완전한 큐의 형태를 구현하고 있어야한다고 생각해서 reloc에서 다시 옮겨주고 함수를 끝냈다.
# 이 코드는 input과 output을 필요할 때 마다 자유자재로 쓴다.
# append는 input에, pop은 output에서.
# 심지어 input에 들어올 때 마다 output으로 옮겨주는게 아니라 output이 다 떨어질 때만 옮기는 것도 너무 현명하다ㅠㅠ
# 요소들의 순서가 복잡하게 얽히는 것을 고민할 필요가 없고 연산시간도 분할상환분석으로 O(1)이 된다.
# 하여간 너무 똑똑한 방법!!