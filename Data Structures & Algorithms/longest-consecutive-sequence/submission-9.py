class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # itialize a counter
        # sort the list
        # when looping through check if curr is equal to prev continue
        # if curr is one less then the forward then add count
        # return count
        num_set = set(nums)
        longest_length = 0
    
        for num in num_set:
            if num - 1 not in num_set:  # Check if the number is the start of a sequence
                current_num = num
                current_length = 1
                
                while current_num + 1 in num_set:  # Count the length of current consecutive sequence
                    current_num += 1
                    current_length += 1
                
                longest_length = max(longest_length, current_length)  # Update the longest length
        
        return longest_length

            

            



            