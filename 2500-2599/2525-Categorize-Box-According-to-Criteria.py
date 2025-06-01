class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        bulky = False
        heavy = mass >= 100
        
        if length >= 10**4 or width >= 10**4 or height >= 10**4:
            bulky = True
        else:
            volume = length * width * height
            if volume >= 10**9:
                bulky = True
        
        if bulky and heavy:
            return "Both"
        elif bulky:
            return "Bulky"
        elif heavy:
            return "Heavy"
        else:
            return "Neither"