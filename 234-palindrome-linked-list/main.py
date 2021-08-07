from copy import deepcopy


class Solution:
    """Runtime: 816 ms, faster than 58.83% of Python3 online submissions for Palindrome Linked List.
    Memory Usage: 47.1 MB, less than 44.28% of Python3 online submissions for Palindrome Linked List."""
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l_ = []
        while head:
            l_.append(head.val)
            head = head.next
        return l_ == l_[::-1]


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        reverse_ln = self.get_reversed_ln(head)
        while head:
            if head.val != reverse_ln.val:
                return False
            head = head.next
            reverse_ln = reverse_ln.next
        return True

    def get_reversed_ln(self, ln: ListNode):
        prev = None
        curr = deepcopy(ln)
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev
