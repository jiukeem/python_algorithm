class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],

        }