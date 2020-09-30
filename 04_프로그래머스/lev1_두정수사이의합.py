def solution(a, b):
    return sum(range(a, b + 1)) if a <= b else sum(range(b, a + 1))
# 예에 한줄로 깔끔

# 다른 사람들꺼 보니 이 코드도 좋아보인다.
def solution(a, b):
    return sum(range(min(a, b), max(a, b)+1))
