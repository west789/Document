class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # # 转化成数组然后反转后再转化为链表
    # def reverseList(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     if not head:
    #         return head
    #     nList = []
    #     while head:
    #         nList.append(head.val)
    #         head = head.next
    #     nList.reverse()
    #     print(nList)
    #     newNode = ListNode(nList[0])
    #     headNew = newNode
    #     for index in range(1, len(nList)):
    #         print("item:", index)
    #         newNode.next = ListNode(nList[index])
    #         newNode = newNode.next
    #     return headNew
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        prev = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            if tmp:
                cur = tmp
            else:
                break
        return cur
if __name__ == '__main__':
    sol = Solution()
    n1, n2, n3, n4 = ListNode(1), ListNode(2), ListNode(3)\
    , ListNode(4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    head = n1
    while head:
        print(head.val)
        head = head.next
    print('*'*20)
    res = sol.reverseList(n1)
    while res:
        print(res.val)
        res = res.next