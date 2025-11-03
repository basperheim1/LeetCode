class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        total = 0
        remaining_index = None 
        for i in range(1, len(colors)):
            if colors[i] == colors[i-1]:
                
                if remaining_index is not None: 
                    if neededTime[remaining_index] > neededTime[i]:
                        total += neededTime[i]

                    else:
                        total += neededTime[remaining_index]
                        remaining_index = i

                else: 
                    print("ONCE")
                    if neededTime[i] > neededTime[i-1]:
                        total += neededTime[i-1]
                        remaining_index = i 

                    else:
                        total += neededTime[i]
                        remaining_index = i - 1

            else:
                remaining_index = i

        return total
