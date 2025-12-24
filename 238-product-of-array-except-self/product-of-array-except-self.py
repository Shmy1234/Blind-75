class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = []
        p = 1
        if nums.count(0) > 1:
            return [0]*len(nums)
        elif nums.count(0) == 1:
            for num in nums:
                if num !=0:
                    p *= num 
            l = [0] * (len(nums) - 1)
            l.insert(nums.index(0), p)
        else:
            for num in nums:
                p *= num 
            for num in nums:
                l.append(int(p/num))
        
        return l