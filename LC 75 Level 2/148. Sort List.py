class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head
        pointer = self.findMiddle(head)
        next_pointer = pointer.next
        pointer.next = None
        return self.mergeSort(self.sortList(head), self.sortList(next_pointer))

    def findMiddle(self, root):
        prev = None
        slow = root
        fast = root
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        return prev

    def mergeSort(self, first_pointer, second_pointer):
        start = ListNode()
        curr = start
        while first_pointer and second_pointer:
            if first_pointer.val <= second_pointer.val:
                curr.next = first_pointer
                first_pointer = first_pointer.next
            else:
                curr.next = second_pointer
                second_pointer = second_pointer.next
            curr = curr.next

        if first_pointer == None:
            curr.next = second_pointer
        else:
            curr.next = first_pointer
        return start.next