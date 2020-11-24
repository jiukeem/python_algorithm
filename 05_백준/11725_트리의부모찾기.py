# coding=utf-8
from collections import deque
import sys
sys.setrecursionlimit(10 ** 9)

n = int(sys.stdin.readline())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [False for _ in range(n+1)]
parent_node = [None for _ in range(n+1)]

q = deque([1])
visited[1] = True
while q:
    curr_node = q.popleft()
    for child in tree[curr_node]:
        if not visited[child]:
            q.append(child)
            visited[child] = True
            parent_node[child] = curr_node

for ans in parent_node[2:]:
    print(ans)

# Status: Accepted
# Note: 이거 알고리즘은 BFS로 금방 짰는데 input 처리에서 엄청 애를 먹었다. - 그리고 아직도 의문이 많은 상태
#       처음에는 map(int, input().split()) 으로 했더니 n은 제대로 처리하고 두번째 줄 넣고 엔터치는 순간에 syntax error: unexpected EOF 에러가 났다.
#       도대체 뭐가 무엇인고 하면서 스택오버플로우를 훑다가 raw_input 으로 바꿔보라는 답변이 있어 수정해봤더니 제대로 돌아갔다!
#       근데 여기서 의문은 raw_input 은 python2 에서 사용하던거고 3에 들어서는 없어졌다는데 도대체 왜..?
#       그리고 나는 두번째 줄을 넣는 순간에 포문이 실행되어버려서(n-1번) 그 밑의 줄이 없으니 에러가 나는건가- 추측했는데 복붙으로 한번에 넣어도 에러가 난다. 그럼 이유가 무엇??
#       두번째 의문은 raw_input 으로 파이참에서는 잘 돌아가는 것을 확인했는데 백준에 그대로 제출했더니 런타임 에러가 난다. 뭐가 다르길래..?
#       결국 구글링을 통해서 sys.stdin.readline() 으로 해결했다. 파이썬 내부에서, 그리고 인터프리터 상에서 이 세가지가 어떻게 다르게 동작하는건지 찾아봐야겠다.

