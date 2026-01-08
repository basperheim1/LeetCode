class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)

        dp = [[0]*n for _ in range(m)]

        for i in range(0, m):
            for j in range(0, n):

                if i == 0 and j == 0: 
                    dp[i][j] = nums1[0]*nums2[0]

                elif i == 0: 
                    dp[i][j] = max(dp[i][j-1], nums1[i]*nums2[j])

                elif j == 0: 
                    dp[i][j] = max(dp[i-1][j], nums1[i]*nums2[j])

                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j], dp[i-1][j-1] + nums1[i]*nums2[j], nums1[i]*nums2[j])

        return dp[m-1][n-1]

