class Solution:

    def buildConnectionDS(self, connections, c):

        connection_lookup = dict()
        for i in range(1, c+1): 
            connection_lookup[i] = []

        for connection in connections: 
            first = connection[0]
            second = connection[1]

            connection_lookup[first].append(second)
            connection_lookup[second].append(first)

        return connection_lookup


    def dfs(self, current_node, grid_nodes, connection_lookup, seen_nodes):
        grid_nodes.add(current_node)
        seen_nodes.add(current_node)

        for node in connection_lookup[current_node]:
            if node not in grid_nodes: 
                self.dfs(node, grid_nodes, connection_lookup, seen_nodes)

    def createHeaps(self, grids):
        for i in range(len(grids)):
            grids[i] = list(grids[i])
            heapq.heapify(grids[i])


    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        operational = dict()
        grids = []
        connection_lookup = self.buildConnectionDS(connections, c)
        grid_lookup = dict()

        keep_going = True
        seen_nodes = set()
        for current_node in range(1, c+1):
            operational[current_node] = True
            if current_node in seen_nodes: 
                continue 

            grid_nodes = set()
            self.dfs(current_node, grid_nodes, connection_lookup, seen_nodes)
            grids.append(grid_nodes)

        self.createHeaps(grids)

        for grid in grids: 
            for node in grid: 
                grid_lookup[node] = grid

        print("made it here")


            
        return_list = []
        for query in queries: 
            node = query[1]
            if query[0] == 1: 
                if operational[node]:
                    return_list.append(node)

                else:
                    grid = grid_lookup[node]

                    min_station = -1
                    while len(grid) > 0: 
                        if operational[grid[0]]:
                            min_station = grid[0]
                            break

                        else:
                            heapq.heappop(grid)

                    return_list.append(min_station)


            else:
                operational[query[1]] = False

        return return_list 
