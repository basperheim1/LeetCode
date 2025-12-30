class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        count = 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m-2):
            for j in range(n-2):
                nums = set()
                for k in range(3):
                    for l in range(3):
                        nums.add(grid[i+k][j+l])

                if len(nums) == 9 and max(nums) == 9: 
                    left_diagonal = grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2]
                    right_diagonal = grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j]
                    h_top = grid[i][j] + grid[i][j+1] + grid[i][j+2]
                    h_middle = grid[i+1][j] + grid[i+1][j+1] + grid[i+1][j+2]
                    h_bottom = grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
                    v_left = grid[i][j] + grid[i+1][j] + grid[i+2][j]
                    v_middle = grid[i][j+1] + grid[i+1][j+1] + grid[i+2][j+1]
                    v_right = grid[i][j+2] + grid[i+1][j+2] + grid[i+2][j+2]

                    if left_diagonal == right_diagonal == h_top == h_middle == h_bottom == v_left == v_middle == v_right: 
                        count += 1

        return count 
