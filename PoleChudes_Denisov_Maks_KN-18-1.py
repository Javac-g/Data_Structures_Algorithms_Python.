import random
import re

l=[]
one =[]
two = []
three= []
four =[]
one = input("Введите первое секретное слово = ").lower()
l.append(one)
two = input("Введите второе секретное слово = ").lower()
l.append(two)
three = input("Введите третье секретное слово = ").lower()
l.append(three)
four = input("Введите четвертое последнее слово = ").lower()
l.append(four)
print("П О Л Е - Ч У Д Е С")
ch=input('Введите "старт" чтобы начать игру: ')
z=random.choice(l)
x=("-"*len(z))
noimp,imp=[],[]
print()
count,d = 0,0
while(count<8):
    print()
    print(x)
    n=input("Введите букву:  ").lower()
    
    if(n.islower() and (len(n)==1)):
        if(n in z):
            if(n in noimp):
                print("Вы уже ввели эту букву")       
            else:
                for m in re.finditer(n, z):
                    x = x[:m.start()] + n + x[m.start()+1:]
                noimp.append(n)
        else:              
            if(n in imp):
                print("Вы уже ввели эту букву")             
            else:
                print("Такая буква отсутствует")
                count+=1
                imp.append(n)
        if(x == z):
            print(z)
            d=1
            break
            
    else:
        if(len(n)!=1):
            print("Вы можете ввести только одну букву")
        elif(not n.islower()):
            print("Нет")
        
if(d==1):
    print("""Победа! ---- вы выиграли автомобиль""")
else:
    print("Вы проиграли!")
    