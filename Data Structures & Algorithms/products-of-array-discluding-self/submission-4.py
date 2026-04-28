# Prefix and Postfix product solution (optimal) - O(n) | O(n)
# [2,3,1,4]
# [1,2,6,6]
# [12,8,24,6]
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        for i in range(1,n):
            res[i] = nums[i-1] * res[i-1]
        postfix = 1
        for i in range(n-2,-1,-1):
            postfix *= nums[i+1]
            res[i] *= postfix

        return res