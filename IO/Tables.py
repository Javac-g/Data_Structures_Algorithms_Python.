#The school decided to recruit three new math classes. 
#Since they have classes in mathematics at the same time, it was decided to allocate an office for each class and buy new desks in them. 
#No more than two students can sit at each desk. 
#The number of students in each of the three classes is known. How many desks do you need to buy in order to have enough for all students?
#The program receives as input three natural numbers: the number of students in each of the three classes.
a = int(input())
b = int(input())
c = int(input())
print(a // 2 + b // 2 + c // 2 + a % 2 + b % 2 + c % 2)
