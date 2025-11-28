class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping.values():  # Opening brackets
                stack.append(char)
            elif char in mapping:         # Closing brackets
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                # Invalid character (not needed for LeetCode, but safe)
                return False

        return not stack  # Valid if stack is empty