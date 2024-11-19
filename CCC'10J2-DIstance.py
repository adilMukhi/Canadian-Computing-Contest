a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())
stepsNikky = 0
stepsByron = 0
posNeg = 1

for i in range(s):
    #if posNeg == 1:
    stepsNikky += a
    stepsByron += c
        #posNeg = -1
    #elif posNeg == -1:
    stepsNikky -= b
    stepsByron -= d
        #posNeg = 1

if stepsNikky > stepsByron:
    print("Nikky")
elif stepsByron > stepsNikky:
    print("Byron")
else:
    print("Tied")