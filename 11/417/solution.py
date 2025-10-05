class Cell:
    def __init__(self, r, c, height):
        self.r = r
        self.c = c
        self.height = height

    def __hash__(self):
        return hash((self.r, self.c, self.height))

    def __eq__(self, other):
        if not isinstance(other, Cell):
            return NotImplemented
        return self.r == other.r and self.c == other.c and self.height == other.height

    def exploreAdjacent(self, cells):

        adjacent_cells = []
        if self.r > 0:
            adjacent_cells.append(cells[self.r-1][self.c])

        if self.c > 0:
            adjacent_cells.append(cells[self.r][self.c-1])

        if self.r != len(cells) - 1: 
            adjacent_cells.append(cells[self.r+1][self.c])

        if self.c != len(cells[0]) - 1:
            adjacent_cells.append(cells[self.r][self.c+1])

        return adjacent_cells

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        m = len(heights)
        n = len(heights[0])

        cells = [[] for i in range(m)]

        for i in range(m):
            for j in range(n):
                cells[i].append(Cell(i, j, heights[i][j]))

        pacific_ocean_cells = set()
        pacific_ocean_stack = deque()
        
        atlantic_ocean_cells = set()
        atlantic_ocean_stack = deque()

        for i in range(n):
            pacific_ocean_cells.add(cells[0][i])
            pacific_ocean_stack.append(cells[0][i])

        for i in range(m):
            pacific_ocean_cells.add(cells[i][0])
            pacific_ocean_stack.append(cells[i][0])

        for i in range(n):
            atlantic_ocean_cells.add(cells[m-1][i])
            atlantic_ocean_stack.append(cells[m-1][i])

        for i in range(m):
            atlantic_ocean_cells.add(cells[i][n-1])
            atlantic_ocean_stack.append(cells[i][n-1])
        
        while len(atlantic_ocean_stack) > 0: 
            current_cell = atlantic_ocean_stack.pop()

            neighbors = current_cell.exploreAdjacent(cells)

            for neighbor in neighbors: 
                if neighbor.height >= current_cell.height: 
                    if neighbor not in atlantic_ocean_cells:
                        atlantic_ocean_cells.add(neighbor)
                        atlantic_ocean_stack.append(neighbor)

        while len(pacific_ocean_stack) > 0: 
            current_cell = pacific_ocean_stack.pop()

            neighbors = current_cell.exploreAdjacent(cells)

            for neighbor in neighbors: 
                if neighbor.height >= current_cell.height: 
                    if neighbor not in pacific_ocean_cells:
                        pacific_ocean_cells.add(neighbor)
                        pacific_ocean_stack.append(neighbor)

        result = []

        for cell in pacific_ocean_cells: 
            if cell in atlantic_ocean_cells: 
                result.append([cell.r, cell.c])

        return result 


        
