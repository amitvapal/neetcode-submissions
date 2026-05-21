class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word)) + "#" + word

        return result



    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            length = ""

            while s[i] != '#':
                length += s[i]
                i+=1

            wd_len = int(length)
            i+=1

            word = s[i:i+wd_len]
            result.append(word)
            i+=wd_len
        return result

            

