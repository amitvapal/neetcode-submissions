class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s)).lower()
        og = ""
        rev = ""
        for i in range(len(s)):
            og+=s[i]

        for j in range(len(s)-1, -1, -1):
            rev += s[j]
        
        

        return og == rev
        


        