class Cell: 
    def __init__(self): 
        self.is_guarded = False
        self.is_wall = False 
        self.is_guard = False
        self.north_guarded = False
        self.south_guarded = False
        self.east_guarded = False 
        self.west_guarded = False 



class Solution:

    def exploreNeighbors(self, m, n, cells):

        current_y = m - 1
        current_x = n
        while current_y >= 0: 

            current_cell = cells[current_y][current_x]

            if current_cell.is_wall or current_cell.is_guard: 
                break


            current_cell.is_guarded = True 
            if current_cell.north_guarded: 
                break 

            current_cell.north_guarded = True 
            current_y -= 1

        current_y = m 
        current_x = n - 1
        while current_x >= 0: 
            current_cell = cells[current_y][current_x]

            if current_cell.is_wall or current_cell.is_guard: 
                break

            current_cell.is_guarded = True 
            if current_cell.west_guarded: 
                break 

            current_cell.west_guarded = True 
            current_x -= 1

        current_y = m + 1
        current_x = n
        while current_y < len(cells): 
            current_cell = cells[current_y][current_x]

            if current_cell.is_wall or current_cell.is_guard: 
                break

            current_cell.is_guarded = True 
            if current_cell.south_guarded: 
                break 

            current_cell.south_guarded = True 
            current_y += 1

        current_y = m 
        current_x = n + 1
        while current_x < len(cells[0]): 
            current_cell = cells[current_y][current_x]

            if current_cell.is_wall or current_cell.is_guard: 
                break

            current_cell.is_guarded = True 
            if current_cell.east_guarded: 
                break 

            current_cell.east_guarded = True 
            current_x += 1

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        cells = [[Cell() for i in range(n)] for j in range(m)]

        for wall in walls: 
            cells[wall[0]][wall[1]].is_wall = True 

        for guard in guards: 
            cells[guard[0]][guard[1]].is_guard = True 

        for guard in guards:
            self.exploreNeighbors(guard[0], guard[1], cells)

        total = 0
        for i in range(m):
            for j in range(n):
                if not cells[i][j].is_wall and not cells[i][j].is_guard and not cells[i][j].is_guarded: 
                    total += 1

        return total 

