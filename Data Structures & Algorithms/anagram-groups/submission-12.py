class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        visited = set()
        for i in range(len(strs)):
            if i in visited:
                continue
            items = []
            for j in range(len(strs)):    
                if Counter(strs[i]) == Counter(strs[j]):
                    items.append(strs[j])
                    visited.add(j)

            result.append(items)
        return result
            
        