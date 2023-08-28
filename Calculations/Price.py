#A pie in the cafeteria costs a rubles and b kopecks. Determine how many rubles and kopecks you need to pay for n pies. 
#The program receives three numbers as input: a, b, n, and must output two numbers: the purchase price in rubles and kopecks.
import math
a = int(input()) 
b = int(input())
c = int(input())
a = a *c
b = b *c
if b > 100:
    a = a + (b // 100)
    b = b % 100
    print(a ,b )
else:

    print(a,b)
