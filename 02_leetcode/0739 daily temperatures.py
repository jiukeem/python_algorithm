# 내 풀이
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = [(0, 0)]
        # 첫번째 예외처리를 해주기 보다는 그냥 없어질 값을 넣어줬다
        result = {}
        for i, temp in enumerate(T):
            while temp > stack[-1][1]:
                result[stack[-1][1]] = (i - stack.pop()[0])
                stack.append((i, temp))
                # 새로 들어오는 값이 stack의 마지막 값보다 큰 경우,
                # 마지막 값은 빼주고 인덱스 차이를 result에 기록
                # 새로 넣을 값보다 큰 값을 만날 때까지 반복
            stack.append((i, temp))

        output  = []
        for key, value in sorted(result.keys()):
            output.append(value)
            # 인덱스 순으로 정렬해서 인덱스는 버리고 값만 기록
        return output
# 잘 짠거 같은데 에러가 난다.. 어려워 흑흑
# 일단 stack의 첫번째 값으로 넣어준 애는 첫 for문에서 빠질 것이며, result에 0, 0 으로 기록된다.
# 첫번째 요소가 stack에서 빠질 때 result[0]의 값이 업데이트 되므로 자연스럽게 사라진다.


# 책 풀이



