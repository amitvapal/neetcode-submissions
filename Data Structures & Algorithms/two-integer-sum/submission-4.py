class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for i in range(len(nums)):
            numbers[nums[i]] = i

        for i in range(len(nums)):
            num = nums[i]
            diff = target - num

            if diff in numbers and i != numbers[diff]:
                return sorted([numbers[diff], i])

        return []

        
              

