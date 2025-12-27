class Solution:
    def bestClosingTime(self, customers: str) -> int:
        min_penalty = customers.count("Y")
        current_penalty = min_penalty
        index = 0

        for i in range(len(customers)):
            customer = customers[i]
            print(current_penalty)
            if customer == "Y":
                current_penalty -= 1

            else:
                current_penalty += 1

            if current_penalty < min_penalty:
                min_penalty = current_penalty
                index = i + 1

        return index
