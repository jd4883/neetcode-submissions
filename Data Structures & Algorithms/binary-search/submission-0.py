class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = -1
        if nums and len(nums)==len(set(nums)):
            for index, num in enumerate(nums):
                if num == target:
                    result = index
        return result
        