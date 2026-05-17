class Solution:
    def binary_search(self, l: int, r: int, nums: list[int], target: int) -> int:
        if l > r:
            return -1
        m = l + (r-1) // 2

        if nums[m] == target:
            return m
        if nums[m] < target:
            return self.binary_search(l, m-1, nums, target)
        return self.binary_search(l, m-1, nums, target)
    
    def search(self, nums: List[int], target: int) -> int:
        # return self.binary_search(0, len(nums) - 1, nums, target)
        result = -1
        if nums and len(nums)==len(set(nums)):
            for index, num in enumerate(nums):
                if num == target:
                    result = index
        return result
        