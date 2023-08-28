#The chocolate has the form of a rectangle divided into n × m slices. Chocolate can be broken once in a straight line into two parts. Determine whether it is possible to break off a part of a chocolate bar in this way, consisting of exactly k slices. The program receives three numbers as input: n, m, k and should output YES or NO.
n = int(input())
m = int(input()) 
k = int(input())
if  n * m > k and( k % n == 0 or k % m == 0):
    print('YES')
else:    
    print('NO')
