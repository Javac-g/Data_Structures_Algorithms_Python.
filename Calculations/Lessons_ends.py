#Some schools start at 9:00. The duration of the lesson is 45 minutes, after the 1st, 3rd, 5th, etc.
#lessons change 5 minutes, and after the 2nd, 4th, 6th, etc. - 15 minutes.
#The lesson number is given (a number from 1 to 10). Determine when the specified lesson ends.
#Print two integers: the end time of the lesson in hours and minutes.

n = [1,2,3,4,5,6,7,8,9,10]
m = [45,35,35,25,25,15,15,5,5,55]
h = [9,10,11,12,13,14,15,16,17,17]
x = int(input())
print(h[x-1],m[x-1])
