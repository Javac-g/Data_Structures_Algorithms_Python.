#The chess bishop moves diagonally. Given two different cells on a chessboard, determine if the bishop can get from the first cell to the second in one move.
x1 = int(input()) 
y1 = int(input())
x2 = int(input())
y2 = int(input())

if abs(x1-x2) == abs(y1-y2) :
    print('YES')

else:
    print('NO')
