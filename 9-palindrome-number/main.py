class Solution1:
    """Runtime: 64 ms, faster than 52.34% of Python3 online submissions for Palindrome Number.
    Memory Usage: 14.3 MB, less than 49.54% of Python3 online submissions for Palindrome Number."""
    def isPalindrome(self, x: int) -> bool:
        list_x = list(str(x))
        while len(list_x) >= 2:
            try:
                start, end = int(list_x.pop(0)), int(list_x.pop(-1))
            except ValueError:
                return False
            if start - end != 0:
                return False
        return True


class Solution2:
    """Runtime: 134 ms, faster than 5.13% of Python3 online submissions for Palindrome Number.
    Memory Usage: 14.1 MB, less than 92.67% of Python3 online submissions for Palindrome Number."""
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False

        reverse_num = 0
        digits_of_num = self.get_digits_of_num(x)

        x_copy = x
        while digits_of_num > 0:
            digit = x_copy % 10
            x_copy = x_copy // 10
            digits_of_num -= 1
            reverse_num += digit * (10 ** digits_of_num)

        if x == reverse_num:
            return True
        return False

    def get_digits_of_num(self, x):
        n_digits = 0
        while x != 0:
            x //= 10
            n_digits += 1
        return n_digits


class Solution3:
    """Runtime: 81 ms, faster than 15.36% of Python3 online submissions for Palindrome Number.
    Memory Usage: 14.2 MB, less than 77.73% of Python3 online submissions for Palindrome Number."""
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False

        digits_of_num = self.get_digits_of_num(x)

        while digits_of_num > 0:
            fst_digit = x // 10 ** (digits_of_num - 1)
            last_digit = x % 10
            if fst_digit != last_digit:
                return False

            x = (x // 10) % 10 ** (digits_of_num - 2)
            digits_of_num -= 2

        return True

    def get_digits_of_num(self, x):
        n_digits = 0
        while x != 0:
            x //= 10
            n_digits += 1
        return n_digits


class Solution4:
    """Lol seriously???
    Runtime: 48 ms, faster than 95.31% of Python3 online submissions for Palindrome Number.
    Memory Usage: 14 MB, less than 99.04% of Python3 online submissions for Palindrome Number."""
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        return str_x == str_x[::-1]


class Solution5:
    """Runtime: 52 ms, faster than 89.19% of Python3 online submissions for Palindrome Number.
    Memory Usage: 14.4 MB, less than 16.54% of Python3 online submissions for Palindrome Number.
    """
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted_num = 0
        while x > reverted_num:
            reverted_num = reverted_num * 10 + x % 10
            x //= 10

        return x == reverted_num or x == reverted_num // 10
