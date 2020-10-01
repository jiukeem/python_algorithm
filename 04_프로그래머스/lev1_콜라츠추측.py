# my solution
def solution(num):
    for i in range(500):
        if num == 1:
            return i
        if num % 2 == 0:
            num = num // 2
        else:
            num = (num * 3) + 1

    return -1
# Status: Accepted
# Note: 처음에는 while문을 생각했다가 for문이 더 깔끔할 것 같아 바꿈
#       그리고 num == 1 조건을 앞에 따지느냐(i 반환) num 계산 한 뒤에 따지느냐(i + 1 반환) 가 아무 차이 없을거라고 생각했는데,
#       지금보니까 이 방식이 num = 1로 주어진 경우까지 커버할 수 있어서 맞는 방식이다. 차이가 있었네