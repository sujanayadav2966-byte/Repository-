class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # If needle is empty, return 0 (optional edge case)
        if not needle:
            return 0

        # Sliding window search
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1