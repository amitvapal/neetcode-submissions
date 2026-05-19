from collections import Counter 
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for key, count in counter.items():
            if count != 1:
                return True
        return False

         