'''def solution(n):
    ans = 1
    for i in range(3, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            ans += 1

    return ans'''
# 시간복잡도는 그렇다치고, else가 저 자리에 있는데 왜 에러가 안나는거지?
# else 없이 ans += 1 을 하면 j에 관한 포문 결과에 상관없이 결국 모든 i들에 대해 작동하게 돼서 문제가 생긴다.
# 흠, break과 else의 관계에 대해서 좀 찾아봐야겠다.
# 이 게시글이 이해하기 쉽다. https://kongdols-room.tistory.com/42
# if문이 아니라 while문과 for문에도 else를 사용할 수 있구나. 저 else는 for j 에 따라오는 절이며, for문이 종료되는 시점에 else 절의 내용을 실행한다.
# for문에 포함된 절이므로 break으로 for문을 깨고 나오는 경우, else 절은 실행되지 않는다 -> 이걸 이용한거네!
# 어쨌든 이 풀이는 시간초과가 난다. 더 줄일 방법을 생각해보자


# 에라토스테네스의 체 이용
import math
def solution(n):
    sieve = [True] * (n + 1)

    m = int(math.sqrt(n))
    for i in range(2, m + 1):
        if sieve[i] is True:
            for j in range(i + i, n + 1, i):
                sieve[j] = False

    return sum(sieve[2:])
# Status: Accepted
# Note: 좋은 코드다. 구글링하니 에라토스테네스의 체를 이용한 코드가 굉장히 많더라.
#       음 나였으면 우선 [True] 를 이용할 생각을 못했을 것 같다. if sieve[i] is True 한 줄로 간단히 다음 걸러낼 소수를 찾을 수 있다
#       j 범위 설정에 i 단위 증가도 좋은 방법이다.
#       일단 sieve[0]은 버리고 sieve[1]은 1은 True지만 소수가 아니므로 버리고 [2]부터 쓰면된다.
#       import math가 없어도 n ** 0.5하면 똑같지만 저게 더 의미가 명확한 듯해서 sqrt를 사용했다.
#       그리고 if sieve[i]:, if sieve[i] is True:, if sieve[i] == True: 세가지 전부 통과한다. 일단 False는 None처럼 여겨지는 듯하고 is와 ==는 아직도 헷갈린다.
#       파이참의 가이드는 is True를 권한다.


# 다른 사람의 풀이
def solution(n):
    num = set(range(2,n+1))

    for i in range(2,int(n ** 0.5)+1):
        if i in num:
            num -= set(range(2*i,n+1,i))
    return len(num)
# 같은 원리지만 이것도 참 간단하다. True/False 값이 없어도 if i in num 으로 체크하면 되네. set을 좀 더 자주 활용해보면 좋겠다.