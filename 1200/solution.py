class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n = len(arr)

        min_difference = 9999999
        for i in range(1, n): 
            first_num = arr[i-1]
            second_num = arr[i]
            current_difference = second_num - first_num

            min_difference = min(min_difference, current_difference)

        result = []
        for i in range(1, n): 
            first_num = arr[i-1]
            second_num = arr[i]
            current_difference = second_num - first_num

            if current_difference == min_difference: 
                result.append([first_num, second_num])

        return result
