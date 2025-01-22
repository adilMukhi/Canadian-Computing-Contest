n = int(input())
antoniaScore = 100
davidScore = 100

for i in range(n):
    temp = input().split()
    if temp[0] > temp[1]:
        davidScore -= int(temp[0])
    elif temp[0] < temp[1]:
        antoniaScore -= int(temp[1])

print(antoniaScore)
print(davidScore)