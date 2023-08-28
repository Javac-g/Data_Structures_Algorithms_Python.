#Max swam in a pool measuring N × M meters and got tired. At that moment, he found himself at a distance of x meters from one of the long ledges (not necessarily the nearest one) and y meters from one of the short ledges. What is the minimum distance Max must swim to get out of the pool onto the edge? The program receives numbers N, M, x, y as input. The program should print the number of meters that Max needs to swim to the edge.
N = int(input())
M = int(input())
x = int(input())
y = int(input())

print(min(x, y, min(N, M)-x, max(N, M)-y))
