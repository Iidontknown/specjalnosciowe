from asyncio.windows_events import NULL


def combSort(tab):
    gap = len(tab)
    zmiana = True
    temp=gap-1
    while gap > 1 or zmiana:
        gap = max(temp, int(gap / 1.3)) 
        zmiana = False
        for i in range(len(tab) - gap):
            j = i+gap
            if tab[i] > tab[j]:
                tab[i], tab[j] = tab[j], tab[i]
                zmiana = True
        if temp!=1:
            temp=1

def kompresj(str):
    out=""
    tab=list(str)
    print(tab)
    litera=""
    licznik=1
    for i in range(0,len(str)-1):
        
        if str[i]==str[i+1]:
            licznik=licznik+1
            # print("abs",licznik)
            if i==len(str)-1:
                print(str[i],licznik)
        else:
            print(str[i],licznik)
            licznik=1
            if i==len(str)-1:
                print(str[i+1],1)
    return out


    
tab_list = [75, 16, 55, 19, 48, 14, 2, 61, 22, 3,12,1]
print("przed: ", tab_list)
combSort(tab_list)
print("po:  ", tab_list)
kompresj("aaalllllaaaaab")  