# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# class Solution:
#     def removeNthFromEnd(self, head, n):
#         """
#         :type head: ListNode
#         :type n: int
#         :rtype: ListNode
#         """
#         result = ListNode(0)
#         result.next = head
#         first = result
#         second = result
#         index = 0
#         while True:
#             if first.next == None:
#                 second.next = second.next.next
#                 break
#             first = first.next
#             index += 1
#             if index > n:
#                 second = second.next
#         return result.next

# if __name__ == '__main__':
#     sol = Solution()
#     n1 = ListNode(2)
#     n2 = ListNode(5)
#     n3 = ListNode(6)
#     n1.next = n2
#     n2.next = n3
#     res = sol.removeNthFromEnd(n1, 0)
#     while res:
#         print(res.val)
#         res = res.next

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        result = ListNode(0)
        result.next = head
        first = result
        second = result
        index = 0
        while True:
            if first.next == None:
                second.next = second.next.next
                break
            first = first.next
            index += 1
            if index > n:
                second = second.next
        return result.next

if __name__ == '__main__':
    n1 = ListNode(3)
    n2 = ListNode(5)
    n3 = ListNode(4)
    n4 = ListNode(1)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    res = Solution().removeNthFromEnd(n1, 3)
    while res:
        print(res.val)
        res = res.next