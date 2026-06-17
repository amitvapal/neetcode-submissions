class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        mapper = dict()
        for ch in s:
            if ch in mapper:
                mapper[ch] += 1
            else:
                mapper[ch] = 1

        for ch in t:
            if ch in mapper:
                mapper[ch] -= 1
            else:
                mapper[ch] = 1
        for key in mapper:
            if mapper[key] != 0:
                return False

        return True


        