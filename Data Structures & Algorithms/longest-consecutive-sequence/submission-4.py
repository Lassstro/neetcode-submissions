class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        longest = 1
        lenght = 1
        for num in nums_set:
            curr = num
            if curr-1 not in nums_set:
                while curr+1 in nums_set:
                    lenght += 1
                    curr+=1
                longest = max(longest, lenght)
                lenght = 1
        return longest
