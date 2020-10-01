# my solution
def solution(n):
    return sum([int(i) for i in str(n)])
# Status: Accepted
# Note: 한줄로 간단하긴 하지만 int로 주어진걸 str로 바꿨다가 다시 int로 변환하는게 좀 별로다.


# map 사용
def solution(n):
    return sum(map(int, str(n)))
# map은 어렵지도 않은데 언제나 생각을 못해낸다. 흠
# map(f, iterable)은 이터러블의 각 요소가 함수 f에 의해 수행된 결과를 묶어서 return


# 다른 사람의 solution
def solution(n):
    if n < 10:
        return n
    return (n % 10) + solution(n // 10)
# 이거지! 재귀 너무 멋지당 흑흑
# 포문을 돌릴 수 있는 문제는 재귀를 쓸 수 있다. 상황에 맞게 더 깔끔하게 구현가능한 걸 쓰면 되는 것.
# n의 범위는 최대 9자리까지이므로 재귀를 돌리기에 문제 없다.