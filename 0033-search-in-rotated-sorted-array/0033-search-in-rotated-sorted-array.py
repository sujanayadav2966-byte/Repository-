from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            # If left..mid is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # mid..right is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

# Example / quick test
if __name__ == "__main__":
    s = Solution()
    print(s.search([4,5,6,7,0,1,2], 0))  # expected 4
    print(s.search([4,5,6,7,0,1,2], 3))  # expected -1
    print(s.search([], 1))               # expected -1
