class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_sorted = sorted(nums)
        longest = 1
        lenght = 1
        for i in range(len(nums_sorted)-1):
            if nums_sorted[i] == nums_sorted[i+1] - 1:
                lenght += 1
            elif nums_sorted[i] == nums_sorted[i+1]:
                continue
            else:
                longest = longest if longest > lenght else lenght
                lenght = 1
        return longest if longest > lenght else lenght