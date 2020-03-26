'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = self.getNumber(l1)
        n2 = self.getNumber(l2)
        sum = n1 + n2
        l = self.numberToList(sum)

        return l

    def numberToList(self, number):
        i = 0
        t_number = number
        l = ListNode(t_number % 10)
        t_number = t_number // 10
        p = l
        while t_number != 0:
            p.next = ListNode(t_number % 10)
            t_number = t_number // 10
            p = p.next

        return l

    def printList(self, l):
        p = l
        while p:
            print(p.val, end=' ')
            p = p.next
        print()

    def getNumber(self, l: ListNode):
        if not l:
            return 0

        p = l

        number = 0
        i = 1
        while p:
            number = p.val * i + number
            i *= 10
            p = p.next
        return number


if __name__ == '__main__':
    solution = Solution()
    l1 = ListNode(2)
    p = l1
    p.next = ListNode(4)
    p = p.next
    p.next = ListNode(3)

    l2 = ListNode(5)
    p = l2
    p.next = ListNode(6)
    p = p.next
    p.next = ListNode(4)

    solution.printList(solution.addTwoNumbers(l1, l2))