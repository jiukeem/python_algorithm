# my solution
def solution(n):
    if n ** 0.5 - int(n ** 0.5) == 0:
        return int((n ** 0.5 + 1) ** 2)
    else:
        return -1
# Status: Accepted
# Note: 이프문을 if n ** 0.5 % 1 == 0: 으로 할 수도 있다.