from collections import deque

queue = deque()

# 맨 뒤에 데이터 추가
queue.append('지우')
queue.append('광호')
queue.append('지희')
queue.append('주현')
queue.append('용현')

print(queue)

# 맨 앞 데이터에 접근
print(queue[0])

# 맨 앞 데이터 삭제(삭제하는 데이터를 return)
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())

print(queue)
