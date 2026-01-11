class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    if j == 0: 
                        dp[i][j] = 1

                    else:
                        dp[i][j] = dp[i][j-1] + 1

                else:
                    dp[i][j] = 0

        max_area = 0
        for i in range(m):
            for j in range(n):
                min_width = dp[i][j]
                current_area = 0 
                for k in range(i, -1, -1):
                    min_width = min(min_width, dp[k][j])
                    current_area = max(current_area, min_width*(i - k + 1))
                    if min_width == 0: 
                        break

                max_area = max(current_area, max_area)

        return max_area

