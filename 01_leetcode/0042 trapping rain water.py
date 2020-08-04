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
# 코드는 내가 의도한대로 짰는데 아예 풀이방식이 틀렸음. 반영하지 못하는 예외가 너무 많다.
# 다른 풀이방법을 생각해보자~~




