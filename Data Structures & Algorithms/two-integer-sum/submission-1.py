class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {nums[0] : 0}
        for i in range(1, len(nums)):
            if (target - nums[i]) in temp:
                return [temp[target-nums[i]], i]
            else:
                temp[nums[i]] = i

