class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        low_val = 0
        high_val = 10**10
        mid = 0

        while low_val < high_val: 
            mid = (high_val + low_val) / 2
            
            area_below = 0
            area_above = 0

            for square in squares: 
                if mid < square[1]:
                    area_above += square[2]**2

                elif square[1] + square[2] < mid: 
                    area_below += square[2]**2

                else:
                    ratio_above = (square[1] + square[2] - mid) / square[2]
                    ratio_below = 1 - ratio_above
                    area_above +=  ratio_above*(square[2]**2)
                    area_below += ratio_below*(square[2]**2)

            if area_above > area_below: 
                low_val = mid + 10**-6

            else: 
                high_val = mid - 10**-6
        
        return mid 
