class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxLeft = 0
        maxRight = 0
        totalArea = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= maxLeft:
                    maxLeft = max(maxLeft, height[left])
                else:
                    totalArea += maxLeft-height[left]
                left += 1
            else:
                if height[right] >= maxRight:
                    maxRight = max(maxRight, height[right])
                else:
                    totalArea += maxRight - height[right]
                right -= 1

        return totalArea




        