# na tablicy
def selection_sort(T):
    pom = None

    for i in range(len(T)):
        pom = i
        for j in range(i+1, len(T)):
            if T[j] < T[pom]:
                pom = j

    T[i], T[pom] = T[pom], T[i]

# na liście
def selection_sort_linked_list(p):
    # lista nie jest pusta
    prev, m = find_min(p)

    if prev is None and m.next is None:
        return m

    sorted = m

    if prev is not None:
        prev.next = m.next
    else:
        not_sorted = m.next
    m.next = None

def find_min(p): # potrzebne do znalezienia min do selection_sort_linked_list
    if p.next is None:
        return None, p

    min_val = p.next
    prev=p
    first=p

    while p.next is not None:
        if min_val.val < p.val:
            min_val = p.next
            prev=p
    # return p.next, min_val # komentarz na one sec
    if min_val.val > first.val:
        return first, None
    else:
        return min_val, prev