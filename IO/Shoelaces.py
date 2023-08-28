#The shoe factory is going to start producing an elite model of boots.
#The holes for lacing will be arranged in two rows, the distance between the rows is a, and the distance between the holes in the row is b.
#The number of holes in each row is N. Lacing should take place in an elite way “up, horizontally to another row, up, horizontally, etc.” (see picture). 
#In addition, in order for the laces to be tied with an elite bow, the length of the free end of the lace should be l.
#What is the length of the lace for these boots?

#The program receives as input four natural numbers a, b, l and N - in that order - and must output one number - the desired length of the lace.
a = int(input())
b = int(input())
L = int(input())
N = int(input())
print(2 * L + (2 * N - 1) * a + 2 * (N - 1) * b)
