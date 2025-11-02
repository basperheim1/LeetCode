class Solution:

    def _minNumberOperations(self, target: List[int], left_endpoint: int, right_endpoint: int, baseline: int) -> int: 
        min_val = min(target[left_endpoint:right_endpoint])

        total = min_val - baseline 

        new_left_endpoint = None 

        for i in range(left_endpoint, right_endpoint):
            current_val = target[i]

            if current_val == min_val: 
                if new_left_endpoint is None: 
                    continue 

                total += self._minNumberOperations(target, new_left_endpoint, i, min_val)
                new_left_endpoint = None

            else:
                if new_left_endpoint is None: 
                    new_left_endpoint = i

                if i == right_endpoint - 1: 
                    total += self._minNumberOperations(target, new_left_endpoint, right_endpoint, min_val)

        return total 

    def minNumberOperations(self, target: List[int]) -> int:
        # return self._minNumberOperations(target, 0, len(target), 0)

        n = len(target)
        total = target[0]

        for i in range(1, n): 
            current_val = target[i]
            if current_val > target[i-1]:
                total += current_val - target[i-1]

        return total 

            



