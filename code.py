class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d1={}
        for maz in s:
            if maz not in d1:
                d1[maz]=1
            else:
                d1[maz]+=1
        print(d1)
        for ran in t:
            if ran not in d1:
                return ran
            elif ran in d1:
                d1[ran]-=1
                if d1[ran]<0:
                    return ran

        
