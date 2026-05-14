class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        counter = Counter(nums)
        while k > 0:
            largest_key = max(counter, key=counter.get)
            result.append(largest_key)
            del counter[largest_key]
            k -= 1
        return result
        
        