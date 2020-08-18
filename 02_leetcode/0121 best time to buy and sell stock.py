# 브루트포스
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i, price in enumerate(prices):
            for selling_price in prices[i+1:]:
                max_profit = max(max_profit, selling_price - price)

        return max_profit
# 타임아웃


# 책 풀이
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit
# 이렇게 간결한 코드라니 너무 좋다.ㅜㅜ 
# 나는 아직 컴퓨터식 사고가 잘 안되나보다. 한번에 답을 찾아낼 수 있는 수학적 방식으로만 접근한다. max로 계속 따져주면 될 것을..
# 나는 처음에 min_price를 max(prices)로 설정했는데 prices가 빈리스트[]로 들어올 경우 에러가 난다.
# sys.maxsize 라는 개념을 배웠땅. 혹은 float('inf')로 해줄 수도 있다고 한다
# 책에 따르면 파이썬은 무한대의 값을 지정할 수 있는 숫자형을 사용하기 때문에 sys.maxsize가 큰 의미가 없다고 한다
# 하지만 코딩테스트는 모든 언어에 대응하는 테스트케이스만 나오므로 이렇게 하는거라고 함.
# 물론 문제에서 인풋 범위가 제시되어있으면 그 값을 쓰면 된다.
# runtime, memory usage 모두 적당하다