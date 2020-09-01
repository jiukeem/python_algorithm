# 내 풀이 - 큐 이용
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict
        from collections import deque
        num_in_q = defaultdict(int)
        # 각 char이 현재 큐 안에 들어있는 횟수
        result = 0
        queue = deque()
        for char in s:
            queue.append(char)
            while num_in_q[char] > 0:
                # 큐 안에 char이 없어질 때까지
                deleted_char = queue.popleft()
                num_in_q[deleted_char] -= 1
            num_in_q[char] += 1
            result = max(result, len(queue))

        return result
# 우와 성공!
# runtime 상위30프로 memory usage 상위 70프로
# 공간복잡도는 O(n)인 num_in_q 딕셔너리와 O(n)인 큐가 있어서 O(n)
# 시간복잡도는 최악의 경우 O(n^2)일 듯


# 책 풀이
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        maxlen = 0
        start = 0
        for i, char in enumerate(s):
            if char in used and used[char] >= start:
                start = used[char] + 1
            used[char] = i
            maxlen = max(maxlen, i - start + 1)

        return maxlen
# 내가 짠 코드와 비슷해서 기분이 좋당
# 책의 코드가 더 나은 부분이 있는데 딕셔너리에 등장횟수 대신 인덱스를 value로 넣는 부분!
# 나도 어차피 value(등장횟수)가 1이 넘지 않게 관리하고 있으므로 인덱스가 더 나은 선택이다.
# 그리고 while 문을 쓸 필요없이 바로 해당 인덱스로 갈 수 있어서 시간이 절약된다.



