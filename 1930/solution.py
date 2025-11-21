class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        first_occurance = [-1]*26
        last_occurance = [-1]*26 

        for i in range(n): 
            char = s[i]
            char_index = ord(char) - ord('a')
            if first_occurance[char_index] == -1:
                first_occurance[char_index] = i

        for i in range(n-1, -1, -1): 
            char = s[i]
            char_index = ord(char) - ord('a')
            if last_occurance[char_index] == -1:
                last_occurance[char_index] = i

        pals = set()

        for i in range(26): 
            first_index = first_occurance[i]
            last_index = last_occurance[i]
            char = chr(first_index + ord('a'))
            for j in range(first_index + 1, last_index): 
                pals.add(char + s[j] + char)

        return len(pals)


