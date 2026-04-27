class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = []
        while (strs):
            base = strs[0]
            strs.pop(0)
            base_count = Counter(base)

            anagram = [base]
            remove = []

            for j in range(len(strs)):
                if base_count == Counter(strs[j]):
                    anagram.append(strs[j])
                    remove.append(j)

            for i in reversed(remove):
                strs.pop(i)

            results.append(anagram)
        return results