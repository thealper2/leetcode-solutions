from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        year_changes = {}

        for birth, death in logs:
            year_changes[birth] = year_changes.get(birth, 0) + 1
            year_changes[death] = year_changes.get(death, 0) - 1

        max_population = 0
        max_year = float('inf')
        current_population = 0

        for year in sorted(year_changes.keys()):
            current_population += year_changes[year]
            if current_population > max_population:
                max_population = current_population
                max_year = year

        return max_year
