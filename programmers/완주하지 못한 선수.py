participant = input().split()
completion = input().split()

for name in participant:
    if name not in completion:
        print(name)
    else:
        completion.remove(name)

# for 문의 시간복잡도는 O(n), remove도 모든 요소를 살펴보면서 맞는 걸 찾기때문에 O(n) 
# 즉 내 코드의 복잡도는 O(n^2)가 된다.
# 앗, in 혹은 not in 도 O(n)이다 나는 겁나 쓰잘데기 없이 오래걸리는 코드를 짠 것..
# 지금까지 시간복잡도, 공간복잡도라는 개념을 한번도 접해본 적이 없는데 이제 여기에 신경 써서 짜는 연습을 해야할 것 같다.
# 시간복잡도를 O(n)까지 줄이자