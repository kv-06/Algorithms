def ins_sort(a):
    n = len(a)
    for i in range(1,n):
        j = i
        while(j>0 and a[j]<a[j-1]):
            a[j], a[j-1] = a[j-1], a[j]
            j-=1
    return a

l = [9,2,1,2,3,4,3,5,45,23,34,1,2]
print(ins_sort(l))

def shell_sort(l):
    n = len(l)
    gap = n//2

    while gap>0:
        for i in range(gap, n):
            j = i
            while j>=gap and l[j]<l[j-gap]:
                l[j], l[j-gap] = l[j-gap], l[j]
                j-=gap
        gap//=2

    return l

l = [9,2,1,2,3,4,3,5,45,23,34,1,2]
print(shell_sort(l))


def radix_sort(l):
    #no. of digits in the max elm
    n = len(str(max(l)))
    for i in range(1,n+1):
        l.sort(key = lambda x: (x%10**i)//10**(i-1))
    return l

'''
def radix_sort(l):
    #no. of digits in the max elm
    n = len(str(max(l)))
    for i in range(1,n+1):
        for x in l:
            print((x%10**i)//10**(i-1))
        print()
    return l
'''



l = [123,234,234,245,232,32423,231,9,2,1,2,3,4,3,5,45,23,34,1,2]
print(radix_sort(l))

def counting_sort(arr,exp):
    n = len(arr)
    out = [0]*n
    count = [0]*10

    for i in range(n):
        index = arr[i]//exp
        count[index%10] +=1
    
    for i in range(1,10):
        count[i]+=count[i-1]

    i = n-1
    while i>=0:
        index = arr[i]//exp
        out[count[index%10] - 1] = arr[i]
        count[index%10]-=1
        i-=1

    for i in range(n):
        arr[i] = out[i]

def radix(arr):
    maxi = max(arr)
    dig = len(str(maxi))
    for i in range(dig):
        counting_sort(arr,10**i)


a = [23,43,1,2,322,422,222,34,56,0]
radix(a)
print(a)


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

def merge_sort(l):
    n = len(l)
    if n==1:
        return l
    
    la = merge_sort(l[:n//2])
    ra = merge_sort(l[n//2:])

    i=0
    j=0

    ln = len(la)
    rn = len(ra)

    ml = []
    while i<ln and j<rn:
        if la[i] < ra[j]:
            ml.append(la[i])
            i+=1
        else:
            ml.append(ra[j])
            j+=1
        
    while i<ln:
        ml.append(la[i])
        i+=1

    while j<rn:
        ml.append(ra[j])
        j+=1
    return ml

l = [123,234,234,245,232,32423,231,9,2,1,2,3,4,3,5,45,23,34,1,2]
print(merge_sort(l))