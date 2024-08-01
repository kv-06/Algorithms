def free_scholar(sch_match):
    for i in range(len(sch_match)):
        if sch_match[i]==-1:
            return i
    return -1

def gale_shapely(n,spm, apm):
    sch_match = [-1] * n
    ad_match = [-1] * n
    
    while(True):
        free_sch= free_scholar(sch_match)
        if  free_sch== -1:
            break
        
        index = 0
        while True:
            #flag = 0
            adv = spm[free_sch][index]
            if ad_match[adv] == -1:
                #flag = 1
                ad_match[adv] = free_sch
                sch_match[free_sch] = adv
                break
            else:
                current_sch = ad_match[adv]
                if apm[adv].index(current_sch) < apm[adv].index(free_sch):
                    index+=1
                else:
                    sch_match[current_sch] = -1
                    sch_match[free_sch] = adv
                    ad_match[adv] = free_sch
                    break
    return sch_match, ad_match


n = int(input("Enter the num of scholars: "))
print()
spm = [list(map(int,input("Enter the preference of scholar " + str(i) + " : ").split())) for i in range(n)]
print()
apm = [list(map(int,input("Enter the preference of advisor " + str(i) + " : ").split())) for i in range(n)]

sm, am = gale_shapely(n,spm, apm)
print("\nScholar  Advisor")
for i in range(n):
    print(f"   {i}   \t   {sm[i]} ")