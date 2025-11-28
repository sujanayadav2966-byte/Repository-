class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s  # No zigzag needed

        # Initialize rows
        rows = [''] * numRows
        curRow = 0
        goingDown = False

        for char in s:
            rows[curRow] += char
            # Reverse direction at top or bottom row
            if curRow == 0 or curRow == numRows - 1:
                goingDown = not goingDown
            # Move to next row
            if goingDown:
                curRow += 1
            else:
                curRow -= 1

        # Combine all rows into final string
        return ''.join(rows)
