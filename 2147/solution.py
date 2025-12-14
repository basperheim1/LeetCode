class Solution:
    def numberOfWays(self, corridor: str) -> int:
        n = len(corridor)
        s_count = 0
        num_ways = 1
        current_combos = 0
        for i in range(n): 
            char = corridor[i]
            if char == "S":
                s_count += 1

            if s_count % 2 == 0 and s_count != 0:
                current_combos += 1

            else:
                if s_count > 2 and corridor[i] == "S": 
                    num_ways *= current_combos
                    current_combos = 0

            

        if s_count % 2 != 0 or s_count == 0: 
            return 0

        return num_ways % (10**9 + 7)

