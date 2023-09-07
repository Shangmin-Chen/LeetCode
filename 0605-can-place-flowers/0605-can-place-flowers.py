class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        #creating variables
        i = 0
        count = 0
        pots = 0
        length = len(flowerbed)

        # to check first and last indexes to see if index is pottable, or to check if only 1 empty pot
        if n == 0:
            return True
        if length == 1:
            if flowerbed[0] == 0:
                return True
            else:
                return False
        if (length != 1 and flowerbed[0] == 0 and flowerbed[1] == 0):
            pots += 1
            flowerbed[0] = 1
        if (length != 1 and flowerbed[length-1] == 0 and flowerbed[length-2] == 0):
            pots += 1
            flowerbed[length-1] = 1
        
        # the loop to check 3 consecutive 0's and changing pot index to 1 and set i to pot index
        while i < length:
            
            if flowerbed[i] == 0:
                count += 1
            else:
                count = 0
            
            if count == 3:
                count = 0
                pots += 1
                flowerbed[i-1] = 1
                i = i-1

            i+=1

        # end condition    
        if pots >= n:
            return True
        else:
            return False
        