class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

#zakładamy, ze jest przynajmniej 1 element
def insert(p: Node, v : int):
    wynik = p # wartownik na początek listy
    p = p.next
    prev = p

    while p is not None:
        if p.val > v:
            a = Node(v)
            a.next = p

            if prev is not None:
                prev.next = a
                return wynik
            else:
                return a
        prev = p
        p = p.next

    a=Node(v)
    p.next=a
    a.next=None
    return wynik