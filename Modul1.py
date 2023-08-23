Spisok=[]
def PoloZh(Spisok):
    Itog=0
    for i in Spisok:
        if Spisok[i]>0:
            Itog=Itog+1
    return Itog

def Otric(Spisok):
    Itog=0
    for i in Spisok:
        if Spisok[i]<0:
            Itog=Itog+1
    return Itog

def Nolik(Spisok):
    Itog=0
    for i in Spisok:
        if Spisok[i]==0:
            Itog=Itog+1
    return Itog