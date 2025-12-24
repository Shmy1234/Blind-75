class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        d = {}
        for n in nums: 
            if n -1 in d:
                d[n] = d[n-1] + 1
            else:
                d[n] = 1
        if list(d.values()):
            return max(list(d.values()))
        else:
            return 0