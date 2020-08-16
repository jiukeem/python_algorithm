# 우선 노드부터
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next
    # 노드는 값(item)과 링크(next)를 가지고 있음

class Stack:
    def __init__(self):
        self.last = None

    def push(self, item):
        self.last = Node(item, self.last)
    # push를 통해 item을 마지막 노드로 집어넣으며, 얘는 다시 기존의 last로 향하는 링크를 가짐

    def pop(self):
        item = self.last.item
        self.last = self.last.next
        return item
    # self.last의 값(item)을 반환하며, self.last를 self.last의 다음 노드로 바꾼다.

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

for _ in range(5):
    print(stack.pop())
# >> 5, 4, 3, 2, 1 순서로 출력

# stack의 노드의 링크는 전부 자신의 이전값을 가리킨다. 즉 회살표가 시작되는 노드가 last이다.
# 나중에 들어온 개체가 head가 된다. .next라고 표기하는게 헷갈림을 초래하는 것 같다.
# 구글링하면서 내가 다시 구현해보자. 후입선출의 개념을 좀 더 잘 드러낼 수 있도록


# next를 prev로 바꿔서 한번 더
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None

    def __str__(self):
        return str(self.data)

class Stack2:
    def __init__(self):
        self.head = None
        self.top = 0

    def push(self, data):
        new_node = Node(data)
        if self.head == None:
        # 첫 push인 경우
            self.head = new_node
            return

        new_node.prev = self.head
        # push할 노드의 링크를 head로 지정
        self.head = new_node

    def pop(self):
        data = self.head.data
        self.head = self.head.prev
        return data

    def __str__(self):
        node = self.head
        if node == None:
            return None
        print_stack = '<=> [ '
        while node:
            print_stack += str(node.data) + ' '
            node = node.prev
        print_stack += ']'
        return print_stack
    
# 위의 코드보다 훨씬 번잡하다. 근데 이렇게 한번 더 써보고 나서 위의 코드를 다시 읽으니 이해가 됐다!
# 좋아좋아 스택 문제 다 덤벼

stack = Stack2()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

for _ in range(5):
    print(stack.pop())

if __name__=="__main__":
    m_stack = Stack2()
    m_stack.push(5)
    m_stack.push(4)
    m_stack.push(3)
    print(m_stack)
    print('Stack pop :', m_stack.pop())
    print(m_stack)
    print('Stack pop :', m_stack.pop())
    print('Stack pop :', m_stack.pop())
    print(m_stack)