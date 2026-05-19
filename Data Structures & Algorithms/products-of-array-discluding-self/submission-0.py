class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # intializd empty list
        result = []
        product = 1
        divide = 0
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(i != j):
                    product *= nums[j]
            result.append(product)
            product = 1

        return result
        
            
                
                

        