class link:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

def mergesort(a,b):
    if a is None:
        return b
    elif b is None:
        return a
    elif a.val < b.val:
        a.next = mergesort(a.next,b)
        return a
    else:
        b.next = mergesort(a,b.next)
        return b
