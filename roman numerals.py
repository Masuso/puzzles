
# Puzzle:
# Given a roman numeral, convert it to an integer.

def romanToInt(self, s: str) -> int:
    #67 ms, 13.9 mb, o(n)
    #struggled a bit to keep track of indexes and variable types
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for i in range(len(s)):
        if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
            total = total - roman[s[i]]
        else:
            total = total + roman[s[i]]
    return total

