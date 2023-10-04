class MyHashMap:

    def __init__(self):
        # Initialize an empty list with 1000 slots
        self.size = 1000
        self.table = [None] * self.size

    def put(self, key: int, value: int) -> None:
        # Compute the hash value
        hash_value = key % self.size
        
        # Check if there's already a bucket at the hash value
        if self.table[hash_value] is None:
            self.table[hash_value] = []
        
        # Check if the key exists in the bucket
        for pair in self.table[hash_value]:
            if pair[0] == key:
                pair[1] = value  # Update the value if key exists
                return
        
        # Otherwise, insert the new (key, value) pair into the bucket
        self.table[hash_value].append([key, value])

    def get(self, key: int) -> int:
        # Compute the hash value
        hash_value = key % self.size

        # Check if there's a bucket at the hash value
        if self.table[hash_value] is not None:
            # Search for the key in the bucket
            for pair in self.table[hash_value]:
                if pair[0] == key:
                    return pair[1]  # Return the value if key exists
            
        return -1  # Key does not exist

    def remove(self, key: int) -> None:
        # Compute the hash value
        hash_value = key % self.size

        # Check if there's a bucket at the hash value
        if self.table[hash_value] is not None:
            # Search and remove the key from the bucket
            for i, pair in enumerate(self.table[hash_value]):
                if pair[0] == key:
                    del self.table[hash_value][i]
                    return