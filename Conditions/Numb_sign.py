#In mathematics, the function sign(x) (the sign of a number) is defined as follows:
#sign(x) = 1 if x > 0,
#sign(x) = -1 if x < 0,
#sign(x) = 0 if x = 0.
#For the given number x print the value of sign(x). It is desirable to solve this problem using cascading if... elif... else statements.

x = int(input())
if x > 0 :
    print('1')
elif x<0:
    print('-1')
else:print('0')
