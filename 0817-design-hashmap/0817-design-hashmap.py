#my hash function is f(x) = x
#my map size is constant at 10E6
class MyHashMap:

    def __init__(self):
        self.vals = [-1] * int(10E6)
        

    def put(self, key: int, value: int) -> None:
        self.vals[key] = value

    def get(self, key: int) -> int:
        return self.vals[key]

    def remove(self, key: int) -> None:
        self.vals[key] = -1