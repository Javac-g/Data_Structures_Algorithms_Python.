c = 1
i = 0
n = int(input())
for i in range(1,n):
    i +=1
    c = i * c
    if i ==n:
        break
print(c)
