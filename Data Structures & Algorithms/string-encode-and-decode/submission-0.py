class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += (str(len(s)) + "#" + s)
        return res

    def decode(self, ss: str) -> List[str]:
        res = []
        len_s = ""
        i = 0
        len_ss = len(ss)
        while i < len_ss:
            j = i
            while ss[j] != "#":
                j += 1
            len_s = int(ss[i:j])

            i = j + 1
            res.append(ss[i:i+len_s])
            i += len_s
        return res