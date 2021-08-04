import inspect
import timeit
import sys


class Solution1:
    """Runtime: 228 ms, faster than 94.75% of Python3 online submissions for Longest Palindromic Substring.
        Memory Usage: 14.1 MB, less than 99.13% of Python3 online submissions for Longest Palindromic Substring."""
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s

        max_palindrome = ""

        for i in range(len(s)):
            for j in range(2):
                palindrome = self.getPalindrome(s, len(s), i, i + j)
                max_palindrome = palindrome if len(max_palindrome) < len(palindrome) else max_palindrome

        return max_palindrome

    def getPalindrome(self, s, len_s, l, r):
        while l >= 0 and r < len_s and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1: r]


# Test Case
test_string = "sasdasadfadffaaff"

# timeit params
timeit_repeat = 1
timeit_numbers = 100


if __name__ == '__main__':
    solutions = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    for _, solution in solutions:
        if _.startswith("Solution"):
            result = solution().longestPalindrome(s=test_string)
            t = timeit.Timer(
                lambda: solution().longestPalindrome(s=test_string)
            ).repeat(timeit_repeat, timeit_numbers)
            print(result, t)
