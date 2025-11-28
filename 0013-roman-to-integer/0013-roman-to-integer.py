class Solution:
    def romanToInt(self, s):
        # Map of Roman numerals to integer values
        roman_to_val = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        total = 0
        prev_value = 0
        
        # Iterate through the Roman numeral from right to left
        for char in reversed(s):
            value = roman_to_val[char]
            if value < prev_value:
                # Subtractive case
                total -= value
            else:
                total += value
            prev_value = value
        
        return total
