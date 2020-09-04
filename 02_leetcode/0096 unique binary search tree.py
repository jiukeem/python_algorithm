# my solution
class Solution:
    def numTrees(self, n: int) -> int:
        table = {
            0: 1,
            1: 1,
        }

        for i in range(2, n+1):
            res = 0
            for j in range(i):
                res += table[j] * table[i-j-1]

            table[i] = res

        return table[n]
# Status: Accepted
# Algorithm: Dynamic Programming(Tabulation)
# Time Complexity: O(n^2)
# Runtime: 24ms (top 4.4%)
# 잘했어!