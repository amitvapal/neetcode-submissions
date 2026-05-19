from collections import *
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Intialize a list
        # Loop through each word in list, apply Counter method to nested for loop 
        # If the freq is same for words add to temp list then add that list to og list

        anagrams = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagrams[sorted_word].append(word)

        result = list(anagrams.values())    
        

        
        return result

            


        