
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

# Puzzle:
# Given an integer, convert it to a roman numeral.

def intToRoman(self, num: int) -> str:
    # 59 ms, 13.8 mb, o(n)
    # learned some neat symbols like what // and % does
    symbols = [[1, 'I'], [4, 'IV'], [5, 'V'], [9, 'IX'],
               [10, 'X'], [40, 'XL'], [50, 'L'], [90, 'XC'],
               [100, 'C'], [400, 'CD'], [500, 'D'], [900, 'CM'],
               [1000, 'M']]
    roman_numeral = ''
    for val, sym in reversed(symbols):
        if num // val:
            roman_numeral += sym * (num // val)
            num = num % val
    return roman_numeral


