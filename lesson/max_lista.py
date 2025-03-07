class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def find_max(head):
    p = head
    maks = None

    while p is not None:
        if maks is None:
            maks = p.val
        else:
            if p.val > maks:
                maks = p.val

        p = p.next

    return maks