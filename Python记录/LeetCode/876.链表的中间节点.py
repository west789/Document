class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        flag = ListNode(0)
        flag.next = head
        slow = flag
        fast = flag
        while fast.next and fast.next.next:
            slow = slow.next
            fast =  fast.next.next
        return slow.next
if __name__ == '__main__':
    sol = Solution()
    n1, n2, n3, n4, n5 = ListNode(1), ListNode(2), ListNode(3)\
    , ListNode(4), ListNode(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    head = n1
    while head:
        print(head.val)
        head = head.next
    print('*'*20)
    res = sol.middleNode(n1)
    print(res.val)
    