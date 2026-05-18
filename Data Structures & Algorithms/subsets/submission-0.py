class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            
            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res
        
        # n = len(nums)
        # res = []
        # for i in range(1 << n):
        #     subset = [nums[j] for j in range(n) if (i & (1 << j))]
        #     res.append(subset)
        # return res
        