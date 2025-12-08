class Solution:
    def countTriples(self, n: int) -> int:
        triples = set()
        for i in range(n+1):
            triples.add(i**2)

        count = 0
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                if (i**2 + j**2) in triples: 
                    count += 2

        return count 
