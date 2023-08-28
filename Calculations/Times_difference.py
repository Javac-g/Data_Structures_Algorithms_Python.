#The values of two points of time belonging to the same day are given: hours, minutes and seconds for each of the points of time. It is known that the #second moment of time came not earlier than the first. Determine how many seconds elapsed between two points in time.

#The program receives three integers as input: hours, minutes, seconds, specifying the first moment of time and three integers, specifying the second #moment of time.

#Print the number of seconds between these times.
h = int(input('hour =  '))
m = int(input('minute = '))
s = int(input('seconds = '))
h2 = int(input('hour =  '))
m2 = int(input('minute = '))
s2 = int(input('seconds = '))

H = (h2 * 3600) - (h * 3600)
M = (m2 * 60) - ( m * 60)
S = s2 - s
ans= H + M +S
print(ans)
