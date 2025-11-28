class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0  # slow pointer (where to place next valid number)

        for j in range(len(nums)):  # fast pointer (scans all numbers)
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        return i
        