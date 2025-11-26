class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        remainder = 0
        digits = 1
        seen_remainders = set()

        while True: 
            remainder = (remainder*10 + 1) % k
            if remainder == 0:
                return digits 

            if remainder in seen_remainders: 
                return -1

            digits += 1
            seen_remainders.add(remainder)


            
