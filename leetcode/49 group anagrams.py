# 내 풀이
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 인풋을 알파벳순으로 정렬
        sorted_words = []
        for word in strs:
            sorted_words.append(''.join(sorted(word)))

        # 정렬된 리스트에서 값이 같은 인덱스들을 딕셔너리의 value로 모음
        anagram = {}
        for i in range(len(sorted_words)):
            if sorted_words[i] in anagram.keys():
                anagram[sorted_words[i]].append(strs[i])
            else:
                anagram[sorted_words[i]] = [strs[i]]

        # 딕셔너리의 value만 출력
        return anagram.values()
# runtime 상위 5프로, memory usage 상위 50프로


# 책 풀이
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)

        return anagrams.values()
# 내 풀이와 과정은 똑같지만 두가지가 다르다.
# sorted_words 리스트를 만들 필요없이 바로 딕셔너리의 키로 넣어버림
# 새로 등장하는 key에 대해 에러가 나지 않게 defaultdict 를 사용함 (내가 if로 해결한 부분)
# defaultdict 객체는 존재하지 않는 키에 대해, 에러가 나는 대신 디폴트값을 기준으로 value를 생성해준다.
# 즉 여기서 defaultdict 안에 list를 입력했으므로 append 구문을 돌릴 때 존재하지 않는 키에 대해서는 빈 리스트 []에 append 해준다
# runtime은 내것보다 조금 빠르고, 메모리는 더 차지함