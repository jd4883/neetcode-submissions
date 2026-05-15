class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(list(set(nums)))
        max_sequence = 1
        current_sequence = 1
        for index, n in enumerate(nums):
            if index == 0:
                continue
            if n == (1+nums[index-1]):
                current_sequence +=1
                if current_sequence > max_sequence:
                    max_sequence = current_sequence
            else:
                current_sequence = 1
        return max_sequence

