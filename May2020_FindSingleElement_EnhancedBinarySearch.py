class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        


        start = 0
        end = len(nums) - 1
        
        while start<end:
            middle = (start + end)//2
            
            # navigate middle pointer to even index, if current is an odd index
            if middle%2 != 0:
                middle -= 1
            
            # if next element of middle ele is not same, then single ele is on LEFT side, since the order has been broken by the single element
            if nums[middle] == nums[middle + 1]:
                start = middle + 2 # 2 since the duplicate would be on middle - 1
                
            elif nums[middle] == nums[middle - 1]:
                end = middle - 2
            
            else:
                return nums[middle]
        
        return nums[start]
