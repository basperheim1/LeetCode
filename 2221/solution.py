class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        parentArr = nums

        while len(parentArr) > 1: 
            newArr = []
            for i in range(len(parentArr)): 
                if i == 0:
                    newArr.append(parentArr[i])

                elif i == len(parentArr) - 1:
                    newArr[i-1] += parentArr[i]

                else:
                    newArr[i-1] += parentArr[i]
                    newArr.append(parentArr[i])

            parentArr = newArr

        return parentArr[0] % 10


