class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        m = len(bank)
        n = len(bank[0])

        total_lasers = 0
        prev_row_count = None 

        for i in range(m):
            if prev_row_count is None: 
                prev_row_count = bank[i].count("1")

            else:
                current_row_count = bank[i].count("1")
                total_lasers += current_row_count*prev_row_count

                if current_row_count > 0:
                    prev_row_count = current_row_count

        return total_lasers 
