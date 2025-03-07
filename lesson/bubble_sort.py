# na tablicy
def bubble_sort(T):
    for i in range(len(T)):
        for j in range(1, len(T) - i):
            if T[j - 1] > T[j]:
                T[j - 1], T[j] = T[j], T[j - 1]

    return T

# na linked liście
