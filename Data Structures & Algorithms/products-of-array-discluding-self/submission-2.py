class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            pro = 1
            for j in range(i):
                pro *= nums[j]
            for j in range(i+1, len(nums)):
                pro *= nums[j]
            res.append(pro)
        return res
# O(n*n) brute-force solution