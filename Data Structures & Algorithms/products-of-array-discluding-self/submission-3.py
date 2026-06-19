class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        leftProd = 1
        rightProd = 1
        for i in range(len(nums)):
            output[i] *= leftProd
            leftProd *= nums[i]

        for j in range(len(nums)-1, -1, -1):
            output[j] *= rightProd
            rightProd *= nums[j]

        return output





            


        