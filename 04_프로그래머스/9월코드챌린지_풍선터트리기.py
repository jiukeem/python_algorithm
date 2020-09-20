def solution(a):
    prefix_min, suffix_min, n = a[0], a[-1], len(a)
    mins = [[None, None] for _ in range(n)]

    for i in range(n - 1):
        prefix_min = min(prefix_min, a[i])
        suffix_min = min(suffix_min, a[n - 1 - i])
        mins[i + 1][0] = prefix_min
        mins[n - 2 - i][1] = suffix_min

    ans = 0
    for m, num in zip(mins, a):
        if None in m or num <= m[0] or num <= m[1]:
            ans += 1

    return ans
# Status: Accepted
# Note: 해설을 보고 푼 답안. 챌린지 때는 divide and conquer 로 시도했었다. 그 방법으로는 자꾸 예외가 생겼었음
#       주어진 문제의 조건을 단순화하는 연습이 필요할 것 같다.
#       나는 조금 읽기 힘들어도 prefix 와 suffix 계산을 하나의 포문에 같이 돌렸는데
#       같은 코드가 반복되더라도 더 이해가 잘되게 따로따로 두번 쓰는게 더 좋은 코드일까?
#       같은 O(n)이더라도 prefix, suffix min 을 계산하면서 동시에 체크해주는 방식이 더 빠르겠다. 흠 괜히 더 복잡해지려나?

def solution(a):
    n = len(a)
    prefix_min, suffix_min = a[0], a[-1]
    mins = [[None, None] for _ in range(n)]

    for i in range(n):
        prefix_min = min(prefix_min, a[i])
        mins[i][0] = prefix_min

    for i in range(n-1, -1, -1):
        suffix_min = min(suffix_min, a[i])
        mins[i][1] = suffix_min

    ans = 0
    for i in range(n):
        if a[i] <= mins[i][0] or a[i] <= mins[i][1]:
            ans += 1

    return ans
# Status: Accepted
# Note: 이게 훨씬 읽기 쉽다. 그리고 왠지 모르겠는데 이게 좀 더 빠르다