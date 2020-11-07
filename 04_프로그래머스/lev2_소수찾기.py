# coding=utf-8
# my solution
import itertools

def solution(numbers):
    possible_nums = []
    for i in range(1, len(numbers) + 1):
        possible_nums += map(''.join, itertools.permutations(numbers, i))

    possible_nums = set(map(int, possible_nums))
    target_number = max(possible_nums)

    sieve = [True] * (target_number + 1)
    sieve[0], sieve[1] = False, False
    for i in range(2, int(target_number ** 0.5) + 1):
        for j in range(2*i, target_number + 1, i):
            sieve[j] = False

    answer = 0
    for candidate in possible_nums:
        if sieve[candidate] is True:
            print(candidate)
            answer += 1

    return answer
# Status: Accepted
# Note: 크게 두 부분으로 나뉘어지는데 가능한 모든 경우의 수 pool을 만드는 것과 그 pool의 요소들이 소수인지 아닌지 판별하는 것.
#       뒷부분은 에라토스테네스의 체를 사용했고 앞부분은 permutation을 다 합한뒤 int형으로 변환, set으로 중복을 걸렀다.
#       permutation의 결과물이 붙어나오지 않아서 permutation 을 다시 순회하면서 join으로 붙여야하나 고민했는데 map에 ''.join 도 가능하더라. 왕 편리함!


# 다른 사람의 풀이
def solution(numbers):
    a = set()
    for i in range(len(numbers)):
        a |= set(map(int, map("".join, itertools.permutations(numbers, i + 1))))

    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(2 * i, max(a) + 1, i))

    return len(a)
# Note: 사실상 원리는 같다. 근데 더 간결하고 축약시킨 것.
#       주의해서 볼 점은 |= 부분. set끼리는 += 가 안되는데 |= 와 -=는 가능하다. 그리고 set()안에 바로 range를 쓴 것도 기억해두면 유용하게 쓸 것 같다.
#       특히나 마지막 줄은 리스트 컴프리헨션처럼 j for j in range()로 가능하려나 생각했는데 그냥 저렇게 간단히 쓸 수 있다.