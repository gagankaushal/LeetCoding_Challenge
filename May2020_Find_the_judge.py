class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        # Track the number of people each person trusts using a dictionary
        tracker = dict.fromkeys(range(1,N+1),0)
        
        for i in trust:
            tracker[i[0]] += 1
        
        
        # Initially assume that judge doesn't exist
        judgeCandidate = -1
        
        # Find the candidate key of a judge (because he doesn't trust anyone)
        for person, numberOfPeopleTrusted in tracker.items():
            # check if values are all equal
            if numberOfPeopleTrusted == 0:
                # count += 1
                judgeCandidate = person
                break
                # return -1   
        
        # if no judge found 
        if judgeCandidate == -1:
            return -1
        
        # Check if remaining people trust the judge or not by counting votes
        votes = 0
        
        for pair in trust:
            if pair[0]!= judgeCandidate and pair[1] == judgeCandidate:
                votes +=1
        
        # All but the judge trust the judge
        if votes == N-1:
            return judgeCandidate
        
        else:
            return -1
        
        
#         # print(tracker)
#         # return 0
        
#         count = 0
        
#         oldnumberOfPeopleTrusted = tracker[1]
#         for person, numberOfPeopleTrusted in tracker.items():
#             # check if values are all equal
#             if oldnumberOfPeopleTrusted != numberOfPeopleTrusted:
#                 count += 1
#                 # return -1
#         # if count == 1:
#         #     return 
        
#         for person, numberOfPeopleTrusted in tracker.items():
#             if count == 1 and numberOfPeopleTrusted == 0:
#                 return person
        
#         return -1
            