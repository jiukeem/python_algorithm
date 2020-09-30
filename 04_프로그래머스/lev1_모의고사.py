def solution(answers):
    pat_1 = [1, 2, 3, 4, 5]
    pat_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pat_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0, 0, 0]
    ans = []

    for idx, a in enumerate(answers):
        if pat_1[idx % len(pat_1)] == a:
            scores[0] += 1
        if pat_2[idx % len(pat_2)] == a:
            scores[1] += 1
        if pat_3[idx % len(pat_3)] == a:
            scores[2] += 1

    for i, s in enumerate(scores):
        if s == max(scores):
            ans.append(i + 1)

    return ans
# Status: Accepted
# Note: 내용이 어려운건 아니었는데 도저히 깔끔하게가 안짜져서 다른 사람들 코드를 보고 다시 짰다.
#       pattern으로 비교하지 않고 세명의 답을 전부 짜놓으려 한 부분이 좀 지저분해 진 것 같다.(최대 10000개라서 공간복잡도도 너무 커진다)


# 예전에 짜다가 떄려친 코드
def solution(answers):
    n = len(answers)
    anss = [None for _ in range(3)]
    anss[0] = [i % 5 + 1 for i in range(n)]
    anss[1] = [2, 1, 2, 3, 2, 4, 2, 5] * (n // 8 + 1)
    anss[2] = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (n // 10 + 1)

    anss[1] = anss[1][:n]
    anss[2] = anss[2][:n]

    scores = [0, 0, 0]
    for i in range(3):
        score = 0
        for j in answers:
            if answers[j] == anss[i][j]:
                score += 1

    max(scores)]
