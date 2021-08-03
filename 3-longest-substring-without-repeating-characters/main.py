import inspect
import timeit
import sys
import string
import random


class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Runtime: 352 ms, faster than 18.78% of Python3 online submissions for Longest Substring ...
            Memory Usage: 14.3 MB, less than 80.36% of Python3 online submissions for Longest Substring ..."""
        len_s = len(s)
        if len_s <= 1:
            return len_s

        all_substr_length = set()
        current_substr = set()

        for i in range(len_s):
            for char in s[i:]:
                if char in current_substr:
                    all_substr_length.add(len(current_substr))
                    current_substr.clear()
                    break
                current_substr.add(char)
        return max(all_substr_length)


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Runtime: 148 ms, faster than 23.44% of Python3 online submissions for Longest Substring ...
            Memory Usage: 14.3 MB, less than 54.56% of Python3 online submissions for Longest Substring ..."""
        len_s = len(s)
        if len_s <= 1:
            return len_s

        all_chars = {char: 0 for char in s}

        start_idx = 0
        end_idx = 1
        max_len_substr = 0

        for i in range(len_s):
            all_chars[s[i]] += 1

            if all_chars[s[i]] > 1:
                start_idx += 1
                all_chars[s[i]] -= 1
            else:
                if len(set(s[start_idx: end_idx])) < len(s[start_idx: end_idx]):
                    for char in all_chars:
                        all_chars[char] = 0
                    all_chars[s[i]] += 1
                    start_idx += 1

            max_len_substr = max(max_len_substr, len(s[start_idx: end_idx]))
            end_idx += 1

        return max_len_substr


class Solution3:
    """Runtime: 48 ms, faster than 96.59% of Python3 online submissions for Longest Substring Without Repeating Char...
        Memory Usage: 14.5 MB, less than 25.41% of Python3 online submissions for Longest Substring Without Repeating C.
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_ = 0
        substring = list()
        for i in range(len(s)):
            if s[i] in substring:
                del substring[0: substring.index(s[i]) + 1]
            substring.append(s[i])
            max_ = len(substring) if len(substring) > max_ else max_
        return max_


class Solution4:
    """Runtime: 48 ms, faster than 96.59% of Python3 online submissions for Longest Substring Without Repeat ...
        Memory Usage: 14.3 MB, less than 80.42% of Python3 online submissions for Longest Substring Without Repeat ...
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ''
        max_ = 0
        for char in s:
            if char in substring:
                substring = substring.split(char)[1]
            substring += char
            max_ = len(substring) if len(substring) > max_ else max_
        return max_


class Solution5:
    """Runtime: 48 ms, faster than 96.59% of Python3 online submissions for Longest Substring Without Repeating ...
        Memory Usage: 14.3 MB, less than 54.63% of Python3 online submissions for Longest Substring Without Rep ..."""
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ''
        left = right = 0
        max_ = 0
        for char in s:
            if char in substring:
                left += substring.index(char) + 1
            substring = s[left: right+1]
            max_ = len(substring) if len(substring) > max_ else max_
            right += 1
        return max_


# Test Case
string_length = 1000
long_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=string_length))

# timeit params
timeit_repeat = 1
timeit_numbers = 1000


if __name__ == '__main__':
    solutions = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    for _, solution in solutions:
        if _.startswith("Solution"):
            result = solution().lengthOfLongestSubstring(s=long_string)
            t = timeit.Timer(
                lambda: solution().lengthOfLongestSubstring(s=long_string)
            ).repeat(timeit_repeat, timeit_numbers)
            print(result, t)
