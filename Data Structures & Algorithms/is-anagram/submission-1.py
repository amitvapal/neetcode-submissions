from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counterS = Counter(s)
        counterT = Counter(t)
        if(len(s) != len(t)):
            return False

        for key in counterS:
            if counterS[key] != counterT[key]:
                return False
        return True
        