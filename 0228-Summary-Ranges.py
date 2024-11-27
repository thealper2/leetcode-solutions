class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        
        ranges = []
        start = nums[0]
        end = nums[0]

        for num in nums[1:]:
            if num != end + 1:
                if start == end:
                    ranges.append(str(start))
                else:
                    ranges.append(f"{start}->{end}")

                start = num

            end = num

        if start == nums[-1]:
            ranges.append(str(start))
        else:
            ranges.append(f"{start}->{end}")

        return ranges