class Solution:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Width of the container
            width = right - left
            # Height is limited by the shorter line
            current_height = min(height[left], height[right])
            # Compute area
            max_area = max(max_area, width * current_height)

            # Move the pointer of the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

        