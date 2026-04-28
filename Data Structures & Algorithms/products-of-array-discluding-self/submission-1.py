# Tìm tích tiền tố và hậu tố của mỗi số, sau đấy nhân lại là được
# nums = [1,2,4,6]
# prefix = [1,1,2,8]
# postfix = [48,24,6,1]
# res = [48,24,12,8]
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        prefix = [0] * n
        postfix = [0] * n

        prefix[0] = 1
        postfix[n-1] = 1

        for i in range(1,n):
            prefix[i] = nums[i-1] * prefix[i-1]
        for i in range(n-2,-1,-1):
            postfix[i] = nums[i+1] * postfix[i+1]

        return [prefix[i] * postfix[i] for i in range(n)]
