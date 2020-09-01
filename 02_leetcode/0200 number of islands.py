# 문제가 너무 귀엽다! 1로 이루어진 섬이라니~.~

class Solution:
    def dfs(self, i, j, grid):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return

        grid[i][j] = -1
        # 한번 본 곳은 다시 탐색하지 않기 위해 value 변경

        self.dfs(i+1 ,j, grid)
        self.dfs(i-1, j, grid)
        self.dfs(i, j+1, grid)
        self.dfs(i, j-1, grid)


    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(i, j, grid)
                    num_islands += 1

        return num_islands
# 책의 풀이를 읽고 내가 다시 짜본 코드다. 문제보고 접근 방식을 전혀 모르겠어서 약간 띠용했달까
# 비선형구조 문제를 처음 풀어서 그런 것 같다. dfs를 이런 데에 쓸 수 있구나
# 책의 풀이에서는 중첩함수를 써서 조금 더 간단하게 구현했다.


# 책 풀이 - dfs
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j):
            if i < 0 or i >= len(grid) or \
                j < 0 or j >= len(grid[0]) or \
                grid[i][j] != '1':
                    return

            grid[i][j] = 0
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1

        return count
# 중첩함수로 dfs를 numIslands 안에 구현하면 grid를 따로 파라미터로 넣어주지 않아도 된다.
