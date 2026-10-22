class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def put(self, key, value):
        if len(self.cache) >= self.capacity and key not in self.cache:
            self.cache.popitem(0)


        self.cache[key] = value
        self.cache.move_to_end(key, last=True)
        # print("Put: ", self.cache)
    
    def get(self, key: int):
        if not (key in self.cache): return -1

        self.cache.move_to_end(key, last=True)
        # print("Get: ", self.cache)
        return self.cache[key]