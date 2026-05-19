from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # intialize a result list
        # apply counter method on list then traverse through counter dictionary
        # and append the numbers who frequency has equal or more then k
        counter = Counter(nums)
        heap = [(v,k)for(k,v) in counter.items()]
        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)
        return [num for (freq,num) in heap]
        

            


        
        