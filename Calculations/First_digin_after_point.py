#Given a positive real number X. Print its first digit after the decimal point.
import math
def truncate(number, decimals=0):
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer.")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more.")
    elif decimals == 0:
        return math.trunc(number)

    factor = 10.0 ** decimals
    return math.trunc(number * factor) / factor
x = float(input())
z = x % 1
y = z // 10
f = 1 - z
g = z - f
p = g % 10
B = truncate(z-f,7)
A = truncate(p, 3)
C = truncate(f, 1)
D = truncate(x, 1)
E = truncate(x - D,3)
AA = truncate((z -E)*10,0)
 
p = truncate((g % 10),7)
print(AA)
