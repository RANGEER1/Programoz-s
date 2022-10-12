'''szam= int(input('adj meg egy számot'))
if szam < 0:
    print('A megadott szám negatív')
elif szam ==0:
    print("A szám nulla")

else:
    print("A szám nem negatív")
    print('>>A program vége<<')'''
'''import random
szam1=random.randint(1,6)
szam2=random.randint(1,6)
szam3=random.randint(1,6)
print(szam1,szam2,szam3)'''
import random
szam1= random.randint(1,3)
print(szam1)
if szam1 == 1:
    tipp ="kő"
elif szam1 == 2:
    tipp ="papír"
else:
    tipp ="olló"
print(tipp,'>>A program vége<<')