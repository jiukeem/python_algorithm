n = int(input())
a = list(map(int, input().split()))

'''
map(f, iterable)은 iterable의 모든 component를 f 수행해서 돌려준다. 
내가 쓴건 3 5 5 7 을 input으로 받았을 때 스페이스로 구분해서 리스트로 만든 뒤(split) -  
각 컴포넌트에 대해 int로 바꿔주고(int) - 그걸 다시 리스트로 돌려준다(list)
for 문 돌렸을 작업을 한 줄에 표현할 수 있다. 
'''

'''
b = set(a)
a_new = list(b)
a_new.reverse()

print(a_new[1])
print(a_new)
돌아가긴 하는데 음수가 들어있으면 제대로 정렬을 못한다. 1 2 -10 7 5 -8 1 이면
[-8, -10, 7, 5, 2, 1] 이 나온다. 다른 방법을 찾아보자
'''
b = set(a)
a_new = list(b)
a_new.sort(reverse=True)

print(a_new[1])

#아, sort에 reverse = True 로 했더니 된다! 나이스
