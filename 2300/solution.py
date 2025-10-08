class Solution:

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        n = len(spells)
        m = len(potions)

        potions.sort()

        pairs = []

        for i in range(n): 
            val = success / spells[i]
            index = bisect.bisect_left(potions, val)
            pairs.append(m - index)

        return pairs 

