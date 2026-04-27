class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        freqs = [[] for _ in range(len(nums))]
        for num, freq in count.items():
            freqs[freq-1].append(num)

        res = []
        for i in range(len(freqs),0,-1):
            for num in freqs[i-1]:
                res.append(num)
                if len(res) == k:
                    return res
