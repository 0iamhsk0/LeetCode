#
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # latest sol
        left = 0
        for right in range(0, len(nums)):
            # swapping 
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                        
        return nums



        