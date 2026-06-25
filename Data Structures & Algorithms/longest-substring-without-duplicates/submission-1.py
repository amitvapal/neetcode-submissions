class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        start = 0
        end = 0
        maxLen = 0

        if not s:
            return 0

        while end < len(s):
            while s[end] in unique:
                unique.remove(s[start])
                start += 1
            unique.add(s[end])
            maxLen = max(maxLen, end - start + 1)
            end+=1
        return maxLen
                

        