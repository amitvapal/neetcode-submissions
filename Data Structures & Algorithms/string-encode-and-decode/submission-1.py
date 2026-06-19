class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word)) + "#" + word
        return result



    def decode(self, s: str) -> List[str]:
        result = []
        poin = 0
        num = ""

        while poin < len(s):
            num = ""
            while s[poin] != "#":
                num += s[poin]
                poin+=1
            
            split = s[poin+1:poin + int(num)+1]

            result.append(split)

            poin += 1 + int(num)

        return result

            






         

            

