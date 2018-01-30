# class to create linklist node
class link:
    def __init__(self,val,next):
        self.val = val
        self.next = next

# Function to zip the linlist nodes
def Ziplinklist(elem):
    first = elem.next
    eve = first
    od = elem
    if elem ==None or elem.next==None:
        return elem
    while True:
        try:
            elem.next = eve.next
            elem = eve.next
            eve.next = eve.next.next
            eve = eve.next
        except:
            break
    if eve.next:
        elem.next = eve.next
        elem = elem.next
        elem = None
    eve.next = od

    return first
