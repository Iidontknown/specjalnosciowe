def insertionSort(tab):
    for x in range(1, len(tab)):
        temp = tab[x]
        y = x-1
        while y >=0 and temp < tab[y] :
                tab[y+1] = tab[y]
                y =y-1
        tab[y+1] = temp
    return tab

def printSame(taba,tabb,tabc):
    a=0
    b=0
    c=0
    while a<len(taba) and b<len(tabb) and c<len(tabc) :
        if taba[a]==tabb[b]==tabc[c]:
            print(taba[a])
            a=a+1
            b=b+1
            c=c+1
        elif taba[a]<tabb[b] or taba[a]<tabb[c] :
            a=a+1
        elif taba[b]<tabb[a] or taba[b]<tabb[c] :
            b=b+1
        elif taba[c]<tabb[b] or taba[c]<tabb[a] :
            c=c+1



    
testa=[1,2,5,7,8,9]
testb=[2,4,5,7,9,10,15]
testc=[2,3,5,7,8,11,22,90]
tabtest=[1,5,4,3,2,10,7,22,6]
print("zad 1")
print(tabtest)
print(insertionSort(tabtest))

print("zad 2")


printSame(testa,testb,testc)
