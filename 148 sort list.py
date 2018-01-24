class Solution(object):
    def sortList(self, head):
        """
          :type head: ListNode
          :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        mid = head
        front = head
        while front.next != None:
            front = front.next
            if front.next != None:
                mid = mid.next
                front = front.next
        lefthalf = head
        righthalf = mid.next
        mid.next = None
        left = self.sortList(lefthalf)
        right = self.sortList(righthalf)
        list = self.mergesort(left,right)
        return list

    def mergesort(self,h1,h2):
        head_sorted = ListNode(0)
        head_sorted.next = end_sorted
        while h1 and h2:
            if h1.val<h2.val:
                end_sorted.next = h2
                h1 = h1.next
            else:
                end_sorted.next = h2
                h2 = h2.next
            end_sorted = end_sorted.next
        if h1:
            end_sorted.next = h1
        else:
            end_sorted.next = h2
        return head_sorted.next
        
        
