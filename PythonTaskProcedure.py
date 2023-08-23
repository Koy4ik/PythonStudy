import random
import Modul1
#Сто чисел рандомом. Процент +,-,0.
Spisok=[]


for i in range(100):
    Spisok.append(random.randint (-100,100))

a=Modul1.PoloZh(Spisok)
b=Modul1.Otric(Spisok)
c=Modul1.Nolik (Spisok)
print (a,b,c)