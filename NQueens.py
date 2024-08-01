
def issafe(row,col,match):
    for r in range(row):
        if match[r] == col or abs(row-r)==abs(col-match[r]):
            return False
    return True

def pnq(match):
    n = len(match)
    mat = [[0 for i in range(n)] for i in range(n)]
    for r in range(n):
        col = match[r]
        mat[r][col] = 'Q'
    
    for x in mat:
        print(x)
    print("\n\n")

def nq(n,row,match):
    if n==row:
        pnq(match)
        return True
    
    for col in range(n):
        if issafe(row,col,match):
            match[row] = col
            nq(n,row+1, match)
            #match[row] = -1
            #return nq(n,row+1, match) or flag

n = 5
mat = [-1]*n
nq(n,0,mat)
#print(mat)
#pnq(mat)
