class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []

        # Mapping of digits to letters
        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        result = []

        # Backtracking function
        def backtrack(index, path):
            if index == len(digits):
                result.append("".join(path))
                return

            for letter in phone_map[digits[index]]:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()  # undo choice

        backtrack(0, [])
        return result