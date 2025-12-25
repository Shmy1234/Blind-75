class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        m = 0 
        for n in nums:
            if n > 1 and n == m:
                continue 
            if n > 1 and n-1 == m:
                m += 1
            elif n == 1:
                m = 1
            elif n > 1:
                return m + 1
        return m + 1