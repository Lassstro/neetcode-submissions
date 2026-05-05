class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = {}
        res = 0

        for x in nums:
            if x in mp:
                continue

            left = mp.get(x - 1, 0)
            right = mp.get(x + 1, 0)

            length = left + right + 1

            mp[x] = length
            mp[x - left] = length
            mp[x + right] = length

            res = max(res, length)

        return res