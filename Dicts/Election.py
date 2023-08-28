num_votes = {}
for _ in range(int(input())):
    candidate, votes = input().split()
    num_votes[candidate] = num_votes.get(candidate, 0) + int(votes)
 
for candidate, votes in sorted(num_votes.items()):
    print(candidate, votes)
