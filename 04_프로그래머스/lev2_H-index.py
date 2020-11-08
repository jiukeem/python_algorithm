# coding=utf-8
# my solution
def solution(citations):
    citations = sorted(citations, reverse=True)
    for i in range(len(citations) - 1, -1, -1):
        if citations[i] >= i + 1:
            return i + 1

    return 0
# Status: Accepted
# Note: 인용 횟수가 전부 0인 경우를 생각해서 마지막에 return 0을 해줘야한다. 포문을 다 돌아도 이프문을 한번도 만족하지 못하는 경우