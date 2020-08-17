# 내 풀이
class Solution:
    def trap(self, height: List[int]) -> int:
        extreme_point = []

        # 양쪽 끝에 대한 예외처리
        if height[0] > height[1]:
            extreme_point.append(heigt[0])
        if height[-1] > height[-2]:
            extreme_point.append(height[-1])

        # height[i]가 극소, 극대점일 때 extreme_point 에 인덱스 추가
        for i in range(1, len(height)-1):
            if (height[i-1] > height[i] and height[i+1] > height[i]) or \
                    (height[i-1] < height[i] and height[i+1] < height[i]):
                extreme_point.append(height[i])

        # 극소 양쪽의 극대를 비교해서 (더 작은 극대 - 극소) * 2 가 그 부근 물의 양
        total_water = 0
        for i in range(1, len(extreme_point), 2):
            max_point = min(extreme_point[i-1], extreme_point[i+1])
            min_point = extreme_point[i]
            water = 2 * (max_point - min_point)
            total_water += water

        return total_water
# 코드는 내가 의도한대로 짰는데 아예 풀이방식이 틀렸음. 반영하지 못하는 예외가 너무 많다. W자 형태라던지 등등
# 다른 풀이방법을 생각해보자~~

# 이거 너무 어렵당ㅜㅜ 책에서는 투포인터와 스택을 쓰는 방법 두가지를 알려주는데 둘 다 이해가 잘 안간다ㅠㅜ
# 일단 패스..


# 브루트포스 풀이 
class Solution:
    def trap(self, height: List[int]) -> int:

        rain = 0
        for i, h in enumerate(height):
            while True:
                condition = 0
                for j, height_left in enumerate(height[:i]):
                    if height_left > h:
                        condition += 1
                        break

                for k, height_right in enumerate(height[i + 1:]):
                    if height_right > h:
                        condition += 1
                        break

                if condition == 2:
                    rain += 1
                else:
                    break

                h += 1

        return rain
# O(n^3) 이라 time limit exceeded 지만 짤 수 있다는 것만으로도 일단은 발전이다


# 좀 더 발전한 브루트포스 하나 더!
class Solution:
    def trap(self, height: List[int]) -> int:
        rain = 0
        for i, h in enumerate(height):
            max_left = 0
            max_right = 0
            for j, height_left in enumerate(height[:i]):
                max_left = max(height_left, max_left)
            for k, height_right in enumerate(height[i+1:]):
                max_right = max(max_right, height_right)

            if max_right > h and max_left > h:
                rain += min(max_left, max_right) - h

        return rain
# O(n^2) 이다! 여전히 타임아웃이지만 그래도ㅎㅎ




