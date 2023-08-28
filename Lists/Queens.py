#It is known that 8 queens can be placed on an 8×8 board so that they do not attack each other.
#You are given an arrangement of 8 queens on the board, determine if there is a pair of them that beat each other.
#The program receives eight pairs of numbers as input, each number from 1 to 8 is the coordinates of 8 queens.
#If the queens don't beat each other, print the word NO, otherwise print YES.
n = 8
x = []
y = []
for i in range(n):
    new_x, new_y = [int(s) for s in input().split()]
    x.append(new_x)
    y.append(new_y)
 
correct = True
for i in range(n):
    for j in range(i + 1, n):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            correct = False
 
if correct:
    print('NO')
else:
    print('YES')
