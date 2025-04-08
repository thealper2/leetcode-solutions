from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        result = 0
        n = len(students)
        i = 0
        no_match = 0
        
        while i < n and sandwiches:
            if students[i] == sandwiches[0]:
                sandwiches.pop(0)
                students.pop(i)
                n -= 1
                no_match = 0 
                i = 0
            else:
                student = students.pop(i)
                students.append(student)
                no_match += 1
                if no_match >= n:
                    result = n
                    break
        
        return result