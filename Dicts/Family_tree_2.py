def is_ancestor(man, older_man):
    if man == older_man:
        return True
    while man in p_tree:
        man = p_tree[man]
        if man == older_man:
            return True
    return False
     
p_tree = dict()
n = int(input())
for i in range(n - 1):
    child, parent = input().split()
    p_tree[child] = parent
 
for i in range(int(input())):
    first, second = input().split()
    if is_ancestor(second, first):
        print(1, end=' ')
    elif is_ancestor(first, second):
        print(2, end=' ')
    else:
        print(0, end=' ')
