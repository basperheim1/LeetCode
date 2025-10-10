class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:

        n = len(skill)
        m = len(mana)

        total_time = 0

        for i in range(1, m):

            second_time = 0
            first_time = 0
            additional_time = mana[i-1]*skill[0]

            for j in range(1, n):
                first_time += mana[i-1]*skill[j]
                second_time += mana[i]*skill[j-1]

                if second_time < first_time: 
                    difference = first_time - second_time 
                    additional_time += difference
                    first_time -= difference

            total_time += additional_time

        print(total_time)

        total_time += sum([mana[m-1]*skill[i] for i in range(n)])

        return total_time 
