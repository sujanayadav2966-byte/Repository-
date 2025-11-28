class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Step 1: Handle overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Step 2: Determine sign
        negative = (dividend < 0) ^ (divisor < 0)

        # Step 3: Work with positive numbers
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0

        # Step 4: Subtract divisor using bit shifting
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quotient += multiple

        # Step 5: Apply sign
        if negative:
            quotient = -quotient

        # Step 6: Clamp within 32-bit signed integer range
        return max(min(quotient, INT_MAX), INT_MIN)
        