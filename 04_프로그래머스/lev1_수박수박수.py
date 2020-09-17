def solution(n):
    count = n // 2
    ans = ''
    for _ in range(count):
        ans += '수박'
    if n % 2 == 1:
        ans += '수'

    return ans