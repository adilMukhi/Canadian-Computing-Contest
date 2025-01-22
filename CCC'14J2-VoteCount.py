n = int(input())
a_count = 0
b_count = 0

votes = input()
list_votes = list(votes)
for A in list_votes:
    if A == 'A':
        a_count += 1
    else:
        b_count += 1
if a_count > b_count:
    print('A')
elif a_count < b_count:
    print('B')
else:
    print('Tie')