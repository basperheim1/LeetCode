class Solution:

    def determineDivisors(self, num, divisors) -> Set[int]: 
        if num in divisors: 
            return divisors[num]

        divisors[num] = set([num, 1])

        for i in range(2, num // 2):
            if num % i == 0: 
                additional_divisors = self.determineDivisors(i, divisors).union(self.determineDivisors(num // i, divisors))
                divisors[num] = divisors[num].union(additional_divisors)
                return divisors[num]

        return divisors[num]

        

    def sumFourDivisors(self, nums: List[int]) -> int:
        nums.sort()
        divisors = dict()
        total = 0

        for num in nums: 
            if num not in divisors:
                self.determineDivisors(num, divisors)
            if len(divisors[num]) == 4:
                    total += sum(divisors[num]) 

        return total 

