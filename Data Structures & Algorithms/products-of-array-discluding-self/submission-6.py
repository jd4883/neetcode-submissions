class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        for index, n in enumerate(nums):
            for i in nums[:index] + nums[index + 1:]:
                result[index] *= i
        return result

            
            
        