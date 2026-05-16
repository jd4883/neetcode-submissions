class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_found = 0
        current_found = 0
        if 1 <= len(nums) <= 100000:
            for i in range(len(nums)):
                if not nums[i]==0 and not nums[i]==1:
                    return 0
                if nums[i]==1:
                    current_found += 1
                    if current_found > max_found:
                        max_found = current_found
                else:
                    current_found = 0
        return max_found
                
            

        