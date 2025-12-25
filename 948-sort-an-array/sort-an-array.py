class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        r = self.sortArray(nums[:len(nums)//2])
        l = self.sortArray(nums[len(nums)//2:])
        return self.merge(r, l)


    def merge(self, left: List[int], right: List[int]) -> List[int]:
        l = 0
        r = 0
        m = []
        while len(left) > l and len(right) > r:
            if left[l] < right[r]:
                m.append(left[l])
                l += 1
            else:
                m.append(right[r])
                r += 1
        return m + left[l:] + right[r:]
        