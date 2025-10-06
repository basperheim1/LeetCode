class Cell: 
    def __init__(self, y, x, height):
        self.y = y
        self.x = x
        self.height = height 

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y 

    def __hash__(self):
        return hash((self.x, self.y))

    def __lt__(self, other):
        return self.height < other.height

class Solution:

    def exploreNeighbors(self, cell: Cell, grid: List[List[int]]) -> List[Cell]:
        y = cell.y
        x = cell.x

        neighbors = []
        if y > 0:
            neighbors.append(Cell(y-1, x, grid[y-1][x]))

        if x > 0: 
            neighbors.append(Cell(y, x-1, grid[y][x-1]))

        if y != len(grid) - 1: 
            neighbors.append(Cell(y+1, x, grid[y+1][x]))

        if x != len(grid[0]) - 1: 
            neighbors.append(Cell(y, x+1, grid[y][x+1]))

        return neighbors 


    def swimInWater(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        cells = [[] for i in range(m)]
        for i in range(m):
            for j in range(n):
                cells[i].append(Cell(i, j, grid[i][j]))

        terminating_cell = Cell(m-1, n-1, grid[m-1][n-1])
        starting_cell = Cell(0, 0, grid[0][0])

        explored_cells = set()
        pq = []

        explored_cells.add(starting_cell)
        pq.append(starting_cell)
        min_time = terminating_cell.height

        while terminating_cell not in explored_cells: 
            current_cell = heapq.heappop(pq)
            min_time = max(current_cell.height, min_time)

            neighbors = self.exploreNeighbors(current_cell, grid)

            for neighbor in neighbors: 
                if neighbor not in explored_cells: 
                    explored_cells.add(neighbor)
                    heapq.heappush(pq, neighbor)

        return min_time
