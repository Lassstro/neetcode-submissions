class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort_strs = [''.join(sorted(s)) for s in strs]
        d = {}
        results = []
        for i, s in enumerate(sort_strs):
            if s not in d:
                d[s] = [i]
            else:
                d[s].append(i)
        for v in d.values():
            anas = []
            for i in v:
                anas.append(strs[i])
            results.append(anas)
        return results
