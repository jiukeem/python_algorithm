def solution(n):
    return int(''.join(sorted([i for i in str(n)], reverse=True)))
# Status: Accepted
# Note: 틀린 부분은 없는데 비효율적인 부분은 있다.
#       str을 sorted하면 list로 나오고, 또 리스트 컴프리헨션은 list(str(n))으로 해도 된다.
#       즉, 다음처럼 쓰는게 맞다.

# 한번 개선시키면
def solution(n):
    return int(''.join(sorted(list(str(n)), reverse=True)))

# 한번 더 개선시켜서
def solution(n):
    return int(''.join(sorted(str(n), reverse=True)))