#n schoolchildren divide k apples equally, the non-divisible remainder remains in the basket. How many apples will each student get? 
#How many apples will be left in the basket? The program receives the numbers n and k as input and must output the desired number of apples (two numbers).
import math
n = int(input('students'))
k = int(input('apple'))

r = math.trunc(k/n)
c = k - (r *n)
print((r))
print(c)
