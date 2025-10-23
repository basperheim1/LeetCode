class Solution:
    def hasSameDigits(self, s: str) -> bool:

        n = len(s)

        while n != 2: 
            new_string = ""

            for i in range(n-1):
                new_string += str((int(s[i]) + int(s[i+1])) % 10)

            s = new_string 
            n = len(s)

        return s[0] == s[1]


