import inspect
import random
import sys
import timeit
from typing import List, Union, Tuple, Dict


class Solution:
    """Runtime: 64 ms, faster than 58.17% of Python3 online submissions for Two Sum.
    Memory Usage: 16.1 MB, less than 9.42% of Python3 online submissions for Two Sum."""
    def twoSum(self, nums: Union[List, Tuple], target: int) -> Union[Tuple[int, int], None]:
        enum_nums_dict__value_index: Dict[int, List] = dict()
        for el_index, el_value in enumerate(nums):
            enum_nums_dict__value_index.setdefault(el_value, []).append(el_index)

        for key, all_indices_fst_el in enum_nums_dict__value_index.items():
            all_indices_snd_el = enum_nums_dict__value_index.get(target - key)
            if all_indices_snd_el:
                if all_indices_fst_el != all_indices_snd_el:
                    return all_indices_fst_el[0], all_indices_snd_el[0]
                elif all_indices_fst_el == all_indices_snd_el:
                    try:
                        return all_indices_fst_el[0], all_indices_snd_el[1]
                    except IndexError:
                        continue


# Test Case
nums = [random.randint(1, 3000) for i in range(10000)]
target = random.randint(1, 3000)

# timeit params
timeit_repeat = 1
timeit_numbers = 100


if __name__ == '__main__':
    solutions = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    for _, solution in solutions:
        result = solution().twoSum(nums=nums, target=target)
        t = timeit.Timer(
            lambda: solution().twoSum(nums=nums, target=target)
        ).repeat(timeit_repeat, timeit_numbers)
        print(result, t)
