
class link:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

def print_list(l):
    print("new list")
    while l:
        print(l.val)
        l = l.next


def Rmvdup(elem):
    if elem is None or elem.next is None:
        return elem
    first = elem
    while elem.next:
        if elem.val == elem.next.val:
            elem.next = elem.next.next
            continue
        else:
            elem = elem.next
    return first

