import inspect
import timeit
import sys


class Solution1:
    """Runtime: 28 ms, faster than 88.77% of Python3 online submissions for Reverse Integer.
    Memory Usage: 14.3 MB, less than 12.33% of Python3 online submissions for Reverse Integer."""
    def reverse(self, x: int) -> int:
        start = None
        sign = 0

        if x < 0:
            start = 0
            sign = 1

        result = int("".join([char for char in str(x)[:start:-1]]))

        if sign == 1:
            result = -result

        if -2 ** 31 < result < (2 ** 31) - 1:
            return result
        return 0


class Solution2:
    """Runtime: 20 ms, faster than 99.50% of Python3 online submissions for Reverse Integer.
    Memory Usage: 14.2 MB, less than 74.16% of Python3 online submissions for Reverse Integer."""
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        abs_x = abs(x)

        n_digits = self.get_n_digits(abs_x)

        result = 0
        for i in range(n_digits - 1, -1, -1):
            result += (abs_x % 10) * (10 ** i)
            abs_x = abs_x // 10

        result = sign * result
        if -2 ** 31 < result < (2 ** 31) - 1:
            return result
        return 0

    def get_n_digits(self, x):
        n_digits = 0
        while x > 0:
            x //= 10
            n_digits += 1
        return n_digits


# Test Case
test_num = -5123125412

# timeit params
timeit_repeat = 1
timeit_numbers = 100


if __name__ == '__main__':
    solutions = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    for _, solution in solutions:
        if _.startswith("Solution"):
            result = solution().reverse(x=test_num)
            t = timeit.Timer(
                lambda: solution().reverse(x=test_num)
            ).repeat(timeit_repeat, timeit_numbers)
            print(result, t)
