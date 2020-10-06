# my solution
def solution(brown, yellow):
    # (w - 2) * (h - 2) = yellow
    # (w + h - 2) * 2 = brown

    width = 1 + 0.25 * brown + 0.5 * ((0.25 * (brown ** 2) - 2 * brown - 4 * yellow + 4) ** 0.5)
    height = 1 + 0.25 * brown - 0.5 * ((0.25 * (brown ** 2) - 2 * brown - 4 * yellow + 4) ** 0.5)
    return [int(width), int(height)]
# Status: Accepted
# Intuition: 간단한 연립방정식이므로 근의 공식을 써줬다.
#            이 문제는 완전탐색 문제로 분류되어 있다. 이쪽으로도 생각해보자

# 완전 탐색으로 푼 코드 (다른 사람의 코드 참고)
def solution(brown, yellow):
    for i in range(1, brown):
        if brown % i == 0:
            if yellow // i + 2 == 0.5 * brown - i:
                return [yellow // i + 2, i + 2]
# Status: Accepted
# Note: 위의 두 방정식을 이용한 것으로 사실상 풀이는 같다. 위가 바로 답을 계산한다면 얘는 1부터 완전탐색으로 탐색해나감
#       답 i는 언제나 두 정답 중 더 작은 수이므로 height로 들어간다. (i는 h - 2를 치환한 것(
#       다만 좀 더 생각해봐야할 점은 range 범위인데, 일단 brown까지 잡는 것은 너무 낭비다 (코드에 문제가 없다면 사실 똑같겠지만 문제가 생길경우 너무 시간을 낭비한다.)
#       i = h - 2 라고 했을 때 i가 가장 클 수 있는 경우는 width == height 인 경우, 즉 루트 yellow 이다.
#       그래서 범위를 range(1, int(yellow ** 0.5) + 1)로 해주면 가장 효율적이다.

