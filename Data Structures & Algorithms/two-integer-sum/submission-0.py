class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, x in enumerate(nums):
            if x in seen:
                return [seen[x], i]
            seen[target - x] = i