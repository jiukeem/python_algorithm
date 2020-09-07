class Solution:
    def fib(self, N: int) -> int:
        table = {
            0: 0,
            1: 1
        }

        for i in range(2, N + 1):
            table[i] = table[i - 1] + table[i - 2]

        return table[N]
# Status: Accepted
# Algorithm: Tabulation
# Time Complexity: O(N)
# Runtime: 24ms (top 3.9%)
