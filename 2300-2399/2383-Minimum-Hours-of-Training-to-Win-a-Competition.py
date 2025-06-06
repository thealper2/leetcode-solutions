from typing import List


class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        total = 0
        n = len(energy)

        for i in range(n):
            if initialEnergy <= energy[i]:
                training = energy[i] - initialEnergy + 1
                total += training
                initialEnergy += training

            if initialExperience <= experience[i]:
                training = experience[i] - initialExperience + 1
                total += training
                initialExperience += training

            initialEnergy -= energy[i]
            initialExperience += experience[i]

        return total