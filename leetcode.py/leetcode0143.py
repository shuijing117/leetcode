# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
# 示例 1:
#
# 给定链表 1->2->3->4, 重新排列为 1->4->2->3.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reorder-list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        t = list()
        p = head
        while p:
            t.append(p)
            p = p.next

        p = head
        self.printList(p)
        self.printList(head)
        i = len(t)-1
        while t[i] != p:
            t[i].next = p.next
            p.next = t[i]

            i -= 1
            p = p.next.next
            print("%d %d %d %d" % (head.val, head.next.val, head.next.next.val, head.next.next.next.val))
            print("%d   %d" % (p.val, t[i].val))
        p.next = None

    def printList(self, head: ListNode) -> None:
        p = head
        while p:
            print("%d -> " % p.val, end='')
            p = p.next
        print()


if __name__ == '__main__':
    n4 = ListNode(4)
    n3 = ListNode(3, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)
    solution = Solution()
    solution.printList(n1)
    solution.reorderList(n1)
    solution.printList(n1)