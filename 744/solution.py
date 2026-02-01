class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        for i in range(n):
            letter = letters[i]
            if letter > target: 
                return letter

        return letters[0]
