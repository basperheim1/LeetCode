class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[None for i in range(n)] for j in range(m)]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i][j] = dict()
                current_value = grid[i][j]
                found = False 
                if i + 1 != m:
                    found = True
                    for key, value in dp[i+1][j].items():
                        dp[i][j][(key + current_value) % k] = value 

                if j + 1 != n: 
                    found = True 
                    for key, value in dp[i][j+1].items():
                        if ((key + current_value) % k) in dp[i][j]:
                            dp[i][j][(key + current_value) % k] += value 

                        else:
                            dp[i][j][(key + current_value) % k] = value 

                if not found: 
                    dp[i][j][current_value % k] = 1
        if 0 in dp[0][0]:
            return dp[0][0][0] % (10**9 + 7)

        return 0
