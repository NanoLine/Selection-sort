def f(l):
    for i in range(len(l)-1): 
        minimum = i
        for j in range(i + 1, len(l)):
            if l[j] < l[minimum]:
                minimum = j
        if minimum != i:
            temp = l[i]
            l[i] = l[minimum]
            l[minimum] = temp

    return l

print(f([1, 4, 2, 5, 3]))