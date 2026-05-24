class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        for num, freq in counter.items():
            if freq == 1:
                return num
        
