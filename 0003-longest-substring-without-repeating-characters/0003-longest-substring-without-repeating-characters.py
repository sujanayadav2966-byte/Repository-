class Solution:
    def lengthOfLongestSubstring(self, s):
        char_index = {}  # stores last seen index of each char
        left = 0         # left boundary of the window
        max_len = 0

        for right in range(len(s)):
            if s[right] in char_index and char_index[s[right]] >= left:
                # Move left pointer to skip the previous duplicate
                left = char_index[s[right]] + 1

            # Update last seen index of current char
            char_index[s[right]] = right

            # Update maximum window length
            max_len = max(max_len, right - left + 1)

        return max_len

