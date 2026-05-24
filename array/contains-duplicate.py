class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # seen = set()
        
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        
        # return False
        temp = set(nums)
        if len(temp) == len(nums):
            return False
        else:
            return True
