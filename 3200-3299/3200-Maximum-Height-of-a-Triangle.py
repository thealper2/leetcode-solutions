class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def calculate_height(start_red):
            height = 0
            r, b = red, blue
            current_color = 'red' if start_red else 'blue'
            
            while True:
                blocks_needed = height + 1
                if current_color == 'red':
                    if r >= blocks_needed:
                        r -= blocks_needed
                        height += 1
                        current_color = 'blue'
                    else:
                        break
                else:
                    if b >= blocks_needed:
                        b -= blocks_needed
                        height += 1
                        current_color = 'red'
                    else:
                        break
            return height
        
        height_start_red = calculate_height(True)
        height_start_blue = calculate_height(False)
        
        return max(height_start_red, height_start_blue)
