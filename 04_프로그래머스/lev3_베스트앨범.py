# my solution
from collections import defaultdict

def solution(genres, plays):
    n = len(plays)
    genres_sum = defaultdict(list)
    for i, genre, play in zip(range(n), genres, plays):
        genres_sum[genre].append([play, i])

    genres_sum = sorted(genres_sum, key=lambda genre: sum(genres_sum[genre][:][0]), reverse=True)
    for plays in genres_sum.values():
        plays = sorted(plays, reverse=True)

    ans = []
    for plays in genre_sum.values():
        ans.append(plays[0][1])
        if len(plays) > 1:
            ans.append(plays[1][1])

    return ans
# sorted에서 딕셔너리가 리스트로 전환되어 버림. 한번 더 도전!

from collections import defaultdict


def solution(genres, plays):
    n = len(plays)
    tot = defaultdict(list)

    for genre, play, i in zip(genres, plays, range(n)):
        tot[genre].append((plays, i))

    for pairs in tot.values():
        pairs = sorted(pairs, key=lambda pair: (pair[0], pair[1]), reverse=True)
    # 딕셔너리 tot에 대해 gerne : [(play, i), (play, i)], gerne: [], gerne: [] ... 정렬
    # play가 높은 순, play가 같을 경우 i가 높은 순으로 정렬완료

    return tot.values()

    ord = defaultdict(int)
    for genre, play in zip(genres, plays):
        ord[genre] += play

    ge_or = sorted(ord.items(), key=lambda x: x[1], reverse=True)

    ans = []
    for genre, _ in ge_or:
        ans.append(tot[genre][0][1])
        if len(tot[genre]) > 1:
            ans.append(tot[genre][1][1])

    return ans
# 에러는 안나지만 제대로 된 값이 안나온다. 어디가 문제일까~



