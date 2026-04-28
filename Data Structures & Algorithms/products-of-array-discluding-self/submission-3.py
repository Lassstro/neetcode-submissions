class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zero_cnt = 0
        all_prod = 1
        res = [0] * n
        for num in nums:
            if num == 0:
                zero_cnt += 1
                if zero_cnt == 2:
                    return [0] * n
            else:
                all_prod *= num
        for i in range(n):
            if zero_cnt == 1:
                if nums[i] == 0:
                    res[i] = all_prod
            else:
                res[i] = all_prod//nums[i]
        return res
                
        