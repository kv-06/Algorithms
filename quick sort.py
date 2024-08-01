
def quk_sor(l):
    #print("l = ",l)
    n = len(l)
    if n <= 1:
        return l
    i = 0
    j = n - 1
    res = [0] * n

    for ind in range(1, n):        
        if l[ind] < l[0]:
            res[i] = l[ind]
            i += 1
        elif l[ind] > l[0]:
            res[j] = l[ind]
            j -= 1

    for ind in range(i, j + 1):
        res[ind] = l[0]
    #print("res = ", res)
    res[:i ] = quk_sor(res[:i ])
    res[j + 1:] = quk_sor(res[j + 1:])

    return res


# Example usage:


l = [5,6,3,4,8,9,1,2]

#print(l)

print(quk_sor(l))