class MyHashMap:

    def __init__(self):
        self.size = 2333
        self.buckets = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        hash_val = self._hash(key)
        if self.buckets[hash_val]:
            for i in range(len(self.buckets[hash_val])):
                if self.buckets[hash_val][i][0] == key:
                    self.buckets[hash_val][i] = (key, value)
                    return
        self.buckets[hash_val].append((key, value))
        

    def get(self, key: int) -> int:
        hash_val = self._hash(key)
        if self.buckets[hash_val]:
            for i in range(len(self.buckets[hash_val])):
                if self.buckets[hash_val][i][0] == key:
                    return self.buckets[hash_val][i][1]
        return -1

    def remove(self, key: int) -> None:
        hash_val = self._hash(key)
        if self.buckets[hash_val]:
            for i in range(len(self.buckets[hash_val])):
                if self.buckets[hash_val][i][0] == key:
                    del self.buckets[hash_val][i]
                    break
                

    def _hash(self, key):
        return hash(key) % self.size