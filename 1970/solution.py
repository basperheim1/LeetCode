class Solution:

    def getNeighbors(self, row, col, cell_y, cell_x, dead_cells): 
        neighbor_cells = []
        if cell_y != 0: 
            neighbor_cells.append((cell_y-1, cell_x))

        if cell_x != 0: 
            neighbor_cells.append((cell_y, cell_x-1))

        if cell_y != row-1: 
            neighbor_cells.append((cell_y+1, cell_x))

        if cell_x != col-1: 
            neighbor_cells.append((cell_y, cell_x+1))

        alive_cells = []
        for cell in neighbor_cells: 
            if cell not in dead_cells:
                alive_cells.append(cell)

        return alive_cells 

    def exploreNeighbors(self, row, col, cell_y, cell_x, dead_cells, reachable_cells): 
        neighbors = self.getNeighbors(row, col, cell_y, cell_x, dead_cells)
        for neighbor in neighbors: 
            if neighbor not in reachable_cells: 
                reachable_cells.add(neighbor)
                neighbor_y = neighbor[0]
                neighbor_x = neighbor[1]
                if neighbor_y == row - 1: 
                    return True 
                if self.exploreNeighbors(row, col, neighbor[0], neighbor[1], dead_cells, reachable_cells):
                    return True 

        return False 

    def canCross(self, row, col, cells, index) -> bool: 
        dead_cells = set([(cell[0]-1, cell[1]-1) for cell in cells[0:index]])

        reachable_cells = set()
        for i in range(col):
            if (0, i) not in dead_cells: 
                if (0, i) not in reachable_cells: 
                    reachable_cells.add((0, i))
                    if self.exploreNeighbors(row, col, 0, i, dead_cells, reachable_cells):
                        return True 

        return False 

    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        left = 0
        right = row*col - 1
        mid = (right + left) // 2

        while left < right: 

            if self.canCross(row, col, cells, mid):
                left = mid + 1

            else:
                right = mid - 1

            mid = (right + left) // 2

        if self.canCross(row, col, cells, mid + 1):
            return mid + 1

        if not self.canCross(row, col, cells, mid):
            return mid - 1

        return mid 
