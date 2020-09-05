# my solution
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1 and len(trust) == 0:
            return 1

        def check(num):
            for pair in trust:
                if pair[0] == num:
                    return False
            return True

        from collections import defaultdict
        trusted = defaultdict(int)
        for pair in trust:
            trusted[pair[1]] += 1

        candidates = []
        for num in trusted:
            if trusted[num] == N - 1:
                candidates.append(num)

        for num in candidates:
            result = check(num)
            if result == True:
                return num

        return -1
# Status: Accepted
# Algorithm:
# Time Complexity: O(n^2)
# Runtime: 776ms (top 10.2%)
# Intuition: town judge가 있다면 trust안의 list에서 두번째 자리에는 N-1번 등장할 것이고, 첫번째 자리에는 한번도 등장하지 않을 것이다.
#            trust를 살펴보면서 각 번호의 사람을 믿고 있는 사람이 몇명인지 센다(trusted 딕셔너리)
#            그 중에 N-1 값을 가지고 있는 사람들을 candidates 리스트로 모은다.
#            후보자들에 대해서 한번 더 포문을 돌리면서 한번이라도 첫번째 자리에 등장하면 제끼고 한번도 등장하지 않으면 바로 그 사람을 return 한다.
# Note: 단계가 많고, 예외처리도 따로 해줘야 하고, 새로운 함수도 만들었고, 포문도 여러번 돌려서 굉장히 안좋은 코드라고 생각하며 짰는데 시간/공간 복잡도 모두 잘 나와서 얼떨떨하다.
#       더 깔끔하게 할 수 있을 것 같은데. trusted를 만들면서 pair[0]에 등장하면 바로 뺴버리는 걸 동시에 할 수 있는지 해보자.


# my solution 2
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1 and len(trust) == 0:
            return 1

        trusted = defaultdict(int)
        for pair in trust:
            trusted[pair[1]] += 1

        for pair in trust:
            if pair[0] in trusted:
                del trusted[pair[0]]

        for num, freq in trusted.items():
            if freq == N - 1:
                return num

        return -1
# Status: Accepted
# Algorithm:
# Time Complexity: O(n^2)
# Runtime: 736ms (top 0.04%)
# 오예!
