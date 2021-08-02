import inspect
import random
import sys
import timeit
from typing import List, Union, Tuple, Dict


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    """Runtime: 64 ms, faster than 90.32% of Python3 online submissions for Two Sum.
        Memory Usage: 14.6 MB, less than 13.22% of Python3 online submissions for Two Sum."""
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_list: List = []
        l2_list: List = []

        while l1:
            l1_list.append(str(l1.val))
            l1: Union[ListNode, None] = l1.next
        while l2:
            l2_list.append(str(l2.val))
            l2: Union[ListNode, None] = l2.next

        l1_num: int = int("".join(l1_list[::-1]))
        l2_num: int = int("".join(l2_list[::-1]))

        result: List = [int(char) for char in str(l1_num + l2_num)]

        result_ln: Union[ListNode, None] = None
        for num in result:
            result_ln = ListNode(val=num, next=result_ln)

        return result_ln


class Solution2:
    """Runtime: 68 ms, faster than 76.51% of Python3 online submissions for Two Sum.
        Memory Usage: 14.4 MB, less than 44.82% of Python3 online submissions for Two Sum."""
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        division: int = 0
        result_list: List[int] = []

        while l1 or l2 or division != 0:
            try:
                l1_val = l1.val
                l1 = l1.next
            except AttributeError:
                l1_val = 0

            try:
                l2_val = l2.val
                l2 = l2.next
            except AttributeError:
                l2_val = 0

            sum_: int = l1_val + l2_val + division

            if division > 0: division -= 1
            division += sum_ // 10

            result = sum_ % 10
            result_list.append(result)

        result_ln: Union[ListNode, None] = None
        for el in result_list[::-1]:
            result_ln = ListNode(val=el, next=result_ln)
        return result_ln


class Solution3:
    """Runtime: 68 ms, faster than 76.51% of Python3 online submissions for Two Sum.
        Memory Usage: 14.1 MB, less than 90.62% of Python3 online submissions for Two Sum."""
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_list: List[int] = self.getList(ln=l1)[::-1]
        l2_list: List[int] = self.getList(ln=l2)[::-1]

        sm_list, lng_list = sorted([l1_list, l2_list], key=len)

        division: int = 0
        result_list: List[int] = []

        for i in range(len(lng_list)):
            try:
                num_sm_list = sm_list[i]
            except IndexError:
                num_sm_list = 0

            sum_: int = lng_list[i] + num_sm_list + division

            if division > 0: division -= 1

            division += sum_ // 10

            result = sum_ % 10
            result_list.insert(0, result)

        if division:
            result_list.insert(0, division)

        result_ln: Union[ListNode, None] = None
        for el in result_list:
            result_ln = ListNode(val=el, next=result_ln)
        return result_ln

    def getList(self, ln: ListNode) -> List[int]:
        result_list = []
        while ln:
            result_list.append(ln.val)
            ln = ln.next
        return result_list[::-1]


# Test Case
fst_value = 9999999
snd_value = 9999

fst_value = [int(char) for char in str(fst_value)[::-1]]
snd_value = [int(char) for char in str(snd_value)[::-1]]

result_ln1 = None
result_ln2 = None

for num in fst_value:
    result_ln1 = ListNode(val=num, next=result_ln1)
for num in snd_value:
    result_ln2 = ListNode(val=num, next=result_ln2)

# timeit params
timeit_repeat = 1
timeit_numbers = 100


if __name__ == '__main__':
    solutions = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    for _, solution in solutions:
        if _.startswith("Solution"):
            result = solution().addTwoNumbers(l1=result_ln1, l2=result_ln2)
            t = timeit.Timer(
                lambda: solution().addTwoNumbers(l1=result_ln1, l2=result_ln2)
            ).repeat(timeit_repeat, timeit_numbers)
            print(result, t)
