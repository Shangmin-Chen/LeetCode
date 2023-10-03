class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # Create an empty dictionary to store the count of each number
        hashMap = {}
        # Initialize a count to keep track of the number of identical pairs
        count = 0
        # Iterate through each number in the input list 'nums'
        for number in nums:
            # If the current number is already present in the dictionary
            if number in hashMap:
                # Increase the 'count' by the value associated with the current number in the dictionary
                count = count + hashMap[number]
                # Increment the count associated with the current number in the dictionary
                hashMap[number] += 1
            else:
                # If the current number is not present in the dictionary, add it with a count of 2
                hashMap[number] = 1
        # Return the final count of identical pairs
        return count