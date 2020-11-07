# coding=utf-8
# my solution
def solution(number, k):
    i, count = 0, 0
    while True:
        if int(number[i]) < int(number[i+1]):
            number = number[:i] + number[i+1:]
            count += 1
            i = 0
        else:
            i += 1
        if count == k:
            break

    return number
# Status: Timeout
# Algorithm: Greedy
# Note: 가장 큰 문제는 i를 0으로 돌려서 다시 처음부터 체크하게 하는 부분이다. number 가 최대 1000000자리이기 때문에 타임아웃 당하는 테스트케이스가 생긴다
#       그렇다고 -= 1 로 하면 number = number[] + number[] 부분과 상충해서 문제가 생긴다. 다른 방법을 강구해봐야 할 듯!

def solution(number, k):


