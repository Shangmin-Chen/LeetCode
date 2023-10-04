class MyHashMap:

    def __init__(self):
        self.keys = []
        self.values = []

    def put(self, key: int, value: int) -> None:
        try:
            i = self.keys.index(key)
            self.values[i] = value
        except:
            self.keys.append(key)
            self.values.append(value)        


    def get(self, key: int) -> int:
        try:
            i = self.keys.index(key)
            return self.values[i]
        except:        
            return -1

    def remove(self, key: int) -> None:
        try:
            i = self.keys.index(key)
            self.keys.remove(key)
        except:
            return -1
        self.values.pop(i)        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)