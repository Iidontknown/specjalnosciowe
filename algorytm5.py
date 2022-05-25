import random
def shuffle(tab):
    n = len(tab)
    for i in range (0,n):
        r = random.randint(0,n-1)
        tab[i], tab[r] = tab[r], tab[i]
    return tab
def issorted(tab):
    i=1
    while i < len(tab):
        if (tab[i]<tab[i-1]):
            return False
        i+=1
    return True
licznik=0
tab=[1,11,22,2,77,52,888,654]
while issorted(tab)== False:
    tab=shuffle(tab)
    licznik+=1
print(licznik,tab)

def interpolationSearch(tab,lo,hi,search):
    if lo<=hi and search >= arr[lo] and search <= arr[hi]:
        pos =int( lo + ((hi - lo) / (tab[hi] - tab[lo]) *(search - tab[lo])))
        if tab[pos]==search:
            return pos
        if tab[pos]<search:
            return interpolationSearch(tab,pos+1,hi,search)
        if tab[pos]>search:
            return interpolationSearch(tab,lo,pos-1,search)
    return -1
arr=[1,5,8,11]
print(interpolationSearch(arr,0,len(arr)-1,11))
