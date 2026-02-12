class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_length = 0

        for i in range(n):
            letter_freq = dict()
            for j in range(i, n):
                char = s[j]
                if char in letter_freq: 
                    letter_freq[char] += 1

                else:
                    letter_freq[char] = 1

                frequency = None
                keep_going = True
                for val in letter_freq.values():
                    if frequency: 
                        if val != frequency: 
                            keep_going = False
                            break

                    frequency = val 

                if keep_going: 
                    max_length = max(max_length, j - i + 1)
        
        return max_length
