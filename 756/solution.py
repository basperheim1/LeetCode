class Solution:
    LETTERS = {"A", "B", "C", "D", "E", "F"}

    def _pyramidTransition(self, current_bottom: str, current_level: str, index: int, allowed: Set[str], invalid_rows: Set[str]):
        if current_bottom in invalid_rows: 
            return False 
        for letter in self.LETTERS: 
            # print(f"Current bottom: {current_bottom}")
            # print(f"current level: {current_level}")
            # print(f"current test: {current_bottom[index:index + 2] + letter}")
            # print()

            if current_bottom[index:index + 2] + letter in allowed: 
                
                if len(current_bottom) == index + 2: 
                    if len(current_level) == 0: 
                        print("WO")
                        return True

                    if self._pyramidTransition(current_level + letter, "", 0, allowed, invalid_rows): 
                        return True 

                if self._pyramidTransition(current_bottom, current_level + letter, index + 1, allowed, invalid_rows):
                    return True

        if index == 0: 
            invalid_rows.add(current_bottom)
        return False


    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        return self._pyramidTransition(bottom, "", 0, set(allowed), set())

