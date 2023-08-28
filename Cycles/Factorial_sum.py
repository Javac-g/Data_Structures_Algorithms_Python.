n = int(input())
d = 1
c = 0
for i in range(1, n + 1):
    d*= i
    c += d
print(c)
