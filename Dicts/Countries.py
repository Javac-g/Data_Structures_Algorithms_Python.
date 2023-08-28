motherland = {}
for i in range(int(input())):
    country, *cities = input().split()
    for city in cities:
        motherland[city] = country
         
for i in range(int(input())):
    print(motherland[input()])
