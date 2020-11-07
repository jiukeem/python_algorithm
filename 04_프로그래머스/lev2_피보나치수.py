# coding=utf-8
# my solution
def solution(n):
    current, prev = 1, 0
    for _ in range(n):
        current, prev = current + prev, current

    return prev % 1234567
# Status: Accepted
# Note: 왜 lev2에 있지? 응용이 아닌 너무 기본적인 피보나치 문제