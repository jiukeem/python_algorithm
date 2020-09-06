# my solution
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0 or '0' in digits or '1' in digits:
            return None

        keypad = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        def permutation(digits, keypad, idx=None):
            if idx is None:
                idx = len(digits) - 1

            if idx == 0:
                return keypad[digits[0]]
            else:
                res = []
                for alp in keypad[digits[idx]]:
                    res += [prev + alp for prev in permutation(digits, keypad, idx - 1)]
                return res

        return permutation(digits, keypad)
# Status: Accepted
# Algorithm: Recursion (Divide and Conquer)
# Time Complexity: O(3^n)
# Runtime: 28ms (top 16.6%)


