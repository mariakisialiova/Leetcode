class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        len_nums = len(nums)
        a = 0
        for i in range(len_nums):
            if nums[i] != 0:
                nums[a], nums[i] = nums[i], nums[a]
                a += 1
      
