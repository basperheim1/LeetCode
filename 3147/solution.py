class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:

        n = len(energy)

        max_energy_from_starting = [None for i in range(n)]

        for i in range(n-1, -1, -1):
            total_energy = energy[i]
            current_index = i 

            while current_index + k < n:
                current_index += k 
                if max_energy_from_starting[current_index] is not None: 
                    total_energy += max_energy_from_starting[current_index]
                    break

                total_energy += energy[current_index]

            max_energy_from_starting[i] = total_energy 

        return max(max_energy_from_starting)

            
