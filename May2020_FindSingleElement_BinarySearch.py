class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        '''
        1. Initiate the starting, end positions
        keep doing until start < end
        2. find middle
        3. update start and end based on following cases:
        
        -- case 1: right half had even elements AND duplicate on right
        --> start = mid + 2
        '''
        
        start = 0
        end = len(nums)-1
        # middle = (start + (end))//2
        # while loop
        while start<end:
            # middle = (start + (end - start))//2
            middle = (start + (end ))//2

            # focusses on right side
            isEven = (end - middle)%2 == 0 
            
            # if next element is same and array on right side contains even number of elements before considering the duplicate next element.
            # So, the single number should be on right side
            if nums[middle] == nums[middle+1] and isEven:
                start = middle + 2

            
            elif nums[middle] == nums[middle+1] and not isEven:
                end = middle - 1

            
            elif nums[middle] == nums[middle-1] and not isEven:
                start = middle + 1
            
            
            elif nums[middle] == nums[middle-1] and  isEven:
                end = middle - 2

            else:
                return nums[middle]
        
        return nums[start]

