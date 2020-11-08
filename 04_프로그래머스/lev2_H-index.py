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

# 다른사람의 풀이
def solution(citations):
    citations.sort(reverse=True)
    return max(map(min, enumerate(citations, start=1)))
# Note: 일단 간결하고 가독성도 나쁘진 않은데 시간복잡도가 너무 크다. 내 풀이랑 비교해서 약 6배정도.
#       여기서 배울 점은 map의 활용방법. int, str도 사실 함수인데 맨날 데이터 타입 변환에만 사용해서 다른 함수를 쓰는걸 떠울리기가 어렵다.
#       그리고 enumerate에 start 키워드는 처음 알았다. 언젠가 활용해보자