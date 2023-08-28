x = int(input('X = '))
y = int(input('Y = '))
n = 1

s = -1
if x < y:
    y=y + 1
    for it in range(x, y, 1):
        print(it, end = " ", )
elif x > y:
    y = y -1
    for it in range(x, y, -1):
        print(it, end = " ")
elif x == y:
    print(x)
