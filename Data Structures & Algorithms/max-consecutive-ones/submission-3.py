class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        maximum = 0
        tmp  = 0
        for i in range(length):
            if nums[i]== 0:
                tmp = max(maximum, tmp)
                maximum = 0
            else:
                maximum += 1
        return max(maximum, tmp)