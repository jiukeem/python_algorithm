class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_words = []
        for word in strs:
            sorted_word = word.split().sort()
            sorted_words.append(sorted_word)

        return sorted_words