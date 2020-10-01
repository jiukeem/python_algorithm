# my solution
def solution(n):
    ans = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            ans.add(i)
            ans.add(n // i)

    return sum(ans)
# Status: Accepted
# Note: 처음에 일부 tc에서 실패가 떴는데 제곱수일 경우에 문제가 생겼었다.
#       예를 들어 9일 경우 1 + 9 + 3 = 13 이어야 하는데 3을 한번 더 더해서 16을 return 했다.
#       그걸 막기위한 방법으로는 ans = 0 해두고 if i != n // i: 조건을 다는 방법이나 ans를 set()으로 설정해서 add 로 걸러내는 방법이 있겠다.
#       list comprehension으로 좀 더 깔끔하게 쓸 수 있긴 하지만 그럼 적어도 n/2까지는 탐색을 해야하기 때문에 n이 커질수록 제곱근까지만 체크하는 이 방법이 유리하다.


# list comprehesion 사용하기
def solution(n):
    return sum([i for i in range(1, n + 1) if n %i == 0])

def solution(n):
    return n + sum([i for i in range(1, (n // 2) + 1) if n %i == 0])