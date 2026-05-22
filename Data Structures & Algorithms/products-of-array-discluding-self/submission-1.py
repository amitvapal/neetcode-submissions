class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        l = 1
        r = 1
        for i in range(len(nums)):
            output[i] = l
            l *= nums[i]

        for i in range(len(nums) -1, -1, -1):
            output[i] *= r
            r *= nums[i]

        return output



            


        