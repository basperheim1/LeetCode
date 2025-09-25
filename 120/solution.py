class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        above_min = [triangle[0][0]]
        current_min = [0]*(len(above_min) + 1)

        for i in range(1, len(triangle)):
            current_dimension = len(current_min)
            for j in range(current_dimension): 
                if j == 0:
                    current_min[0] = triangle[i][j] + above_min[0]

                elif j == current_dimension - 1:
                    current_min[j] = triangle[i][j] + above_min[j-1]

                else:
                    current_min[j] = triangle[i][j] + min(above_min[j-1], above_min[j])

            above_min = current_min
            current_min = [0]*(len(above_min) + 1)


        return min(above_min)