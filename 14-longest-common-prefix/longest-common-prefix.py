class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        p = ""
        for i in range(len(strs[0])):
            p2 = strs[0][i]
            for s in strs:
                if i >= len(s) or p2 != s[i]:
                    return p
            p += p2
        return p 