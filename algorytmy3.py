import math


def JumpSearch(tab,x):
    n=len(tab)
    krok = math.sqrt(n)
     
    tyl = 0
    while tab[int(min(krok, n)-1)] < x:
        tyl = krok
        krok =krok+ math.sqrt(n)
        if tyl >= n:
            return -1
        if tab[int(min(krok, n)-1 )] == x:
            return int(tyl)+1
    tyl=int(min(krok, n)-1 )
    while tab[tyl] > x:
        tyl -= 1
        if tab[tyl] == x:
            return tyl
        if tyl == min(krok, n):
            
            return -1
            
    return -1
def addTab(taba,tabb):
    a=0
    b=0
    while a<len(taba)-1 and b<len(tabb)-1 :
        if  taba[a]>=tabb[b]:
            taba.insert(a,tabb[b])
            b=b+1
        if  taba[a]<tabb[b]:
            a=a+1 

    return taba
tab=[0,1,1,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
tabb=[0,0,0,0,1,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
print(JumpSearch(tab,19))
print(addTab(tab,tabb))