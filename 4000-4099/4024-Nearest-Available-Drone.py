class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        tx, ty = target
        best_idx = -1
        best_dist = float('inf')
        
        for i, drone in enumerate(drones):
            xi, yi, rangei = drone
            dist = abs(xi - tx) + abs(yi - ty)
            
            if dist <= rangei:
                if dist < best_dist:
                    best_dist = dist
                    best_idx = i
        
        return best_idx