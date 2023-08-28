x = int(input('X = '))
y = int(input('Y = '))
for x in range(x,y-1,-1):
    if x % 2 != 0: 
        print(x)
