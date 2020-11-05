# coding=utf-8
# my solution
def solution(n, words):
    idx = None
    for i in range(1, len(words)):
        if words[i - 1][-1] != words[i][0] or words[i] in words[:i]:
            idx = i + 1
            break
    else:
        return [0, 0]

    ans_1 = idx % n if idx % n != 0 else n
    ans_2 = idx // n if idx % n == 0 else idx // n + 1
    return [ans_1, ans_2]
# Status: Accepted
# Note: 나는 순서를 생각해서 idx를 i+1로 설정해준 뒤, 조금 복잡하게 계산했는데(그래서 idx 변수도 따로 만들어야 했음) 오히려 i를 그대로 쓰면 밑과 같이 더 간단히 쓸 수 있다.


def solution(n, words):
    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0] or words[i] in words[:i]:
            return [i%n + 1, i//n + 1]
    else:
        return [0, 0]