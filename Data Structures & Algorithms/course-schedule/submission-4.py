class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        for dest, src in prerequisites:
            adj[src].append(dest)
        
        visit = [0] * numCourses
        def has_cycle(curr):
            if visit[curr] == 1: return True
            if visit[curr] == 2: return False
            visit[curr] = 1
            for neighbor in adj[curr]:
                if has_cycle(neighbor): return True
            visit[curr] = 2
            return False
        
        for i in range(numCourses):
            if has_cycle(i): return False
        return True