class Solution:
    def arrangeCoins(self, n: int) -> int:
       
    
        '''
        if n == 0:
            return 0
        
        index = 1
        count = 2
        
        
        while index <= n   :
            index +=  count
            count +=1
        if index == n:
            return count - 1
        
        else:
            return count - 2
        
        '''
        left, right = 0,n
        
        
        while left<=right:
            middle = (left + right)//2
            currValue = middle * (middle + 1)//2
            
            if currValue == n:
                return middle
            elif currValue > n:
                right = middle - 1
            
            else:
                left = middle + 1
        return right
