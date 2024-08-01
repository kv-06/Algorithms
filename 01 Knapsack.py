def knapSack_greedy(items, W): #v, wt, v/wt
    for item in items:
        item.append(item[0]/item[1])

    items.sort(key = lambda x : x[2], reverse = True)

    res = []
    total = 0
    for item in items:
        if item[1] <= W:
            res.append(item)
            W-=item[1]
            total += item[0]
        if W==0:
            break
    
    return res, total

def knapSack_dp(items, W):
    n = len(items)
    K = [[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif items[i-1][1] <= w:
                K[i][w] = max(items[i-1][0] + K[i-1][w-items[i-1][1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    res = []
    w = W
    for i in range(n, 0, -1):
        if K[i][w] != K[i - 1][w]:
            res.append(items[i - 1])
            w -= items[i - 1][1]

    return res, K[n][W]



n = int(input("Enter the no. of items : "))
items = [list(map(int,input("Enter value and weight of item " + str(i+1) + " : ").split()))  for i in range(n)]

W = int(input("\nEnter capacity of bag : "))

print("\nGreedy approach : ")
res, total = knapSack_greedy(items, W)
print("\nValue\tWeight")
for item in res:
    print(f"{item[0]}\t  {item[1]}")
print("\nTotal value =", total)


print("\n\n\nDynamic Programming approach : ")
res, total = knapSack_dp(items, W)
print("\nValue\tWeight")
for item in res:
    print(f"{item[0]}\t  {item[1]}")
print("\nTotal value =", total)


