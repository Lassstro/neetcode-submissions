# Boundary merge: với mỗi num mình tìm merge nó vào đón left và right của nó
# sau đó cập nhật left và right để sẵn sàng merge tiếp với cái tiếp theo
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