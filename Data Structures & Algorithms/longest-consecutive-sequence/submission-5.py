class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        longest = 1
        lenght = 1
        for num in nums_set:
            if num-1 not in nums_set:
                while num+1 in nums_set:
                    lenght += 1
                    num+=1
                longest = max(longest, lenght)
                lenght = 1
        return longest
