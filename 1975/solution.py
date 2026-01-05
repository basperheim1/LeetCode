class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        matrix_sum = 0
        min_element = abs(matrix[0][0])
        negative = False 

        for i in range(m):
            for j in range(n):
                element = matrix[i][j]
                if element < 0:
                    negative = not negative
                    element *= -1 

                matrix_sum += element 
                if element < min_element: 
                    min_element = element 

        if negative: 
            return matrix_sum - 2*min_element

        return matrix_sum 

                
