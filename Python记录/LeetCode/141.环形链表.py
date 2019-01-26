class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

if __name__ == '__main__':
    sol = Solution()
    n1, n2, n3, n4, n5, n6, n7, n8 = ListNode(1), ListNode(2), ListNode(3)\
    , ListNode(4), ListNode(1), ListNode(2), ListNode(3), ListNode(4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    n7.next = n8
    n8.next = n2
    res = sol.hasCycle(n1)
    print(res)