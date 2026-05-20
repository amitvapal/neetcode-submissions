class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        result = []

        for num in nums:
            if num not in count:
                count[num] = 0
            count[num]+=1

        freq = [[] for i in range(len(nums)+1)]

        for key in count:
            freq[count[key]].append(key)

        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
        

        


        