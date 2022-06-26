# Puzzle:
# Given an integer x, return true if x is palindrome integer.

def isPalindrome(self, x: int) -> bool:
    # 85 ms, 13.8 mb
    # independent try, downsides: cumbersome code, requires non-constant space
    reversed_lst = []
    lst = []
    for i in str(x):
        lst.append(i)
        reversed_lst.insert(0, i)
    if lst == reversed_lst:
        return True

def isPalindrome_string(self, x: int) -> bool:
    # 56 ms, 13.9 mb
    # after reading up on reversing strings
    string = str(x)
    if string == string[::-1]:
        return True

def isPalindrome_pointers(self, x: int) -> bool:
    # 86 ms, 13.9 mb
    # after reading about pointers. Slower, but does not require non-constant space.
    x = str(x)
    l, r = 0, len(x) - 1
    while l < r:
        if x[l] != x[r]:
            return False
        l, r = l + 1, r - 1
    return True
