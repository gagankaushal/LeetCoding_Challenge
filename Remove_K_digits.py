class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        stack = []
        
        numRemove = k
        for i in num:
            
            # delete 1st ele if it is greater than next ele
            while stack and k and stack[-1]>i:
                stack.pop()
                k -= 1
            stack.append(i)
        

        answer = "".join(stack[:len(num)-numRemove]).lstrip("0")
        
        if len(answer):
            return answer
        else:
            return "0"
  