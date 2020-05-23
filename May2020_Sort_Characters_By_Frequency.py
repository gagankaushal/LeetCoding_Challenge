class Solution:
    def frequencySort(self, s: str) -> str:
        
        dict = {}
        
        for i in s:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        
        
        dictNew =  sorted(dict.items(), key = lambda x: x[1], reverse = True)
        ans = ""
        for key,val in dictNew:
            ans += key*val
            
        return ans 
