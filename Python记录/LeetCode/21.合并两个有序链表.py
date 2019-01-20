class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        first, second = l1, l2
        l3 = ListNode(0)
        l4 = l3
        while first and second:
            if first.val <= second.val:
                l3.next = first
                first = first.next
                l3 = l3.next
            else:
                l3.next = second
                second = second.next
                l3 = l3.next
        if first:
            l3.next = first
        if second:
            l3.next = second
        return l4.next

if __name__ == '__main__':
    sol = Solution()
    n1, n2, n3, n4, n5, n6, n7, n8 = ListNode(1), ListNode(2), ListNode(3)\
    , ListNode(4), ListNode(1), ListNode(2), ListNode(3), ListNode(4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n5.next = n6
    n6.next = n7
    n7.next = n8
    res = sol.mergeTwoLists(n1, n5)
    while res:
        print(res.val)
        res = res.next
    # while n1:
    #     print(n1.val)
    #     n1 = n1.next
    # while n5:
    #     print(n5.val)
    #     n5 = n5.next
