#The political life of one country is very lively. There are K political parties in the country, each of which regularly declares a national strike. The days when at least one of the parties goes on strike, provided that it is not Saturday or Sunday (when no one works anyway), cause great damage to the country's economy.

#The i-th party announces strikes strictly every b_i days, starting from the day with number a_i. That is, the i-th party declares strikes on days a_i, a_i + b_i, a_i + 2 * b_i, etc. If on any given day several parties go on strike, it counts as one nationwide strike.

#There are N days in the country's calendar, numbered starting from one. The first day of the year is Monday, the sixth and seventh days of the year are holidays, the week consists of seven days.

#The first line contains the numbers N and K. Then there are K lines describing the schedules of the strikes. The i-th line contains numbers a_i and b_i. You need to determine the number of strikes that occurred in this country during the year.

N, K = [int(s) for s in input().split()]
work_days = set([day for day in range(1, N + 1) if day % 7 not in (6, 0)])
no_strikes = set(work_days)
for party in range(K):
    a, b = [int(s) for s in input().split()]
    max_strikes = (N - a) // b + 1
    no_strikes -= {a + b*i for i in range(max_strikes)}
print(len(work_days) - len(no_strikes))
