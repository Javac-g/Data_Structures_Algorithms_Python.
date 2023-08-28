def height(man):
    if man not in p_tree:
        return 0
    else:
        return 1 + height(p_tree[man])
 
p_tree = {}
n = int(input())
for i in range(n - 1):
    child, parent = input().split()
    p_tree[child] = parent
 
heights = {}
for man in set(p_tree.keys()).union(set(p_tree.values())):
    heights[man] = height(man)
 
for key, value in sorted(heights.items()):
    print(key, value)
