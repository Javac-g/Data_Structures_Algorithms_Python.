#Two cells of a chessboard are given. If they are painted in the same color, 
#then print the word YES, and if they are in different colors, then print NO.
#The program receives as input four numbers from 1 to 8 each, 
#specifying the column number and row number, 
#first for the first cell, then for the second cell.

x1=int(input())
x2=int(input())
y1=int(input())
y2=int(input())
one= (x1+x2)%2
two= (y1+y2)%2
sum = one + two
if  sum == 0 :
    print('YES')
elif one == 0 and two == 0:
    print ('NO')
elif one > 0 and two >0 :
    print('YES')
elif one == 0 and two >0 :
         print ('NO')
elif one > 0 and two == 0 :
         print ('NO')
