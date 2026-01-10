class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n = len(s1)
        m = len(s2)

        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m+1):
            for j in range(n+1): 
                if i == 0 and j == 0: 
                    continue

                elif i == 0: 
                    dp[0][j] = dp[0][j-1] + ord(s1[j-1])

                elif j == 0: 
                    dp[i][0] = dp[i-1][0] + ord(s2[i-1])

                else:
                    if s1[j-1] == s2[i-1]:
                        dp[i][j] = dp[i-1][j-1]

                    else:
                        dp[i][j] = min(dp[i-1][j] + ord(s2[i-1]), dp[i][j-1] + ord(s1[j-1]))
                        
        return dp[m][n]

