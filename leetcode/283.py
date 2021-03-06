class Solution:
    def addBinary(self, a: str, b: str) -> str:

        # Make given variable 'a' and 'b' decimal numbers
        a_decimal = int(a, 2)
        b_decimal = int(b, 2)

        total = a_decimal+b_decimal

        # Remove the '0b' prefix
        return bin(total)[2:]
