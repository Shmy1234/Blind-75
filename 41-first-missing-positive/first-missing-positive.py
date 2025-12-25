class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        count, m = 0, 0
        for n in nums:
            if n > 1 and n == count:
                continue 
            if n > 1 and n-1 == count:
                count += 1
                m += 1
            elif n == 1:
                count = 1
                m = 1
            elif n > 1:
                return m + 1
        return m + 1