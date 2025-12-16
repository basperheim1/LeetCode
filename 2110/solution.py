class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        total = 1
        current_total = 1
        for i in range(1, n): 
            if prices[i] - prices[i-1] == -1:
                current_total += 1

            else:
                current_total = 1

            total += current_total

        return total 

