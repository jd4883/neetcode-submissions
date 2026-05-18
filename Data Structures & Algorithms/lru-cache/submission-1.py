class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = []
        

    def get(self, key: int) -> int:
        result = -1
        for i in range(len(self.cache)):
            if self.cache[i][0] == key: 
                result = self.cache[i][1]
                tmp = self.cache.pop(i)
                self.cache.append(tmp)
                break
        return result
        

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                tmp = self.cache.pop(i)
                tmp[1] = value
                self.cache.append(tmp)
                return
        if self.capacity == len(self.cache): self.cache.pop(0)
        self.cache.append([key, value])