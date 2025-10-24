class Solution:
    def nextBeautifulNumber(self, n: int) -> int:

        
        while True: 
            n += 1

            num_dict = dict()
            for char in str(n):
                if char in num_dict: 
                    num_dict[char] += 1

                else:
                    num_dict[char] = 1

            found = True
            for key in num_dict: 
                if key != str(num_dict[key]):
                    found = False
                    break


            if found: 
                return n
