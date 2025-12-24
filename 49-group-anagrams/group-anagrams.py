class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            lst = [0]*26
            for c in s:
                lst[ord(c) - ord("a")] += 1
            d[tuple(lst)] = [s] + d.get(tuple(lst), [])
        return list(d.values())