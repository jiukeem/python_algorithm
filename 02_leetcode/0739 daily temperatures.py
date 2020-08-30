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


# 0830 다시도전
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        result = {}
        for i, temp in enumerate(T):
            while stack and temp > stack[-1][1]:
                to_pop = stack.pop()
                result[to_pop[0]] = i - to_pop[0]
            stack.append([i, temp])

        while stack:
            to_pop = stack.pop()
            result[to_pop[0]] = 0

        output  = []
        for key in sorted(result.keys()):
            output.append(result[key])
            # 인덱스 순으로 정렬해서 인덱스는 버리고 값만 기록
        return output
# 위에 내가 썼던 코드가 어디가 틀렸는지 눈에 보여서 수정해줬다 기쁘당
# memory usage가 좀 높다. stack은 필수적인 부분이라서 괜찮은데 output과 result가 굳이 두번이나 기록될 필요는 없어보인다.


# 책 풀이
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        answer = [0] * len(T)
        stack = []
        for i, cur in enumerate(T):
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                answer[last] = i = last
            stack.append(i)
            
        return answer
# 오! 딱 내가 부족한 부분을 깔끔히 해결한 코드다.
# 우선 stack에 기온을 저장하지 않고 매번 접근 연산으로 불러온다.
# 접근 연산은 O(1)이고 answer에 값을 업데이트 해줄 때는 온도가 필요하지 않으므로 이게 더 좋은 방식인 것 같다.
# 그리고 나와 다르게 결과값을 저장하는 변수가 한개다. 
# 저렇게 0으로 디폴트 된 리스트에 인덱스로 접근해서 업데이트 해주면 나중에 다시 정렬할 일도, 
# dict를 순환하면서 value를 빼올 일도, stack에 남은 값들(더 따뜻한 날이 없어서 0으로 기록해줘야하는 날들)을 처리해줄 필요도 없다.
# 시간도 아끼고 코드도 짧고 공간도 절약하는 참 좋은 방법이다.









