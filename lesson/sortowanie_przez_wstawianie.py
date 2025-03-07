def sort(T):
    n = len(T)

    for i in range(1,n):
        for j in range(i-1,-1,-1):
            if T[j]>T[j+1]:
                T[j], T[j+1] = T[j+1], T[j]
            else:
                break