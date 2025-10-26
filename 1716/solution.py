class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        bump = 0
        for i in range(n):
            if i % 7 == 0: 
                bump += 1

            addition = i % 7 + bump
            total += addition

        return total 
