from collections import deque

stack = deque()

# 맨 끝에 데이터 추가
stack.append('J')
stack.append('E')
stack.append('E')
stack.append('W')
stack.append('O')
stack.append('O')

print(stack)

# 맨 끝 데이터에 접근
print(stack[-1])

# 맨 끝 데이터 삭제
print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack)

# 큐와 다르게 스택은 동적배열과 이중연결리스트가 같은 시간복잡도를 가진다
# 데크는 이중연결리스트 자료구조를 사용하고 파이썬의 리스트는 동적배열을 사용하므로
# 파이썬의 리스트 자료형을 이용해도 스택을 구현할 수 있다.
# stack = deque() 대신 stack = []를 해도 똑같다 (메소드 이름도 똑같음)
