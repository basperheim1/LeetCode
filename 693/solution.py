class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binaryRep = bin(n)
        for i in range(3, len(binaryRep)):
            if binaryRep[i] == binaryRep[i-1]:
                return False

        return True 

