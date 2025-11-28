class Solution:
    def generateParenthesis(self, n: int):
        result = []

        def backtrack(current, open_count, close_count):
            # If the string is complete (2 * n chars), add to result
            if len(current) == 2 * n:
                result.append(current)
                return

            # Add '(' if we can still open new parentheses
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            # Add ')' if it would not lead to invalid sequence
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        # Start recursion
        backtrack("", 0, 0)
        return result
        