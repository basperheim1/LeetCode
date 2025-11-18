class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)

        one_count = 0
        for i in range(n-2, -1, -1):
            if bits[i] == 1: 
                one_count += 1

            else:
                break 

        return one_count % 2 == 0
